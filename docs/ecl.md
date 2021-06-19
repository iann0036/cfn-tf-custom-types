# NTT Enterprise Cloud 2.0 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ecl**. The below arguments may be included as the key/value or JSON properties in the secret:

* `auth_url` - (Optional; required if `cloud` is not specified) The Identity
  authentication URL.

* `cloud` - (Optional; required if `auth_url` is not specified) An entry in a
  `clouds.yaml` file. See the ECL CLI `os-client-config`
  [documentation](https://ecl.ntt.com/en/documents/tutorials/eclc/rsts/installation.html)
  for more information about `clouds.yaml` files.

* `region` - (Optional) The region of the Enterprise Cloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region Enterprise Cloud environments, but this behavior
  may vary depending on the Enterprise Cloud environment being used.

* `user_name` - (Optional) The Username to login with.

* `user_id` - (Optional) The User ID to login with.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `tenant_name` - (Optional) The Name of the Tenant to login with.
  If omitted, the `OS_TENANT_NAME` or `OS_PROJECT_NAME` environment
  variable are used.

* `password` - (Optional) The Password to login with.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform. If omitted, the `OS_TOKEN` or `OS_AUTH_TOKEN` environment
  variables are used.

* `user_domain_name` - (Optional) The domain name where the user is located.

* `user_domain_id` - (Optional) The domain ID where the user is located.

* `project_domain_name` - (Optional) The domain name where the project is
  located.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3).

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).

* `default_domain` - (Optional) The ID of the Domain to scope to if no other
  domain is specified (Identity v3).

* `insecure` - (Optional) Trust self-signed SSL certificates.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key.

* `endpoint_type` - (Optional) Specify which type of endpoint to use from the
  service catalog. It can be set using the OS_ENDPOINT_TYPE environment
  variable. If not set, public endpoints is used.


## Supported Resources

* [TF::ECL::BaremetalKeypairV2](../resources/ecl/TF-ECL-BaremetalKeypairV2/docs/README.md)
* [TF::ECL::BaremetalServerV2](../resources/ecl/TF-ECL-BaremetalServerV2/docs/README.md)
* [TF::ECL::ComputeInstanceV2](../resources/ecl/TF-ECL-ComputeInstanceV2/docs/README.md)
* [TF::ECL::ComputeKeypairV2](../resources/ecl/TF-ECL-ComputeKeypairV2/docs/README.md)
* [TF::ECL::ComputeVolumeAttachV2](../resources/ecl/TF-ECL-ComputeVolumeAttachV2/docs/README.md)
* [TF::ECL::ComputeVolumeV2](../resources/ecl/TF-ECL-ComputeVolumeV2/docs/README.md)
* [TF::ECL::DedicatedHypervisorLicenseV1](../resources/ecl/TF-ECL-DedicatedHypervisorLicenseV1/docs/README.md)
* [TF::ECL::DedicatedHypervisorServerV1](../resources/ecl/TF-ECL-DedicatedHypervisorServerV1/docs/README.md)
* [TF::ECL::DnsRecordsetV2](../resources/ecl/TF-ECL-DnsRecordsetV2/docs/README.md)
* [TF::ECL::DnsZoneV2](../resources/ecl/TF-ECL-DnsZoneV2/docs/README.md)
* [TF::ECL::ImagestoragesImageV2](../resources/ecl/TF-ECL-ImagestoragesImageV2/docs/README.md)
* [TF::ECL::ImagestoragesMemberAccepterV2](../resources/ecl/TF-ECL-ImagestoragesMemberAccepterV2/docs/README.md)
* [TF::ECL::ImagestoragesMemberV2](../resources/ecl/TF-ECL-ImagestoragesMemberV2/docs/README.md)
* [TF::ECL::NetworkCommonFunctionGatewayV2](../resources/ecl/TF-ECL-NetworkCommonFunctionGatewayV2/docs/README.md)
* [TF::ECL::NetworkGatewayInterfaceV2](../resources/ecl/TF-ECL-NetworkGatewayInterfaceV2/docs/README.md)
* [TF::ECL::NetworkInternetGatewayV2](../resources/ecl/TF-ECL-NetworkInternetGatewayV2/docs/README.md)
* [TF::ECL::NetworkLoadBalancerV2](../resources/ecl/TF-ECL-NetworkLoadBalancerV2/docs/README.md)
* [TF::ECL::NetworkNetworkV2](../resources/ecl/TF-ECL-NetworkNetworkV2/docs/README.md)
* [TF::ECL::NetworkPortV2](../resources/ecl/TF-ECL-NetworkPortV2/docs/README.md)
* [TF::ECL::NetworkPublicIpV2](../resources/ecl/TF-ECL-NetworkPublicIpV2/docs/README.md)
* [TF::ECL::NetworkStaticRouteV2](../resources/ecl/TF-ECL-NetworkStaticRouteV2/docs/README.md)
* [TF::ECL::NetworkSubnetV2](../resources/ecl/TF-ECL-NetworkSubnetV2/docs/README.md)
* [TF::ECL::ProviderConnectivityTenantConnectionRequestV2](../resources/ecl/TF-ECL-ProviderConnectivityTenantConnectionRequestV2/docs/README.md)
* [TF::ECL::ProviderConnectivityTenantConnectionV2](../resources/ecl/TF-ECL-ProviderConnectivityTenantConnectionV2/docs/README.md)
* [TF::ECL::RcaUserV1](../resources/ecl/TF-ECL-RcaUserV1/docs/README.md)
* [TF::ECL::SecurityHostBasedV2](../resources/ecl/TF-ECL-SecurityHostBasedV2/docs/README.md)
* [TF::ECL::SecurityNetworkBasedDeviceHaV2](../resources/ecl/TF-ECL-SecurityNetworkBasedDeviceHaV2/docs/README.md)
* [TF::ECL::SecurityNetworkBasedDeviceSingleV2](../resources/ecl/TF-ECL-SecurityNetworkBasedDeviceSingleV2/docs/README.md)
* [TF::ECL::SecurityNetworkBasedWafSingleV2](../resources/ecl/TF-ECL-SecurityNetworkBasedWafSingleV2/docs/README.md)
* [TF::ECL::SssApprovalRequestV1](../resources/ecl/TF-ECL-SssApprovalRequestV1/docs/README.md)
* [TF::ECL::SssTenantV1](../resources/ecl/TF-ECL-SssTenantV1/docs/README.md)
* [TF::ECL::SssUserV1](../resources/ecl/TF-ECL-SssUserV1/docs/README.md)
* [TF::ECL::StorageVirtualstorageV1](../resources/ecl/TF-ECL-StorageVirtualstorageV1/docs/README.md)
* [TF::ECL::StorageVolumeV1](../resources/ecl/TF-ECL-StorageVolumeV1/docs/README.md)
* [TF::ECL::VnaApplianceV1](../resources/ecl/TF-ECL-VnaApplianceV1/docs/README.md)