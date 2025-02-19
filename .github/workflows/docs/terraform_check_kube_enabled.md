# Terraform Check Kubernetes Enabled Workflow

This workflow validates whether Kubernetes features are enabled in a Terraform configuration, ensuring proper infrastructure setup for Kubernetes deployments.

## Usage

```yaml
jobs:
  check:
    uses: ZeroGachis/.github/.github/workflows/terraform_check_kube_enabled.yml@v4
    with:
      environment_name: production
      terraform_dir: terraform/environments/prod
    secrets: inherit
```

## Inputs

### Required Inputs

| Input              | Description                                  |
| ------------------ | -------------------------------------------- |
| `environment_name` | Target environment for the check             |
| `terraform_dir`    | Directory containing Terraform configuration |

### Optional Inputs

| Input                       | Default | Description                          |
| --------------------------- | ------- | ------------------------------------ |
| `vault_url`                 | -       | Vault server URL                     |
| `vault_github_actions_role` | -       | Role to use for Vault authentication |

## Features

- 🔍 Automated Kubernetes configuration validation
- 🏗️ Infrastructure verification
- 🔒 Secure credential management
- 📊 Detailed check reporting
- ⚡ Fast execution
- 🌐 Multi-environment support

## Example Usage

### Basic Check

```yaml
jobs:
  validate:
    uses: ZeroGachis/.github/.github/workflows/terraform_check_kube_enabled.yml@v4
    with:
      environment_name: staging
      terraform_dir: terraform/environments/staging
```
