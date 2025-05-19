# DBT Manifest Upload Workflow

This workflow handles the compilation and uploading of DBT manifest files to S3, with support for Snowflake integration and secure secret management.

## Usage

```yaml
jobs:
  upload:
    uses: ZeroGachis/.github/.github/workflows/upload-dbt-manifest.yml@v4
    with:
      project_dir: smartway
      environment_name: develop
    secrets: inherit
```

## Inputs

### Required Inputs

None - All inputs have default values.

### Optional Inputs

| Input                     | Default           | Description                                    |
| ------------------------- | ----------------- | ---------------------------------------------- |
| `aws_credentials_enabled` | `false`          | Enable AWS credentials configuration           |
| `snowflake_dbt_schema`   | `dbt_ci`         | Schema name for DBT compilation                |
| `project_dir`            | `smartway`        | Project directory containing DBT files         |
| `aws_github_role_name`   | `github_oidc`     | AWS IAM role name for GitHub Actions          |
| `aws_account_id`         | -                 | AWS account ID                                 |
| `environment_name`       | -                 | Target environment name                        |
| `python_version`         | `"3.12"`          | Python version to use                         |

## Features

- 📦 Automated DBT manifest compilation
- 🚀 S3 upload integration
- ❄️ Snowflake integration
- 🔐 Vault secrets management
- 🔄 GitHub Actions integration
- 📊 Poetry dependency management

## Example Usage

### Basic Manifest Upload

```yaml
jobs:
  upload-manifest:
    uses: ZeroGachis/.github/.github/workflows/upload-dbt-manifest.yml@v4
    with:
      project_dir: smartway
      environment_name: ${{ github.ref_name }}
```

### With AWS Credentials and Custom Environment

```yaml
jobs:
  upload-manifest:
    uses: ZeroGachis/.github/.github/workflows/upload-dbt-manifest.yml@v4
    with:
      aws_credentials_enabled: true
      project_dir: smartway
      environment_name: main
      aws_github_role_name: custom_role
      aws_account_id: "123456789012"
```

### In a Complete CI Pipeline

```yaml
name: DBT Manifest Pipeline

on:
  push:
    branches: [main]

jobs:
  tests:
    uses: ZeroGachis/.github/.github/workflows/run-dbt-tests.yml@v4
    with:
      project_dir: smartway
    secrets: inherit

  upload-manifest:
    needs: tests
    uses: ZeroGachis/.github/.github/workflows/upload-dbt-manifest.yml@v4
    with:
      project_dir: smartway
      environment_name: main
    secrets: inherit
```

## Process Overview

1. Sets up Python environment with Poetry
2. Configures AWS credentials (if enabled)
3. Installs DBT dependencies
4. Compiles DBT manifest
5. Compresses manifest file
6. Uploads to specified S3 bucket 