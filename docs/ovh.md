# OVH Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ovh**. The below arguments may be included as the key/value or JSON properties in the secret:

* `endpoint` - (Required) Specify which API endpoint to use.
  It can be set using the `OVH_ENDPOINT` environment
  variable. e.g. `ovh-eu` or `ovh-ca`.

* `application_key` - (Optional) The API Application Key.

* `application_secret` - (Optional) The API Application Secret.

* `consumer_key` - (Optional) The API Consumer key.


## Supported Resources

* [TF::OVH::CloudProjectContainerregistryUser](../resources/ovh/TF-OVH-CloudProjectContainerregistryUser/docs/README.md)
* [TF::OVH::CloudProjectContainerregistry](../resources/ovh/TF-OVH-CloudProjectContainerregistry/docs/README.md)
* [TF::OVH::CloudProjectKubeNodepool](../resources/ovh/TF-OVH-CloudProjectKubeNodepool/docs/README.md)
* [TF::OVH::CloudProjectKube](../resources/ovh/TF-OVH-CloudProjectKube/docs/README.md)
* [TF::OVH::CloudProjectNetworkPrivateSubnet](../resources/ovh/TF-OVH-CloudProjectNetworkPrivateSubnet/docs/README.md)
* [TF::OVH::CloudProjectNetworkPrivate](../resources/ovh/TF-OVH-CloudProjectNetworkPrivate/docs/README.md)
* [TF::OVH::CloudProjectUser](../resources/ovh/TF-OVH-CloudProjectUser/docs/README.md)
* [TF::OVH::DedicatedCephAcl](../resources/ovh/TF-OVH-DedicatedCephAcl/docs/README.md)
* [TF::OVH::DedicatedServerInstallTask](../resources/ovh/TF-OVH-DedicatedServerInstallTask/docs/README.md)
* [TF::OVH::DedicatedServerRebootTask](../resources/ovh/TF-OVH-DedicatedServerRebootTask/docs/README.md)
* [TF::OVH::DedicatedServerUpdate](../resources/ovh/TF-OVH-DedicatedServerUpdate/docs/README.md)
* [TF::OVH::DomainZoneRecord](../resources/ovh/TF-OVH-DomainZoneRecord/docs/README.md)
* [TF::OVH::DomainZoneRedirection](../resources/ovh/TF-OVH-DomainZoneRedirection/docs/README.md)
* [TF::OVH::IpReverse](../resources/ovh/TF-OVH-IpReverse/docs/README.md)
* [TF::OVH::IploadbalancingHttpFarmServer](../resources/ovh/TF-OVH-IploadbalancingHttpFarmServer/docs/README.md)
* [TF::OVH::IploadbalancingHttpFarm](../resources/ovh/TF-OVH-IploadbalancingHttpFarm/docs/README.md)
* [TF::OVH::IploadbalancingHttpFrontend](../resources/ovh/TF-OVH-IploadbalancingHttpFrontend/docs/README.md)
* [TF::OVH::IploadbalancingHttpRouteRule](../resources/ovh/TF-OVH-IploadbalancingHttpRouteRule/docs/README.md)
* [TF::OVH::IploadbalancingHttpRoute](../resources/ovh/TF-OVH-IploadbalancingHttpRoute/docs/README.md)
* [TF::OVH::IploadbalancingRefresh](../resources/ovh/TF-OVH-IploadbalancingRefresh/docs/README.md)
* [TF::OVH::IploadbalancingTcpFarmServer](../resources/ovh/TF-OVH-IploadbalancingTcpFarmServer/docs/README.md)
* [TF::OVH::IploadbalancingTcpFarm](../resources/ovh/TF-OVH-IploadbalancingTcpFarm/docs/README.md)
* [TF::OVH::IploadbalancingTcpFrontend](../resources/ovh/TF-OVH-IploadbalancingTcpFrontend/docs/README.md)
* [TF::OVH::IploadbalancingVrackNetwork](../resources/ovh/TF-OVH-IploadbalancingVrackNetwork/docs/README.md)
* [TF::OVH::MeIdentityUser](../resources/ovh/TF-OVH-MeIdentityUser/docs/README.md)
* [TF::OVH::MeInstallationTemplatePartitionSchemeHardwareRaid](../resources/ovh/TF-OVH-MeInstallationTemplatePartitionSchemeHardwareRaid/docs/README.md)
* [TF::OVH::MeInstallationTemplatePartitionSchemePartition](../resources/ovh/TF-OVH-MeInstallationTemplatePartitionSchemePartition/docs/README.md)
* [TF::OVH::MeInstallationTemplatePartitionScheme](../resources/ovh/TF-OVH-MeInstallationTemplatePartitionScheme/docs/README.md)
* [TF::OVH::MeInstallationTemplate](../resources/ovh/TF-OVH-MeInstallationTemplate/docs/README.md)
* [TF::OVH::MeIpxeScript](../resources/ovh/TF-OVH-MeIpxeScript/docs/README.md)
* [TF::OVH::MeSshKey](../resources/ovh/TF-OVH-MeSshKey/docs/README.md)
* [TF::OVH::VrackCloudproject](../resources/ovh/TF-OVH-VrackCloudproject/docs/README.md)
* [TF::OVH::VrackDedicatedServerInterface](../resources/ovh/TF-OVH-VrackDedicatedServerInterface/docs/README.md)
* [TF::OVH::VrackDedicatedServer](../resources/ovh/TF-OVH-VrackDedicatedServer/docs/README.md)
* [TF::OVH::VrackIploadbalancing](../resources/ovh/TF-OVH-VrackIploadbalancing/docs/README.md)