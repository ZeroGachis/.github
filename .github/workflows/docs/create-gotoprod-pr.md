# Create Go-To-Prod Pull Request Workflow

This workflow automates the creation of production deployment pull requests, including automatic reviewer assignment and comprehensive change documentation.

## Usage

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v4
    with:
      base: main
```

## Inputs

### Optional Inputs

| Input  | Default | Description                      |
| ------ | ------- | -------------------------------- |
| `base` | `main`  | Base branch for the pull request |

## Features

- 🤖 Automated PR creation
- 👥 Automatic reviewer assignment
- 📝 Comprehensive change documentation
- 🏷️ Automatic labeling
- 🔄 PR update support
- 📊 Change categorization

## Example Usage

### Basic Usage

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v4
```

### With Custom Base Branch

```yaml
jobs:
  create-pr:
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v4
    with:
      base: production
```

### In a Deployment Pipeline

```yaml
name: Production Deployment

on:
  workflow_dispatch:
  schedule:
    - cron: "0 10 * * 1" # Every Monday at 10:00 UTC

jobs:
  tests:
    uses: ./.github/workflows/run-tests.yml

  create-pr:
    needs: tests
    uses: ZeroGachis/.github/.github/workflows/create-gotoprod-pr.yml@v4
    with:
      base: main
```

## Technical Details

1. **Pull Request Creation**:

   - Creates or updates existing PR
   - Assigns meaningful title
   - Generates comprehensive description
   - Adds appropriate labels

2. **Change Documentation**:

   - Lists merged pull requests
   - Documents direct commits
   - Categorizes changes
   - Links related issues

3. **Reviewer Management**:
   - Identifies contributors from commits
   - Automatically assigns reviewers
   - Excludes bot accounts
   - Maintains reviewer history

## Generated PR Structure

The workflow generates a pull request with the following structure:

```markdown
## 🚀 Automated PR to prepare Go-To-Production

**Branch**: `feature/new-feature`
**Base**: `main`

### 🔍 Changes

#### 🔄 Merged Pull Requests

- Implement new authentication system (#123)
- Fix database performance issues (#124)
- Update documentation (#125)

#### 📝 Commits

- Update configuration files
- Fix typos in README
- Add new test cases

### 👥 Contributors

- @developer1
- @developer2
- @developer3
```

## Labels

The workflow automatically adds the following labels:

- `go-to-prod`: Identifies production deployment PRs
- `:robot: automated-pr`: Indicates automated creation
