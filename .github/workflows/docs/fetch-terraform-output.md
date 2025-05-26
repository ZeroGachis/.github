
# Fetch Terraform Output GitHub Action

This reusable GitHub Actions workflow fetches a single output variable from a Terraform remote state file. It's designed to be called from other workflows to retrieve specific Terraform output values.

## Usage

To use this workflow in your GitHub Actions, call it using the `workflow_call` trigger:

```yaml
jobs:
  get-terraform-output:
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable: "my_output_variable"
      # ... other optional inputs
```

## Inputs

| Input | Required | Type | Default | Description |
|-------|----------|------|---------|-------------|
| `variable` | ✅ | string | - | The name of the variable to fetch from the Terraform state file |
| `workdir` | ❌ | string | `${{ github.workspace }}` | Working directory where Terraform files are located |
| `environment_name` | ❌ | string | - | GitHub environment name to use for the job |
| `terraform_workspace` | ❌ | string | `${{ github.ref_name }}` | Terraform workspace to select |
| `terraform_backend` | ❌ | string | - | S3 bucket name for Terraform backend (defaults to `tfstate-{AWS_ACCOUNT_ID}`) |
| `tailscale_enabled` | ❌ | boolean | `true` | Whether to connect to Tailscale VPN |
| `vault_enabled` | ❌ | boolean | `true` | Whether to authenticate with HashiCorp Vault |
| `aws_github_role_name` | ❌ | string | `"github_oidc_readonly"` | AWS IAM role name for GitHub OIDC authentication |

## Outputs

| Output | Description |
|--------|-------------|
| `TF_OUTPUT_VAR` | The value of the specified Terraform output variable |

## Required Environment Variables

The workflow expects the following variables to be configured in your GitHub repository or environment:

### Vault Configuration (if `vault_enabled: true`)
- `VAULT_URL` or `PULLREQUEST_VAULT_URL`: HashiCorp Vault server URL
- `VAULT_GITHUB_ACTIONS_ROLE`: Vault role for GitHub Actions authentication

### AWS Configuration
- `AWS_ACCOUNT_ID` or `PULL_REQUEST_AWS_ACCOUNT_ID`: AWS account ID
- `AWS_REGION` or `AWS_DEFAULT_REGION`: AWS region

### Terraform Configuration
- `TF_VERSION`: Terraform version to use

### Tailscale Configuration (if `tailscale_enabled: true`)
- `TAILSCALE_VERSION`: Tailscale version to use

## Required Secrets

### Tailscale (if `tailscale_enabled: true`)
- `TS_OAUTH_CLIENT_ID`: Tailscale OAuth client ID
- `TS_OAUTH_SECRET`: Tailscale OAuth client secret

## Prerequisites

1. **AWS OIDC Setup**: Your repository must be configured for AWS OIDC authentication with the specified IAM role
2. **Terraform Backend**: Your Terraform configuration should use an S3 backend
3. **Vault Access** (optional): If using Vault, ensure proper authentication is configured
4. **Tailscale** (optional): If using Tailscale, ensure OAuth credentials are configured

## Example Usage

### Basic Usage

```yaml
jobs:
  fetch-output:
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable: "vpc_id"

  use-output:
    needs: fetch-output
    runs-on: ubuntu-latest
    steps:
      - name: Use Terraform output
        run: echo "VPC ID is ${{ needs.fetch-output.outputs.TF_OUTPUT_VAR }}"
```

### Advanced Usage with Custom Configuration

```yaml
jobs:
  fetch-output:
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable: "database_endpoint"
      workdir: "./infrastructure"
      environment_name: "production"
      terraform_workspace: "prod"
      terraform_backend: "my-custom-tfstate-bucket"
      tailscale_enabled: false
      vault_enabled: false
      aws_github_role_name: "custom-github-role"
```

## Workflow Steps

The workflow performs the following steps:

1. **Tailscale Connection** (optional): Connects to Tailscale VPN if enabled
2. **DNS Resolution Check** (if Vault enabled): Verifies Vault server DNS resolution
3. **Vault Authentication** (optional): Authenticates with HashiCorp Vault and imports secrets
4. **Terraform Setup**: Installs the specified Terraform version
5. **Code Checkout**: Checks out the repository code
6. **AWS Authentication**: Configures AWS credentials using OIDC
7. **Terraform Initialization**: Initializes Terraform with the specified backend
8. **Workspace Selection**: Selects the specified Terraform workspace
9. **Output Export**: Exports Terraform outputs to JSON
10. **Variable Extraction**: Extracts the requested variable and sets it as output

## Error Handling

- DNS resolution for Vault is retried up to 100 times with 15-second intervals
- The workflow will fail if required variables or secrets are not properly configured
- Terraform errors during init, workspace selection, or output export will cause the workflow to fail

## Security Considerations

- Uses AWS OIDC for secure authentication without long-lived credentials
- Vault tokens are exported for use in subsequent steps if Vault is enabled
- Tailscale provides secure network access to private resources
- The workflow runs with read-only permissions by default
