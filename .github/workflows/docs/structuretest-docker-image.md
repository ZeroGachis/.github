# Structure Test Docker Image Workflow

This workflow provides automated testing of Docker images using Google's Container Structure Test framework, ensuring image consistency and compliance with best practices.

## Usage

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/structuretest-docker-image.yml@v4
    with:
      image_url: ghcr.io/zerogachis/my-app:latest
      test_file: structuretest.yaml
    secrets: inherit
```

## Inputs

### Required Inputs

| Input       | Description                                   |
| ----------- | --------------------------------------------- |
| `image_url` | URL of the Docker image to test               |
| `test_file` | Path to the structure test configuration file |

### Optional Inputs

| Input              | Default | Description                          |
| ------------------ | ------- | ------------------------------------ |
| `environment_name` | -       | Target environment for configuration |

## Features

- 🔍 Automated Docker image testing
- 📋 Comprehensive test configuration
- 🛠️ Multiple test types support
- 🔒 Security scanning capabilities
- 📊 Detailed test reporting
- ⚡ Fast test execution

## Example Usage

### Basic Test Configuration

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/structuretest-docker-image.yml@v4
    with:
      image_url: ghcr.io/zerogachis/api:latest
      test_file: tests/docker/structuretest.yaml
```

### With Environment Configuration

```yaml
jobs:
  test:
    uses: ZeroGachis/.github/.github/workflows/structuretest-docker-image.yml@v4
    with:
      image_url: ghcr.io/zerogachis/web:latest
      test_file: tests/docker/prod-structuretest.yaml
      environment_name: production
```
