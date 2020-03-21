# PagerDuty Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/pagerduty**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) The v2 authorization token. See [API Documentation](https://v2.developer.pagerduty.com/docs/authentication) for more information.
* `skip_credentials_validation` - (Optional) Skip validation of the token against the PagerDuty API.


## Supported Resources

* [Terraform::PagerDuty::Addon](../resources/pagerduty/Terraform-PagerDuty-Addon/docs/README.md)
* [Terraform::PagerDuty::EscalationPolicy](../resources/pagerduty/Terraform-PagerDuty-EscalationPolicy/docs/README.md)
* [Terraform::PagerDuty::EventRule](../resources/pagerduty/Terraform-PagerDuty-EventRule/docs/README.md)
* [Terraform::PagerDuty::Extension](../resources/pagerduty/Terraform-PagerDuty-Extension/docs/README.md)
* [Terraform::PagerDuty::MaintenanceWindow](../resources/pagerduty/Terraform-PagerDuty-MaintenanceWindow/docs/README.md)
* [Terraform::PagerDuty::Schedule](../resources/pagerduty/Terraform-PagerDuty-Schedule/docs/README.md)
* [Terraform::PagerDuty::ServiceIntegration](../resources/pagerduty/Terraform-PagerDuty-ServiceIntegration/docs/README.md)
* [Terraform::PagerDuty::Service](../resources/pagerduty/Terraform-PagerDuty-Service/docs/README.md)
* [Terraform::PagerDuty::TeamMembership](../resources/pagerduty/Terraform-PagerDuty-TeamMembership/docs/README.md)
* [Terraform::PagerDuty::Team](../resources/pagerduty/Terraform-PagerDuty-Team/docs/README.md)
* [Terraform::PagerDuty::UserContactMethod](../resources/pagerduty/Terraform-PagerDuty-UserContactMethod/docs/README.md)
* [Terraform::PagerDuty::UserNotificationRule](../resources/pagerduty/Terraform-PagerDuty-UserNotificationRule/docs/README.md)
* [Terraform::PagerDuty::User](../resources/pagerduty/Terraform-PagerDuty-User/docs/README.md)