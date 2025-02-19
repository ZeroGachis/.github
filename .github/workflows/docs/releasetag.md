# ReleaseTag Definition Workflow

This workflow generates a unique release tag based on the current timestamp, providing consistent and traceable version identifiers for releases.

## Usage

```yaml
jobs:
  tag:
    uses: ZeroGachis/.github/.github/workflows/releasetag.yml@v4
```

## Outputs

| Output       | Description                                           |
| ------------ | ----------------------------------------------------- |
| `releasetag` | Generated release tag in format `dd-mm-yyyy_hh-mm-ss` |

## Features

- 🕒 Timestamp-based versioning
- 🔄 Automatic tag generation
- 📅 Date-based tracking
- 🔍 Traceable releases
- 🏷️ Consistent formatting
- 🔗 Workflow integration

## Example Usage

### Basic Usage

```yaml
jobs:
  tag:
    uses: ZeroGachis/.github/.github/workflows/releasetag.yml@v4
```

### With Image Build

```yaml
jobs:
  tag:
    uses: ZeroGachis/.github/.github/workflows/releasetag.yml@v4

  build:
    needs: tag
    uses: ./.github/workflows/build-image.yml
    with:
      image_tag: ${{ needs.tag.outputs.releasetag }}
```
