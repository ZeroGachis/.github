# GitHub Release Please Workflow

This workflow automates the release process using Google's Release Please action, which implements the Conventional Commits specification to automate version management and changelog generation.

## Triggers

This workflow can be triggered in two ways:
- **Workflow Call**: As a reusable workflow from other workflows
- **Push Event**: Automatically runs on pushes to the `main` branch

## Usage

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v4
    with:
      release_type: node
      major_and_minor_tags: true
```

## Inputs

### Optional Inputs

| Input                          | Default                         | Description                                    |
| ------------------------------ | ------------------------------- | ---------------------------------------------- |
| `major_and_minor_tags`         | `true`                          | Whether to create major and minor version tags |
| `release_type`                 | -                               | Type of release (e.g., node, python)           |
| `release_please_config_file`   | `release-please-config.json`    | Path to Release Please config file             |
| `release_please_manifest_file` | `.release-please-manifest.json` | Path to Release Please manifest file           |
| `target_branch`                | `main`                          | Target branch for the release                  |

## Outputs

| Output            | Description                           |
| ----------------- | ------------------------------------- |
| `release_created` | Whether a release was created         |
| `release_number`  | The version number of the new release |

## Features

- 🔄 Automated version bumping
- 📝 Changelog generation
- 🏷️ Automatic tag creation
- 🔖 Major/minor version tagging
- 🤖 Pull request creation
- 📦 Release automation
- 🔐 GitHub App authentication

## Technical Details

### Authentication

The workflow uses GitHub App authentication for enhanced security and rate limits:
- Generates a GitHub App token using `actions/create-github-app-token@v1`
- Falls back to public app credentials if organization app is not available
- Uses secrets: `SW_BOT_APP_ID`, `SW_BOT_APP_PRIVATE_KEY` (or their `_PUBLIC_` variants)

### Release Process

1. **Token Generation**: Creates a GitHub App token with appropriate permissions
2. **Code Checkout**: Checks out the repository with the generated token
3. **Release Please**: Runs the Release Please action with the specified configuration
4. **Version Tagging**: Optionally creates major and minor version tags

### Major and Minor Version Tagging

When `major_and_minor_tags` is set to `true`, the workflow:
- Deletes existing major and minor version tags (if any)
- Creates new tags for the major version (e.g., `v5`)
- Creates new tags for the major.minor version (e.g., `v5.1`)
- Pushes the new tags to the repository

This allows users to reference workflows using simplified version tags like `@v5` instead of full semantic versions.

## Permissions Required

- `contents: write` - For creating releases and tags
- `pull-requests: write` - For creating release PRs

## Example Usage

### Basic Usage

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v6
    secrets: inherit
    with:
      release_type: node
```

### With Custom Configuration

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v6
    secrets: inherit
    with:
      release_type: python
      major_and_minor_tags: true
      release_please_config_file: .release-please/config.json
      target_branch: develop
```

### Disable Major/Minor Tags

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v6
    secrets: inherit
    with:
      release_type: node
      major_and_minor_tags: false
```

### Full Pipeline with Outputs

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v6
    secrets: inherit
    with:
      release_type: node
  
  deploy:
    needs: release
    if: needs.release.outputs.release_created == 'true'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy new release
        run: |
          echo "Deploying version ${{ needs.release.outputs.release_number }}"
          # Add deployment steps here
```

## Configuration Files

### release-please-config.json

Example configuration file:

```json
{
  "packages": {
    ".": {
      "release-type": "node",
      "package-name": "my-package",
      "changelog-path": "CHANGELOG.md"
    }
  }
}
```

### .release-please-manifest.json

Example manifest file:

```json
{
  ".": "1.0.0"
}
```

## Related Documentation

- [Release Please Documentation](https://github.com/googleapis/release-please)
- [Conventional Commits Specification](https://www.conventionalcommits.org/)
