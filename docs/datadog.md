# Datadog Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/datadog**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) Datadog API key.
* `app_key` - (Required) Datadog APP key.
* `api_url` - (Optional) The API Url. Note that this URL must not end with the `/api/` path. For example, `https://api.datadoghq.com/` is a correct value, while `https://api.datadoghq.com/api/` is not.


## Supported Resources

* [Terraform::Datadog::DashboardList](../resources/datadog/Terraform-Datadog-DashboardList/docs/README.md)
* [Terraform::Datadog::Dashboard](../resources/datadog/Terraform-Datadog-Dashboard/docs/README.md)
* [Terraform::Datadog::Downtime](../resources/datadog/Terraform-Datadog-Downtime/docs/README.md)
* [Terraform::Datadog::IntegrationAws](../resources/datadog/Terraform-Datadog-IntegrationAws/docs/README.md)
* [Terraform::Datadog::IntegrationGcp](../resources/datadog/Terraform-Datadog-IntegrationGcp/docs/README.md)
* [Terraform::Datadog::IntegrationPagerdutyServiceObject](../resources/datadog/Terraform-Datadog-IntegrationPagerdutyServiceObject/docs/README.md)
* [Terraform::Datadog::IntegrationPagerduty](../resources/datadog/Terraform-Datadog-IntegrationPagerduty/docs/README.md)
* [Terraform::Datadog::LogsCustomPipeline](../resources/datadog/Terraform-Datadog-LogsCustomPipeline/docs/README.md)
* [Terraform::Datadog::LogsIndexOrder](../resources/datadog/Terraform-Datadog-LogsIndexOrder/docs/README.md)
* [Terraform::Datadog::LogsIndex](../resources/datadog/Terraform-Datadog-LogsIndex/docs/README.md)
* [Terraform::Datadog::LogsIntegrationPipeline](../resources/datadog/Terraform-Datadog-LogsIntegrationPipeline/docs/README.md)
* [Terraform::Datadog::LogsPipelineOrder](../resources/datadog/Terraform-Datadog-LogsPipelineOrder/docs/README.md)
* [Terraform::Datadog::MetricMetadata](../resources/datadog/Terraform-Datadog-MetricMetadata/docs/README.md)
* [Terraform::Datadog::Monitor](../resources/datadog/Terraform-Datadog-Monitor/docs/README.md)
* [Terraform::Datadog::Screenboard](../resources/datadog/Terraform-Datadog-Screenboard/docs/README.md)
* [Terraform::Datadog::ServiceLevelObjective](../resources/datadog/Terraform-Datadog-ServiceLevelObjective/docs/README.md)
* [Terraform::Datadog::SyntheticsTest](../resources/datadog/Terraform-Datadog-SyntheticsTest/docs/README.md)
* [Terraform::Datadog::Timeboard](../resources/datadog/Terraform-Datadog-Timeboard/docs/README.md)
* [Terraform::Datadog::User](../resources/datadog/Terraform-Datadog-User/docs/README.md)