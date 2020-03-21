# Oracle Public Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/opc**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Optional) The username to use, generally your email address.

* `password` - (Optional) The password associated with the username to use.

* `identity_domain` - (Optional) The Identity Domain name (for Traditional accounts) or Identity Service ID (for IDCS accounts) of the environment to use.  

* `endpoint` - (Optional) The Compute Classic API endpoint to use, associated with your Oracle Cloud Account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_endpoint` - (Optional) The Storage Classic API endpoint to use, associated with your Oracle Storage Cloud account. This is known as the `REST Endpoint` within the Oracle portal.

* `storage_service_id` - (Optional) The Storage Service ID for authentication with the `storage_endpoint`  If not set the `identity_domain` value is used.

* `max_retries` - (Optional) The maximum number of tries to make for a successful response when operating on resources. Defaults to 1.

* `insecure` - (Optional) Skips TLS Verification for using self-signed certificates. Should only be used if absolutely needed.


## Supported Resources

* [Terraform::OPC::ComputeAcl](../resources/opc/Terraform-OPC-ComputeAcl/docs/README.md)
* [Terraform::OPC::ComputeImageListEntry](../resources/opc/Terraform-OPC-ComputeImageListEntry/docs/README.md)
* [Terraform::OPC::ComputeImageList](../resources/opc/Terraform-OPC-ComputeImageList/docs/README.md)
* [Terraform::OPC::ComputeInstance](../resources/opc/Terraform-OPC-ComputeInstance/docs/README.md)
* [Terraform::OPC::ComputeIpAddressAssociation](../resources/opc/Terraform-OPC-ComputeIpAddressAssociation/docs/README.md)
* [Terraform::OPC::ComputeIpAddressPrefixSet](../resources/opc/Terraform-OPC-ComputeIpAddressPrefixSet/docs/README.md)
* [Terraform::OPC::ComputeIpAddressReservation](../resources/opc/Terraform-OPC-ComputeIpAddressReservation/docs/README.md)
* [Terraform::OPC::ComputeIpAssociation](../resources/opc/Terraform-OPC-ComputeIpAssociation/docs/README.md)
* [Terraform::OPC::ComputeIpNetworkExchange](../resources/opc/Terraform-OPC-ComputeIpNetworkExchange/docs/README.md)
* [Terraform::OPC::ComputeIpNetwork](../resources/opc/Terraform-OPC-ComputeIpNetwork/docs/README.md)
* [Terraform::OPC::ComputeIpReservation](../resources/opc/Terraform-OPC-ComputeIpReservation/docs/README.md)
* [Terraform::OPC::ComputeMachineImage](../resources/opc/Terraform-OPC-ComputeMachineImage/docs/README.md)
* [Terraform::OPC::ComputeOrchestratedInstance](../resources/opc/Terraform-OPC-ComputeOrchestratedInstance/docs/README.md)
* [Terraform::OPC::ComputeRoute](../resources/opc/Terraform-OPC-ComputeRoute/docs/README.md)
* [Terraform::OPC::ComputeSecRule](../resources/opc/Terraform-OPC-ComputeSecRule/docs/README.md)
* [Terraform::OPC::ComputeSecurityApplication](../resources/opc/Terraform-OPC-ComputeSecurityApplication/docs/README.md)
* [Terraform::OPC::ComputeSecurityAssociation](../resources/opc/Terraform-OPC-ComputeSecurityAssociation/docs/README.md)
* [Terraform::OPC::ComputeSecurityIpList](../resources/opc/Terraform-OPC-ComputeSecurityIpList/docs/README.md)
* [Terraform::OPC::ComputeSecurityList](../resources/opc/Terraform-OPC-ComputeSecurityList/docs/README.md)
* [Terraform::OPC::ComputeSecurityProtocol](../resources/opc/Terraform-OPC-ComputeSecurityProtocol/docs/README.md)
* [Terraform::OPC::ComputeSecurityRule](../resources/opc/Terraform-OPC-ComputeSecurityRule/docs/README.md)
* [Terraform::OPC::ComputeSnapshot](../resources/opc/Terraform-OPC-ComputeSnapshot/docs/README.md)
* [Terraform::OPC::ComputeSshKey](../resources/opc/Terraform-OPC-ComputeSshKey/docs/README.md)
* [Terraform::OPC::ComputeStorageAttachment](../resources/opc/Terraform-OPC-ComputeStorageAttachment/docs/README.md)
* [Terraform::OPC::ComputeStorageVolumeSnapshot](../resources/opc/Terraform-OPC-ComputeStorageVolumeSnapshot/docs/README.md)
* [Terraform::OPC::ComputeStorageVolume](../resources/opc/Terraform-OPC-ComputeStorageVolume/docs/README.md)
* [Terraform::OPC::ComputeVnicSet](../resources/opc/Terraform-OPC-ComputeVnicSet/docs/README.md)
* [Terraform::OPC::ComputeVpnEndpointV2](../resources/opc/Terraform-OPC-ComputeVpnEndpointV2/docs/README.md)
* [Terraform::OPC::LbaasCertificate](../resources/opc/Terraform-OPC-LbaasCertificate/docs/README.md)
* [Terraform::OPC::LbaasListener](../resources/opc/Terraform-OPC-LbaasListener/docs/README.md)
* [Terraform::OPC::LbaasLoadBalancer](../resources/opc/Terraform-OPC-LbaasLoadBalancer/docs/README.md)
* [Terraform::OPC::LbaasPolicy](../resources/opc/Terraform-OPC-LbaasPolicy/docs/README.md)
* [Terraform::OPC::LbaasServerPool](../resources/opc/Terraform-OPC-LbaasServerPool/docs/README.md)
* [Terraform::OPC::StorageContainer](../resources/opc/Terraform-OPC-StorageContainer/docs/README.md)
* [Terraform::OPC::StorageObject](../resources/opc/Terraform-OPC-StorageObject/docs/README.md)