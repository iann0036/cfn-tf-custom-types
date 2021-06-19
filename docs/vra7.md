# VMware vRealize Automation 7 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vra7**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) This is the username for vRA7 API operations.
* `password` - (Required) This is the password for vRA7 API operations.
* `tenant` - (Required) This is the vRA tenant ID vRA API
  operations. Can also be specified with the `VRA7_SERVER` environment
  variable.
* `host` - (Required) This is the vRA server name for vRA API
  operations. Can also be specified with the `VRA7_HOST` environment
  variable.
* `insecure` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is `false`.


## Supported Resources

* [TF::VRA7::Deployment](../resources/vra7/TF-VRA7-Deployment/docs/README.md)