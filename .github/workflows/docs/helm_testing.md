# Helm Testing Workflow

This workflow provides automated testing for Helm charts, ensuring they pass linting checks using the chart-testing (ct) tool.

## Usage

```yaml
jobs:
  test-charts:
    uses: ZeroGachis/.github/.github/workflows/helm_testing.yaml@v4
    with:
      charts_root_dir: "charts"
```

## Inputs

### Inputs

| Input             | Type   | Description                              | Required |
| ----------------- | ------ | ---------------------------------------- | -------- |
| `charts_root_dir` | string | Directory containing Helm charts to test | Yes      |
| `target_branch`   | string | Target branch to compare changes against | No       |

## Features

- 📊 Automated Helm chart testing
- ✅ Chart linting validation
- 📝 Detailed test reports
- 🚀 Works as a reusable workflow

## Example Usage

### Basic Usage

```yaml
jobs:
  test-charts:
    uses: ZeroGachis/.github/.github/workflows/helm_testing.yaml@v4
    with:
      charts_root_dir: "charts"
```

### Custom Chart Directory

```yaml
jobs:
  test-charts:
    uses: ZeroGachis/.github/.github/workflows/helm_testing.yaml@v4
    with:
      charts_root_dir: "helm-charts/services"
```

### Specific Target Branch

```yaml
jobs:
  test-charts:
    uses: ZeroGachis/.github/.github/workflows/helm_testing.yaml@v4
    with:
      charts_root_dir: "charts"
      target_branch: "main"
```

## How It Works

1. The workflow can be called from other workflows
2. Sets up Helm, Python, and chart-testing tools
3. Runs chart-testing linting against the specified charts directory
4. Validates charts against best practices and requirements

## Implementation Details

The workflow includes the following steps:

1. **Checkout code** - Fetches repository content with full history
2. **Install Helm** - Sets up Helm CLI tools
3. **Setup Python** - Installs Python environment for testing
4. **Setup chart-testing** - Installs the chart-testing (ct) tool
5. **Run linting** - Executes linting checks on Helm charts

## Security

The workflow runs with minimal permissions:

- `contents: read` - Read access to repository contents
