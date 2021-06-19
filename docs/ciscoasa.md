# Cisco ASA Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ciscoasa**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_url` - (Required) URL of the API for the ASA Firewall. This is typically not enabled by default, please refer to the [Cisco documentation](https://www.cisco.com/c/en/us/td/docs/security/asa/api/qsg-asa-api.html) for how to enable it.

* `username` - (Required) The username for logging in to the API.

* `password` - (Required) The password for logging in to the API.

* `ssl_no_verify` - (Required) A flag indicating whether or not to verify the TLS certificate.


## Supported Resources

* [TF::CiscoASA::AccessInRules](../resources/ciscoasa/TF-CiscoASA-AccessInRules/docs/README.md)
* [TF::CiscoASA::AccessOutRules](../resources/ciscoasa/TF-CiscoASA-AccessOutRules/docs/README.md)
* [TF::CiscoASA::Acl](../resources/ciscoasa/TF-CiscoASA-Acl/docs/README.md)
* [TF::CiscoASA::NetworkObjectGroup](../resources/ciscoasa/TF-CiscoASA-NetworkObjectGroup/docs/README.md)
* [TF::CiscoASA::NetworkObject](../resources/ciscoasa/TF-CiscoASA-NetworkObject/docs/README.md)
* [TF::CiscoASA::NetworkServiceGroup](../resources/ciscoasa/TF-CiscoASA-NetworkServiceGroup/docs/README.md)
* [TF::CiscoASA::StaticRoute](../resources/ciscoasa/TF-CiscoASA-StaticRoute/docs/README.md)