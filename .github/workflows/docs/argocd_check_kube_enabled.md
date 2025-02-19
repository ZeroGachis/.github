# ArgoCD Check Kube Enabled Workflow

This workflow provides a conditional ArgoCD synchronization based on whether Kubernetes is enabled for a specific environment.

## Usage

```yaml
jobs:
  deploy:
    uses: ZeroGachis/.github/.github/workflows/argocd_check_kube_enabled.yml@v4
    with:
      app_name: my-application
      environment_name: production
    secrets: inherit
```

## Inputs

### Required Inputs

| Input              | Description                                |
| ------------------ | ------------------------------------------ |
| `app_name`         | Name of the ArgoCD application to sync     |
| `environment_name` | Environment to check for Kubernetes status |

## Features

- 🔍 Automatic Kubernetes enablement check
- 🔄 Conditional ArgoCD synchronization
- 🌐 Environment-specific configuration
- ⚡ Fast environment variable checking
- 🔗 Integration with ArgoCD sync workflow

## How It Works

1. **Environment Check**:

   - Checks the `kube_enabled` variable in the specified environment
   - Returns the status as a job output

2. **Conditional Execution**:
   - Only proceeds with ArgoCD sync if Kubernetes is enabled
   - Skips synchronization if Kubernetes is disabled
   - Provides clear status in the workflow logs

## Example Usage

### Basic Usage

```yaml
jobs:
  deploy:
    uses: ZeroGachis/.github/.github/workflows/argocd_check_kube_enabled.yml@v4
    with:
      app_name: my-service
      environment_name: staging
    secrets: inherit
```

### In a Complete Deployment Pipeline

```yaml
name: Deploy Application

on:
  push:
    branches:
      - main

jobs:
  build:
    uses: ./.github/workflows/build-image.yml
    with:
      dockerfile_context: .
      regitry_url: ghcr.io
    secrets: inherit

  deploy:
    needs: build
    uses: ZeroGachis/.github/.github/workflows/argocd_check_kube_enabled.yml@v4
    with:
      app_name: my-service
      environment_name: ${{ github.ref_name }}
    secrets: inherit
```

### With Multiple Environments

```yaml
name: Multi-Environment Deployment

on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Target environment"
        required: true
        type: choice
        options:
          - staging
          - production

jobs:
  deploy:
    uses: ZeroGachis/.github/.github/workflows/argocd_check_kube_enabled.yml@v4
    with:
      app_name: my-service
      environment_name: ${{ inputs.environment }}
    secrets: inherit
```
