# Packet Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/packet**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `auth_token` - (Required) This is your Packet API Auth token.


## Supported Resources

* [Terraform::Packet::BgpSession](../resources/packet/Terraform-Packet-BgpSession/docs/README.md)
* [Terraform::Packet::Connect](../resources/packet/Terraform-Packet-Connect/docs/README.md)
* [Terraform::Packet::Device](../resources/packet/Terraform-Packet-Device/docs/README.md)
* [Terraform::Packet::IpAttachment](../resources/packet/Terraform-Packet-IpAttachment/docs/README.md)
* [Terraform::Packet::Organization](../resources/packet/Terraform-Packet-Organization/docs/README.md)
* [Terraform::Packet::PortVlanAttachment](../resources/packet/Terraform-Packet-PortVlanAttachment/docs/README.md)
* [Terraform::Packet::ProjectSshKey](../resources/packet/Terraform-Packet-ProjectSshKey/docs/README.md)
* [Terraform::Packet::Project](../resources/packet/Terraform-Packet-Project/docs/README.md)
* [Terraform::Packet::ReservedIpBlock](../resources/packet/Terraform-Packet-ReservedIpBlock/docs/README.md)
* [Terraform::Packet::SpotMarketRequest](../resources/packet/Terraform-Packet-SpotMarketRequest/docs/README.md)
* [Terraform::Packet::SshKey](../resources/packet/Terraform-Packet-SshKey/docs/README.md)
* [Terraform::Packet::Vlan](../resources/packet/Terraform-Packet-Vlan/docs/README.md)
* [Terraform::Packet::VolumeAttachment](../resources/packet/Terraform-Packet-VolumeAttachment/docs/README.md)
* [Terraform::Packet::Volume](../resources/packet/Terraform-Packet-Volume/docs/README.md)