# PagerDuty Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/pagerduty**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The v2 authorization token. See [API Documentation](https://v2.developer.pagerduty.com/docs/authentication) for more information.
* `skip_credentials_validation` - (Optional) Skip validation of the token against the PagerDuty API.


## Supported Resources

* [TF::PagerDuty::Addon](../resources/pagerduty/TF-PagerDuty-Addon/docs/README.md)
* [TF::PagerDuty::BusinessService](../resources/pagerduty/TF-PagerDuty-BusinessService/docs/README.md)
* [TF::PagerDuty::EscalationPolicy](../resources/pagerduty/TF-PagerDuty-EscalationPolicy/docs/README.md)
* [TF::PagerDuty::EventRule](../resources/pagerduty/TF-PagerDuty-EventRule/docs/README.md)
* [TF::PagerDuty::Extension](../resources/pagerduty/TF-PagerDuty-Extension/docs/README.md)
* [TF::PagerDuty::MaintenanceWindow](../resources/pagerduty/TF-PagerDuty-MaintenanceWindow/docs/README.md)
* [TF::PagerDuty::ResponsePlay](../resources/pagerduty/TF-PagerDuty-ResponsePlay/docs/README.md)
* [TF::PagerDuty::RulesetRule](../resources/pagerduty/TF-PagerDuty-RulesetRule/docs/README.md)
* [TF::PagerDuty::Ruleset](../resources/pagerduty/TF-PagerDuty-Ruleset/docs/README.md)
* [TF::PagerDuty::Schedule](../resources/pagerduty/TF-PagerDuty-Schedule/docs/README.md)
* [TF::PagerDuty::ServiceDependency](../resources/pagerduty/TF-PagerDuty-ServiceDependency/docs/README.md)
* [TF::PagerDuty::ServiceEventRule](../resources/pagerduty/TF-PagerDuty-ServiceEventRule/docs/README.md)
* [TF::PagerDuty::ServiceIntegration](../resources/pagerduty/TF-PagerDuty-ServiceIntegration/docs/README.md)
* [TF::PagerDuty::Service](../resources/pagerduty/TF-PagerDuty-Service/docs/README.md)
* [TF::PagerDuty::TeamMembership](../resources/pagerduty/TF-PagerDuty-TeamMembership/docs/README.md)
* [TF::PagerDuty::Team](../resources/pagerduty/TF-PagerDuty-Team/docs/README.md)
* [TF::PagerDuty::UserContactMethod](../resources/pagerduty/TF-PagerDuty-UserContactMethod/docs/README.md)
* [TF::PagerDuty::UserNotificationRule](../resources/pagerduty/TF-PagerDuty-UserNotificationRule/docs/README.md)
* [TF::PagerDuty::User](../resources/pagerduty/TF-PagerDuty-User/docs/README.md)