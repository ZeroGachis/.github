# Fetch Terraform Output GitHub Action

This reusable GitHub Actions workflow fetches a single output variable from a cached Terraform outputs JSON file. It's designed to be called from other workflows to retrieve specific Terraform output values that have been previously cached.

## Usage

To use this workflow in your GitHub Actions, call it using the `workflow_call` trigger:

```yaml
jobs:
  get-terraform-output:
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable_name: "my_output_variable"
```

## Inputs

| Input | Required | Type | Description |
|-------|----------|------|-------------|
| `variable_name` | ✅ | string | The name of the variable to fetch from the cached Terraform outputs JSON file |

## Outputs

| Output | Description |
|--------|-------------|
| `TF_OUTPUT_VAR` | The value of the specified Terraform output variable |

## Prerequisites

1. **Cached Terraform Outputs**: The workflow expects a `tf-output.json` file to be available in the GitHub Actions cache with the key `tf-output-${{ github.run_id }}-${{ github.run_attempt }}`
2. **JSON Format**: The cached file should contain Terraform outputs in JSON format where each output follows the structure: `{"output_name": {"value": "actual_value"}}`

## Example Usage

### Basic Usage

```yaml
jobs:
  # First, you need a job that generates and caches the tf-output.json file
  generate-terraform-outputs:
    runs-on: ubuntu-latest
    steps:
      # ... steps to generate tf-output.json ...
      - uses: actions/cache/save@v4
        with:
          path: tf-output.json
          key: tf-output-${{ github.run_id }}-${{ github.run_attempt }}

  # Then use this workflow to fetch specific variables
  fetch-vpc-id:
    needs: generate-terraform-outputs
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable_name: "vpc_id"

  use-output:
    needs: fetch-vpc-id
    runs-on: ubuntu-latest
    steps:
      - name: Use Terraform output
        run: echo "VPC ID is ${{ needs.fetch-vpc-id.outputs.TF_OUTPUT_VAR }}"
```

### Multiple Variables

```yaml
jobs:
  generate-terraform-outputs:
    runs-on: ubuntu-latest
    steps:
      # ... steps to generate tf-output.json ...
      - uses: actions/cache/save@v4
        with:
          path: tf-output.json
          key: tf-output-${{ github.run_id }}-${{ github.run_attempt }}

  fetch-vpc-id:
    needs: generate-terraform-outputs
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable_name: "vpc_id"

  fetch-subnet-id:
    needs: generate-terraform-outputs
    uses: ./.github/workflows/fetch-terraform-output.yml
    with:
      variable_name: "subnet_id"

  deploy:
    needs: [fetch-vpc-id, fetch-subnet-id]
    runs-on: ubuntu-latest
    steps:
      - name: Deploy with outputs
        run: |
          echo "Deploying to VPC: ${{ needs.fetch-vpc-id.outputs.TF_OUTPUT_VAR }}"
          echo "Using subnet: ${{ needs.fetch-subnet-id.outputs.TF_OUTPUT_VAR }}"
```

## Workflow Steps

The workflow performs the following steps:

1. **Cache Restoration**: Attempts to restore the `tf-output.json` file from GitHub Actions cache using the key `tf-output-${{ github.run_id }}-${{ github.run_attempt }}`
2. **Cache Validation**: Checks if the cache was successfully restored; fails if cache miss occurs
3. **Variable Extraction**: Uses `jq` to extract the specified variable's value from the JSON file
4. **Output Setting**: Sets the extracted value as the workflow output `TF_OUTPUT_VAR`

## Expected JSON Format

The cached `tf-output.json` file should follow the standard Terraform output format:

```json
{
  "vpc_id": {
    "value": "vpc-12345678"
  },
  "subnet_id": {
    "value": "subnet-87654321"
  },
  "database_endpoint": {
    "value": "db.example.com:5432"
  }
}
```

## Error Handling

- **Cache Miss**: The workflow will fail if the expected cache entry is not found
- **Invalid JSON**: The workflow will fail if the cached file is not valid JSON
- **Missing Variable**: If the specified variable doesn't exist in the JSON file, `jq` will return `null`
- **JSON Parsing**: Any `jq` parsing errors will cause the workflow to fail

## Security Considerations

- The workflow only reads from cache and doesn't perform any authentication or external API calls
- No sensitive credentials are required for this workflow
- The workflow runs with minimal permissions and only accesses cached data

## Limitations

- Depends on a previously cached `tf-output.json` file
- Can only fetch one variable per workflow call
- Cache keys are tied to specific GitHub run ID and attempt number
- No validation of variable existence before extraction
