# PyTest Runner Workflow

This workflow provides a specialized environment for running Python tests with pytest, including coverage reporting and PostgreSQL database support.

## Usage

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-pytest.yml@v4
    with:
      image_url: ghcr.io/zerogachis/python-test:latest
      workdir: /app
      directory_to_test: "tests/"
      env_django_settings_module: "myapp.settings.test"
    secrets: inherit
```

## Inputs

### Required Inputs

| Input                        | Description                               |
| ---------------------------- | ----------------------------------------- |
| `image_url`                  | Docker image URL to use                   |
| `workdir`                    | Working directory inside the container    |
| `directory_to_test`          | Directory containing tests to run         |
| `env_django_settings_module` | Django settings module for test execution |

### Optional Inputs

| Input              | Default | Description             |
| ------------------ | ------- | ----------------------- |
| `environment_name` | -       | Target environment name |

## Features

- 🧪 Automated pytest execution
- 📊 Coverage reporting
- 🗃️ PostgreSQL database integration
- 📈 Coverage comments on PRs
- 📝 JUnit XML report generation
- 🔄 GitHub Actions integration

## Example Usage

### Basic Test Execution

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-pytest.yml@v4
    with:
      image_url: ghcr.io/zerogachis/python-test:latest
      workdir: /app
      directory_to_test: "tests/"
      env_django_settings_module: "myapp.settings.test"
```

### With Environment Configuration

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/run-pytest.yml@v4
    with:
      image_url: ghcr.io/zerogachis/django-test:latest
      workdir: /app
      directory_to_test: "tests/integration/"
      env_django_settings_module: "myapp.settings.integration"
      environment_name: staging
```

### In a Complete CI Pipeline

```yaml
name: CI Pipeline

on:
  pull_request:
    branches: [main]

jobs:
  lint:
    uses: ./.github/workflows/run-python.yml
    with:
      run_command: "flake8"

  test:
    needs: lint
    uses: ./.github/workflows/run-pytest.yml
    with:
      image_url: ghcr.io/zerogachis/python-test:latest
      workdir: /app
      directory_to_test: "tests/"
      env_django_settings_module: "myapp.settings.test"
```
