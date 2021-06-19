# Equinix Metal Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/metal**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_token` - (Required) This is your Equinix Metal API Auth token.
* `max_retries` - Maximum number of retries in case of network failure.
* `max_retry_wait_seconds` - Maximum time to wait in case of network failure.


## Supported Resources

* [TF::Metal::BgpSession](../resources/metal/TF-Metal-BgpSession/docs/README.md)
* [TF::Metal::Connection](../resources/metal/TF-Metal-Connection/docs/README.md)
* [TF::Metal::DeviceNetworkType](../resources/metal/TF-Metal-DeviceNetworkType/docs/README.md)
* [TF::Metal::Device](../resources/metal/TF-Metal-Device/docs/README.md)
* [TF::Metal::IpAttachment](../resources/metal/TF-Metal-IpAttachment/docs/README.md)
* [TF::Metal::Organization](../resources/metal/TF-Metal-Organization/docs/README.md)
* [TF::Metal::PortVlanAttachment](../resources/metal/TF-Metal-PortVlanAttachment/docs/README.md)
* [TF::Metal::ProjectSshKey](../resources/metal/TF-Metal-ProjectSshKey/docs/README.md)
* [TF::Metal::Project](../resources/metal/TF-Metal-Project/docs/README.md)
* [TF::Metal::ReservedIpBlock](../resources/metal/TF-Metal-ReservedIpBlock/docs/README.md)
* [TF::Metal::SpotMarketRequest](../resources/metal/TF-Metal-SpotMarketRequest/docs/README.md)
* [TF::Metal::SshKey](../resources/metal/TF-Metal-SshKey/docs/README.md)
* [TF::Metal::VirtualCircuit](../resources/metal/TF-Metal-VirtualCircuit/docs/README.md)
* [TF::Metal::Vlan](../resources/metal/TF-Metal-Vlan/docs/README.md)
* [TF::Metal::VolumeAttachment](../resources/metal/TF-Metal-VolumeAttachment/docs/README.md)
* [TF::Metal::Volume](../resources/metal/TF-Metal-Volume/docs/README.md)