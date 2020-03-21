# HuaweiCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/huaweicloud**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - (Optional) The access key of the HuaweiCloud to use.

* `secret_key` - (Optional) The secret key of the HuaweiCloud to use.

* `auth_url` - (Required) The Identity authentication URL. To find the auth_url, you can
  refer to [Regions and Endpoints](https://developer.huaweicloud.com/en-us/endpoint)

* `region` - (Optional) The region of the HuaweiCloud to use. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region HuaweiCloud environments, but this behavior may vary
  depending on the HuaweiCloud environment being used.

* `user_name` - (Optional) The Username to login with.

* `user_id` - (Optional) The User ID to login with.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with.

* `password` - (Optional) The Password to login with.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3).

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).

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
  will only work when used with the HuaweiCloud Object Storage resources.

* `use_octavia` - (Optional) If set to `true`, API requests will go the Load Balancer
  service (Octavia) instead of the Networking service (Neutron).

* `agency_name` - (Optional) if authorized by assume role, it must be set. The
  name of agency.

* `agency_domain_name` - (Optional) if authorized by assume role, it must be set.
  The name of domain who created the agency (Identity v3).

* `delegated_project` - (Optional) The name of delegated project (Identity v3).


## Supported Resources

* [Terraform::HuaweiCloud::ApiGatewayApi](../resources/huaweicloud/Terraform-HuaweiCloud-ApiGatewayApi/docs/README.md)
* [Terraform::HuaweiCloud::ApiGatewayGroup](../resources/huaweicloud/Terraform-HuaweiCloud-ApiGatewayGroup/docs/README.md)
* [Terraform::HuaweiCloud::AsConfigurationV1](../resources/huaweicloud/Terraform-HuaweiCloud-AsConfigurationV1/docs/README.md)
* [Terraform::HuaweiCloud::AsGroupV1](../resources/huaweicloud/Terraform-HuaweiCloud-AsGroupV1/docs/README.md)
* [Terraform::HuaweiCloud::AsPolicyV1](../resources/huaweicloud/Terraform-HuaweiCloud-AsPolicyV1/docs/README.md)
* [Terraform::HuaweiCloud::BlockstorageVolumeV2](../resources/huaweicloud/Terraform-HuaweiCloud-BlockstorageVolumeV2/docs/README.md)
* [Terraform::HuaweiCloud::CceClusterV3](../resources/huaweicloud/Terraform-HuaweiCloud-CceClusterV3/docs/README.md)
* [Terraform::HuaweiCloud::CceNodesV3](../resources/huaweicloud/Terraform-HuaweiCloud-CceNodesV3/docs/README.md)
* [Terraform::HuaweiCloud::CdmClusterV1](../resources/huaweicloud/Terraform-HuaweiCloud-CdmClusterV1/docs/README.md)
* [Terraform::HuaweiCloud::CdnDomainV1](../resources/huaweicloud/Terraform-HuaweiCloud-CdnDomainV1/docs/README.md)
* [Terraform::HuaweiCloud::CesAlarmrule](../resources/huaweicloud/Terraform-HuaweiCloud-CesAlarmrule/docs/README.md)
* [Terraform::HuaweiCloud::CloudtableClusterV2](../resources/huaweicloud/Terraform-HuaweiCloud-CloudtableClusterV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeFloatingipAssociateV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeFloatingipAssociateV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeFloatingipV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeFloatingipV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeInstanceV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeInstanceV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeInterfaceAttachV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeInterfaceAttachV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeKeypairV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeKeypairV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeSecgroupV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeSecgroupV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeServergroupV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeServergroupV2/docs/README.md)
* [Terraform::HuaweiCloud::ComputeVolumeAttachV2](../resources/huaweicloud/Terraform-HuaweiCloud-ComputeVolumeAttachV2/docs/README.md)
* [Terraform::HuaweiCloud::CsClusterV1](../resources/huaweicloud/Terraform-HuaweiCloud-CsClusterV1/docs/README.md)
* [Terraform::HuaweiCloud::CsPeeringConnectV1](../resources/huaweicloud/Terraform-HuaweiCloud-CsPeeringConnectV1/docs/README.md)
* [Terraform::HuaweiCloud::CsRouteV1](../resources/huaweicloud/Terraform-HuaweiCloud-CsRouteV1/docs/README.md)
* [Terraform::HuaweiCloud::CsbsBackupPolicyV1](../resources/huaweicloud/Terraform-HuaweiCloud-CsbsBackupPolicyV1/docs/README.md)
* [Terraform::HuaweiCloud::CsbsBackupV1](../resources/huaweicloud/Terraform-HuaweiCloud-CsbsBackupV1/docs/README.md)
* [Terraform::HuaweiCloud::CssClusterV1](../resources/huaweicloud/Terraform-HuaweiCloud-CssClusterV1/docs/README.md)
* [Terraform::HuaweiCloud::CtsTrackerV1](../resources/huaweicloud/Terraform-HuaweiCloud-CtsTrackerV1/docs/README.md)
* [Terraform::HuaweiCloud::DcsInstanceV1](../resources/huaweicloud/Terraform-HuaweiCloud-DcsInstanceV1/docs/README.md)
* [Terraform::HuaweiCloud::DisStreamV2](../resources/huaweicloud/Terraform-HuaweiCloud-DisStreamV2/docs/README.md)
* [Terraform::HuaweiCloud::DliQueueV1](../resources/huaweicloud/Terraform-HuaweiCloud-DliQueueV1/docs/README.md)
* [Terraform::HuaweiCloud::DmsGroupV1](../resources/huaweicloud/Terraform-HuaweiCloud-DmsGroupV1/docs/README.md)
* [Terraform::HuaweiCloud::DmsInstanceV1](../resources/huaweicloud/Terraform-HuaweiCloud-DmsInstanceV1/docs/README.md)
* [Terraform::HuaweiCloud::DmsQueueV1](../resources/huaweicloud/Terraform-HuaweiCloud-DmsQueueV1/docs/README.md)
* [Terraform::HuaweiCloud::DnsPtrrecordV2](../resources/huaweicloud/Terraform-HuaweiCloud-DnsPtrrecordV2/docs/README.md)
* [Terraform::HuaweiCloud::DnsRecordsetV2](../resources/huaweicloud/Terraform-HuaweiCloud-DnsRecordsetV2/docs/README.md)
* [Terraform::HuaweiCloud::DnsZoneV2](../resources/huaweicloud/Terraform-HuaweiCloud-DnsZoneV2/docs/README.md)
* [Terraform::HuaweiCloud::DwsCluster](../resources/huaweicloud/Terraform-HuaweiCloud-DwsCluster/docs/README.md)
* [Terraform::HuaweiCloud::EcsInstanceV1](../resources/huaweicloud/Terraform-HuaweiCloud-EcsInstanceV1/docs/README.md)
* [Terraform::HuaweiCloud::ElbBackendecs](../resources/huaweicloud/Terraform-HuaweiCloud-ElbBackendecs/docs/README.md)
* [Terraform::HuaweiCloud::ElbHealthcheck](../resources/huaweicloud/Terraform-HuaweiCloud-ElbHealthcheck/docs/README.md)
* [Terraform::HuaweiCloud::ElbListener](../resources/huaweicloud/Terraform-HuaweiCloud-ElbListener/docs/README.md)
* [Terraform::HuaweiCloud::ElbLoadbalancer](../resources/huaweicloud/Terraform-HuaweiCloud-ElbLoadbalancer/docs/README.md)
* [Terraform::HuaweiCloud::FgsFunctionV2](../resources/huaweicloud/Terraform-HuaweiCloud-FgsFunctionV2/docs/README.md)
* [Terraform::HuaweiCloud::FwFirewallGroupV2](../resources/huaweicloud/Terraform-HuaweiCloud-FwFirewallGroupV2/docs/README.md)
* [Terraform::HuaweiCloud::FwPolicyV2](../resources/huaweicloud/Terraform-HuaweiCloud-FwPolicyV2/docs/README.md)
* [Terraform::HuaweiCloud::FwRuleV2](../resources/huaweicloud/Terraform-HuaweiCloud-FwRuleV2/docs/README.md)
* [Terraform::HuaweiCloud::GesGraphV1](../resources/huaweicloud/Terraform-HuaweiCloud-GesGraphV1/docs/README.md)
* [Terraform::HuaweiCloud::IamAgencyV3](../resources/huaweicloud/Terraform-HuaweiCloud-IamAgencyV3/docs/README.md)
* [Terraform::HuaweiCloud::IdentityGroupMembershipV3](../resources/huaweicloud/Terraform-HuaweiCloud-IdentityGroupMembershipV3/docs/README.md)
* [Terraform::HuaweiCloud::IdentityGroupV3](../resources/huaweicloud/Terraform-HuaweiCloud-IdentityGroupV3/docs/README.md)
* [Terraform::HuaweiCloud::IdentityProjectV3](../resources/huaweicloud/Terraform-HuaweiCloud-IdentityProjectV3/docs/README.md)
* [Terraform::HuaweiCloud::IdentityRoleAssignmentV3](../resources/huaweicloud/Terraform-HuaweiCloud-IdentityRoleAssignmentV3/docs/README.md)
* [Terraform::HuaweiCloud::IdentityUserV3](../resources/huaweicloud/Terraform-HuaweiCloud-IdentityUserV3/docs/README.md)
* [Terraform::HuaweiCloud::ImagesImageV2](../resources/huaweicloud/Terraform-HuaweiCloud-ImagesImageV2/docs/README.md)
* [Terraform::HuaweiCloud::KmsKeyV1](../resources/huaweicloud/Terraform-HuaweiCloud-KmsKeyV1/docs/README.md)
* [Terraform::HuaweiCloud::LbCertificateV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbCertificateV2/docs/README.md)
* [Terraform::HuaweiCloud::LbL7policyV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbL7policyV2/docs/README.md)
* [Terraform::HuaweiCloud::LbL7ruleV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbL7ruleV2/docs/README.md)
* [Terraform::HuaweiCloud::LbListenerV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbListenerV2/docs/README.md)
* [Terraform::HuaweiCloud::LbLoadbalancerV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbLoadbalancerV2/docs/README.md)
* [Terraform::HuaweiCloud::LbMemberV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbMemberV2/docs/README.md)
* [Terraform::HuaweiCloud::LbMonitorV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbMonitorV2/docs/README.md)
* [Terraform::HuaweiCloud::LbPoolV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbPoolV2/docs/README.md)
* [Terraform::HuaweiCloud::LbWhitelistV2](../resources/huaweicloud/Terraform-HuaweiCloud-LbWhitelistV2/docs/README.md)
* [Terraform::HuaweiCloud::MaasTaskV1](../resources/huaweicloud/Terraform-HuaweiCloud-MaasTaskV1/docs/README.md)
* [Terraform::HuaweiCloud::MlsInstance](../resources/huaweicloud/Terraform-HuaweiCloud-MlsInstance/docs/README.md)
* [Terraform::HuaweiCloud::MrsClusterV1](../resources/huaweicloud/Terraform-HuaweiCloud-MrsClusterV1/docs/README.md)
* [Terraform::HuaweiCloud::MrsJobV1](../resources/huaweicloud/Terraform-HuaweiCloud-MrsJobV1/docs/README.md)
* [Terraform::HuaweiCloud::NatDnatRuleV2](../resources/huaweicloud/Terraform-HuaweiCloud-NatDnatRuleV2/docs/README.md)
* [Terraform::HuaweiCloud::NatGatewayV2](../resources/huaweicloud/Terraform-HuaweiCloud-NatGatewayV2/docs/README.md)
* [Terraform::HuaweiCloud::NatSnatRuleV2](../resources/huaweicloud/Terraform-HuaweiCloud-NatSnatRuleV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingFloatingipAssociateV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingFloatingipAssociateV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingFloatingipV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingFloatingipV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingNetworkV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingNetworkV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingPortV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingPortV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingRouterInterfaceV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingRouterInterfaceV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingRouterRouteV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingRouterRouteV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingRouterV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingRouterV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingSecgroupRuleV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingSecgroupRuleV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingSecgroupV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingSecgroupV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingSubnetV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingSubnetV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingVipAssociateV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingVipAssociateV2/docs/README.md)
* [Terraform::HuaweiCloud::NetworkingVipV2](../resources/huaweicloud/Terraform-HuaweiCloud-NetworkingVipV2/docs/README.md)
* [Terraform::HuaweiCloud::ObsBucketObject](../resources/huaweicloud/Terraform-HuaweiCloud-ObsBucketObject/docs/README.md)
* [Terraform::HuaweiCloud::ObsBucket](../resources/huaweicloud/Terraform-HuaweiCloud-ObsBucket/docs/README.md)
* [Terraform::HuaweiCloud::RdsInstanceV1](../resources/huaweicloud/Terraform-HuaweiCloud-RdsInstanceV1/docs/README.md)
* [Terraform::HuaweiCloud::RdsInstanceV3](../resources/huaweicloud/Terraform-HuaweiCloud-RdsInstanceV3/docs/README.md)
* [Terraform::HuaweiCloud::RdsParametergroupV3](../resources/huaweicloud/Terraform-HuaweiCloud-RdsParametergroupV3/docs/README.md)
* [Terraform::HuaweiCloud::RtsSoftwareConfigV1](../resources/huaweicloud/Terraform-HuaweiCloud-RtsSoftwareConfigV1/docs/README.md)
* [Terraform::HuaweiCloud::RtsStackV1_](../resources/huaweicloud/Terraform-HuaweiCloud-RtsStackV1_/docs/README.md)
* [Terraform::HuaweiCloud::S3BucketObject](../resources/huaweicloud/Terraform-HuaweiCloud-S3BucketObject/docs/README.md)
* [Terraform::HuaweiCloud::S3BucketPolicy](../resources/huaweicloud/Terraform-HuaweiCloud-S3BucketPolicy/docs/README.md)
* [Terraform::HuaweiCloud::S3Bucket](../resources/huaweicloud/Terraform-HuaweiCloud-S3Bucket/docs/README.md)
* [Terraform::HuaweiCloud::SfsFileSystemV2](../resources/huaweicloud/Terraform-HuaweiCloud-SfsFileSystemV2/docs/README.md)
* [Terraform::HuaweiCloud::SmnSubscriptionV2](../resources/huaweicloud/Terraform-HuaweiCloud-SmnSubscriptionV2/docs/README.md)
* [Terraform::HuaweiCloud::SmnTopicV2](../resources/huaweicloud/Terraform-HuaweiCloud-SmnTopicV2/docs/README.md)
* [Terraform::HuaweiCloud::VbsBackupPolicyV2](../resources/huaweicloud/Terraform-HuaweiCloud-VbsBackupPolicyV2/docs/README.md)
* [Terraform::HuaweiCloud::VbsBackupV2](../resources/huaweicloud/Terraform-HuaweiCloud-VbsBackupV2/docs/README.md)
* [Terraform::HuaweiCloud::VpcBandwidthV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpcBandwidthV2/docs/README.md)
* [Terraform::HuaweiCloud::VpcEipV1](../resources/huaweicloud/Terraform-HuaweiCloud-VpcEipV1/docs/README.md)
* [Terraform::HuaweiCloud::VpcPeeringConnectionAccepterV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpcPeeringConnectionAccepterV2/docs/README.md)
* [Terraform::HuaweiCloud::VpcPeeringConnectionV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpcPeeringConnectionV2/docs/README.md)
* [Terraform::HuaweiCloud::VpcRouteV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpcRouteV2/docs/README.md)
* [Terraform::HuaweiCloud::VpcSubnetV1](../resources/huaweicloud/Terraform-HuaweiCloud-VpcSubnetV1/docs/README.md)
* [Terraform::HuaweiCloud::VpcV1](../resources/huaweicloud/Terraform-HuaweiCloud-VpcV1/docs/README.md)
* [Terraform::HuaweiCloud::VpnaasEndpointGroupV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpnaasEndpointGroupV2/docs/README.md)
* [Terraform::HuaweiCloud::VpnaasIkePolicyV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpnaasIkePolicyV2/docs/README.md)
* [Terraform::HuaweiCloud::VpnaasIpsecPolicyV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpnaasIpsecPolicyV2/docs/README.md)
* [Terraform::HuaweiCloud::VpnaasServiceV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpnaasServiceV2/docs/README.md)
* [Terraform::HuaweiCloud::VpnaasSiteConnectionV2](../resources/huaweicloud/Terraform-HuaweiCloud-VpnaasSiteConnectionV2/docs/README.md)