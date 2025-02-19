# ArgoCD Sync Workflow

This reusable workflow synchronizes applications with ArgoCD, providing automated deployment capabilities through GitOps practices.

## Usage

```yaml
jobs:
  sync:
    uses: ZeroGachis/.github/.github/workflows/argocd_sync.yml@v4
    with:
      app_name: my-application
      environment_name: production
    secrets: inherit
```

## Inputs

### Required Inputs

| Input      | Description                            |
| ---------- | -------------------------------------- |
| `app_name` | Name of the ArgoCD application to sync |

### Optional Inputs

| Input                       | Default | Description                          |
| --------------------------- | ------- | ------------------------------------ |
| `argocd_server`             | -       | ArgoCD server URL                    |
| `environment_name`          | -       | Target environment for deployment    |
| `vault_url`                 | -       | Vault server URL for secrets         |
| `vault_github_actions_role` | -       | Role to use for Vault authentication |

## Features

- 🔄 Automated application synchronization
- 🔒 Secure authentication with ArgoCD
- 🔑 HashiCorp Vault integration
- 🌐 Tailscale VPN support
- ⏱️ Timeout protection (15 minutes)

## Example Usage

### Basic Usage

```yaml
jobs:
  sync:
    uses: ZeroGachis/.github/.github/workflows/argocd_sync.yml@v4
    with:
      app_name: my-service
      environment_name: staging
    secrets: inherit
```

### Advanced Usage with Custom Configuration

```yaml
jobs:
  sync:
    uses: ZeroGachis/.github/.github/workflows/argocd_sync.yml@v4
    with:
      app_name: my-service
      environment_name: production
      argocd_server: https://argocd.example.com
      vault_url: https://vault.example.com
      vault_github_actions_role: github-production
    secrets: inherit
```

### Usage with ArgoCD Check

For environments where you want to conditionally sync based on whether Kubernetes is enabled:

```yaml
jobs:
  deploy:
    uses: ZeroGachis/.github/.github/workflows/argocd_check_kube_enabled.yml@v4
    with:
      app_name: my-service
      environment_name: production
    secrets: inherit
```

## Technical Details

1. The workflow includes DNS resolution checks to ensure connectivity to ArgoCD server
2. Uses Homebrew to install the ArgoCD CLI
3. Performs both sync and wait operations to ensure successful deployment
4. Integrates with GitHub Environments for deployment tracking
5. Supports GRPC web communication with ArgoCD server
