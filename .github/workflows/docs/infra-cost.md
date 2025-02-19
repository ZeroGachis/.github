# Infrastructure Cost Workflow

This workflow provides automated cost estimation for Terraform infrastructure changes using Infracost, enabling cost visibility and control in pull requests.

## Usage

```yaml
jobs:
  cost:
    uses: ZeroGachis/.github/.github/workflows/infra-cost.yml@v4
    with:
      infracost_terraform_workspace: production
    secrets: inherit
```

## Inputs

### Optional Inputs

| Input                           | Default | Description                                  |
| ------------------------------- | ------- | -------------------------------------------- |
| `infracost_terraform_workspace` | "main"  | Comma-delimited list of Terraform workspaces |
| `terraform_vars`                | -       | Terraform variables to add to CLI            |

## Features

- 💰 Automated cost estimation
- 📊 Pull request cost diff comments
- 🔄 Multi-workspace support
- 📝 Detailed cost breakdowns
- 🔍 Resource-level cost analysis
- 📈 Cost trend tracking

## Example Usage

### Basic Usage

```yaml
jobs:
  cost:
    uses: ZeroGachis/.github/.github/workflows/infra-cost.yml@v4
    with:
      infracost_terraform_workspace: production
```

### Multiple Workspaces

```yaml
jobs:
  cost:
    uses: ZeroGachis/.github/.github/workflows/infra-cost.yml@v4
    with:
      infracost_terraform_workspace: staging,production
```

### With Terraform Variables

```yaml
jobs:
  cost:
    uses: ZeroGachis/.github/.github/workflows/infra-cost.yml@v4
    with:
      infracost_terraform_workspace: production
      terraform_vars: "-var='environment=production' -var='region=eu-west-3'"
```

## Generated Report Example

The workflow generates detailed cost reports in pull requests:

```markdown
💰 Infracost estimate: Monthly cost will increase by $25.10 📈

## Cost Breakdown

### Production Workspace

| Resource         | Hourly  | Monthly |
| ---------------- | ------- | ------- |
| AWS EC2 instance | $0.0342 | $24.62  |
| AWS S3 Storage   | $0.0007 | $0.48   |

### Staging Workspace

| Resource         | Hourly  | Monthly |
| ---------------- | ------- | ------- |
| AWS RDS instance | $0.0856 | $61.63  |
| AWS ECS tasks    | $0.0428 | $30.82  |

Total Monthly Change: +$117.55
```
