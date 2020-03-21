# Chef Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/chef**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `server_url` - (Required) The HTTP(S) API URL of the Chef server to use. If
  the target Chef server supports organizations, use the full URL of the
  organization you wish to configure.
* `client_name` - (Required) The name of the client account to use when making
  requests. This must have been already configured on the Chef server.
* `key_material` - (Required) The PEM-formatted private key contents belonging to
  the configured client. This is issued by the server when a new client object
  is created.
* `allow_unverified_ssl` - (Optional) Boolean indicating whether to make
  requests to a Chef server whose SSL certicate cannot be verified. Defaults
  to ``false``.


## Supported Resources

* [Terraform::Chef::DataBagItem](../resources/chef/Terraform-Chef-DataBagItem/docs/README.md)
* [Terraform::Chef::DataBag](../resources/chef/Terraform-Chef-DataBag/docs/README.md)
* [Terraform::Chef::Environment](../resources/chef/Terraform-Chef-Environment/docs/README.md)
* [Terraform::Chef::Node](../resources/chef/Terraform-Chef-Node/docs/README.md)
* [Terraform::Chef::Role](../resources/chef/Terraform-Chef-Role/docs/README.md)