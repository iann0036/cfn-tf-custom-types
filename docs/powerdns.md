# PowerDNS Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/powerdns**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) The PowerDNS API key.
* `server_url` - (Required) The address of PowerDNS server. When no schema is provided, the default is `https`.
* `ca_certificate` - (Optional) A valid path of a Root CA Certificate in PEM format _or_ the content of a Root CA certificate in PEM format.
* `insecure_https` - (Optional) Set this to `true` to disable verification of the PowerDNS server's TLS certificate.


## Supported Resources

* [Terraform::PowerDNS::Record](../resources/powerdns/Terraform-PowerDNS-Record/docs/README.md)
* [Terraform::PowerDNS::Zone](../resources/powerdns/Terraform-PowerDNS-Zone/docs/README.md)