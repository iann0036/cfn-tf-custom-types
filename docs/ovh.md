# OVH Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ovh**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `endpoint` - (Required) Specify which API endpoint to use.
  It can be set using the `OVH_ENDPOINT` environment
  variable. e.g. `ovh-eu` or `ovh-ca`.

* `application_key` - (Optional) The API Application Key.

* `application_secret` - (Optional) The API Application Secret.

* `consumer_key` - (Optional) The API Consumer key.


## Supported Resources

* [Terraform::OVH::CloudNetworkPrivateSubnet](../resources/ovh/Terraform-OVH-CloudNetworkPrivateSubnet/docs/README.md)
* [Terraform::OVH::CloudNetworkPrivate](../resources/ovh/Terraform-OVH-CloudNetworkPrivate/docs/README.md)
* [Terraform::OVH::CloudUser](../resources/ovh/Terraform-OVH-CloudUser/docs/README.md)
* [Terraform::OVH::DedicatedServerInstallTask](../resources/ovh/Terraform-OVH-DedicatedServerInstallTask/docs/README.md)
* [Terraform::OVH::DedicatedServerRebootTask](../resources/ovh/Terraform-OVH-DedicatedServerRebootTask/docs/README.md)
* [Terraform::OVH::DedicatedServerUpdate](../resources/ovh/Terraform-OVH-DedicatedServerUpdate/docs/README.md)
* [Terraform::OVH::DomainZoneRecord](../resources/ovh/Terraform-OVH-DomainZoneRecord/docs/README.md)
* [Terraform::OVH::DomainZoneRedirection](../resources/ovh/Terraform-OVH-DomainZoneRedirection/docs/README.md)
* [Terraform::OVH::IpReverse](../resources/ovh/Terraform-OVH-IpReverse/docs/README.md)
* [Terraform::OVH::IploadbalancingHttpFarmServer](../resources/ovh/Terraform-OVH-IploadbalancingHttpFarmServer/docs/README.md)
* [Terraform::OVH::IploadbalancingHttpFarm](../resources/ovh/Terraform-OVH-IploadbalancingHttpFarm/docs/README.md)
* [Terraform::OVH::IploadbalancingHttpFrontend](../resources/ovh/Terraform-OVH-IploadbalancingHttpFrontend/docs/README.md)
* [Terraform::OVH::IploadbalancingHttpRouteRule](../resources/ovh/Terraform-OVH-IploadbalancingHttpRouteRule/docs/README.md)
* [Terraform::OVH::IploadbalancingHttpRoute](../resources/ovh/Terraform-OVH-IploadbalancingHttpRoute/docs/README.md)
* [Terraform::OVH::IploadbalancingRefresh](../resources/ovh/Terraform-OVH-IploadbalancingRefresh/docs/README.md)
* [Terraform::OVH::IploadbalancingTcpFarmServer](../resources/ovh/Terraform-OVH-IploadbalancingTcpFarmServer/docs/README.md)
* [Terraform::OVH::IploadbalancingTcpFarm](../resources/ovh/Terraform-OVH-IploadbalancingTcpFarm/docs/README.md)
* [Terraform::OVH::IploadbalancingTcpFrontend](../resources/ovh/Terraform-OVH-IploadbalancingTcpFrontend/docs/README.md)
* [Terraform::OVH::IploadbalancingVrackNetwork](../resources/ovh/Terraform-OVH-IploadbalancingVrackNetwork/docs/README.md)
* [Terraform::OVH::MeInstallationTemplatePartitionSchemeHardwareRaid](../resources/ovh/Terraform-OVH-MeInstallationTemplatePartitionSchemeHardwareRaid/docs/README.md)
* [Terraform::OVH::MeInstallationTemplatePartitionSchemePartition](../resources/ovh/Terraform-OVH-MeInstallationTemplatePartitionSchemePartition/docs/README.md)
* [Terraform::OVH::MeInstallationTemplatePartitionScheme](../resources/ovh/Terraform-OVH-MeInstallationTemplatePartitionScheme/docs/README.md)
* [Terraform::OVH::MeInstallationTemplate](../resources/ovh/Terraform-OVH-MeInstallationTemplate/docs/README.md)
* [Terraform::OVH::MeSshKey](../resources/ovh/Terraform-OVH-MeSshKey/docs/README.md)
* [Terraform::OVH::PubliccloudPrivateNetworkSubnet](../resources/ovh/Terraform-OVH-PubliccloudPrivateNetworkSubnet/docs/README.md)
* [Terraform::OVH::PubliccloudPrivateNetwork](../resources/ovh/Terraform-OVH-PubliccloudPrivateNetwork/docs/README.md)
* [Terraform::OVH::PubliccloudUser](../resources/ovh/Terraform-OVH-PubliccloudUser/docs/README.md)
* [Terraform::OVH::VrackCloudproject](../resources/ovh/Terraform-OVH-VrackCloudproject/docs/README.md)
* [Terraform::OVH::VrackDedicatedServerInterface](../resources/ovh/Terraform-OVH-VrackDedicatedServerInterface/docs/README.md)
* [Terraform::OVH::VrackDedicatedServer](../resources/ovh/Terraform-OVH-VrackDedicatedServer/docs/README.md)
* [Terraform::OVH::VrackIploadbalancing](../resources/ovh/Terraform-OVH-VrackIploadbalancing/docs/README.md)
* [Terraform::OVH::VrackPubliccloudAttachment](../resources/ovh/Terraform-OVH-VrackPubliccloudAttachment/docs/README.md)