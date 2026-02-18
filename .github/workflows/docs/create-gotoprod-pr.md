# Create Go-To-Prod Pull Request Workflow

This workflow automates the creation of production deployment pull requests, including automatic reviewer assignment and comprehensive change documentation. It intelligently handles both PR creation and updates for existing PRs.

## Triggers

This workflow is designed to be called by other workflows using `workflow_call`.

## Usage

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v4
    with:
      base: main
```

## Inputs

### Optional Inputs

| Input  | Default | Description                      |
| ------ | ------- | -------------------------------- |
| `base` | `main`  | Base branch for the pull request |

## Features

- 🤖 Automated PR creation and updates
- 👥 Automatic reviewer assignment from contributors
- 📝 Comprehensive change documentation
- 🏷️ Automatic labeling with color coding
- 🔄 Smart PR update support
- 📊 Change categorization (Merged PRs vs Direct Commits)
- 🔐 GitHub App authentication
- 🛡️ Graceful error handling for reviewer assignment

## Technical Details

### Authentication

The workflow uses GitHub App authentication for enhanced security:
- Generates a GitHub App token using `actions/create-github-app-token@v1`
- Uses organization secrets: `SW_BOT_APP_ID` and `SW_BOT_APP_PRIVATE_KEY`
- Token provides appropriate permissions for PR and content operations

### Workflow Process

1. **Token Generation**: Creates a GitHub App token with necessary permissions
2. **Code Checkout**: Checks out the repository with the generated token
3. **PR Management**: Creates or updates existing PR using GitHub Scripts
4. **Change Analysis**: Compares branches to identify changes
5. **Contributor Identification**: Extracts unique contributors from commits
6. **Reviewer Assignment**: Requests reviews from all contributors (with graceful fallback)
7. **Documentation Generation**: Creates comprehensive PR description
8. **Labeling**: Applies color-coded labels for easy identification

### Smart PR Handling

The workflow checks for existing PRs:
- If an **existing PR** is found: Updates the title and description
- If **no PR exists**: Creates a new PR with complete documentation

### Contributor Extraction

The workflow identifies contributors by:
- Analyzing all commits in the PR
- Extracting both authors and committers
- Filtering out bot accounts (containing `[bot]`)
- Removing duplicates
- Attempting to assign them as reviewers (with error handling if they're not collaborators)

### Change Categorization

Changes are categorized into two types:
- **Merged Pull Requests**: Commits with multiple parents (merge commits)
- **Direct Commits**: Regular commits with single parent

## Permissions Required

- `contents: write` - For accessing repository content
- `pull-requests: write` - For creating and updating PRs

## Generated PR Structure

The workflow generates a pull request with the following structure:

```markdown
## 🚀 Automated PR to prepare Go-To-Production

**Branch**: `release/v6`
**Base**: `main`

### 🔍 Changes

#### 🔄 Merged Pull Requests

- Merge pull request #123 from feature/authentication
- Merge pull request #124 from fix/database-performance

#### 📝 Commits

- Update configuration files
- Fix typos in README
- Add new test cases

### 👥 Contributors

- @developer1
- @developer2
- @developer3
```

If no human contributors are found, the PR will display "No human contributors identified" instead of the contributor list.

## Labels

The workflow automatically adds and configures the following labels:

- `go-to-prod`: Identifies production deployment PRs (color: `ff7f00` - orange)
- `:robot: automated-pr`: Indicates automated creation

## Example Usage

### Basic Usage

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v6
    secrets: inherit
```

### With Custom Base Branch

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v6
    secrets: inherit
    with:
      base: production
```

### In a Deployment Pipeline

```yaml
name: Production Deployment

on:
  workflow_dispatch:
  schedule:
    - cron: "0 10 * * 1" # Every Monday at 10:00 UTC

jobs:
  tests:
    uses: ./.github/workflows/run-tests.yml

  create-pr:
    needs: tests
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v6
    secrets: inherit
    with:
      base: main
```

### With Release Workflow

```yaml
name: Release and Deploy

on:
  push:
    branches:
      - release/*

jobs:
  create-gotoprod-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v6
    secrets: inherit
    with:
      base: main
```

## Error Handling

The workflow includes robust error handling:

- **Reviewer Assignment**: Continues if some contributors cannot be assigned as reviewers
- **Label Creation**: Attempts to update label color, continues if label doesn't exist
- **PR Creation**: Logs errors but doesn't fail the workflow

Error messages are logged to the console for troubleshooting while maintaining workflow stability.

## Best Practices

1. **Branch Naming**: Use descriptive branch names (e.g., `release/v6`, `staging`)
2. **Base Branch**: Ensure the base branch is protected with required reviews
3. **Contributor Permissions**: Add frequent contributors as repository collaborators for automatic reviewer assignment
4. **Regular Updates**: Run the workflow regularly to keep PRs up-to-date
5. **Review Process**: Ensure all contributors review changes before merging to production

## Troubleshooting

### Contributors Not Added as Reviewers

If contributors aren't automatically added as reviewers:
- Check that they are repository collaborators
- Review workflow logs for specific error messages
- Contributors will still be listed in the PR description even if reviewer assignment fails

### PR Not Created

If the PR isn't created:
- Verify that the head branch differs from the base branch
- Check that the GitHub App has appropriate permissions
- Review workflow logs for authentication or API errors

### Labels Not Applied

If labels aren't applied:
- Ensure the repository allows label creation
- Check that the GitHub App token has `pull-requests: write` permission
- Labels will be created automatically if they don't exist

## Related Documentation

- [GitHub Actions Script Documentation](https://github.com/actions/github-script)
- [GitHub REST API - Pulls](https://docs.github.com/en/rest/pulls)
- [GitHub App Authentication](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app)
