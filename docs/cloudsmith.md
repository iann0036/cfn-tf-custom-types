# Cloudsmith Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudsmith**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) The API key for authenticating with the Cloudsmith API.
* `api_host` - (Optional) The API host to connect to (used to connect to a non-production Cloudsmith instance, mostly useful for testing).


## Supported Resources

* [TF::Cloudsmith::Entitlement](../resources/cloudsmith/TF-Cloudsmith-Entitlement/docs/README.md)
* [TF::Cloudsmith::Repository](../resources/cloudsmith/TF-Cloudsmith-Repository/docs/README.md)