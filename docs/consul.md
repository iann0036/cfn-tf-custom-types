# Consul Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/consul**. The below arguments may be included as the key/value or JSON properties in the secret:

* `address` - (Optional) The HTTP(S) API address of the agent to use. Defaults to "127.0.0.1:8500".
* `scheme` - (Optional) The URL scheme of the agent to use ("http" or "https"). Defaults to "http".
* `http_auth` - (Optional) HTTP Basic Authentication credentials to be used when communicating with Consul, in the format of either `user` or `user:pass`.
* `datacenter` - (Optional) The datacenter to use. Defaults to that of the agent.
* `token` - (Optional) The ACL token to use by default when making requests to the agent.
* `ca_file` - (Optional) A path to a PEM-encoded certificate authority used to verify the remote agent's certificate.
* `ca_pem` - (Optional) PEM-encoded certificate authority used to verify the remote agent's certificate.
* `cert_file` - (Optional) A path to a PEM-encoded certificate provided to the remote agent; requires use of `key_file` or `key_pem`.
* `cert_pem` - (Optional) PEM-encoded certificate provided to the remote agent; requires use of `key_file` or `key_pem`.
* `key_file`- (Optional) A path to a PEM-encoded private key, required if `cert_file` or `cert_pem` is specified.
* `key_pem`- (Optional) PEM-encoded private key, required if `cert_file` or `cert_pem` is specified.
* `ca_path` - (Optional) A path to a directory of PEM-encoded certificate authority files to use to check the authenticity of client and server connections.
* `insecure_https`- (Optional) Boolean value to disable SSL certificate verification; setting this value to true is not recommended for production use. Only use this with scheme set to "https".


## Supported Resources

* [TF::Consul::AclAuthMethod](../resources/consul/TF-Consul-AclAuthMethod/docs/README.md)
* [TF::Consul::AclBindingRule](../resources/consul/TF-Consul-AclBindingRule/docs/README.md)
* [TF::Consul::AclPolicy](../resources/consul/TF-Consul-AclPolicy/docs/README.md)
* [TF::Consul::AclRole](../resources/consul/TF-Consul-AclRole/docs/README.md)
* [TF::Consul::AclTokenPolicyAttachment](../resources/consul/TF-Consul-AclTokenPolicyAttachment/docs/README.md)
* [TF::Consul::AclTokenRoleAttachment](../resources/consul/TF-Consul-AclTokenRoleAttachment/docs/README.md)
* [TF::Consul::AclToken](../resources/consul/TF-Consul-AclToken/docs/README.md)
* [TF::Consul::AgentService](../resources/consul/TF-Consul-AgentService/docs/README.md)
* [TF::Consul::AutopilotConfig](../resources/consul/TF-Consul-AutopilotConfig/docs/README.md)
* [TF::Consul::CatalogEntry](../resources/consul/TF-Consul-CatalogEntry/docs/README.md)
* [TF::Consul::CertificateAuthority](../resources/consul/TF-Consul-CertificateAuthority/docs/README.md)
* [TF::Consul::ConfigEntry](../resources/consul/TF-Consul-ConfigEntry/docs/README.md)
* [TF::Consul::Intention](../resources/consul/TF-Consul-Intention/docs/README.md)
* [TF::Consul::KeyPrefix](../resources/consul/TF-Consul-KeyPrefix/docs/README.md)
* [TF::Consul::Keys](../resources/consul/TF-Consul-Keys/docs/README.md)
* [TF::Consul::License](../resources/consul/TF-Consul-License/docs/README.md)
* [TF::Consul::Namespace](../resources/consul/TF-Consul-Namespace/docs/README.md)
* [TF::Consul::NetworkArea](../resources/consul/TF-Consul-NetworkArea/docs/README.md)
* [TF::Consul::Node](../resources/consul/TF-Consul-Node/docs/README.md)
* [TF::Consul::PreparedQuery](../resources/consul/TF-Consul-PreparedQuery/docs/README.md)
* [TF::Consul::Service](../resources/consul/TF-Consul-Service/docs/README.md)