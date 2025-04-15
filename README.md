# Template Github Workflows

## Template Workflows

This repository contains a set of templates for Github workflows adapted to Smartway context.

Below is the list of available templates and associated documentations:
| Name | Path | Description | Documentation |
|------|------|-------------|---------------|
| Android Format Version Code | `.github/workflows/android-format-version-code.yml` | Generates version code for Android applications | [Documentation](.github/workflows/docs/android-format-version-code.md) |
| ArgoCD Sync | `.github/workflows/argocd_sync.yml` | Synchronizes applications with ArgoCD | [Documentation](.github/workflows/docs/argocd-sync.md) |
| Build Image | `.github/workflows/build-image.yml` | Builds and validates Docker images | [Documentation](.github/workflows/docs/build-image.md) |
| Build Xamarin Libs | `.github/workflows/build-xamarin-libs.yml` | Builds Xamarin libraries | [Documentation](.github/workflows/docs/build-xamarin-lib.md) |
| Create APK Artifact | `.github/workflows/create-apk-artifact.yml` | Creates Android APK artifacts | [Documentation](.github/workflows/docs/create-apk-artifact.md) |
| Create Go-To-Prod PR | `.github/workflows/create-gotoprod-pr.yml` | Creates production deployment pull requests | [Documentation](.github/workflows/docs/create-gotoprod-pr.md) |
| Delete Docker Image | `.github/workflows/delete-docker-image.yml` | Deletes Docker images from registry | [Documentation](.github/workflows/docs/delete-docker-image.md) |
| .NET Build | `.github/workflows/dotnet-build.yml` | Builds and tests .NET applications | [Documentation](.github/workflows/docs/dotnet-build.md) |
| .NET Publish | `.github/workflows/dotnet-publish.yml` | Publishes .NET packages | [Documentation](.github/workflows/docs/dotnet-publish.md) |
| Dockerfile Linter | `.github/workflows/dockerfile-linter.yml` | Lints Dockerfile syntax | [Documentation](.github/workflows/docs/dockerfile-linter.md) |
| GitHub Release Notes | `.github/workflows/gh-release-notes.yml` | Generates GitHub release notes | [Documentation](.github/workflows/docs/gh-release-notes.md) |
| GitHub Release Please | `.github/workflows/gh-release-please.yml` | Automates release process | [Documentation](.github/workflows/docs/gh-release-please.md) |
| Infra Cost | `.github/workflows/infra-cost.yml` | Calculates infrastructure costs | [Documentation](.github/workflows/docs/infra-cost.md) |
| Publish APK to S3 | `.github/workflows/publish-apk-s3.yml` | Publishes Android APKs to S3 | [Documentation](.github/workflows/docs/publish-apk-s3.md) |
| Python Publish | `.github/workflows/python-publish.yml` | Publishes Python packages | [Documentation](.github/workflows/docs/python-publish.md) |
| Push Image GHCR to ECR | `.github/workflows/push-image-ghcr-to-ecr.yml` | Pushes images from GHCR to ECR | [Documentation](.github/workflows/docs/push-image-ghcr-to-ecr.md) |
| Release Tag | `.github/workflows/releasetag.yml` | Generates release tags | [Documentation](.github/workflows/docs/releasetag.md) |
| Run AWS | `.github/workflows/run-aws.yml` | Executes AWS commands | [Documentation](.github/workflows/docs/run-aws.md) |
| Run Docker | `.github/workflows/run-docker.yml` | Runs Docker containers | [Documentation](.github/workflows/docs/run-docker.md) |
| Run Docker with DB | `.github/workflows/run-docker-with-db.yml` | Runs Docker containers with database | [Documentation](.github/workflows/docs/run-docker-with-db.md) |
| Run Docker Upload Artifact | `.github/workflows/run-docker-upload-artifact.yml` | Runs Docker and uploads artifacts | [Documentation](.github/workflows/docs/run-docker-upload-artifact.md) |
| Run Python | `.github/workflows/run-python.yml` | Executes Python scripts | [Documentation](.github/workflows/docs/run-python.md) |
| Run Pytest | `.github/workflows/run-pytest.yml` | Runs Python tests | [Documentation](.github/workflows/docs/run-pytest.md) |
| Send Slack Notification | `.github/workflows/send_slack_notif.yaml` | Sends Slack notifications | [Documentation](.github/workflows/docs/send-slack-notification.md) |
| Send Slack Message | `.github/workflows/send_slack_message.yaml` | Sends Slack messages | [Documentation](.github/workflows/docs/send_slack_message.md) |
| Send Slack Github Actions Status | `.github/workflows/send_slack_gha_status.yaml` | Sends Slack notifications | [Documentation](.github/workflows/docs/send_slack_gha_status.md) |
| Terraform | `.github/workflows/terraform.yml` | Manages Terraform infrastructure | [Documentation](.github/workflows/docs/terraform.md) |
| Terraform Check Kube Enabled | `.github/workflows/terraform_check_kube_enabled.yml` | Checks Kubernetes enablement for Terraform | [Documentation](.github/workflows/docs/terraform-check-kube-enabled.md) |
| Helm Testing | `.github/workflows/helm_testing.yaml` | Tests Helm charts | [Documentation](.github/workflows/docs/helm_testing.md) |
Each workflow template has its own dedicated documentation page with detailed information about inputs, outputs, and usage examples.

## Release Management

This project uses [Release Please](https://github.com/googleapis/release-please) from Google to automate the release process. The tool handles versioning and changelog generation based on commit messages.

### Conventional Commits

To ensure releases are generated correctly, we follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. Commit messages should be structured as follows:

- _feat_: A new feature
- _fix_: A bug fix
- _docs_: Documentation only changes
- _style_: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- _refactor_: A code change that neither fixes a bug nor adds a feature
- _perf_: A code change that improves performance
- _test_: Adding missing or correcting existing tests
- _build_: Changes that affect the build system or external dependencies
- _ci_: Changes to our CI configuration files and scripts
- _chore_: Other changes that don't modify src or test files
- _revert_: Reverts a previous commit

Example:

```
feat: add new workflow to handle peppermint

```

### Breaking Changes and Major Versions

When introducing breaking changes, follow these steps to ensure a new major version is released:

1. **Prefix the commit message with `BREAKING CHANGE:`**: Indicate that the commit introduces breaking changes.
2. **Describe the breaking change in the commit message**: Provide details about what changes are being made and how they affect existing functionality.
3. **Merge the commit**: Once the breaking change commit is merged, `Release Please` will automatically create a new major version.

Example commit message for a breaking change:

```
feat!: add new workflow to handle peppermint

BREAKING CHANGE: This update changes the way the Datadog monitor module interacts with the API, requiring updates to existing configurations.
```

The `!` after `feat` indicates a breaking change, and the `BREAKING CHANGE:` section provides details about the change.
