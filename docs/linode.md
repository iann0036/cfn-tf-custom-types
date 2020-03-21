# Linode Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/linode**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) This is your [Linode APIv4 Token](https://developers.linode.com/api/v4#section/Personal-Access-Token).

* `url` - (Optional) The HTTP(S) API address of the Linode API to use.

* `ua_prefix` - (Optional) An HTTP User-Agent Prefix to prepend in API requests.


## Supported Resources

* [Terraform::Linode::Domain](../resources/linode/Terraform-Linode-Domain/docs/README.md)
* [Terraform::Linode::Image](../resources/linode/Terraform-Linode-Image/docs/README.md)
* [Terraform::Linode::Instance](../resources/linode/Terraform-Linode-Instance/docs/README.md)
* [Terraform::Linode::NodebalancerConfig](../resources/linode/Terraform-Linode-NodebalancerConfig/docs/README.md)
* [Terraform::Linode::NodebalancerNode](../resources/linode/Terraform-Linode-NodebalancerNode/docs/README.md)
* [Terraform::Linode::Nodebalancer](../resources/linode/Terraform-Linode-Nodebalancer/docs/README.md)
* [Terraform::Linode::ObjectStorageBucket](../resources/linode/Terraform-Linode-ObjectStorageBucket/docs/README.md)
* [Terraform::Linode::ObjectStorageKey](../resources/linode/Terraform-Linode-ObjectStorageKey/docs/README.md)
* [Terraform::Linode::Rdns](../resources/linode/Terraform-Linode-Rdns/docs/README.md)
* [Terraform::Linode::Sshkey](../resources/linode/Terraform-Linode-Sshkey/docs/README.md)
* [Terraform::Linode::Stackscript](../resources/linode/Terraform-Linode-Stackscript/docs/README.md)
* [Terraform::Linode::Token](../resources/linode/Terraform-Linode-Token/docs/README.md)
* [Terraform::Linode::Volume](../resources/linode/Terraform-Linode-Volume/docs/README.md)