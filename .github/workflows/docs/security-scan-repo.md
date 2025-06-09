# Security Scan Repo Workflow

This workflow automatically scans repositories for security vulnerabilities when pull requests are opened, synchronized, or reopened. It uses Trivy to perform the scan and uploads the results to GitHub's code scanning interface.

## Usage

```yaml
jobs:
  security_scan:
    uses: ZeroGachis/.github/.github/workflows/security_scan_repo.yml@v4
```

## Trigger Events

The workflow is triggered on the following pull request events:

- `opened`: When a new pull request is created
- `synchronize`: When new commits are pushed to the pull request
- `reopened`: When a closed pull request is reopened

## Permissions

| Permission        | Level | Description                              |
| ----------------- | ----- | ---------------------------------------- |
| `contents`        | read  | Required to checkout the repository      |
| `pull-requests`   | write | Required to comment on pull requests     |
| `security-events` | write | Required to upload security scan results |
| `checks`          | write | Required to create check runs            |
| `actions`         | read  | Required to read workflow metadata       |

## Features

- 🔍 Automated security scanning of repository code
- 🛡️ Integration with GitHub's code scanning interface
- 💬 Automatic PR comments with scan results
- 📊 SARIF format output for detailed vulnerability reporting
- 🔄 Continuous scanning on PR updates

## Workflow Steps

1. **Checkout**: Clones the repository code
2. **Security Scan**: Runs Trivy to scan the filesystem for vulnerabilities
3. **Edit Trivy Sarif result**: Modifies the SARIF output to set the tool name
4. **Comment PR**: Adds a comment to the PR with a link to the scan results
5. **Upload security scan report**: Uploads the SARIF results to GitHub's code scanning interface

## Output

The workflow produces:

- A SARIF file containing detailed security scan results
- A comment on the pull request with a link to the scan results
- Security scan results visible in the repository's Security tab
