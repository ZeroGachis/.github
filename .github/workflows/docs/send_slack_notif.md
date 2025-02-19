# Send Slack Notification Workflow

This workflow automates sending notifications to Slack channels using the Slack API, with support for rich message formatting and secure credential management.

## Usage

```yaml
jobs:
  notify:
    uses: ZeroGachis/.github/.github/workflows/send_slack_notif.yaml@v4
    with:
      payload: |
        {
          "text": "🚀 Deployment successful!",
          "blocks": [
            {
              "type": "section",
              "text": {
                "type": "mrkdwn",
                "text": "*Deployment Status:* Success"
              }
            }
          ]
        }
      environment_name: production
    secrets: inherit
```

## Inputs

### Required Inputs

| Input              | Description                             |
| ------------------ | --------------------------------------- |
| `payload`          | Slack message payload in JSON format    |
| `environment_name` | Target environment for the notification |

### Optional Inputs

| Input                       | Default | Description                          |
| --------------------------- | ------- | ------------------------------------ |
| `vault_url`                 | -       | Vault server URL for secrets         |
| `vault_github_actions_role` | -       | Role to use for Vault authentication |

## Features

- 🔒 Secure bot token management through Vault
- 📝 Support for rich message formatting
- 🎨 Full Slack Block Kit support
- 🌐 Tailscale VPN integration
- ⚡ Reliable message delivery
- 🔑 Secure credential handling

## Example Usage

### Basic Text Message

```yaml
jobs:
  notify:
    uses: ZeroGachis/.github/.github/workflows/send_slack_notif.yaml@v4
    with:
      payload: |
        {
          "text": "Hello from GitHub Actions!"
        }
      environment_name: staging
    secrets: inherit
```
