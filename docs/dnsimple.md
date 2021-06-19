# DNSimple Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dnsimple**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) The DNSimple API v2 token. Please note that this must be an [API v2 token](https://support.dnsimple.com/articles/api-access-token/). You can use either an User or Account token, but an Account token is recommended.
* `account` - (Required) The ID of the account associated with the token.
* `sandbox` - Set to true to connects to the API [sandbox environment](https://developer.dnsimple.com/sandbox/).


## Supported Resources

* [TF::DNSimple::EmailForward](../resources/dnsimple/TF-DNSimple-EmailForward/docs/README.md)
* [TF::DNSimple::Record](../resources/dnsimple/TF-DNSimple-Record/docs/README.md)