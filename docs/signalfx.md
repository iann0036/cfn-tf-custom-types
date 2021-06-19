# SignalFx Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/signalfx**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_token` - (Required) The auth token for [authentication](https://developers.signalfx.com/basics/authentication.html).
* `api_url` - (Optional) The API URL to use for communicating with SignalFx. This is helpful for organizations who need to set their Realm or use a proxy.
* `custom_app_url` - (Optional)  The application URL that users should use to interact with assets in the browser. This is used by organizations using specific realms or those with a custom [SSO domain](https://docs.signalfx.com/en/latest/admin-guide/sso.html).
* `timeout_seconds` - (Optional) The total timeout duration, in seconds, to wait when making HTTP API calls to SignalFx. Defaults to 120.


## Supported Resources

* [TF::SignalFx::AlertMutingRule](../resources/signalfx/TF-SignalFx-AlertMutingRule/docs/README.md)
* [TF::SignalFx::AwsExternalIntegration](../resources/signalfx/TF-SignalFx-AwsExternalIntegration/docs/README.md)
* [TF::SignalFx::AwsIntegration](../resources/signalfx/TF-SignalFx-AwsIntegration/docs/README.md)
* [TF::SignalFx::AwsTokenIntegration](../resources/signalfx/TF-SignalFx-AwsTokenIntegration/docs/README.md)
* [TF::SignalFx::AzureIntegration](../resources/signalfx/TF-SignalFx-AzureIntegration/docs/README.md)
* [TF::SignalFx::DashboardGroup](../resources/signalfx/TF-SignalFx-DashboardGroup/docs/README.md)
* [TF::SignalFx::Dashboard](../resources/signalfx/TF-SignalFx-Dashboard/docs/README.md)
* [TF::SignalFx::DataLink](../resources/signalfx/TF-SignalFx-DataLink/docs/README.md)
* [TF::SignalFx::Detector](../resources/signalfx/TF-SignalFx-Detector/docs/README.md)
* [TF::SignalFx::EventFeedChart](../resources/signalfx/TF-SignalFx-EventFeedChart/docs/README.md)
* [TF::SignalFx::GcpIntegration](../resources/signalfx/TF-SignalFx-GcpIntegration/docs/README.md)
* [TF::SignalFx::HeatmapChart](../resources/signalfx/TF-SignalFx-HeatmapChart/docs/README.md)
* [TF::SignalFx::JiraIntegration](../resources/signalfx/TF-SignalFx-JiraIntegration/docs/README.md)
* [TF::SignalFx::ListChart](../resources/signalfx/TF-SignalFx-ListChart/docs/README.md)
* [TF::SignalFx::OpsgenieIntegration](../resources/signalfx/TF-SignalFx-OpsgenieIntegration/docs/README.md)
* [TF::SignalFx::OrgToken](../resources/signalfx/TF-SignalFx-OrgToken/docs/README.md)
* [TF::SignalFx::PagerdutyIntegration](../resources/signalfx/TF-SignalFx-PagerdutyIntegration/docs/README.md)
* [TF::SignalFx::SingleValueChart](../resources/signalfx/TF-SignalFx-SingleValueChart/docs/README.md)
* [TF::SignalFx::SlackIntegration](../resources/signalfx/TF-SignalFx-SlackIntegration/docs/README.md)
* [TF::SignalFx::Team](../resources/signalfx/TF-SignalFx-Team/docs/README.md)
* [TF::SignalFx::TextChart](../resources/signalfx/TF-SignalFx-TextChart/docs/README.md)
* [TF::SignalFx::TimeChart](../resources/signalfx/TF-SignalFx-TimeChart/docs/README.md)
* [TF::SignalFx::VictorOpsIntegration](../resources/signalfx/TF-SignalFx-VictorOpsIntegration/docs/README.md)
* [TF::SignalFx::WebhookIntegration](../resources/signalfx/TF-SignalFx-WebhookIntegration/docs/README.md)