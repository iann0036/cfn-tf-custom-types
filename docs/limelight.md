# Limelight Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/limelight**. The below arguments may be included as the key/value or JSON properties in the secret:

* `config_api_base_url` - (Optional) The base URL to the Limelight Configuration API without the trailing slash
  included. This argument should remain
  unset in most cases.

* `edgefunctions_api_base_url` - (Optional) The base URL to the Limelight EdgeFunctions API without the trailing slash
  included. This argument should
  remain unset in most cases.

* `username` - (Required) Your Limelight Networks username.

* `api_key` - (Required) The shared API key for your username.


## Supported Resources

* [TF::Limelight::Delivery](../resources/limelight/TF-Limelight-Delivery/docs/README.md)
* [TF::Limelight::EdgefunctionAlias](../resources/limelight/TF-Limelight-EdgefunctionAlias/docs/README.md)
* [TF::Limelight::Edgefunction](../resources/limelight/TF-Limelight-Edgefunction/docs/README.md)