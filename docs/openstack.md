# OpenStack Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/openstack**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `auth_url` - (Optional; required if `cloud` is not specified) The Identity
  authentication URL.

* `cloud` - (Optional; required if `auth_url` is not specified) An entry in a
  `clouds.yaml` file. See the OpenStack `openstacksdk`
  [documentation](https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html)
  for more information about `clouds.yaml` files.

* `region` - (Optional) The region of the OpenStack cloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region OpenStack environments, but this behavior may vary
  depending on the OpenStack environment being used.

* `user_name` - (Optional) The Username to login with.

* `user_id` - (Optional) The User ID to login with.

* `application_credential_id` - (Optional) (Identity v3 only) The ID of an
    application credential to authenticate with. An
    `application_credential_secret` has to bet set along with this parameter.

* `application_credential_name` - (Optional) (Identity v3 only) The name of an
    application credential to authenticate with. Conflicts with the
    `application_credential_name`, requires `user_id`, or `user_name` and
    `user_domain_name` (or `user_domain_id`) to be set.

* `application_credential_secret` - (Optional) (Identity v3 only) The secret of an
    application credential to authenticate with. Required by
    `application_credential_id` or `application_credential_name`.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

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

* `endpoint_overrides` - (Optional) A set of key/value pairs that can
  override an endpoint for a specified OpenStack service. Setting an override
  requires you to specify the full and complete endpoint URL. This might
  also invalidate any region you have set, too. Please see below for more details.
  Please use this at your own risk.

* `swauth` - (Optional) Set to `true` to authenticate against Swauth, a
  Swift-native authentication system. If omitted, the `OS_SWAUTH` environment
  variable is used. You must also set `username` to the Swauth/Swift username
  such as `username:project`. Set the `password` to the Swauth/Swift key.
  Finally, set `auth_url` as the location of the Swift service. Note that this
  will only work when used with the OpenStack Object Storage resources.

* `use_octavia` - (Optional) If set to `true`, API requests will go the Load Balancer
  service (Octavia) instead of the Networking service (Neutron).

* `disable_no_cache_header` - (Optional) If set to `true`, the HTTP
  `Cache-Control: no-cache` header will not be added by default to all API requests.
  If omitted this header is added to all API requests to force HTTP caches (if any)
  to go upstream instead of serving cached responses.

* `delayed_auth` - (Optional) If set to `true`, OpenStack authorization will be perfomed,
  when the service provider client is called.

* `allow_reauth` - (Optional) If set to `true`, OpenStack authorization will be
  perfomed automatically, if the initial auth token get expired. This is useful,
  when the token TTL is low or the overall Terraform provider execution time
  expected to be greater than the initial token TTL.


## Supported Resources

