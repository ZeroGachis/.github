# Python Package Publishing Workflow

This workflow automates the process of building and publishing Python packages to AWS CodeArtifact, ensuring consistent and secure package distribution.

## Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/python-publish.yml@v4
    with:
      environment_name: staging
```

## Inputs

### Required Inputs

| Input              | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| `environment_name` | Target environment for package publishing (e.g., staging, production) |

### Optional Inputs

| Input            | Description                                       | Default |
| ---------------- | ------------------------------------------------- | ------- |
| `python_version` | Python version to use for building and publishing | `3.11`  |
| `aws_account_id` | AWS account ID for CodeArtifact repository        | -       |
| `aws_region`     | AWS region for CodeArtifact repository            | -       |

## Features

- 🐍 Poetry package management
- 🔐 Secure AWS CodeArtifact integration
- 🔄 Automated build and publish process
- 📦 Package version management
- 🔑 Secure credential handling
- 🌐 Multi-environment support

## Example Usage

### Basic Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/python-publish.yml@v4
    with:
      environment_name: staging
```

### Custom Python Version

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/python-publish.yml@v4
    with:
      environment_name: production
      python_version: "3.10"
```

### Custom AWS Configuration

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/python-publish.yml@v4
    with:
      environment_name: staging
      aws_account_id: "123456789012"
      aws_region: "eu-west-1"
```
