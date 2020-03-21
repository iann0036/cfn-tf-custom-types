# OpenTelekomCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opentelekomcloud**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - (Optional) The access key of the OpenTelekomCloud cloud to use.

* `secret_key` - (Optional) The secret key of the OpenTelekomCloud cloud to use.

* `auth_url` - (Optional; required if `cloud` is not specified) The Identity
  authentication URL.

* `cloud` - (Optional; required if `auth_url` is not specified) An entry in a
  `clouds.yaml` file. See the OpenStack `os-client-config`
  [documentation](https://docs.openstack.org/os-client-config/latest/user/configuration.html)
  for more information about `clouds.yaml` files.

* `user_name` - (Optional) The Username to login with.

* `tenant_name` - (Required) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `password` - (Optional) The Password to login with.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform.

* `security_token` - (Optional) Security token to use for OBS federated authentication.

* `domain_name` - (Required) The Name of the Domain to scope to (Identity v3).

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

* `swauth` - (Optional) Set to `true` to authenticate against Swauth, a
  Swift-native authentication system. If omitted, the `OS_SWAUTH` environment
  variable is used. You must also set `username` to the Swauth/Swift username
  such as `username:project`. Set the `password` to the Swauth/Swift key.
  Finally, set `auth_url` as the location of the Swift service. Note that this
  will only work when used with the OpenTelekomCloud Object Storage resources.

* `agency_name` - (Optional) if authorized by assume role, it must be set. The
  name of agency.

* `agency_domain_name` - (Optional) if authorized by assume role, it must be set.
  The name of domain who created the agency (Identity v3).

* `delegated_project` - (Optional) The name of delegated project (Identity v3).


## Supported Resources

* [Terraform::OpenTelekomCloud::AntiddosV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-AntiddosV1/docs/README.md)
* [Terraform::OpenTelekomCloud::AsConfigurationV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-AsConfigurationV1/docs/README.md)
* [Terraform::OpenTelekomCloud::AsGroupV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-AsGroupV1/docs/README.md)
* [Terraform::OpenTelekomCloud::AsPolicyV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-AsPolicyV1/docs/README.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeAttachV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-BlockstorageVolumeAttachV2/docs/README.md)
* [Terraform::OpenTelekomCloud::BlockstorageVolumeV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-BlockstorageVolumeV2/docs/README.md)
* [Terraform::OpenTelekomCloud::CceClusterV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CceClusterV3/docs/README.md)
* [Terraform::OpenTelekomCloud::CceNodeV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CceNodeV3/docs/README.md)
* [Terraform::OpenTelekomCloud::CesAlarmrule](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CesAlarmrule/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeBmsServerV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeBmsServerV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeFloatingipAssociateV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeFloatingipV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeFloatingipV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeInstanceV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeInstanceV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeKeypairV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeKeypairV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeSecgroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeSecgroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeServergroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeServergroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ComputeVolumeAttachV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ComputeVolumeAttachV2/docs/README.md)
* [Terraform::OpenTelekomCloud::CsbsBackupPolicyV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CsbsBackupPolicyV1/docs/README.md)
* [Terraform::OpenTelekomCloud::CsbsBackupV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CsbsBackupV1/docs/README.md)
* [Terraform::OpenTelekomCloud::CssClusterV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CssClusterV1/docs/README.md)
* [Terraform::OpenTelekomCloud::CtsTrackerV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-CtsTrackerV1/docs/README.md)
* [Terraform::OpenTelekomCloud::DcsInstanceV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-DcsInstanceV1/docs/README.md)
* [Terraform::OpenTelekomCloud::DmsGroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-DmsGroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::DmsQueueV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-DmsQueueV2/docs/README.md)
* [Terraform::OpenTelekomCloud::DnsRecordsetV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-DnsRecordsetV2/docs/README.md)
* [Terraform::OpenTelekomCloud::DnsZoneV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-DnsZoneV2/docs/README.md)
* [Terraform::OpenTelekomCloud::EcsInstanceV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-EcsInstanceV1/docs/README.md)
* [Terraform::OpenTelekomCloud::ElbBackend](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ElbBackend/docs/README.md)
* [Terraform::OpenTelekomCloud::ElbHealth](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ElbHealth/docs/README.md)
* [Terraform::OpenTelekomCloud::ElbListener](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ElbListener/docs/README.md)
* [Terraform::OpenTelekomCloud::ElbLoadbalancer](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ElbLoadbalancer/docs/README.md)
* [Terraform::OpenTelekomCloud::EvsVolumeV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-EvsVolumeV3/docs/README.md)
* [Terraform::OpenTelekomCloud::FwFirewallGroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-FwFirewallGroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::FwPolicyV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-FwPolicyV2/docs/README.md)
* [Terraform::OpenTelekomCloud::FwRuleV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-FwRuleV2/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityAgencyV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityAgencyV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityGroupMembershipV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityGroupMembershipV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityGroupV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityGroupV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityProjectV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityProjectV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityRoleAssignmentV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityRoleAssignmentV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityRoleV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityRoleV3/docs/README.md)
* [Terraform::OpenTelekomCloud::IdentityUserV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-IdentityUserV3/docs/README.md)
* [Terraform::OpenTelekomCloud::ImagesImageV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ImagesImageV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ImsDataImageV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ImsDataImageV2/docs/README.md)
* [Terraform::OpenTelekomCloud::ImsImageV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-ImsImageV2/docs/README.md)
* [Terraform::OpenTelekomCloud::KmsKeyV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-KmsKeyV1/docs/README.md)
* [Terraform::OpenTelekomCloud::LbCertificateV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbCertificateV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbL7policyV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbL7policyV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbL7ruleV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbL7ruleV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbListenerV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbListenerV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbLoadbalancerV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbLoadbalancerV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbMemberV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbMemberV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbMonitorV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbMonitorV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbPoolV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbPoolV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LbWhitelistV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LbWhitelistV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LogtankGroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LogtankGroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::LogtankTopicV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-LogtankTopicV2/docs/README.md)
* [Terraform::OpenTelekomCloud::MaasTaskV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-MaasTaskV1/docs/README.md)
* [Terraform::OpenTelekomCloud::MrsClusterV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-MrsClusterV1/docs/README.md)
* [Terraform::OpenTelekomCloud::MrsJobV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-MrsJobV1/docs/README.md)
* [Terraform::OpenTelekomCloud::NatDnatRuleV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NatDnatRuleV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NatGatewayV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NatGatewayV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NatSnatRuleV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NatSnatRuleV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingFloatingipAssociateV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingFloatingipV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingFloatingipV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingNetworkV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingNetworkV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingPortV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingPortV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterInterfaceV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingRouterInterfaceV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterRouteV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingRouterRouteV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingRouterV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingRouterV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupRuleV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingSecgroupRuleV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingSecgroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingSecgroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingSubnetV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingSubnetV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingVipAssociateV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingVipAssociateV2/docs/README.md)
* [Terraform::OpenTelekomCloud::NetworkingVipV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-NetworkingVipV2/docs/README.md)
* [Terraform::OpenTelekomCloud::RdsInstanceV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RdsInstanceV1/docs/README.md)
* [Terraform::OpenTelekomCloud::RdsInstanceV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RdsInstanceV3/docs/README.md)
* [Terraform::OpenTelekomCloud::RdsParametergroupV3](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RdsParametergroupV3/docs/README.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareConfigV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RtsSoftwareConfigV1/docs/README.md)
* [Terraform::OpenTelekomCloud::RtsSoftwareDeploymentV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RtsSoftwareDeploymentV1/docs/README.md)
* [Terraform::OpenTelekomCloud::RtsStackV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-RtsStackV1/docs/README.md)
* [Terraform::OpenTelekomCloud::S3BucketObject](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-S3BucketObject/docs/README.md)
* [Terraform::OpenTelekomCloud::S3BucketPolicy](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-S3BucketPolicy/docs/README.md)
* [Terraform::OpenTelekomCloud::S3Bucket](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-S3Bucket/docs/README.md)
* [Terraform::OpenTelekomCloud::SdrsProtectiongroupV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-SdrsProtectiongroupV1/docs/README.md)
* [Terraform::OpenTelekomCloud::SfsFileSystemV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-SfsFileSystemV2/docs/README.md)
* [Terraform::OpenTelekomCloud::SmnSubscriptionV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-SmnSubscriptionV2/docs/README.md)
* [Terraform::OpenTelekomCloud::SmnTopicV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-SmnTopicV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VbsBackupPolicyV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VbsBackupPolicyV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VbsBackupShareV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VbsBackupShareV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VbsBackupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VbsBackupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcEipV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcEipV1/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcFlow logV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcFlow logV1/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionAccepterV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcPeeringConnectionAccepterV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcPeeringConnectionV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcPeeringConnectionV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcRouteV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcRouteV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcSubnetV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcSubnetV1/docs/README.md)
* [Terraform::OpenTelekomCloud::VpcV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpcV1/docs/README.md)
* [Terraform::OpenTelekomCloud::VpnaasEndpointGroupV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpnaasEndpointGroupV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpnaasIkePolicyV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpnaasIkePolicyV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpnaasIpsecPolicyV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpnaasIpsecPolicyV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpnaasServiceV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpnaasServiceV2/docs/README.md)
* [Terraform::OpenTelekomCloud::VpnaasSiteConnectionV2](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-VpnaasSiteConnectionV2/docs/README.md)
* [Terraform::OpenTelekomCloud::WafCcattackprotectionRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafCcattackprotectionRuleV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafCertificateV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafCertificateV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafDatamaskingRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafDatamaskingRuleV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafDomainV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafDomainV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafFalsealarmmaskingRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafFalsealarmmaskingRuleV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafPolicyV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafPolicyV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafPreciseprotectionRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafPreciseprotectionRuleV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafWebtamperprotectionRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafWebtamperprotectionRuleV1/docs/README.md)
* [Terraform::OpenTelekomCloud::WafWhiteblackipRuleV1](../resources/opentelekomcloud/Terraform-OpenTelekomCloud-WafWhiteblackipRuleV1/docs/README.md)