# Nutanix Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nutanix**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - **(Required)** This is the username for the Prism Elements or Prism Central instance.
* `password` - **(Required)** This is the password for the Prism Elements or Prism Central instance.
* `endpoint` - **(Required)** This is the endpoint for the Prism Elements or Prism Central instance.
* `insecure` - (Optional) This specifies whether to allow verify ssl certificates. This can also be specified with `NUTANIX_INSECURE`. Defaults to `false`.
* `port` - (Optional) This is the port for the Prism Elements or Prism Central instance. Defaults to `9440`.
* `session_auth` - (Optional) This specifies whether to use [session authentication](#session-based-authentication). Defaults to `true`
* `wait_timeout` - (Optional) This specifies the timeout on all resource operations in the provider in minutes. Defaults to `1`. Also see [resource timeouts](#resource-timeouts).
* `proxy_url` - (Optional) This specifies the url to proxy through to access the Prism Elements or Prism Central endpoint.


## Supported Resources

* [TF::Nutanix::AccessControlPolicy](../resources/nutanix/TF-Nutanix-AccessControlPolicy/docs/README.md)
* [TF::Nutanix::CategoryKey](../resources/nutanix/TF-Nutanix-CategoryKey/docs/README.md)
* [TF::Nutanix::CategoryValue](../resources/nutanix/TF-Nutanix-CategoryValue/docs/README.md)
* [TF::Nutanix::Image](../resources/nutanix/TF-Nutanix-Image/docs/README.md)
* [TF::Nutanix::KarbonCluster](../resources/nutanix/TF-Nutanix-KarbonCluster/docs/README.md)
* [TF::Nutanix::KarbonPrivateRegistry](../resources/nutanix/TF-Nutanix-KarbonPrivateRegistry/docs/README.md)
* [TF::Nutanix::NetworkSecurityRule](../resources/nutanix/TF-Nutanix-NetworkSecurityRule/docs/README.md)
* [TF::Nutanix::Project](../resources/nutanix/TF-Nutanix-Project/docs/README.md)
* [TF::Nutanix::ProtectionRule](../resources/nutanix/TF-Nutanix-ProtectionRule/docs/README.md)
* [TF::Nutanix::RecoveryPlan](../resources/nutanix/TF-Nutanix-RecoveryPlan/docs/README.md)
* [TF::Nutanix::Role](../resources/nutanix/TF-Nutanix-Role/docs/README.md)
* [TF::Nutanix::Subnet](../resources/nutanix/TF-Nutanix-Subnet/docs/README.md)
* [TF::Nutanix::User](../resources/nutanix/TF-Nutanix-User/docs/README.md)
* [TF::Nutanix::VirtualMachine](../resources/nutanix/TF-Nutanix-VirtualMachine/docs/README.md)