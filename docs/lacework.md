# Lacework Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/lacework**. The below arguments may be included as the key/value or JSON properties in the secret:

* `profile` - (Optional) This is the Lacework profile name to use, profiles are configured
  at `$HOME/.lacework.toml` via the [Lacework CLI](https://github.com/lacework/go-sdk/wiki/CLI-Documentation).

* `account` - (Optional) This is the Lacework account subdomain of URL (i.e. `<ACCOUNT>`
  .lacework.net).

* `api_key` - (Optional) This is a Lacework API access key.

* `api_secret` - (Optional) This is a Lacework API access secret.

* `subaccount` - (Optional) The sub-account name inside your organization (for organization
  administrators only).

-> **Note:** To generate a set of API access keys follow [this documentation](https://support.lacework.com/hc/en-us/articles/360011403853-Generate-API-Access-Keys-and-Tokens).


## Supported Resources

* [TF::Lacework::AgentAccessToken](../resources/lacework/TF-Lacework-AgentAccessToken/docs/README.md)
* [TF::Lacework::AlertChannelAwsCloudwatch](../resources/lacework/TF-Lacework-AlertChannelAwsCloudwatch/docs/README.md)
* [TF::Lacework::AlertChannelAwsS3](../resources/lacework/TF-Lacework-AlertChannelAwsS3/docs/README.md)
* [TF::Lacework::AlertChannelCiscoWebex](../resources/lacework/TF-Lacework-AlertChannelCiscoWebex/docs/README.md)
* [TF::Lacework::AlertChannelDatadog](../resources/lacework/TF-Lacework-AlertChannelDatadog/docs/README.md)
* [TF::Lacework::AlertChannelGcpPubSub](../resources/lacework/TF-Lacework-AlertChannelGcpPubSub/docs/README.md)
* [TF::Lacework::AlertChannelJiraCloud](../resources/lacework/TF-Lacework-AlertChannelJiraCloud/docs/README.md)
* [TF::Lacework::AlertChannelJiraServer](../resources/lacework/TF-Lacework-AlertChannelJiraServer/docs/README.md)
* [TF::Lacework::AlertChannelMicrosoftTeams](../resources/lacework/TF-Lacework-AlertChannelMicrosoftTeams/docs/README.md)
* [TF::Lacework::AlertChannelNewrelic](../resources/lacework/TF-Lacework-AlertChannelNewrelic/docs/README.md)
* [TF::Lacework::AlertChannelPagerduty](../resources/lacework/TF-Lacework-AlertChannelPagerduty/docs/README.md)
* [TF::Lacework::AlertChannelQradar](../resources/lacework/TF-Lacework-AlertChannelQradar/docs/README.md)
* [TF::Lacework::AlertChannelServiceNow](../resources/lacework/TF-Lacework-AlertChannelServiceNow/docs/README.md)
* [TF::Lacework::AlertChannelSlack](../resources/lacework/TF-Lacework-AlertChannelSlack/docs/README.md)
* [TF::Lacework::AlertChannelSplunk](../resources/lacework/TF-Lacework-AlertChannelSplunk/docs/README.md)
* [TF::Lacework::AlertChannelVictorops](../resources/lacework/TF-Lacework-AlertChannelVictorops/docs/README.md)
* [TF::Lacework::AlertChannelWebhook](../resources/lacework/TF-Lacework-AlertChannelWebhook/docs/README.md)
* [TF::Lacework::IntegrationAwsCfg](../resources/lacework/TF-Lacework-IntegrationAwsCfg/docs/README.md)
* [TF::Lacework::IntegrationAwsCt](../resources/lacework/TF-Lacework-IntegrationAwsCt/docs/README.md)
* [TF::Lacework::IntegrationAwsGovcloudCfg](../resources/lacework/TF-Lacework-IntegrationAwsGovcloudCfg/docs/README.md)
* [TF::Lacework::IntegrationAzureAl](../resources/lacework/TF-Lacework-IntegrationAzureAl/docs/README.md)
* [TF::Lacework::IntegrationAzureCfg](../resources/lacework/TF-Lacework-IntegrationAzureCfg/docs/README.md)
* [TF::Lacework::IntegrationDockerHub](../resources/lacework/TF-Lacework-IntegrationDockerHub/docs/README.md)
* [TF::Lacework::IntegrationDockerV2](../resources/lacework/TF-Lacework-IntegrationDockerV2/docs/README.md)
* [TF::Lacework::IntegrationEcr](../resources/lacework/TF-Lacework-IntegrationEcr/docs/README.md)
* [TF::Lacework::IntegrationGcpAt](../resources/lacework/TF-Lacework-IntegrationGcpAt/docs/README.md)
* [TF::Lacework::IntegrationGcpCfg](../resources/lacework/TF-Lacework-IntegrationGcpCfg/docs/README.md)
* [TF::Lacework::IntegrationGcr](../resources/lacework/TF-Lacework-IntegrationGcr/docs/README.md)