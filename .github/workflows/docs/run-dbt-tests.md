# DBT Tests Runner Workflow

This workflow provides an environment for running DBT tests with Snowflake integration, including schema management and test execution.

## Usage

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-dbt-tests.yml@v4
    with:
      project_dir: smartway
      snowflake_dbt_schema: dbt_ci
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
| `snowflake_dbt_schema`   | `dbt_ci`         | Schema name for DBT tests                      |
| `project_dir`            | `smartway`        | Project directory containing DBT files         |
| `aws_github_role_name`   | `github_oidc_readonly` | AWS IAM role name for GitHub Actions     |
| `aws_account_id`         | -                 | AWS account ID                                 |
| `environment_name`       | -                 | Target environment name [target branch]       |
| `python_version`         | `"3.12"`          | Python version to use                         |

## Features

- 🧪 Automated DBT test execution
- ❄️ Snowflake integration
- 🔐 Vault secrets management
- 🔄 GitHub Actions integration
- 🧹 Automatic test schema cleanup
- 📊 Pre-commit checks with dbt-checkpoint

## Example Usage

### With AWS Credentials and Custom Environment

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-dbt-tests.yml@v4
    with:
      aws_credentials_enabled: true
      project_dir: smartway
      snowflake_dbt_schema: dbt_custom_schema
      environment_name: main
      aws_github_role_name: custom_role
      aws_account_id: "123456789012"
```

### In a Complete CI Pipeline

```yaml
name: DBT CI Pipeline

on:
  pull_request:
    branches: [main]

jobs:
  dbt-tests:
    uses: ZeroGachis/.github/.github/workflows/run-dbt-tests.yml@v4
    with:
      project_dir: smartway
      snowflake_dbt_schema: dbt_ci
      environment_name: main
      python_version: "3.12"
    secrets: inherit
``` 