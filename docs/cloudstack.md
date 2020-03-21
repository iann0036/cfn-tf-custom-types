# CloudStack Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/cloudstack**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_url` - (Optional) This is the CloudStack API URL.

* `api_key` - (Optional) This is the CloudStack API key.

* `secret_key` - (Optional) This is the CloudStack secret key.

* `config` - (Optional) The path to a `CloudMonkey` config file. If set the API
  URL, key and secret will be retrieved from this file.

* `profile` - (Optional) Used together with the `config` option. Specifies which
  `CloudMonkey` profile in the config file to use.

* `http_get_only` - (Optional) Some cloud providers only allow HTTP GET calls to
  their CloudStack API. If using such a provider, you need to set this to `true`
  in order for the provider to only make GET calls and no POST calls.

* `timeout` - (Optional) A value in seconds. This is the time allowed for Cloudstack
  to complete each asynchronous job triggered. Otherwise, this will default to 300
  seconds.


## Supported Resources

* [Terraform::CloudStack::AffinityGroup](../resources/cloudstack/Terraform-CloudStack-AffinityGroup/docs/README.md)
* [Terraform::CloudStack::AutoscaleVmProfile](../resources/cloudstack/Terraform-CloudStack-AutoscaleVmProfile/docs/README.md)
* [Terraform::CloudStack::Disk](../resources/cloudstack/Terraform-CloudStack-Disk/docs/README.md)
* [Terraform::CloudStack::EgressFirewall](../resources/cloudstack/Terraform-CloudStack-EgressFirewall/docs/README.md)
* [Terraform::CloudStack::Firewall](../resources/cloudstack/Terraform-CloudStack-Firewall/docs/README.md)
* [Terraform::CloudStack::Instance](../resources/cloudstack/Terraform-CloudStack-Instance/docs/README.md)
* [Terraform::CloudStack::Ipaddress](../resources/cloudstack/Terraform-CloudStack-Ipaddress/docs/README.md)
* [Terraform::CloudStack::LoadbalancerRule](../resources/cloudstack/Terraform-CloudStack-LoadbalancerRule/docs/README.md)
* [Terraform::CloudStack::NetworkAclRule](../resources/cloudstack/Terraform-CloudStack-NetworkAclRule/docs/README.md)
* [Terraform::CloudStack::NetworkAcl](../resources/cloudstack/Terraform-CloudStack-NetworkAcl/docs/README.md)
* [Terraform::CloudStack::Network](../resources/cloudstack/Terraform-CloudStack-Network/docs/README.md)
* [Terraform::CloudStack::Nic](../resources/cloudstack/Terraform-CloudStack-Nic/docs/README.md)
* [Terraform::CloudStack::PortForward](../resources/cloudstack/Terraform-CloudStack-PortForward/docs/README.md)
* [Terraform::CloudStack::PrivateGateway](../resources/cloudstack/Terraform-CloudStack-PrivateGateway/docs/README.md)
* [Terraform::CloudStack::SecondaryIpaddress](../resources/cloudstack/Terraform-CloudStack-SecondaryIpaddress/docs/README.md)
* [Terraform::CloudStack::SecurityGroupRule](../resources/cloudstack/Terraform-CloudStack-SecurityGroupRule/docs/README.md)
* [Terraform::CloudStack::SecurityGroup](../resources/cloudstack/Terraform-CloudStack-SecurityGroup/docs/README.md)
* [Terraform::CloudStack::SshKeypair](../resources/cloudstack/Terraform-CloudStack-SshKeypair/docs/README.md)
* [Terraform::CloudStack::StaticNat](../resources/cloudstack/Terraform-CloudStack-StaticNat/docs/README.md)
* [Terraform::CloudStack::StaticRoute](../resources/cloudstack/Terraform-CloudStack-StaticRoute/docs/README.md)
* [Terraform::CloudStack::Template](../resources/cloudstack/Terraform-CloudStack-Template/docs/README.md)
* [Terraform::CloudStack::Vpc](../resources/cloudstack/Terraform-CloudStack-Vpc/docs/README.md)
* [Terraform::CloudStack::VpnConnection](../resources/cloudstack/Terraform-CloudStack-VpnConnection/docs/README.md)
* [Terraform::CloudStack::VpnCustomerGateway](../resources/cloudstack/Terraform-CloudStack-VpnCustomerGateway/docs/README.md)
* [Terraform::CloudStack::VpnGateway](../resources/cloudstack/Terraform-CloudStack-VpnGateway/docs/README.md)