# Android Format Version Code Workflow

This workflow generates formatted version codes for Android applications based on GitHub Actions run numbers.

## Usage

```yaml
jobs:
  version:
    uses: ZeroGachis/.github/.github/workflows/android-format-version-code.yml@v4
```

## Outputs

| Output         | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `version-code` | Formatted version code in octal format from the run number |

## Example Usage

### Basic Usage

```yaml
jobs:
  version:
    uses: ZeroGachis/.github/.github/workflows/android-format-version-code.yml@v4
```

### Using the Version Code in Android Build

```yaml
jobs:
  version:
    uses: ZeroGachis/.github/.github/workflows/android-format-version-code.yml@v4

  build:
    needs: version
    runs-on: ubuntu-latest
    steps:
      - name: Build Android App
        run: |
          ./gradlew assembleRelease \
            -PversionCode=${{ needs.version.outputs.version-code }}
```
