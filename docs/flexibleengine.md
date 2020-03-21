# FlexibleEngine Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/flexibleengine**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - (Optional) The access key of the FlexibleEngine cloud to use.
  If omitted, the `OS_ACCESS_KEY` environment variable is used.

* `secret_key` - (Optional) The secret key of the FlexibleEngine cloud to use.
  If omitted, the `OS_SECRET_KEY` environment variable is used.

* `auth_url` - (Required) The Identity authentication URL. If omitted, the
  `OS_AUTH_URL` environment variable is used.

* `region` - (Optional) The region of the FlexibleEngine cloud to use. If omitted,
  the `OS_REGION_NAME` environment variable is used. If `OS_REGION_NAME` is
  not set, then no region will be used. It should be possible to omit the
  region in single-region FlexibleEngine environments, but this behavior may vary
  depending on the FlexibleEngine environment being used.

* `user_name` - (Optional) The Username to login with. If omitted, the
  `OS_USERNAME` environment variable is used.

* `user_id` - (Optional) The User ID to login with. If omitted, the
  `OS_USER_ID` environment variable is used.

* `tenant_id` - (Optional) The ID of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_ID` or
  `OS_PROJECT_ID` environment variables are used.

* `tenant_name` - (Optional) The Name of the Tenant (Identity v2) or Project
  (Identity v3) to login with. If omitted, the `OS_TENANT_NAME` or
  `OS_PROJECT_NAME` environment variable are used.

* `password` - (Optional) The Password to login with. If omitted, the
  `OS_PASSWORD` environment variable is used.

* `token` - (Optional; Required if not using `user_name` and `password`)
  A token is an expiring, temporary means of access issued via the Keystone
  service. By specifying a token, you do not have to specify a username/password
  combination, since the token was already created by a username/password out of
  band of Terraform. If omitted, the `OS_AUTH_TOKEN` environment variable is used.

* `security_token` - (Optional) Security token to use for OBS federated authentication.

* `domain_id` - (Optional) The ID of the Domain to scope to (Identity v3). If
  If omitted, the following environment variables are checked (in this order):
  `OS_USER_DOMAIN_ID`, `OS_PROJECT_DOMAIN_ID`, `OS_DOMAIN_ID`.

* `domain_name` - (Optional) The Name of the Domain to scope to (Identity v3).
  If omitted, the following environment variables are checked (in this order):
  `OS_USER_DOMAIN_NAME`, `OS_PROJECT_DOMAIN_NAME`, `OS_DOMAIN_NAME`,
  `DEFAULT_DOMAIN`.

* `insecure` - (Optional) Trust self-signed SSL certificates. If omitted, the
  `OS_INSECURE` environment variable is used.

* `cacert_file` - (Optional) Specify a custom CA certificate when communicating
  over SSL. You can specify either a path to the file or the contents of the
  certificate. If omitted, the `OS_CACERT` environment variable is used.

* `cert` - (Optional) Specify client certificate file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the certificate. If omitted the `OS_CERT` environment variable is used.

* `key` - (Optional) Specify client private key file for SSL client
  authentication. You can specify either a path to the file or the contents of
  the key. If omitted the `OS_KEY` environment variable is used.

* `endpoint_type` - (Optional) Specify which type of endpoint to use from the
  service catalog. It can be set using the OS_ENDPOINT_TYPE environment
  variable. If not set, public endpoints is used.

* `swauth` - (Optional) Set to `true` to authenticate against Swauth, a
  Swift-native authentication system. If omitted, the `OS_SWAUTH` environment
  variable is used. You must also set `username` to the Swauth/Swift username
  such as `username:project`. Set the `password` to the Swauth/Swift key.
  Finally, set `auth_url` as the location of the Swift service. Note that this
  will only work when used with the FlexibleEngine Object Storage resources.


## Supported Resources

* [Terraform::FlexibleEngine::AntiddosV1](../resources/flexibleengine/Terraform-FlexibleEngine-AntiddosV1/docs/README.md)
* [Terraform::FlexibleEngine::AsConfigurationV1](../resources/flexibleengine/Terraform-FlexibleEngine-AsConfigurationV1/docs/README.md)
* [Terraform::FlexibleEngine::AsGroupV1](../resources/flexibleengine/Terraform-FlexibleEngine-AsGroupV1/docs/README.md)
* [Terraform::FlexibleEngine::AsPolicyV1](../resources/flexibleengine/Terraform-FlexibleEngine-AsPolicyV1/docs/README.md)
* [Terraform::FlexibleEngine::BlockstorageVolumeV2](../resources/flexibleengine/Terraform-FlexibleEngine-BlockstorageVolumeV2/docs/README.md)
* [Terraform::FlexibleEngine::CceClusterV3](../resources/flexibleengine/Terraform-FlexibleEngine-CceClusterV3/docs/README.md)
* [Terraform::FlexibleEngine::CceNodeV3](../resources/flexibleengine/Terraform-FlexibleEngine-CceNodeV3/docs/README.md)
* [Terraform::FlexibleEngine::CesAlarmrule](../resources/flexibleengine/Terraform-FlexibleEngine-CesAlarmrule/docs/README.md)
* [Terraform::FlexibleEngine::ComputeBmsServerV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeBmsServerV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeFloatingipAssociateV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeFloatingipAssociateV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeFloatingipV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeFloatingipV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeInstanceV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeInstanceV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeInterfaceAttachV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeInterfaceAttachV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeKeypairV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeKeypairV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeServergroupV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeServergroupV2/docs/README.md)
* [Terraform::FlexibleEngine::ComputeVolumeAttachV2](../resources/flexibleengine/Terraform-FlexibleEngine-ComputeVolumeAttachV2/docs/README.md)
* [Terraform::FlexibleEngine::CsbsBackupPolicyV1](../resources/flexibleengine/Terraform-FlexibleEngine-CsbsBackupPolicyV1/docs/README.md)
* [Terraform::FlexibleEngine::CsbsBackupV1](../resources/flexibleengine/Terraform-FlexibleEngine-CsbsBackupV1/docs/README.md)
* [Terraform::FlexibleEngine::CtsTrackerV1](../resources/flexibleengine/Terraform-FlexibleEngine-CtsTrackerV1/docs/README.md)
* [Terraform::FlexibleEngine::DcsInstanceV1](../resources/flexibleengine/Terraform-FlexibleEngine-DcsInstanceV1/docs/README.md)
* [Terraform::FlexibleEngine::DdsInstanceV3](../resources/flexibleengine/Terraform-FlexibleEngine-DdsInstanceV3/docs/README.md)
* [Terraform::FlexibleEngine::DnsRecordsetV2](../resources/flexibleengine/Terraform-FlexibleEngine-DnsRecordsetV2/docs/README.md)
* [Terraform::FlexibleEngine::DnsZoneV2](../resources/flexibleengine/Terraform-FlexibleEngine-DnsZoneV2/docs/README.md)
* [Terraform::FlexibleEngine::DrsReplicationV2](../resources/flexibleengine/Terraform-FlexibleEngine-DrsReplicationV2/docs/README.md)
* [Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2](../resources/flexibleengine/Terraform-FlexibleEngine-DrsReplicationconsistencygroupV2/docs/README.md)
* [Terraform::FlexibleEngine::DwsClusterV1](../resources/flexibleengine/Terraform-FlexibleEngine-DwsClusterV1/docs/README.md)
* [Terraform::FlexibleEngine::ElbBackend](../resources/flexibleengine/Terraform-FlexibleEngine-ElbBackend/docs/README.md)
* [Terraform::FlexibleEngine::ElbHealth](../resources/flexibleengine/Terraform-FlexibleEngine-ElbHealth/docs/README.md)
* [Terraform::FlexibleEngine::ElbListener](../resources/flexibleengine/Terraform-FlexibleEngine-ElbListener/docs/README.md)
* [Terraform::FlexibleEngine::ElbLoadbalancer](../resources/flexibleengine/Terraform-FlexibleEngine-ElbLoadbalancer/docs/README.md)
* [Terraform::FlexibleEngine::FwFirewallGroupV2](../resources/flexibleengine/Terraform-FlexibleEngine-FwFirewallGroupV2/docs/README.md)
* [Terraform::FlexibleEngine::FwPolicyV2](../resources/flexibleengine/Terraform-FlexibleEngine-FwPolicyV2/docs/README.md)
* [Terraform::FlexibleEngine::FwRuleV2](../resources/flexibleengine/Terraform-FlexibleEngine-FwRuleV2/docs/README.md)
* [Terraform::FlexibleEngine::ImagesImageV2](../resources/flexibleengine/Terraform-FlexibleEngine-ImagesImageV2/docs/README.md)
* [Terraform::FlexibleEngine::KmsKeyV1](../resources/flexibleengine/Terraform-FlexibleEngine-KmsKeyV1/docs/README.md)
* [Terraform::FlexibleEngine::LbCertificateV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbCertificateV2/docs/README.md)
* [Terraform::FlexibleEngine::LbL7policyV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbL7policyV2/docs/README.md)
* [Terraform::FlexibleEngine::LbL7ruleV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbL7ruleV2/docs/README.md)
* [Terraform::FlexibleEngine::LbListenerV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbListenerV2/docs/README.md)
* [Terraform::FlexibleEngine::LbLoadbalancerV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbLoadbalancerV2/docs/README.md)
* [Terraform::FlexibleEngine::LbMemberV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbMemberV2/docs/README.md)
* [Terraform::FlexibleEngine::LbMonitorV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbMonitorV2/docs/README.md)
* [Terraform::FlexibleEngine::LbPoolV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbPoolV2/docs/README.md)
* [Terraform::FlexibleEngine::LbWhitelistV2](../resources/flexibleengine/Terraform-FlexibleEngine-LbWhitelistV2/docs/README.md)
* [Terraform::FlexibleEngine::MlsInstanceV1](../resources/flexibleengine/Terraform-FlexibleEngine-MlsInstanceV1/docs/README.md)
* [Terraform::FlexibleEngine::MrsClusterV1](../resources/flexibleengine/Terraform-FlexibleEngine-MrsClusterV1/docs/README.md)
* [Terraform::FlexibleEngine::MrsJobV1](../resources/flexibleengine/Terraform-FlexibleEngine-MrsJobV1/docs/README.md)
* [Terraform::FlexibleEngine::NatDnatRuleV2](../resources/flexibleengine/Terraform-FlexibleEngine-NatDnatRuleV2/docs/README.md)
* [Terraform::FlexibleEngine::NatGatewayV2](../resources/flexibleengine/Terraform-FlexibleEngine-NatGatewayV2/docs/README.md)
* [Terraform::FlexibleEngine::NatSnatRuleV2](../resources/flexibleengine/Terraform-FlexibleEngine-NatSnatRuleV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipAssociateV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingFloatingipAssociateV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingFloatingipV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingFloatingipV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingNetworkV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingNetworkV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingPortV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingPortV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingRouterInterfaceV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingRouterInterfaceV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingRouterRouteV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingRouterRouteV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingRouterV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingRouterV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupRuleV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingSecgroupRuleV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingSecgroupV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingSecgroupV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingSubnetV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingSubnetV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingVipAssociateV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingVipAssociateV2/docs/README.md)
* [Terraform::FlexibleEngine::NetworkingVipV2](../resources/flexibleengine/Terraform-FlexibleEngine-NetworkingVipV2/docs/README.md)
* [Terraform::FlexibleEngine::RdsInstanceV1](../resources/flexibleengine/Terraform-FlexibleEngine-RdsInstanceV1/docs/README.md)
* [Terraform::FlexibleEngine::RdsInstanceV3](../resources/flexibleengine/Terraform-FlexibleEngine-RdsInstanceV3/docs/README.md)
* [Terraform::FlexibleEngine::RdsParametergroupV3](../resources/flexibleengine/Terraform-FlexibleEngine-RdsParametergroupV3/docs/README.md)
* [Terraform::FlexibleEngine::RtsSoftwareConfigV1](../resources/flexibleengine/Terraform-FlexibleEngine-RtsSoftwareConfigV1/docs/README.md)
* [Terraform::FlexibleEngine::RtsStackV1](../resources/flexibleengine/Terraform-FlexibleEngine-RtsStackV1/docs/README.md)
* [Terraform::FlexibleEngine::S3BucketObject](../resources/flexibleengine/Terraform-FlexibleEngine-S3BucketObject/docs/README.md)
* [Terraform::FlexibleEngine::S3BucketPolicy](../resources/flexibleengine/Terraform-FlexibleEngine-S3BucketPolicy/docs/README.md)
* [Terraform::FlexibleEngine::S3Bucket](../resources/flexibleengine/Terraform-FlexibleEngine-S3Bucket/docs/README.md)
* [Terraform::FlexibleEngine::SdrsDrillV1](../resources/flexibleengine/Terraform-FlexibleEngine-SdrsDrillV1/docs/README.md)
* [Terraform::FlexibleEngine::SdrsProtectedinstanceV1](../resources/flexibleengine/Terraform-FlexibleEngine-SdrsProtectedinstanceV1/docs/README.md)
* [Terraform::FlexibleEngine::SdrsProtectiongroupV1](../resources/flexibleengine/Terraform-FlexibleEngine-SdrsProtectiongroupV1/docs/README.md)
* [Terraform::FlexibleEngine::SdrsReplicationAttachV1](../resources/flexibleengine/Terraform-FlexibleEngine-SdrsReplicationAttachV1/docs/README.md)
* [Terraform::FlexibleEngine::SdrsReplicationPairV1](../resources/flexibleengine/Terraform-FlexibleEngine-SdrsReplicationPairV1/docs/README.md)
* [Terraform::FlexibleEngine::SfsFileSystemV2](../resources/flexibleengine/Terraform-FlexibleEngine-SfsFileSystemV2/docs/README.md)
* [Terraform::FlexibleEngine::SmnSubscriptionV2](../resources/flexibleengine/Terraform-FlexibleEngine-SmnSubscriptionV2/docs/README.md)
* [Terraform::FlexibleEngine::SmnTopicV2](../resources/flexibleengine/Terraform-FlexibleEngine-SmnTopicV2/docs/README.md)
* [Terraform::FlexibleEngine::VbsBackupPolicyV2](../resources/flexibleengine/Terraform-FlexibleEngine-VbsBackupPolicyV2/docs/README.md)
* [Terraform::FlexibleEngine::VbsBackupV2](../resources/flexibleengine/Terraform-FlexibleEngine-VbsBackupV2/docs/README.md)
* [Terraform::FlexibleEngine::VpcEipV1](../resources/flexibleengine/Terraform-FlexibleEngine-VpcEipV1/docs/README.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionAccepterV2](../resources/flexibleengine/Terraform-FlexibleEngine-VpcPeeringConnectionAccepterV2/docs/README.md)
* [Terraform::FlexibleEngine::VpcPeeringConnectionV2](../resources/flexibleengine/Terraform-FlexibleEngine-VpcPeeringConnectionV2/docs/README.md)
* [Terraform::FlexibleEngine::VpcRouteV2](../resources/flexibleengine/Terraform-FlexibleEngine-VpcRouteV2/docs/README.md)
* [Terraform::FlexibleEngine::VpcSubnetV1](../resources/flexibleengine/Terraform-FlexibleEngine-VpcSubnetV1/docs/README.md)
* [Terraform::FlexibleEngine::VpcV1](../resources/flexibleengine/Terraform-FlexibleEngine-VpcV1/docs/README.md)