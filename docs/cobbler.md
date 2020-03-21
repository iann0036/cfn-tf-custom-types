# Cobbler Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cobbler**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) The username to the Cobbler service.

* `password` - (Required) The password to the Cobbler service.

* `url` - (Required) The url to the Cobbler service.

* `insecure` - (Optional) Ignore SSL certificate warnings and errors.

* `cacert_file` - (Optional) The path or contents of an SSL CA certificate.
  This can also be specified with the `COBBLER_CACERT_FILE` shell environment
  variable.


## Supported Resources

* [Terraform::Cobbler::Distro](../resources/cobbler/Terraform-Cobbler-Distro/docs/README.md)
* [Terraform::Cobbler::KickstartFile](../resources/cobbler/Terraform-Cobbler-KickstartFile/docs/README.md)
* [Terraform::Cobbler::Profile](../resources/cobbler/Terraform-Cobbler-Profile/docs/README.md)
* [Terraform::Cobbler::Repo](../resources/cobbler/Terraform-Cobbler-Repo/docs/README.md)
* [Terraform::Cobbler::Snippet](../resources/cobbler/Terraform-Cobbler-Snippet/docs/README.md)
* [Terraform::Cobbler::System](../resources/cobbler/Terraform-Cobbler-System/docs/README.md)