"""
Create a Notion release notes page from the commits between two git refs.

Extracts Linear issue keys (e.g. SORD-123, FOS-42) from the commits in the
range — both individual commit subjects (including squash-merged commits
with no merge commit of their own, e.g. "feat(FWMS-2300): ...") and PR
branch names — fetches their titles via the Linear GraphQL API, categorizes
them by conventional commit prefix, and creates a formatted page in a Notion
release notes database.

Usage (env vars):
    LINEAR_API_KEY        - Linear API token
    NOTION_API_KEY        - Notion integration token
    VERSION               - Full version string (e.g. 1.4.4.23588748828)
    RELEASE_TYPE          - Value stored in the "Mobile app release type" Notion property
    PR_SOURCE             - Go-to-prod PR number
    REPO                  - GitHub repository (owner/name), used to build PR links
    NOTION_DATABASE_ID    - Notion database ID to create the release notes page into
    LINEAR_WORKSPACE      - Linear workspace slug, used for fallback issue URLs (default: smartway)
    LINEAR_ISSUE_PATTERN  - Regex used to detect Linear issue keys in commit messages (default: [A-Z]{2,10}-\\d+)
    FROM_REF              - Git ref to compare from (default: main)
    TO_REF                - Git ref to compare to (default: develop)
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date

LINEAR_GRAPHQL_URL = "https://api.linear.app/graphql"
NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_BLOCK_API_URL = "https://api.notion.com/v1/blocks"
NOTION_API_VERSION = "2022-06-28"
NOTION_BLOCK_LIMIT = 100


@dataclass
class Issue:
    issue_key: str
    title: str
    url: str
    commit_subject: str


@dataclass
class CategorizedIssues:
    features: list[Issue] = field(default_factory=list)
    fixes: list[Issue] = field(default_factory=list)
    tech: list[Issue] = field(default_factory=list)
    other: list[Issue] = field(default_factory=list)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _boundary_keys(text: str, linear_issue_pattern: str, ignorecase: bool) -> list[str]:
    """Return pattern matches whose key starts a fresh token.

    A match is rejected when the preceding character is a letter, digit or
    hyphen, so a key must sit at a real token boundary (after "/", "(", ":",
    whitespace, ...). This drops mid-word matches such as the "to-56" inside
    "update-expo-to-56", while keeping "fix/fwms-2310" or "feat(FWMS-2303)".
    """
    flags = re.IGNORECASE if ignorecase else 0
    keys: list[str] = []
    for match in re.finditer(linear_issue_pattern, text, flags):
        start = match.start()
        if start > 0 and (text[start - 1].isalnum() or text[start - 1] == "-"):
            continue
        keys.append(match.group(0).upper())
    return keys


def find_issue_keys(text: str, linear_issue_pattern: str) -> list[str]:
    """Find Linear issue keys in a commit subject.

    Upper-case keys are matched anywhere in the subject; lower-case keys are
    only matched inside a conventional-commit scope, e.g. "feat(sord-1234):
    ...", where they reliably appear — restricting the case-insensitive match
    there avoids false positives on lower-case "word-number" prose such as
    "use utf-8 encoding".
    """
    keys = _boundary_keys(text, linear_issue_pattern, ignorecase=False)
    scope = re.match(r"^[a-zA-Z]+(?:\(([^)]*)\))?!?:", text)
    if scope and scope.group(1):
        keys += _boundary_keys(scope.group(1), linear_issue_pattern, ignorecase=True)
    return list(dict.fromkeys(keys))


def find_branch_keys(message: str, linear_issue_pattern: str) -> list[str]:
    """Find Linear issue keys in a merge commit subject (PR branch name).

    Branch names carry keys as path segments (e.g. "from .../fix/fwms-2310"),
    often in lower case, so match case-insensitively — but skip bot branches
    ("renovate/...", "dependabot/...") whose package names ("appium-3.x")
    would otherwise look like tickets.
    """
    if re.search(r"(?:^|[/\s])(?:renovate|dependabot)/", message, re.IGNORECASE):
        return []
    return list(dict.fromkeys(_boundary_keys(message, linear_issue_pattern, ignorecase=True)))


def _categorize(categorized: CategorizedIssues, issue_key: str, subject: str) -> None:
    if subject.startswith("feat"):
        categorized.features.append(Issue(issue_key, "", "", subject))
    elif subject.startswith("fix"):
        categorized.fixes.append(Issue(issue_key, "", "", subject))
    else:
        categorized.tech.append(Issue(issue_key, "", "", subject))


def branch_type(message: str) -> str:
    """Conventional type of a PR branch, e.g. "feat" for ".../feat/fwms-2326".

    Returns "feat"/"fix"/... when the branch is namespaced with a type
    segment, else "". Used to categorize a ticket found only in a branch name,
    whose PR has no conventional-commit subject to key off of.
    """
    match = re.search(r"from \S+?/([a-zA-Z]+)/", message)
    return match.group(1).lower() if match else ""


def extract_categorized_issues(
    from_ref: str, to_ref: str, repo: str, linear_issue_pattern: str
) -> CategorizedIssues:
    def log(*args: str) -> str:
        out = git("log", *args, f"origin/{from_ref}..origin/{to_ref}")
        if not out:
            out = git("log", *args, f"{from_ref}..{to_ref}")
        return out

    categorized = CategorizedIssues()
    seen: set[str] = set()

    # Pass 1 — walk every non-merge commit. This is the only way to catch
    # tickets from PRs that were squash- or rebase-merged (no merge commit),
    # which is the common case: the ticket lives in the commit's own
    # conventional-commit scope, e.g. "feat(FWMS-2300): ...".
    commit_log = log("--no-merges", "--format=%s")
    for subject in commit_log.splitlines():
        if not subject.strip():
            continue
        for issue_key in find_issue_keys(subject, linear_issue_pattern):
            if issue_key in seen:
                continue
            seen.add(issue_key)
            _categorize(categorized, issue_key, subject)

    # Pass 2 — walk merge commits. Handles tickets that only appear in a PR
    # branch name (e.g. "from ZeroGachis/SORD-123-foo") with no ticket in the
    # commit subjects, and collects genuinely ticket-less PRs into "Other".
    merge_log = log("--merges", "--format=%H %s")
    for line in merge_log.splitlines():
        if not line.strip():
            continue

        commit_hash, message = line.split(" ", 1)

        pr_commits = git(
            "log", "--reverse", "--no-merges", "--format=%s",
            f"{commit_hash}^1..{commit_hash}^2",
        ).splitlines()
        first_line = pr_commits[0] if pr_commits else ""

        # Keys from the branch name / merge subject.
        message_keys = find_branch_keys(message, linear_issue_pattern)

        pr_has_key = bool(message_keys) or any(
            find_issue_keys(subject, linear_issue_pattern) for subject in pr_commits
        )

        if not pr_has_key:
            if re.search(rf"from \S+/{re.escape(to_ref)}$", message):
                continue

            pr_match = re.search(r"#(\d+)", message)
            pr_url = (
                f"https://github.com/{repo}/pull/{pr_match.group(1)}"
                if pr_match else ""
            )
            title = first_line or message
            categorized.other.append(Issue("", title, pr_url, ""))
            continue

        # Branch-name-only tickets not already surfaced by a commit subject.
        # Prefer the branch's own type (feat/fwms-2326 -> Features); fall back
        # to the PR's first commit when the branch carries no type segment.
        btype = branch_type(message)
        for issue_key in message_keys:
            if issue_key in seen:
                continue
            seen.add(issue_key)
            if btype in ("feat", "feature"):
                categorized.features.append(Issue(issue_key, "", "", first_line))
            elif btype == "fix":
                categorized.fixes.append(Issue(issue_key, "", "", first_line))
            else:
                _categorize(categorized, issue_key, first_line)

    return categorized


def fetch_linear_issue(issue_key: str, api_key: str, linear_workspace: str) -> Issue:
    query = json.dumps({
        "query": f'{{ issue(id: "{issue_key}") {{ title url }} }}'
    })

    req = urllib.request.Request(
        LINEAR_GRAPHQL_URL,
        data=query.encode(),
        headers={
            "Authorization": api_key,
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())

            errors = data.get("errors")
            if errors:
                print(f"::warning::Linear GraphQL errors for {issue_key}: {errors}")
                title = ""
                url = ""
            else:
                issue_data = data.get("data", {}).get("issue") or {}
                title = issue_data.get("title", "")
                url = issue_data.get("url", "")
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        print(f"::warning::Could not fetch Linear issue {issue_key}: {exc}")
        title = ""
        url = ""

    if not title:
        title = issue_key
        url = f"https://linear.app/{linear_workspace}/issue/{issue_key}"

    return Issue(issue_key, title, url, "")


def enrich_with_linear(categorized: CategorizedIssues, api_key: str, linear_workspace: str) -> None:
    all_lists = [categorized.features, categorized.fixes, categorized.tech]
    for issue_list in all_lists:
        for issue in issue_list:
            enriched = fetch_linear_issue(issue.issue_key, api_key, linear_workspace)
            issue.title = enriched.title
            issue.url = enriched.url
            time.sleep(0.2)


def _heading(level: int, text: str) -> dict:
    block_type = f"heading_{level}"
    return {
        "object": "block",
        "type": block_type,
        block_type: {
            "rich_text": [{"type": "text", "text": {"content": text}}],
        },
    }


def _bullet(issue: Issue) -> dict:
    rich_text: list[dict] = []
    if issue.issue_key:
        rich_text.append({
            "type": "text",
            "text": {"content": issue.issue_key, "link": {"url": issue.url}},
        })
        rich_text.append({
            "type": "text",
            "text": {"content": f": {issue.title}"},
        })
    elif issue.url:
        rich_text.append({
            "type": "text",
            "text": {"content": issue.title, "link": {"url": issue.url}},
        })
    else:
        rich_text.append({
            "type": "text",
            "text": {"content": issue.title},
        })
    if issue.commit_subject:
        rich_text.append({
            "type": "text",
            "text": {"content": f"\n{issue.commit_subject}"},
            "annotations": {"italic": True, "color": "gray"},
        })
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": rich_text},
    }


def build_section(emoji: str, title: str, issues: list[Issue]) -> list[dict]:
    if not issues:
        return []
    return [_heading(1, f"{emoji} {title}")] + [_bullet(issue) for issue in issues]


def build_notion_payload(
    categorized: CategorizedIssues,
    version: str,
    release_type: str,
    repo: str,
    pr_source: str,
    notion_database_id: str,
    today: str,
) -> dict:
    children: list[dict] = []
    children += build_section("✨", "Features", categorized.features)
    children += build_section("\U0001f41b", "Fixes", categorized.fixes)
    children += build_section("\U0001f527", "Technical Improvements", categorized.tech)
    children += build_section("\U0001f4e6", "Other Changes", categorized.other)

    pr_url = f"https://github.com/{repo}/pull/{pr_source}"
    children += [
        _heading(2, "Technical details"),
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [
                    {"type": "text", "text": {"content": "Mobile app changes: "}},
                ],
                "children": [
                    {
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "Go to prod",
                                        "link": {"url": pr_url},
                                    },
                                },
                            ],
                        },
                    },
                ],
            },
        },
    ]

    return {
        "parent": {"database_id": notion_database_id},
        "properties": {
            "Version": {"title": [{"type": "text", "text": {"content": version}}]},
            "Mobile app release type": {"select": {"name": release_type}},
            "Release date": {"date": {"start": today}},
            "Web plaftorm changes": {"checkbox": False},
        },
        "children": children,
    }


def create_notion_page(payload: dict, api_key: str) -> tuple[str, str]:
    body = json.dumps(payload).encode()

    req = urllib.request.Request(
        NOTION_API_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_API_VERSION,
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            return data.get("id", ""), data.get("url", "")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode()
        print(f"::error::Failed to create Notion page (HTTP {exc.code})")
        print("Payload sent:")
        print(json.dumps(payload, indent=2))
        print("Response:")
        try:
            print(json.dumps(json.loads(error_body), indent=2))
        except json.JSONDecodeError:
            print(error_body)
        sys.exit(1)


def append_blocks_to_page(page_id: str, blocks: list[dict], api_key: str) -> None:
    url = f"{NOTION_BLOCK_API_URL}/{page_id}/children"
    body = json.dumps({"children": blocks}).encode()

    req = urllib.request.Request(
        url,
        data=body,
        method="PATCH",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_API_VERSION,
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            resp.read()
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode()
        print(f"::error::Failed to append blocks to page {page_id} (HTTP {exc.code})")
        try:
            print(json.dumps(json.loads(error_body), indent=2))
        except json.JSONDecodeError:
            print(error_body)
        sys.exit(1)


def write_github_summary(version: str, release_type: str, today: str, page_url: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if not summary_path:
        return

    with open(summary_path, "a") as f:
        f.write("### Release notes created\n\n")
        f.write(f"**Version**: {version}\n")
        f.write(f"**Release type**: {release_type}\n")
        f.write(f"**Date**: {today}\n\n")
        f.write(f"[Open in Notion]({page_url})\n")


def write_github_output(page_id: str, page_url: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT", "")
    if not output_path:
        return

    with open(output_path, "a") as f:
        f.write(f"page_id={page_id}\n")
        f.write(f"page_url={page_url}\n")


def main() -> None:
    linear_api_key = os.environ["LINEAR_API_KEY"]
    notion_api_key = os.environ["NOTION_API_KEY"]
    version = os.environ["VERSION"]
    release_type = os.environ["RELEASE_TYPE"]
    pr_source = os.environ["PR_SOURCE"]
    repo = os.environ["REPO"]
    notion_database_id = os.environ["NOTION_DATABASE_ID"]
    linear_workspace = os.environ.get("LINEAR_WORKSPACE", "smartway")
    linear_issue_pattern = os.environ.get("LINEAR_ISSUE_PATTERN", r"[A-Z]{2,10}-\d+")
    from_ref = os.environ.get("FROM_REF", "main")
    to_ref = os.environ.get("TO_REF", "develop")
    today = date.today().isoformat()

    print(f"Extracting issues from merge commits between {from_ref} and {to_ref}...")
    categorized = extract_categorized_issues(from_ref, to_ref, repo, linear_issue_pattern)

    print(f"Features: {[i.issue_key for i in categorized.features] or 'none'}")
    print(f"Fixes:    {[i.issue_key for i in categorized.fixes] or 'none'}")
    print(f"Tech:     {[i.issue_key for i in categorized.tech] or 'none'}")
    print(f"Other:    {[i.title for i in categorized.other] or 'none'}")

    total = len(categorized.features) + len(categorized.fixes) + len(categorized.tech)
    if total == 0:
        print(f"::warning::No Linear issues found in merge commits between {from_ref} and {to_ref}")

    print("Fetching Linear issue details...")
    enrich_with_linear(categorized, linear_api_key, linear_workspace)

    print("Building Notion page...")
    payload = build_notion_payload(
        categorized, version, release_type, repo, pr_source, notion_database_id, today
    )

    all_children = payload.pop("children", [])
    payload["children"] = all_children[:NOTION_BLOCK_LIMIT]

    page_id, page_url = create_notion_page(payload, notion_api_key)

    remaining = all_children[NOTION_BLOCK_LIMIT:]
    for i in range(0, len(remaining), NOTION_BLOCK_LIMIT):
        batch = remaining[i:i + NOTION_BLOCK_LIMIT]
        print(f"Appending {len(batch)} additional blocks...")
        append_blocks_to_page(page_id, batch, notion_api_key)

    print(f"::notice::Release notes created: {page_url}")

    write_github_summary(version, release_type, today, page_url)
    write_github_output(page_id, page_url)


if __name__ == "__main__":
    main()
