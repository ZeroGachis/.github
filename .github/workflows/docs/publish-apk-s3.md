# Publish APK to S3 Workflow

This workflow automates the process of publishing Android APK artifacts to Amazon S3, with support for versioning and secure credential management.

## Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-apk-s3.yml@v4
    with:
      apk-artifact-name: "Release-APK"
      apk-name: "app-release.apk"
      apk-version: "1.0.0"
      vault-path: "path/to/secrets"
      s3-path: "releases/android"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input               | Description                             |
| ------------------- | --------------------------------------- |
| `apk-artifact-name` | Name of the artifact containing the APK |
| `apk-name`          | Name of the APK file                    |
| `apk-version`       | Version of the APK                      |
| `vault-path`        | Path to secrets in Vault                |
| `s3-path`           | Destination path in S3 bucket           |

### Optional Inputs

| Input                  | Default              | Description                     |
| ---------------------- | -------------------- | ------------------------------- |
| `vault-url`            | -                    | Vault server URL                |
| `vault-role`           | github-actions-role  | Role for Vault authentication   |
| `aws_account_id`       | -                    | AWS account ID                  |
| `aws_region`           | -                    | AWS region                      |
| `aws_github_role_name` | github_oidc_readonly | AWS IAM role for GitHub Actions |
| `environment_name`     | -                    | Target environment name         |

## Features

- 📱 APK artifact publishing
- 🔒 Secure credential management
- 🗄️ S3 storage integration
- 🔑 Vault secret integration
- 🌐 Tailscale VPN support
- 📦 Version management

## Example Usage

### Basic Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-apk-s3.yml@v4
    with:
      apk-artifact-name: "Release-APK"
      apk-name: "app-release.apk"
      apk-version: "1.0.0"
      vault-path: "mobile/android"
      s3-path: "releases/android"
    secrets: inherit
```

### With Custom AWS Configuration

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-apk-s3.yml@v4
    with:
      apk-artifact-name: "Release-APK"
      apk-name: "app-release.apk"
      apk-version: "1.0.0"
      vault-path: "mobile/android"
      s3-path: "releases/android"
      aws_account_id: "123456789012"
      aws_region: "eu-west-3"
      aws_github_role_name: "custom-role"
    secrets: inherit
```
