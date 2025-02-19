# Docker with Database Workflow

This workflow provides a Docker execution environment with an integrated PostgreSQL database service, ideal for running tests and applications that require a database.

## Usage

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-docker-with-db.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      workdir: /app
      run_command: "python manage.py test"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input         | Description                            |
| ------------- | -------------------------------------- |
| `image_url`   | Docker image URL to use                |
| `workdir`     | Working directory inside the container |
| `run_command` | Command to execute in the container    |

### Optional Inputs

| Input                        | Default | Description                  |
| ---------------------------- | ------- | ---------------------------- |
| `env_django_settings_module` | -       | Django settings module path  |
| `enable_test_report`         | `false` | Enable test result reporting |
| `test_report_name`           | -       | Name for the test report     |
| `test_report_path`           | -       | Path to test results file    |
| `test_report_format`         | -       | Format of test results       |
| `checkout_enabled`           | `true`  | Enable repository checkout   |
| `aws_credentials_enabled`    | `false` | Enable AWS credentials       |
| `vault_enabled`              | `true`  | Enable Vault integration     |
| `environment_name`           | -       | Target environment name      |
| `tailscale_enabled`          | `true`  | Enable Tailscale VPN         |

## Features

- 🗃️ Integrated PostgreSQL 16 database
- 🔒 Secure credential management
- 🐳 Docker container execution
- 📊 Test reporting capabilities
- 🔑 Vault secret integration
- 🌐 Tailscale VPN support

## Example Usage

### Basic Test Execution

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-docker-with-db.yml@v4
    with:
      image_url: ghcr.io/zerogachis/test-runner:latest
      workdir: /app
      run_command: "pytest"
```

### Django Application Tests

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-docker-with-db.yml@v4
    with:
      image_url: ghcr.io/zerogachis/django-app:latest
      workdir: /app
      run_command: "python manage.py test"
      env_django_settings_module: myapp.settings.test
      enable_test_report: true
      test_report_name: "Django Tests"
      test_report_path: "test-results.xml"
      test_report_format: "junit"
```

### With AWS and Vault Integration

```yaml
jobs:
  integration-test:
    uses: ZeroGachis/.github/.github/workflows/run-docker-with-db.yml@v4
    with:
      image_url: ghcr.io/zerogachis/api:latest
      workdir: /app
      run_command: "npm run test:integration"
      aws_credentials_enabled: true
      vault_enabled: true
      environment_name: staging
```
