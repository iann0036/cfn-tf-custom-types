# CloudScale Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudscale**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) Your cloudscale.ch API token. Please create a cloudscale.ch API token with read/write access in our [Cloud Control Panel](https://control.cloudscale.ch/).


## Supported Resources

* [Terraform::CloudScale::FloatingIp](../resources/cloudscale/Terraform-CloudScale-FloatingIp/docs/README.md)
* [Terraform::CloudScale::Network](../resources/cloudscale/Terraform-CloudScale-Network/docs/README.md)
* [Terraform::CloudScale::ServerGroup](../resources/cloudscale/Terraform-CloudScale-ServerGroup/docs/README.md)
* [Terraform::CloudScale::Server](../resources/cloudscale/Terraform-CloudScale-Server/docs/README.md)
* [Terraform::CloudScale::Volume](../resources/cloudscale/Terraform-CloudScale-Volume/docs/README.md)