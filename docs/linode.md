# Linode Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/linode**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) This is your [Linode APIv4 Token](https://developers.linode.com/api/v4#section/Personal-Access-Token).

* `url` - (Optional) The HTTP(S) API address of the Linode API to use.

* `ua_prefix` - (Optional) An HTTP User-Agent Prefix to prepend in API requests.

* `skip_instance_ready_poll` - (Optional) Skip waiting for a linode_instance resource to be running.

* `min_retry_delay_ms` - (Optional) Minimum delay in milliseconds before retrying a request.

* `max_retry_delay_ms` - (Optional) Maximum delay in milliseconds before retrying a request.


## Supported Resources

* [TF::Linode::DomainRecord](../resources/linode/TF-Linode-DomainRecord/docs/README.md)
* [TF::Linode::Domain](../resources/linode/TF-Linode-Domain/docs/README.md)
* [TF::Linode::Firewall](../resources/linode/TF-Linode-Firewall/docs/README.md)
* [TF::Linode::Image](../resources/linode/TF-Linode-Image/docs/README.md)
* [TF::Linode::InstanceIp](../resources/linode/TF-Linode-InstanceIp/docs/README.md)
* [TF::Linode::Instance](../resources/linode/TF-Linode-Instance/docs/README.md)
* [TF::Linode::LkeCluster](../resources/linode/TF-Linode-LkeCluster/docs/README.md)
* [TF::Linode::NodebalancerConfig](../resources/linode/TF-Linode-NodebalancerConfig/docs/README.md)
* [TF::Linode::NodebalancerNode](../resources/linode/TF-Linode-NodebalancerNode/docs/README.md)
* [TF::Linode::Nodebalancer](../resources/linode/TF-Linode-Nodebalancer/docs/README.md)
* [TF::Linode::ObjectStorageBucket](../resources/linode/TF-Linode-ObjectStorageBucket/docs/README.md)
* [TF::Linode::ObjectStorageKey](../resources/linode/TF-Linode-ObjectStorageKey/docs/README.md)
* [TF::Linode::ObjectStorageObject](../resources/linode/TF-Linode-ObjectStorageObject/docs/README.md)
* [TF::Linode::Rdns](../resources/linode/TF-Linode-Rdns/docs/README.md)
* [TF::Linode::Sshkey](../resources/linode/TF-Linode-Sshkey/docs/README.md)
* [TF::Linode::Stackscript](../resources/linode/TF-Linode-Stackscript/docs/README.md)
* [TF::Linode::Token](../resources/linode/TF-Linode-Token/docs/README.md)
* [TF::Linode::User](../resources/linode/TF-Linode-User/docs/README.md)
* [TF::Linode::Volume](../resources/linode/TF-Linode-Volume/docs/README.md)