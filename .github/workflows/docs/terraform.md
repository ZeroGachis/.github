# Terraform Workflow

This reusable workflow manages infrastructure deployments using Terraform, with support for multiple environments, and security integrations.

## Usage

```yaml
jobs:
  deploy:
    uses: ZeroGachis/.github/.github/workflows/terraform.yml@v4
    with:
      workdir: terraform/
      terraform_workspace: production
    secrets: inherit
```

## Inputs

### Optional Inputs

| Input                           | Default                   | Description                                          |
| ------------------------------- | ------------------------- | ---------------------------------------------------- |
| `workdir`                       | `${{ github.workspace }}` | Working directory containing Terraform configuration |
| `terraform_check_only`          | `true`                    | Only run plan without applying changes               |
| `environment_name`              | -                         | Target environment name                              |
| `terraform_workspace`           | `${{ github.ref_name }}`  | Terraform workspace to use                           |
| `terraform_parallelism`         | "10"                      | Number of parallel operations                        |
| `terraform_backend`             | -                         | Backend configuration                                |
| `terraform_args`                | -                         | Additional Terraform arguments                       |
| `aws_account_id`                | -                         | AWS account ID                                       |
| `aws_region`                    | -                         | AWS region                                           |
| `aws_github_role_name`          | "github_oidc_readonly"    | AWS IAM role for GitHub Actions                      |
| `vault_enabled`                 | `true`                    | Enable Vault integration                             |
| `vault_url`                     | -                         | Vault server URL                                     |
| `vault_github_actions_role`     | -                         | Vault role for authentication                        |
| `vault_secrets`                 | -                         | Additional Vault secrets to fetch                    |
| `aws_secrets`                   | -                         | AWS Secrets Manager secrets to fetch                 |
| `aws_additional_secrets`        | -                         | Additional AWS secrets to fetch                      |
| `tailscale_enabled`             | `true`                    | Enable Tailscale VPN                                 |
| `argocd_enabled`                | `false`                   | Enable ArgoCD sync after apply                       |
| `argocd_server`                 | -                         | ArgoCD server URL                                    |

## Features

- 🔒 Secure credential management with Vault and AWS
- 🔄 Automated state management
- 📝 Terraform formatting and validation
- 🏗️ Plan and apply capabilities
- 🌐 Multi-environment support
- 🔑 Private module access

## Example Usage

### Basic Plan Only

```yaml
jobs:
  plan:
    uses: ZeroGachis/.github/.github/workflows/terraform.yml@v4
    with:
      workdir: terraform/
      terraform_check_only: true
    secrets: inherit
```
