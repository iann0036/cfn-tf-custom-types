# Consul Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/consul**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `address` - (Optional) The HTTP(S) API address of the agent to use. Defaults to "127.0.0.1:8500".
* `scheme` - (Optional) The URL scheme of the agent to use ("http" or "https"). Defaults to "http".
* `http_auth` - (Optional) HTTP Basic Authentication credentials to be used when communicating with Consul, in the format of either `user` or `user:pass`.
* `datacenter` - (Optional) The datacenter to use. Defaults to that of the agent.
* `token` - (Optional) The ACL token to use by default when making requests to the agent.
* `ca_file` - (Optional) A path to a PEM-encoded certificate authority used to verify the remote agent's certificate.
* `cert_file` - (Optional) A path to a PEM-encoded certificate provided to the remote agent; requires use of `key_file`.
* `key_file`- (Optional) A path to a PEM-encoded private key, required if `cert_file` is specified.
* `ca_path` - (Optional) A path to a directory of PEM-encoded certificate authority files to use to check the authenticity of client and server connections.
* `insecure_https`- (Optional) Boolean value to disable SSL certificate verification; setting this value to true is not recommended for production use. Only use this with scheme set to "https".


## Supported Resources

* [Terraform::Consul::AclAuthMethod](../resources/consul/Terraform-Consul-AclAuthMethod/docs/README.md)
* [Terraform::Consul::AclBindingRule](../resources/consul/Terraform-Consul-AclBindingRule/docs/README.md)
* [Terraform::Consul::AclPolicy](../resources/consul/Terraform-Consul-AclPolicy/docs/README.md)
* [Terraform::Consul::AclRole](../resources/consul/Terraform-Consul-AclRole/docs/README.md)
* [Terraform::Consul::AclTokenPolicyAttachment](../resources/consul/Terraform-Consul-AclTokenPolicyAttachment/docs/README.md)
* [Terraform::Consul::AclToken](../resources/consul/Terraform-Consul-AclToken/docs/README.md)
* [Terraform::Consul::AgentService](../resources/consul/Terraform-Consul-AgentService/docs/README.md)
* [Terraform::Consul::AutopilotConfig](../resources/consul/Terraform-Consul-AutopilotConfig/docs/README.md)
* [Terraform::Consul::CatalogEntry](../resources/consul/Terraform-Consul-CatalogEntry/docs/README.md)
* [Terraform::Consul::ConfigEntry](../resources/consul/Terraform-Consul-ConfigEntry/docs/README.md)
* [Terraform::Consul::Intention](../resources/consul/Terraform-Consul-Intention/docs/README.md)
* [Terraform::Consul::KeyPrefix](../resources/consul/Terraform-Consul-KeyPrefix/docs/README.md)
* [Terraform::Consul::Keys](../resources/consul/Terraform-Consul-Keys/docs/README.md)
* [Terraform::Consul::License](../resources/consul/Terraform-Consul-License/docs/README.md)
* [Terraform::Consul::Node](../resources/consul/Terraform-Consul-Node/docs/README.md)
* [Terraform::Consul::PreparedQuery](../resources/consul/Terraform-Consul-PreparedQuery/docs/README.md)
* [Terraform::Consul::Service](../resources/consul/Terraform-Consul-Service/docs/README.md)