# Docker Execution Workflows Documentation

This documentation covers the family of Docker execution workflows:

- Basic Docker Execution (`run-docker.yml`)
- Docker with Database (`run-docker-with-db.yml`)
- Docker with Artifact Upload (`run-docker-upload-artifact.yml`)

## Basic Docker Execution Workflow

This workflow runs commands inside a Docker container with support for various integrations and security features.

### Usage

```yaml
jobs:
  run:
    uses: ZeroGachis/.github/.github/workflows/run-docker.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-image:latest
      workdir: /app
      run_command: "./run-tests.sh"
    secrets: inherit
```

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

## Docker with Database Workflow

Extends the basic workflow with a PostgreSQL database service.

### Usage

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-docker-with-db.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      workdir: /app
      run_command: "python manage.py test"
      env_django_settings_module: myapp.settings.test
    secrets: inherit
```

### Additional Features

- Automatically provides PostgreSQL 16 database
- Sets up database environment variables:
  - `POSTGRES_HOST`: postgres
  - `POSTGRES_PORT`: 5432
  - Default password: postgres

## Docker with Artifact Upload Workflow

Extends the basic workflow with artifact upload capabilities.

### Usage

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

### Additional Required Inputs

| Input           | Description                         |
| --------------- | ----------------------------------- |
| `artifact_name` | Name for the uploaded artifact      |
| `artifact_path` | Path to files to upload as artifact |

## Common Features

All Docker execution workflows include:

- 🔒 Secure authentication with GitHub Packages
- 🔑 Vault integration for secrets
- 🌐 Tailscale VPN support
- 📊 Test reporting capabilities
- ☁️ AWS credentials integration
- 🔄 GitHub Actions integration
