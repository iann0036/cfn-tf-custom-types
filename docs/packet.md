# Packet Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/packet**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_token` - (Required) This is your Equinix Metal API Auth token.


## Supported Resources

* [TF::Packet::BgpSession](../resources/packet/TF-Packet-BgpSession/docs/README.md)
* [TF::Packet::DeviceNetworkType](../resources/packet/TF-Packet-DeviceNetworkType/docs/README.md)
* [TF::Packet::Device](../resources/packet/TF-Packet-Device/docs/README.md)
* [TF::Packet::IpAttachment](../resources/packet/TF-Packet-IpAttachment/docs/README.md)
* [TF::Packet::Organization](../resources/packet/TF-Packet-Organization/docs/README.md)
* [TF::Packet::PortVlanAttachment](../resources/packet/TF-Packet-PortVlanAttachment/docs/README.md)
* [TF::Packet::ProjectSshKey](../resources/packet/TF-Packet-ProjectSshKey/docs/README.md)
* [TF::Packet::Project](../resources/packet/TF-Packet-Project/docs/README.md)
* [TF::Packet::ReservedIpBlock](../resources/packet/TF-Packet-ReservedIpBlock/docs/README.md)
* [TF::Packet::SpotMarketRequest](../resources/packet/TF-Packet-SpotMarketRequest/docs/README.md)
* [TF::Packet::SshKey](../resources/packet/TF-Packet-SshKey/docs/README.md)
* [TF::Packet::Vlan](../resources/packet/TF-Packet-Vlan/docs/README.md)
* [TF::Packet::VolumeAttachment](../resources/packet/TF-Packet-VolumeAttachment/docs/README.md)
* [TF::Packet::Volume](../resources/packet/TF-Packet-Volume/docs/README.md)