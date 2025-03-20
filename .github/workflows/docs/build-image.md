# BuildImage Workflow

This reusable workflow builds and pushes Docker images to a specified registry with security scanning and linting capabilities.

## Usage

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/build-image.yml@v4
    with:
      dockerfile_context: .
      regitry_url: ghcr.io
    secrets: inherit
```

## Inputs

### Required Inputs

| Input                | Description                                                        |
| -------------------- | ------------------------------------------------------------------ |
| `dockerfile_context` | The build context for Docker (directory containing the Dockerfile) |
| `regitry_url`        | The Docker registry URL where the image will be pushed             |

### Optional Inputs

| Input                         | Default                               | Description                                             |
| ----------------------------- | ------------------------------------- | ------------------------------------------------------- |
| `working-directory`           | -                                     | The working directory for the workflow                  |
| `regitry_username`            | -                                     | Registry username for authentication                    |
| `regitry_password`            | -                                     | Registry password for authentication                    |
| `image_name`                  | `${{ github.event.repository.name }}` | Name of the Docker image                                |
| `image_target`                | -                                     | Target stage to build in multi-stage Dockerfile         |
| `build-args`                  | -                                     | Build arguments passed to Docker build                  |
| `tailscale_enabled`           | `true`                                | Enable Tailscale VPN connection                         |
| `vault_enabled`               | `true`                                | Enable HashiCorp Vault integration                      |
| `vault_url`                   | -                                     | Vault server URL                                        |
| `vault_github_actions_role`   | -                                     | Vault role for GitHub Actions                           |
| `environment_name`            | -                                     | GitHub Environment name                                 |
| `linter_tool`                 | `hadolint`                            | Linter tool to use (hadolint/trivy)                     |
| `linter_filter_mode`          | `added`                               | Filter mode for Hadolint (added/diff/file/nofilter)     |
| `linter_fail_level`           | `error`                               | Minimum severity to fail the build (error/warning/info) |
| `security_scan_failed_build`  | `false`                               | Fail build on security scan issues                      |
| `security_scan_output_format` | `table`                               | The format used by the security scanner (table or sarif |
| `trivy_exit-code`             | `0`                                   | Job exits in error if an issue is found, 0 no, 1 yes    |
| `trivy_severity`              | `CRITICAL,HIGH`                       | Which security levels are scanned                       |

## Outputs

| Output          | Description                                    |
| --------------- | ---------------------------------------------- |
| `image-url`     | The full URL of the built image including tags |
| `image-version` | The version/tag of the built image             |

## Features

- 🔒 Automatic registry authentication (GitHub Packages & AWS ECR)
- 🔑 HashiCorp Vault integration for secrets management
- 🌐 Tailscale VPN support
- 📝 Dockerfile linting with Hadolint
- 🛡️ Security scanning with Anchore
- 🏗️ Docker BuildX for efficient builds
- 💾 GitHub Actions cache integration

## Example Usage

### Basic Usage

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/build-image.yml@v4
    with:
      dockerfile_context: .
      regitry_url: ghcr.io
    secrets: inherit
```

### Advanced Usage in Smartway context

```yaml
jobs:
  build:
    uses: ZeroGachis/.github/.github/workflows/build-image.yml@v4
    with:
      image_name: backoffice
      dockerfile_context: .
      vault_enabled: false
      tailscale_enabled: false
      regitry_url: ghcr.io
      security_scan_output_format: sarif
      trivy_exit-code: 1
      trivy_severity: 'CRITICAL,HIGH,MEDIUM'
    secrets: inherit
```
