# Skytap Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/skytap**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) This is the Skytap username.
* `api_token` - (Required) This is the Skytap API token.





## Supported Resources

* [Terraform::Skytap::Environment](../resources/skytap/Terraform-Skytap-Environment/docs/README.md)
* [Terraform::Skytap::IcnrTunnel](../resources/skytap/Terraform-Skytap-IcnrTunnel/docs/README.md)
* [Terraform::Skytap::LabelCategory](../resources/skytap/Terraform-Skytap-LabelCategory/docs/README.md)
* [Terraform::Skytap::Network](../resources/skytap/Terraform-Skytap-Network/docs/README.md)
* [Terraform::Skytap::Project](../resources/skytap/Terraform-Skytap-Project/docs/README.md)
* [Terraform::Skytap::Vm](../resources/skytap/Terraform-Skytap-Vm/docs/README.md)