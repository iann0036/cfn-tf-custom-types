# Brightbox Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/brightbox**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `apiclient` - (optional) This is the Brightbox client id for an
account.

* `apisecret` - (optional) This is the Brightbox client secret. This can
also be specified with the `BRIGHTBOX_CLIENT_SECRET` shell environment
variable.

* `username` - (optional) This is the Brightbox user logon. This can
also be specified with the `BRIGHTBOX_USER_NAME` shell environment
variable.

* `password` - (optional) This is the Brightbox user logon password. This
can also be specified with the `BRIGHTBOX_PASSWORD` shell environment
variable.

* `account` - (optional) This is the Brightbox account you wish to
operate upon.

* `apiurl` - (Optional) Use this to override the default endpoint URL
constructed for the region. It's typically used to connect to custom
Brightbox endpoints.

~> **NOTE:** At least one of `username` or `apiclient` must be specified.


## Supported Resources

* [Terraform::Brightbox::ApiClient](../resources/brightbox/Terraform-Brightbox-ApiClient/docs/README.md)
* [Terraform::Brightbox::Cloudip](../resources/brightbox/Terraform-Brightbox-Cloudip/docs/README.md)
* [Terraform::Brightbox::DatabaseServer](../resources/brightbox/Terraform-Brightbox-DatabaseServer/docs/README.md)
* [Terraform::Brightbox::FirewallPolicy](../resources/brightbox/Terraform-Brightbox-FirewallPolicy/docs/README.md)
* [Terraform::Brightbox::FirewallRule](../resources/brightbox/Terraform-Brightbox-FirewallRule/docs/README.md)
* [Terraform::Brightbox::LoadBalancer](../resources/brightbox/Terraform-Brightbox-LoadBalancer/docs/README.md)
* [Terraform::Brightbox::OrbitContainer](../resources/brightbox/Terraform-Brightbox-OrbitContainer/docs/README.md)
* [Terraform::Brightbox::ServerGroup](../resources/brightbox/Terraform-Brightbox-ServerGroup/docs/README.md)
* [Terraform::Brightbox::Server](../resources/brightbox/Terraform-Brightbox-Server/docs/README.md)