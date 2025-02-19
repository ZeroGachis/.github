# AWS Command Runner Workflow

This workflow provides a secure environment for executing AWS CLI commands with support for Vault secrets and Tailscale VPN integration.

## Usage

```yaml
jobs:
  run:
    uses: ZeroGachis/.github/.github/workflows/run-aws.yml@v4
    with:
      run_command: "aws s3 ls"
      vault_github_actions_role: "github-role"
      vault_secrets: "secret/data/aws credentials | AWS_CREDS"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input         | Description            |
| ------------- | ---------------------- |
| `run_command` | AWS command to execute |

### Optional Inputs

| Input                       | Default                | Description                     |
| --------------------------- | ---------------------- | ------------------------------- |
| `aws_region`                | -                      | AWS region for operations       |
| `aws_account_id`            | -                      | AWS account ID                  |
| `aws_github_role_name`      | "github_oidc_readonly" | AWS IAM role for GitHub Actions |
| `environment_name`          | -                      | Target environment name         |
| `tailscale_enabled`         | `true`                 | Enable Tailscale VPN            |
| `vault_enabled`             | `true`                 | Enable Vault integration        |
| `vault_url`                 | -                      | Vault server URL                |
| `vault_github_actions_role` | -                      | Role for Vault authentication   |
| `vault_secrets`             | -                      | Vault secrets to import         |

## Features

- 🔒 Secure AWS credentials management
- 🔑 HashiCorp Vault integration
- 🌐 Tailscale VPN support
- ☁️ AWS OIDC authentication
- 📝 Command execution logging
- 🔄 Environment variable support

## Example Usage

### Basic AWS Command

```yaml
jobs:
  list-buckets:
    uses: ZeroGachis/.github/.github/workflows/run-aws.yml@v4
    with:
      run_command: "aws s3 ls"
    secrets: inherit
```

### With Custom AWS Configuration

```yaml
jobs:
  describe-instances:
    uses: ZeroGachis/.github/.github/workflows/run-aws.yml@v4
    with:
      run_command: "aws ec2 describe-instances"
      aws_region: "eu-west-3"
      aws_account_id: "123456789012"
      aws_github_role_name: "github_admin"
      environment_name: production
    secrets: inherit
```

### With Vault Secrets

```yaml
jobs:
  access-secrets:
    uses: ZeroGachis/.github/.github/workflows/run-aws.yml@v4
    with:
      run_command: "aws secretsmanager get-secret-value --secret-id my-secret"
      vault_secrets: |
        secret/data/aws/credentials ACCESS_KEY | AWS_ACCESS_KEY
        secret/data/aws/credentials SECRET_KEY | AWS_SECRET_KEY
      environment_name: staging
    secrets: inherit
```
