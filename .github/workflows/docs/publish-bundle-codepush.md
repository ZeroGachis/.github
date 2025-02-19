# Publish Bundle to CodePush Workflow

This workflow automates the process of publishing React Native bundles to Microsoft's CodePush service for over-the-air updates, with support for multiple environments and secure credential management.

## Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-bundle-codepush.yml@v4
    with:
      node-version: "18.x"
      codepush-app: "MyApp/Production"
      apk-version: "1.0.0"
      vault-path: "mobile/codepush"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input          | Description                     |
| -------------- | ------------------------------- |
| `node-version` | Node.js version to use          |
| `codepush-app` | CodePush application identifier |
| `apk-version`  | Version of the app to target    |
| `vault-path`   | Path to secrets in Vault        |

### Optional Inputs

| Input                       | Default | Description                       |
| --------------------------- | ------- | --------------------------------- |
| `is-library-package`        | `false` | Whether this is a library package |
| `is-qa-package`             | `false` | Whether this is a QA package      |
| `working-directory`         | "."     | Working directory for the build   |
| `vault-url`                 | -       | Vault server URL                  |
| `vault_github_actions_role` | -       | Role for Vault authentication     |
| `environment_name`          | -       | Target environment name           |

## Features

- 📦 React Native bundle publishing
- 🔄 Over-the-air updates
- 🔒 Secure credential management
- 🌐 Multi-environment support
- 🔑 Vault secret integration
- 📱 Version targeting

## Example Usage

### Basic Usage

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-bundle-codepush.yml@v4
    with:
      node-version: "18.x"
      codepush-app: "MyApp/Production"
      apk-version: "1.0.0"
      vault-path: "mobile/codepush"
    secrets: inherit
```

### QA Package Deployment

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-bundle-codepush.yml@v4
    with:
      node-version: "18.x"
      codepush-app: "MyApp/QA"
      apk-version: "1.0.0"
      vault-path: "mobile/codepush"
      is-qa-package: true
      environment_name: qa
    secrets: inherit
```

### Library Package Build

```yaml
jobs:
  publish:
    uses: ZeroGachis/.github/.github/workflows/publish-bundle-codepush.yml@v4
    with:
      node-version: "18.x"
      codepush-app: "MyLibrary/Production"
      apk-version: "1.0.0"
      vault-path: "mobile/codepush"
      is-library-package: true
      working-directory: "library"
    secrets: inherit
```

## Required Secrets

The workflow requires the following Vault secrets:

- `CODE_PUSH_KEY_NAME`: Production deployment key name
- `QA_CODE_PUSH_KEY_NAME`: QA deployment key name
- `CODE_PUSH_TOKEN`: CodePush authentication token

3. **Environment Variables**:
   ```yaml
   env:
     CODEPUSH_KEY_NAME: ${{ fromJSON(steps.secrets.outputs.outputs).CODE_PUSH_KEY_NAME }}
     QA_CODEPUSH_KEY_NAME: ${{ fromJSON(steps.secrets.outputs.outputs).QA_CODE_PUSH_KEY_NAME }}
   ```
