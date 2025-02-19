# Python Execution Workflows Documentation

This documentation covers the Python-specific workflows:

- Python Script Execution (`run-python.yml`)
- PyTest Execution (`run-pytest.yml`)

## Python Script Execution Workflow

This workflow provides a secure environment for running Python scripts with support for various integrations and dependencies.

### Usage

```yaml
jobs:
  run:
    uses: ZeroGachis/.github/.github/workflows/run-python.yml@v4
    with:
      run_command: "python script.py"
      vault_github_actions_role: "github-role"
      vault_secrets: "secret/data/my-secrets key | ENV_VAR"
    secrets: inherit
```

### Required Inputs

| Input                       | Description                   |
| --------------------------- | ----------------------------- |
| `run_command`               | Python command to execute     |
| `vault_github_actions_role` | Role for Vault authentication |
| `vault_secrets`             | Vault secrets to import       |

### Optional Inputs

| Input                     | Default | Description               |
| ------------------------- | ------- | ------------------------- |
| `python_version`          | "3.x"   | Python version to use     |
| `environment_name`        | -       | Target environment name   |
| `vault_enabled`           | `true`  | Enable Vault integration  |
| `vault_url`               | -       | Vault server URL          |
| `tailscale_enabled`       | `true`  | Enable Tailscale VPN      |
| `aws_credentials_enabled` | `false` | Enable AWS credentials    |
| `enable_test_report`      | `false` | Enable test reporting     |
| `test_report_name`        | -       | Name for the test report  |
| `test_report_path`        | -       | Path to test results file |
| `test_report_format`      | -       | Format of test results    |
