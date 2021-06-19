# OpsGenie Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opsgenie**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) The API Key for the Opsgenie Integration.

* `api_url` - (Optional) The API url for the Opsgenie.

You can generate an API Key within Opsgenie by creating a new API Integration with Read/Write permissions.


## Supported Resources

* [TF::OpsGenie::AlertPolicy](../resources/opsgenie/TF-OpsGenie-AlertPolicy/docs/README.md)
* [TF::OpsGenie::ApiIntegration](../resources/opsgenie/TF-OpsGenie-ApiIntegration/docs/README.md)
* [TF::OpsGenie::CustomRole](../resources/opsgenie/TF-OpsGenie-CustomRole/docs/README.md)
* [TF::OpsGenie::EmailIntegration](../resources/opsgenie/TF-OpsGenie-EmailIntegration/docs/README.md)
* [TF::OpsGenie::Escalation](../resources/opsgenie/TF-OpsGenie-Escalation/docs/README.md)
* [TF::OpsGenie::Heartbeat](../resources/opsgenie/TF-OpsGenie-Heartbeat/docs/README.md)
* [TF::OpsGenie::IncidentTemplate](../resources/opsgenie/TF-OpsGenie-IncidentTemplate/docs/README.md)
* [TF::OpsGenie::IntegrationAction](../resources/opsgenie/TF-OpsGenie-IntegrationAction/docs/README.md)
* [TF::OpsGenie::Maintenance](../resources/opsgenie/TF-OpsGenie-Maintenance/docs/README.md)
* [TF::OpsGenie::NotificationPolicy](../resources/opsgenie/TF-OpsGenie-NotificationPolicy/docs/README.md)
* [TF::OpsGenie::NotificationRule](../resources/opsgenie/TF-OpsGenie-NotificationRule/docs/README.md)
* [TF::OpsGenie::ScheduleRotation](../resources/opsgenie/TF-OpsGenie-ScheduleRotation/docs/README.md)
* [TF::OpsGenie::Schedule](../resources/opsgenie/TF-OpsGenie-Schedule/docs/README.md)
* [TF::OpsGenie::ServiceIncidentRule](../resources/opsgenie/TF-OpsGenie-ServiceIncidentRule/docs/README.md)
* [TF::OpsGenie::Service](../resources/opsgenie/TF-OpsGenie-Service/docs/README.md)
* [TF::OpsGenie::TeamRoutingRule](../resources/opsgenie/TF-OpsGenie-TeamRoutingRule/docs/README.md)
* [TF::OpsGenie::Team](../resources/opsgenie/TF-OpsGenie-Team/docs/README.md)
* [TF::OpsGenie::UserContact](../resources/opsgenie/TF-OpsGenie-UserContact/docs/README.md)
* [TF::OpsGenie::User](../resources/opsgenie/TF-OpsGenie-User/docs/README.md)