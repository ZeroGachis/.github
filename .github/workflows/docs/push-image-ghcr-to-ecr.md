# Push Image from GHCR to ECR Workflow

This workflow automates the process of transferring Docker images from GitHub Container Registry (GHCR) to Amazon Elastic Container Registry (ECR), with support for multiple tags and environments.

## Usage

```yaml
jobs:
  push:
    uses: ZeroGachis/.github/.github/workflows/push-image-ghcr-to-ecr.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      image_name: my-app
      releasetag: v1.0.0
      environment_name: production
    secrets: inherit
```

## Inputs

### Required Inputs

| Input              | Description             |
| ------------------ | ----------------------- |
| `image_url`        | Source GHCR image URL   |
| `image_name`       | Name for the ECR image  |
| `releasetag`       | Tag for the release     |
| `environment_name` | Target environment name |

### Optional Inputs

| Input                  | Default              | Description                        |
| ---------------------- | -------------------- | ---------------------------------- |
| `ecr_url`              | -                    | Custom ECR registry URL            |
| `ecr_repository_name`  | -                    | Custom ECR repository name         |
| `additional_tags`      | -                    | Comma-separated list of extra tags |
| `aws_account_id`       | -                    | AWS account ID                     |
| `aws_region`           | -                    | AWS region                         |
| `aws_github_role_name` | github_oidc_readonly | AWS IAM role for GitHub Actions    |

## Features

- 🔄 Automated image transfer
- 📦 Multi-tag support
- 🔒 Secure authentication
- 🏷️ Version management
- 🌐 Multi-environment support
- ☁️ AWS integration

## Example Usage

### Basic Usage

```yaml
jobs:
  push:
    uses: ZeroGachis/.github/.github/workflows/push-image-ghcr-to-ecr.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      image_name: my-app
      releasetag: v1.0.0
      environment_name: production
    secrets: inherit
```

### With Additional Tags

```yaml
jobs:
  push:
    uses: ZeroGachis/.github/.github/workflows/push-image-ghcr-to-ecr.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      image_name: my-app
      releasetag: v1.0.0
      environment_name: production
      additional_tags: latest,stable,v1
    secrets: inherit
```

### Custom ECR Configuration

```yaml
jobs:
  push:
    uses: ZeroGachis/.github/.github/workflows/push-image-ghcr-to-ecr.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      image_name: my-app
      releasetag: v1.0.0
      environment_name: production
      ecr_url: 123456789012.dkr.ecr.eu-west-3.amazonaws.com
      ecr_repository_name: custom/my-app
      aws_account_id: "123456789012"
      aws_region: eu-west-3
    secrets: inherit
```
