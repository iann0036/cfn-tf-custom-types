# Oracle Public Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/opc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `user` - (Optional) The username to use, generally your email address.

* `password` - (Optional) The password associated with the username to use.

* `identity_domain` - (Optional) The Identity Domain name (for Traditional accounts) or Identity Service ID (for IDCS accounts) of the environment to use.  

* `endpoint` - (Optional) The Compute Classic API endpoint to use, associated with your Oracle Cloud Account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_endpoint` - (Optional) The Storage Classic API endpoint to use, associated with your Oracle Storage Cloud account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_service_id` - (Optional) The Storage Service ID for authentication with the `storage_endpoint`  If not set the `identity_domain` value is used.

* `max_retries` - (Optional) The maximum number of tries to make for a successful response when operating on resources. Defaults to 1.

* `insecure` - (Optional) Skips TLS Verification for using self-signed certificates. Should only be used if absolutely needed.


## Supported Resources

* [TF::OPC::ComputeAcl](../resources/opc/TF-OPC-ComputeAcl/docs/README.md)
* [TF::OPC::ComputeImageListEntry](../resources/opc/TF-OPC-ComputeImageListEntry/docs/README.md)
* [TF::OPC::ComputeImageList](../resources/opc/TF-OPC-ComputeImageList/docs/README.md)
* [TF::OPC::ComputeInstance](../resources/opc/TF-OPC-ComputeInstance/docs/README.md)
* [TF::OPC::ComputeIpAddressAssociation](../resources/opc/TF-OPC-ComputeIpAddressAssociation/docs/README.md)
* [TF::OPC::ComputeIpAddressPrefixSet](../resources/opc/TF-OPC-ComputeIpAddressPrefixSet/docs/README.md)
* [TF::OPC::ComputeIpAddressReservation](../resources/opc/TF-OPC-ComputeIpAddressReservation/docs/README.md)
* [TF::OPC::ComputeIpAssociation](../resources/opc/TF-OPC-ComputeIpAssociation/docs/README.md)
* [TF::OPC::ComputeIpNetworkExchange](../resources/opc/TF-OPC-ComputeIpNetworkExchange/docs/README.md)
* [TF::OPC::ComputeIpNetwork](../resources/opc/TF-OPC-ComputeIpNetwork/docs/README.md)
* [TF::OPC::ComputeIpReservation](../resources/opc/TF-OPC-ComputeIpReservation/docs/README.md)
* [TF::OPC::ComputeMachineImage](../resources/opc/TF-OPC-ComputeMachineImage/docs/README.md)
* [TF::OPC::ComputeOrchestratedInstance](../resources/opc/TF-OPC-ComputeOrchestratedInstance/docs/README.md)
* [TF::OPC::ComputeRoute](../resources/opc/TF-OPC-ComputeRoute/docs/README.md)
* [TF::OPC::ComputeSecRule](../resources/opc/TF-OPC-ComputeSecRule/docs/README.md)
* [TF::OPC::ComputeSecurityApplication](../resources/opc/TF-OPC-ComputeSecurityApplication/docs/README.md)
* [TF::OPC::ComputeSecurityAssociation](../resources/opc/TF-OPC-ComputeSecurityAssociation/docs/README.md)
* [TF::OPC::ComputeSecurityIpList](../resources/opc/TF-OPC-ComputeSecurityIpList/docs/README.md)
* [TF::OPC::ComputeSecurityList](../resources/opc/TF-OPC-ComputeSecurityList/docs/README.md)
* [TF::OPC::ComputeSecurityProtocol](../resources/opc/TF-OPC-ComputeSecurityProtocol/docs/README.md)
* [TF::OPC::ComputeSecurityRule](../resources/opc/TF-OPC-ComputeSecurityRule/docs/README.md)
* [TF::OPC::ComputeSnapshot](../resources/opc/TF-OPC-ComputeSnapshot/docs/README.md)
* [TF::OPC::ComputeSshKey](../resources/opc/TF-OPC-ComputeSshKey/docs/README.md)
* [TF::OPC::ComputeStorageAttachment](../resources/opc/TF-OPC-ComputeStorageAttachment/docs/README.md)
* [TF::OPC::ComputeStorageVolumeSnapshot](../resources/opc/TF-OPC-ComputeStorageVolumeSnapshot/docs/README.md)
* [TF::OPC::ComputeStorageVolume](../resources/opc/TF-OPC-ComputeStorageVolume/docs/README.md)
* [TF::OPC::ComputeVnicSet](../resources/opc/TF-OPC-ComputeVnicSet/docs/README.md)
* [TF::OPC::ComputeVpnEndpointV2](../resources/opc/TF-OPC-ComputeVpnEndpointV2/docs/README.md)
* [TF::OPC::LbaasCertificate](../resources/opc/TF-OPC-LbaasCertificate/docs/README.md)
* [TF::OPC::LbaasListener](../resources/opc/TF-OPC-LbaasListener/docs/README.md)
* [TF::OPC::LbaasLoadBalancer](../resources/opc/TF-OPC-LbaasLoadBalancer/docs/README.md)
* [TF::OPC::LbaasPolicy](../resources/opc/TF-OPC-LbaasPolicy/docs/README.md)
* [TF::OPC::LbaasServerPool](../resources/opc/TF-OPC-LbaasServerPool/docs/README.md)
* [TF::OPC::StorageContainer](../resources/opc/TF-OPC-StorageContainer/docs/README.md)
* [TF::OPC::StorageObject](../resources/opc/TF-OPC-StorageObject/docs/README.md)