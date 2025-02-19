# .NET Publish Workflow

This workflow automates the publishing of .NET packages to both AWS CodeArtifact and the public NuGet registry, with support for secure credential management and version control.

## Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/dotnet-publish.yml@v4
    with:
      package_to_publish: MyPackage
      package_version: 1.0.0
    secrets: inherit
```

## Inputs

### Required Inputs

| Input                | Description                   |
| -------------------- | ----------------------------- |
| `package_to_publish` | The package name to publish   |
| `package_version`    | The version of package to use |

### Optional Inputs

| Input                        | Default | Description                            |
| ---------------------------- | ------- | -------------------------------------- |
| `publish_to_public_registry` | `true`  | Whether to publish to public NuGet.org |
| `environment_name`           | "main"  | Target environment for deployment      |

## Features

- 📦 Multi-registry publishing
- 🔒 Secure credential management
- 🔄 AWS CodeArtifact integration
- 🌐 Public NuGet.org support
- 🔑 Vault secret integration
- 🏷️ Version management

## Example Usage

### Basic Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/dotnet-publish.yml@v4
    with:
      package_to_publish: MyLibrary
      package_version: 1.2.0
```

### Private Registry Only

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/dotnet-publish.yml@v4
    with:
      package_to_publish: InternalPackage
      package_version: 2.0.0
      publish_to_public_registry: false
```

## Environment Variables

The workflow uses several environment variables:

- `VAULT_ADDR`: Vault server address
- `VAULT_GITHUB_ACTIONS_ROLE`: GitHub Actions role for Vault
- `AWS_ACCOUNT_ID`: AWS account identifier
- `AWS_REGION`: AWS region for CodeArtifact
- `CODEARTIFACT_DOMAIN`: AWS CodeArtifact domain (default: smartway)
- `CODEARTIFACT_REPOSITORY`: Repository name (default: nuget-release)
