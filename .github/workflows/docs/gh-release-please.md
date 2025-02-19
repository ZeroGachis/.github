# GitHub Release Please Workflow

This workflow automates the release process using Google's Release Please action, which implements the Conventional Commits specification to automate version management and changelog generation.

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

## Example Usage

### Basic Usage

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v4
    with:
      release_type: node
```

### With Custom Configuration

```yaml
jobs:
  release:
    uses: ZeroGachis/.github/.github/workflows/gh-release-please.yml@v4
    with:
      release_type: python
      major_and_minor_tags: true
      release_please_config_file: .release-please/config.json
      target_branch: develop
```
