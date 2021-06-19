# VictorOps Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/victorops**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_id` - (Required) An API id tied to an admin user
* `api_key` - (Required) An API key tied to an admin user


## Supported Resources

* [TF::VictorOps::Contact](../resources/victorops/TF-VictorOps-Contact/docs/README.md)
* [TF::VictorOps::EscalationPolicy](../resources/victorops/TF-VictorOps-EscalationPolicy/docs/README.md)
* [TF::VictorOps::RoutingKey](../resources/victorops/TF-VictorOps-RoutingKey/docs/README.md)
* [TF::VictorOps::TeamMembership](../resources/victorops/TF-VictorOps-TeamMembership/docs/README.md)
* [TF::VictorOps::Team](../resources/victorops/TF-VictorOps-Team/docs/README.md)
* [TF::VictorOps::User](../resources/victorops/TF-VictorOps-User/docs/README.md)