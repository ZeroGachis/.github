# Fetch Terraform Output GitHub Action

Reusable workflow that fetches a single output variable directly from a Terraform state file stored in S3. Does not require Terraform to be installed or the repository to be checked out.

## Usage

```yaml
jobs:
  tf-output-cluster:
    uses: ZeroGachis/.github/.github/workflows/fetch-terraform-output.yml@v7
    with:
      variable_name: cluster
      workspace_key_prefix: <project>   # matches workspace_key_prefix in your Terraform backend config
    secrets: inherit
```

## Inputs

| Input | Required | Type | Default | Description |
|-------|----------|------|---------|-------------|
| `variable_name` | ✅ | string | — | Name of the output variable to fetch |
| `workspace_key_prefix` | ✅ | string | — | Matches `workspace_key_prefix` in the Terraform S3 backend config — **not** the repository name |
| `state_key` | ❌ | string | `infra.tfstate` | Terraform state filename |
| `aws_github_role_name` | ❌ | string | `github_oidc_readonly` | IAM role name to assume via OIDC |
| `environment_name` | ❌ | string | `github.base_ref` | GitHub environment used for variable resolution |
| `terraform_workspace` | ❌ | string | `github.base_ref \|\| github.ref_name` | Terraform workspace name (used to build the S3 path) |

## Outputs

| Output | Description |
|--------|-------------|
| `TF_OUTPUT_VAR` | The value of the specified Terraform output variable |

## How it works

The workflow builds the S3 state path as:

```
s3://tfstate-<AWS_ACCOUNT_ID>/<workspace_key_prefix>/<terraform_workspace>/<state_key>
```

It then extracts the variable with `jq` from `.outputs.<variable_name>.value` in the state file.

## Migration from v6

The following inputs have been **removed**:

| Input | Reason |
|---|---|
| `workdir` | No longer needed — no Terraform binary, no checkout |
| `terraform_version` | No longer needed — no Terraform binary |
| `artifact_id` | Removed — was already a no-op in v6 |

The new **required** input `workspace_key_prefix` must match the `workspace_key_prefix` value in your Terraform backend configuration, **not** the repository name (e.g. a repo named `foo-service` likely uses prefix `foo`).
