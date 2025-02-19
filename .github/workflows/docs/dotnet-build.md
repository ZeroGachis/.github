# .NET Build Workflow

This workflow provides a comprehensive build and test pipeline for .NET projects, including code coverage reporting and package creation.

## Usage

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/dotnet-build.yml@v4
    with:
      solution_name: MySolution.sln
      solution_configuration: Release
    secrets: inherit
```

## Inputs

### Required Inputs

| Input           | Description                   |
| --------------- | ----------------------------- |
| `solution_name` | The project SLN file to build |

### Optional Inputs

| Input                     | Default   | Description                         |
| ------------------------- | --------- | ----------------------------------- |
| `dotnet_version`          | "8.0.x"   | .NET SDK version to use             |
| `solution_configuration`  | "Release" | Build configuration (Debug/Release) |
| `solution_version_suffix` | -         | Version suffix for the package      |
| `code_coverage_threshold` | "60 80"   | Min/max coverage thresholds         |
| `code_coverage_enabled`   | `true`    | Enable code coverage reporting      |

## Features

- 🏗️ Automated build process
- 🧪 Unit test execution
- 📊 Code coverage reporting
- 📦 NuGet package creation
- 🔄 GitHub Packages integration
- 📈 Test result reporting

## Example Usage

### Basic Usage

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/dotnet-build.yml@v4
    with:
      solution_name: MySolution.sln
```

### With Custom Configuration

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/dotnet-build.yml@v4
    with:
      solution_name: MySolution.sln
      dotnet_version: "7.0.x"
      solution_configuration: Debug
      code_coverage_threshold: "70 90"
```

### With Version Suffix

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/dotnet-build.yml@v4
    with:
      solution_name: MySolution.sln
      solution_version_suffix: "beta-1"
```
