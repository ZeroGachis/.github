# Xamarin Library Build & Publish Workflow

This GitHub Actions workflow automates the building, testing, and optional publishing of Xamarin libraries.

## Usage

To use this reusable workflow in your GitHub Actions, create a workflow file that calls this workflow using the `workflow_call` trigger.

### Required Inputs

- `lib-version`: Version of the library to build
- `lib-name`: Name of the Xamarin library
- `spec-file`: Path to the specification file
- `configuration`: Build configuration (e.g., "Release" or "Debug")
- `publish`: Boolean flag to determine if the library should be published

### Optional Inputs

- `aws-github-role-name`: AWS IAM role name (default: "github_oidc_readonly")
- `aws-account-id`: AWS account ID (default: "007065811408")
- `aws-ecr-region`: AWS ECR region (default: "eu-west-3")

### Example Workflow

```yaml
name: Build My Xamarin Library

on:
  push:
    branches: [ main ]

jobs:
  build-lib:
    uses: ./.github/workflows/build-xamarin-lib.yml
    with:
      lib-version: '1.0.0'
      lib-name: 'MyXamarinLibrary'
      spec-file: 'MyXamarinLibrary.nuspec'
      configuration: 'Release'
      publish: true
```

## Workflow Steps

1. **ECR Authentication**
   - Configures AWS credentials
   - Logs into Amazon ECR
   - Provides registry credentials for subsequent steps

2. **Build Process**
   - Runs in a custom Xamarin Android container from ECR
   - Checks out the repository
   - Builds the library
   - Runs tests
   - Optionally publishes the library to NuGet

## Prerequisites

- AWS ECR access with appropriate permissions
- NuGet API key (if publishing is enabled)
- Appropriate repository permissions

## Notes

- The workflow uses a custom Docker image from ECR for building Xamarin libraries
- Tests results will be automatically reported to GitHub
- Publishing will only occur if the `publish` input is set to `true`
- Make sure to configure the necessary secrets in your GitHub repository settings

## Security Considerations

- Uses OIDC for AWS authentication
- Requires specific GitHub Actions permissions
- Runs in a containerized environment for isolation

For more information about the individual actions used in this workflow, refer to:
- [build-xamarin-lib](https://github.com/ZeroGachis/.github/actions/build-xamarin-lib)
- [test-xamarin-lib](https://github.com/ZeroGachis/.github/actions/test-xamarin-lib)
- [publish-xamarin-lib](https://github.com/ZeroGachis/.github/actions/publish-xamarin-lib)
