# Docker with Artifact Upload Workflow

This workflow provides a Docker execution environment with the ability to upload execution artifacts to GitHub Actions, combining container-based execution with artifact preservation.

## Usage

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/run-docker-upload-artifact.yml@v4
    with:
      image_url: ghcr.io/zerogachis/builder:latest
      workdir: /app
      run_command: "npm run build"
      artifact_name: "dist-files"
      artifact_path: "dist/"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input           | Description                            |
| --------------- | -------------------------------------- |
| `image_url`     | Docker image URL to use                |
| `workdir`       | Working directory inside the container |
| `run_command`   | Command to execute in the container    |
| `artifact_name` | Name for the uploaded artifact         |
| `artifact_path` | Path to files to upload as artifact    |

### Optional Inputs

| Input                        | Default | Description                 |
| ---------------------------- | ------- | --------------------------- |
| `env_django_settings_module` | -       | Django settings module path |
| `aws_credentials_enabled`    | `false` | Enable AWS credentials      |
| `checkout_enabled`           | `true`  | Enable repository checkout  |
| `vault_enabled`              | `true`  | Enable Vault integration    |
| `environment_name`           | -       | Target environment name     |
| `tailscale_enabled`          | `true`  | Enable Tailscale VPN        |
| `vault_secrets`              | -       | Vault secrets to import     |

## Features

- 📦 Artifact upload capability
- 🐳 Docker container execution
- 🔒 Secure credential management
- 🔑 Vault secret integration
- 🌐 Tailscale VPN support
- ☁️ AWS credentials support

## Example Usage

### Basic Build and Upload

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/run-docker-upload-artifact.yml@v4
    with:
      image_url: ghcr.io/zerogachis/node-builder:latest
      workdir: /app
      run_command: |
        npm ci
        npm run build
      artifact_name: "production-build"
      artifact_path: "dist/"
```

### With AWS Integration

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/run-docker-upload-artifact.yml@v4
    with:
      image_url: ghcr.io/zerogachis/aws-builder:latest
      workdir: /app
      run_command: "npm run build:aws"
      artifact_name: "lambda-package"
      artifact_path: "lambda/"
      aws_credentials_enabled: true
      environment_name: staging
```

### With Vault Secrets

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/run-docker-upload-artifact.yml@v4
    with:
      image_url: ghcr.io/zerogachis/secure-builder:latest
      workdir: /app
      run_command: "npm run build:secure"
      artifact_name: "secure-build"
      artifact_path: "build/"
      vault_enabled: true
      vault_secrets: |
        secret/data/build/keys BUILD_KEY | BUILD_KEY
        secret/data/build/config CONFIG | BUILD_CONFIG
```