* [Terraform::OpenStack::BlockstorageQuotasetV2](../resources/openstack/Terraform-OpenStack-BlockstorageQuotasetV2/docs/README.md)
* [Terraform::OpenStack::BlockstorageQuotasetV3](../resources/openstack/Terraform-OpenStack-BlockstorageQuotasetV3/docs/README.md)
* [Terraform::OpenStack::BlockstorageVolumeAttachV2](../resources/openstack/Terraform-OpenStack-BlockstorageVolumeAttachV2/docs/README.md)
* [Terraform::OpenStack::BlockstorageVolumeAttachV3](../resources/openstack/Terraform-OpenStack-BlockstorageVolumeAttachV3/docs/README.md)
* [Terraform::OpenStack::BlockstorageVolumeV1](../resources/openstack/Terraform-OpenStack-BlockstorageVolumeV1/docs/README.md)
* [Terraform::OpenStack::BlockstorageVolumeV2](../resources/openstack/Terraform-OpenStack-BlockstorageVolumeV2/docs/README.md)
* [Terraform::OpenStack::BlockstorageVolumeV3](../resources/openstack/Terraform-OpenStack-BlockstorageVolumeV3/docs/README.md)
* [Terraform::OpenStack::ComputeFlavorAccessV2](../resources/openstack/Terraform-OpenStack-ComputeFlavorAccessV2/docs/README.md)
* [Terraform::OpenStack::ComputeFlavorV2](../resources/openstack/Terraform-OpenStack-ComputeFlavorV2/docs/README.md)
* [Terraform::OpenStack::ComputeFloatingipAssociateV2](../resources/openstack/Terraform-OpenStack-ComputeFloatingipAssociateV2/docs/README.md)
* [Terraform::OpenStack::ComputeFloatingipV2](../resources/openstack/Terraform-OpenStack-ComputeFloatingipV2/docs/README.md)
* [Terraform::OpenStack::ComputeInstanceV2](../resources/openstack/Terraform-OpenStack-ComputeInstanceV2/docs/README.md)
* [Terraform::OpenStack::ComputeInterfaceAttachV2](../resources/openstack/Terraform-OpenStack-ComputeInterfaceAttachV2/docs/README.md)
* [Terraform::OpenStack::ComputeKeypairV2](../resources/openstack/Terraform-OpenStack-ComputeKeypairV2/docs/README.md)
* [Terraform::OpenStack::ComputeQuotasetV2](../resources/openstack/Terraform-OpenStack-ComputeQuotasetV2/docs/README.md)
* [Terraform::OpenStack::ComputeSecgroupV2](../resources/openstack/Terraform-OpenStack-ComputeSecgroupV2/docs/README.md)
* [Terraform::OpenStack::ComputeServergroupV2](../resources/openstack/Terraform-OpenStack-ComputeServergroupV2/docs/README.md)
* [Terraform::OpenStack::ComputeVolumeAttachV2](../resources/openstack/Terraform-OpenStack-ComputeVolumeAttachV2/docs/README.md)
* [Terraform::OpenStack::ContainerinfraClusterV1](../resources/openstack/Terraform-OpenStack-ContainerinfraClusterV1/docs/README.md)
* [Terraform::OpenStack::ContainerinfraClustertemplateV1](../resources/openstack/Terraform-OpenStack-ContainerinfraClustertemplateV1/docs/README.md)
* [Terraform::OpenStack::DbConfigurationV1](../resources/openstack/Terraform-OpenStack-DbConfigurationV1/docs/README.md)
* [Terraform::OpenStack::DbDatabaseV1](../resources/openstack/Terraform-OpenStack-DbDatabaseV1/docs/README.md)
* [Terraform::OpenStack::DbInstanceV1](../resources/openstack/Terraform-OpenStack-DbInstanceV1/docs/README.md)
* [Terraform::OpenStack::DbUserV1](../resources/openstack/Terraform-OpenStack-DbUserV1/docs/README.md)
* [Terraform::OpenStack::DnsRecordsetV2](../resources/openstack/Terraform-OpenStack-DnsRecordsetV2/docs/README.md)
* [Terraform::OpenStack::DnsZoneV2](../resources/openstack/Terraform-OpenStack-DnsZoneV2/docs/README.md)
* [Terraform::OpenStack::FwFirewallV1](../resources/openstack/Terraform-OpenStack-FwFirewallV1/docs/README.md)
* [Terraform::OpenStack::FwPolicyV1](../resources/openstack/Terraform-OpenStack-FwPolicyV1/docs/README.md)
* [Terraform::OpenStack::FwRuleV1](../resources/openstack/Terraform-OpenStack-FwRuleV1/docs/README.md)
* [Terraform::OpenStack::IdentityApplicationCredentialV3](../resources/openstack/Terraform-OpenStack-IdentityApplicationCredentialV3/docs/README.md)
* [Terraform::OpenStack::IdentityEndpointV3](../resources/openstack/Terraform-OpenStack-IdentityEndpointV3/docs/README.md)
* [Terraform::OpenStack::IdentityProjectV3](../resources/openstack/Terraform-OpenStack-IdentityProjectV3/docs/README.md)
* [Terraform::OpenStack::IdentityRoleAssignmentV3](../resources/openstack/Terraform-OpenStack-IdentityRoleAssignmentV3/docs/README.md)
* [Terraform::OpenStack::IdentityRoleV3](../resources/openstack/Terraform-OpenStack-IdentityRoleV3/docs/README.md)
* [Terraform::OpenStack::IdentityServiceV3](../resources/openstack/Terraform-OpenStack-IdentityServiceV3/docs/README.md)
* [Terraform::OpenStack::IdentityUserV3](../resources/openstack/Terraform-OpenStack-IdentityUserV3/docs/README.md)
* [Terraform::OpenStack::ImagesImageAccessAcceptV2](../resources/openstack/Terraform-OpenStack-ImagesImageAccessAcceptV2/docs/README.md)
* [Terraform::OpenStack::ImagesImageAccessV2](../resources/openstack/Terraform-OpenStack-ImagesImageAccessV2/docs/README.md)
* [Terraform::OpenStack::ImagesImageV2](../resources/openstack/Terraform-OpenStack-ImagesImageV2/docs/README.md)
* [Terraform::OpenStack::KeymanagerContainerV1](../resources/openstack/Terraform-OpenStack-KeymanagerContainerV1/docs/README.md)
* [Terraform::OpenStack::KeymanagerSecretV1](../resources/openstack/Terraform-OpenStack-KeymanagerSecretV1/docs/README.md)
* [Terraform::OpenStack::LbL7policyV2](../resources/openstack/Terraform-OpenStack-LbL7policyV2/docs/README.md)
* [Terraform::OpenStack::LbL7ruleV2](../resources/openstack/Terraform-OpenStack-LbL7ruleV2/docs/README.md)
* [Terraform::OpenStack::LbListenerV2](../resources/openstack/Terraform-OpenStack-LbListenerV2/docs/README.md)
* [Terraform::OpenStack::LbLoadbalancerV2](../resources/openstack/Terraform-OpenStack-LbLoadbalancerV2/docs/README.md)
* [Terraform::OpenStack::LbMemberV1](../resources/openstack/Terraform-OpenStack-LbMemberV1/docs/README.md)
* [Terraform::OpenStack::LbMemberV2](../resources/openstack/Terraform-OpenStack-LbMemberV2/docs/README.md)
* [Terraform::OpenStack::LbMonitorV1](../resources/openstack/Terraform-OpenStack-LbMonitorV1/docs/README.md)
* [Terraform::OpenStack::LbMonitorV2](../resources/openstack/Terraform-OpenStack-LbMonitorV2/docs/README.md)
* [Terraform::OpenStack::LbPoolV1](../resources/openstack/Terraform-OpenStack-LbPoolV1/docs/README.md)
* [Terraform::OpenStack::LbPoolV2](../resources/openstack/Terraform-OpenStack-LbPoolV2/docs/README.md)
* [Terraform::OpenStack::LbVipV1](../resources/openstack/Terraform-OpenStack-LbVipV1/docs/README.md)
* [Terraform::OpenStack::NetworkingAddressscopeV2](../resources/openstack/Terraform-OpenStack-NetworkingAddressscopeV2/docs/README.md)
* [Terraform::OpenStack::NetworkingFloatingipAssociateV2](../resources/openstack/Terraform-OpenStack-NetworkingFloatingipAssociateV2/docs/README.md)
* [Terraform::OpenStack::NetworkingFloatingipV2](../resources/openstack/Terraform-OpenStack-NetworkingFloatingipV2/docs/README.md)
* [Terraform::OpenStack::NetworkingNetworkV2](../resources/openstack/Terraform-OpenStack-NetworkingNetworkV2/docs/README.md)
* [Terraform::OpenStack::NetworkingPortSecgroupAssociateV2](../resources/openstack/Terraform-OpenStack-NetworkingPortSecgroupAssociateV2/docs/README.md)
* [Terraform::OpenStack::NetworkingPortV2](../resources/openstack/Terraform-OpenStack-NetworkingPortV2/docs/README.md)
* [Terraform::OpenStack::NetworkingQosBandwidthLimitRuleV2](../resources/openstack/Terraform-OpenStack-NetworkingQosBandwidthLimitRuleV2/docs/README.md)
* [Terraform::OpenStack::NetworkingQosDscpMarkingRuleV2](../resources/openstack/Terraform-OpenStack-NetworkingQosDscpMarkingRuleV2/docs/README.md)
* [Terraform::OpenStack::NetworkingQosMinimumBandwidthRuleV2](../resources/openstack/Terraform-OpenStack-NetworkingQosMinimumBandwidthRuleV2/docs/README.md)
* [Terraform::OpenStack::NetworkingQosPolicyV2](../resources/openstack/Terraform-OpenStack-NetworkingQosPolicyV2/docs/README.md)
* [Terraform::OpenStack::NetworkingQuotaV2](../resources/openstack/Terraform-OpenStack-NetworkingQuotaV2/docs/README.md)
* [Terraform::OpenStack::NetworkingRbacPolicyV2](../resources/openstack/Terraform-OpenStack-NetworkingRbacPolicyV2/docs/README.md)
* [Terraform::OpenStack::NetworkingRouterInterfaceV2](../resources/openstack/Terraform-OpenStack-NetworkingRouterInterfaceV2/docs/README.md)
* [Terraform::OpenStack::NetworkingRouterRouteV2](../resources/openstack/Terraform-OpenStack-NetworkingRouterRouteV2/docs/README.md)
* [Terraform::OpenStack::NetworkingRouterV2](../resources/openstack/Terraform-OpenStack-NetworkingRouterV2/docs/README.md)
* [Terraform::OpenStack::NetworkingSecgroupRuleV2](../resources/openstack/Terraform-OpenStack-NetworkingSecgroupRuleV2/docs/README.md)
* [Terraform::OpenStack::NetworkingSecgroupV2](../resources/openstack/Terraform-OpenStack-NetworkingSecgroupV2/docs/README.md)
* [Terraform::OpenStack::NetworkingSubnetRouteV2](../resources/openstack/Terraform-OpenStack-NetworkingSubnetRouteV2/docs/README.md)
* [Terraform::OpenStack::NetworkingSubnetV2](../resources/openstack/Terraform-OpenStack-NetworkingSubnetV2/docs/README.md)
* [Terraform::OpenStack::NetworkingSubnetpoolV2](../resources/openstack/Terraform-OpenStack-NetworkingSubnetpoolV2/docs/README.md)
* [Terraform::OpenStack::NetworkingTrunkV2](../resources/openstack/Terraform-OpenStack-NetworkingTrunkV2/docs/README.md)
* [Terraform::OpenStack::ObjectstorageContainerV1](../resources/openstack/Terraform-OpenStack-ObjectstorageContainerV1/docs/README.md)
* [Terraform::OpenStack::ObjectstorageObjectV1](../resources/openstack/Terraform-OpenStack-ObjectstorageObjectV1/docs/README.md)
* [Terraform::OpenStack::ObjectstorageTempurlV1](../resources/openstack/Terraform-OpenStack-ObjectstorageTempurlV1/docs/README.md)
* [Terraform::OpenStack::OrchestrationStackV1](../resources/openstack/Terraform-OpenStack-OrchestrationStackV1/docs/README.md)
* [Terraform::OpenStack::SharedfilesystemSecurityserviceV2](../resources/openstack/Terraform-OpenStack-SharedfilesystemSecurityserviceV2/docs/README.md)
* [Terraform::OpenStack::SharedfilesystemShareAccessV2](../resources/openstack/Terraform-OpenStack-SharedfilesystemShareAccessV2/docs/README.md)
* [Terraform::OpenStack::SharedfilesystemShareV2](../resources/openstack/Terraform-OpenStack-SharedfilesystemShareV2/docs/README.md)
* [Terraform::OpenStack::SharedfilesystemSharenetworkV2](../resources/openstack/Terraform-OpenStack-SharedfilesystemSharenetworkV2/docs/README.md)
* [Terraform::OpenStack::VpnaasEndpointGroupV2](../resources/openstack/Terraform-OpenStack-VpnaasEndpointGroupV2/docs/README.md)
* [Terraform::OpenStack::VpnaasIkePolicyV2](../resources/openstack/Terraform-OpenStack-VpnaasIkePolicyV2/docs/README.md)
* [Terraform::OpenStack::VpnaasIpsecPolicyV2](../resources/openstack/Terraform-OpenStack-VpnaasIpsecPolicyV2/docs/README.md)
* [Terraform::OpenStack::VpnaasServiceV2](../resources/openstack/Terraform-OpenStack-VpnaasServiceV2/docs/README.md)
* [Terraform::OpenStack::VpnaasSiteConnectionV2](../resources/openstack/Terraform-OpenStack-VpnaasSiteConnectionV2/docs/README.md)