# OpsGenie Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opsgenie**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) The API Key for the Opsgenie Integration.

* `api_url` - (Optional) The API url for the Opsgenie.

You can generate an API Key within Opsgenie by creating a new API Integration with Read/Write permissions.


## Supported Resources

* [Terraform::OpsGenie::ApiIntegration](../resources/opsgenie/Terraform-OpsGenie-ApiIntegration/docs/README.md)
* [Terraform::OpsGenie::EmailIntegration](../resources/opsgenie/Terraform-OpsGenie-EmailIntegration/docs/README.md)
* [Terraform::OpsGenie::Escalation](../resources/opsgenie/Terraform-OpsGenie-Escalation/docs/README.md)
* [Terraform::OpsGenie::Heartbeat](../resources/opsgenie/Terraform-OpsGenie-Heartbeat/docs/README.md)
* [Terraform::OpsGenie::Maintenance](../resources/opsgenie/Terraform-OpsGenie-Maintenance/docs/README.md)
* [Terraform::OpsGenie::NotificationPolicy](../resources/opsgenie/Terraform-OpsGenie-NotificationPolicy/docs/README.md)
* [Terraform::OpsGenie::ScheduleRotation](../resources/opsgenie/Terraform-OpsGenie-ScheduleRotation/docs/README.md)
* [Terraform::OpsGenie::Schedule](../resources/opsgenie/Terraform-OpsGenie-Schedule/docs/README.md)
* [Terraform::OpsGenie::TeamRoutingRule](../resources/opsgenie/Terraform-OpsGenie-TeamRoutingRule/docs/README.md)
* [Terraform::OpsGenie::Team](../resources/opsgenie/Terraform-OpsGenie-Team/docs/README.md)
* [Terraform::OpsGenie::UserContact](../resources/opsgenie/Terraform-OpsGenie-UserContact/docs/README.md)
* [Terraform::OpsGenie::User](../resources/opsgenie/Terraform-OpsGenie-User/docs/README.md)