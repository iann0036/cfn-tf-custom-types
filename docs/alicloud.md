# Alicloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/alicloud**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_key` - This is the Alicloud access key.

* `secret_key` - This is the Alicloud secret key.

* `security_token` - Alicloud [Security Token Service](https://www.alibabacloud.com/help/doc-detail/66222.html).

* `ecs_role_name` - "The RAM Role Name attached on a ECS instance for API operations. You can retrieve this from the 'Access Control' section of the Alibaba Cloud console.",

* `region` - This is the Alicloud region.

* `account_id` - (Optional) Alibaba Cloud Account ID. It is used by the Function Compute service and to connect router interfaces.
  If not provided, the provider will attempt to retrieve it automatically with [STS GetCallerIdentity](https://www.alibabacloud.com/help/doc-detail/43767.htm).

* `shared_credentials_file` - (Optional, Available in 1.49.0+) This is the path to the shared credentials file. If this is not set and a profile is specified, ~/.aliyun/config.json will be used.

* `profile` - (Optional, Available in 1.49.0+) This is the Alicloud profile name as set in the shared credentials file.

* `assume_role` - (Optional) An `assume_role` block (documented below). Only one `assume_role` block may be in the configuration.

* `endpoints` - (Optional) An `endpoints` block (documented below) to support custom endpoints.

* `skip_region_validation` - (Optional, Available in 1.52.0+) Skip static validation of region ID. Used by users of alternative AlibabaCloud-like APIs or users w/ access to regions that are not public (yet).

* `configuration_source` - (Optional, Available in 1.56.0+) Use a string to mark a configuration file source, like `terraform-alicloud-modules/terraform-alicloud-ecs-instance` or `terraform-provider-alicloud/examples/vpc`.
The length should not more than 64.

* `protocol` - (Optional, Available in 1.72.0+) The Protocol of used by API request. Valid values: `HTTP` and `HTTPS`. Default to `HTTPS`.

The nested `assume_role` block supports the following:

* `role_arn` - (Required) The ARN of the role to assume. If ARN is set to an empty string, it does not perform role switching.
  Terraform executes configuration on account with provided credentials.

* `policy` - (Optional) A more restrictive policy to apply to the temporary credentials. This gives you a way to further restrict the permissions for the resulting temporary
  security credentials. You cannot use the passed policy to grant permissions that are in excess of those allowed by the access policy of the role that is being assumed.

* `session_name` - (Optional) The session name to use when assuming the role. If omitted, 'terraform' is passed to the AssumeRole call as session name.

* `session_expiration` - (Optional) The time after which the established session for assuming role expires. Valid value range: [900-3600] seconds. Default to 3600 (in this case Alicloud use own default value).

Nested `endpoints` block supports the following:

* `ecs` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom ECS endpoints.

* `rds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom RDS endpoints.

* `slb` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom SLB endpoints.

* `vpc` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom VPC and VPN endpoints.

* `cen` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom CEN endpoints.

* `ess` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Autoscaling endpoints.

* `oss` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom OSS endpoints.

* `dns` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom DNS endpoints.

* `ram` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom RAM endpoints.

* `cs` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Container Service endpoints.

* `cr` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Container Registry endpoints.

* `cdn` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom CDN endpoints.

* `kms` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom KMS endpoints.

* `ots` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Table Store endpoints.

* `cms` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Cloud Monitor endpoints.

* `pvtz` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Private Zone endpoints.

* `sts` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom STS endpoints.

* `log` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Log Service endpoints.

* `drds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom DRDS endpoints.

* `dds` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom MongoDB endpoints.

* `gpdb` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom GPDB endpoints.

* `kvstore` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom R-KVStore endpoints.

* `fc` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Function Computing endpoints.

* `apigateway` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Api Gateway endpoints.

* `datahub` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Datahub endpoints.

* `mns` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom MNS endpoints.

* `location` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Location Service endpoints.",

* `nas` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom nas Service endpoints.",

* `actiontrail` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom actiontrail Service endpoints.",

* `cas` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom CAS endpoints.

* `bssopenapi` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom BSSOPENAPI endpoints.

* `ddoscoo` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom BGP-Line Anti-DDoS Pro endpoints.

* `market` - (Optional) Use this to override the default endpoint URL constructed from the `region`. It's typically used to connect to custom Market endpoints.


## Supported Resources

* [Terraform::Alicloud::Actiontrail](../resources/alicloud/Terraform-Alicloud-Actiontrail/docs/README.md)
* [Terraform::Alicloud::AdbAccount](../resources/alicloud/Terraform-Alicloud-AdbAccount/docs/README.md)
* [Terraform::Alicloud::AdbBackupPolicy](../resources/alicloud/Terraform-Alicloud-AdbBackupPolicy/docs/README.md)
* [Terraform::Alicloud::AdbCluster](../resources/alicloud/Terraform-Alicloud-AdbCluster/docs/README.md)
* [Terraform::Alicloud::AlikafkaConsumerGroup](../resources/alicloud/Terraform-Alicloud-AlikafkaConsumerGroup/docs/README.md)
* [Terraform::Alicloud::AlikafkaInstance](../resources/alicloud/Terraform-Alicloud-AlikafkaInstance/docs/README.md)
* [Terraform::Alicloud::AlikafkaSaslAcl](../resources/alicloud/Terraform-Alicloud-AlikafkaSaslAcl/docs/README.md)
* [Terraform::Alicloud::AlikafkaSaslUser](../resources/alicloud/Terraform-Alicloud-AlikafkaSaslUser/docs/README.md)
* [Terraform::Alicloud::AlikafkaTopic](../resources/alicloud/Terraform-Alicloud-AlikafkaTopic/docs/README.md)
* [Terraform::Alicloud::ApiGatewayApi](../resources/alicloud/Terraform-Alicloud-ApiGatewayApi/docs/README.md)
* [Terraform::Alicloud::ApiGatewayAppAttachment](../resources/alicloud/Terraform-Alicloud-ApiGatewayAppAttachment/docs/README.md)
* [Terraform::Alicloud::ApiGatewayApp](../resources/alicloud/Terraform-Alicloud-ApiGatewayApp/docs/README.md)
* [Terraform::Alicloud::ApiGatewayGroup](../resources/alicloud/Terraform-Alicloud-ApiGatewayGroup/docs/README.md)
* [Terraform::Alicloud::ApiGatewayVpcAccess](../resources/alicloud/Terraform-Alicloud-ApiGatewayVpcAccess/docs/README.md)
* [Terraform::Alicloud::CasCertificate](../resources/alicloud/Terraform-Alicloud-CasCertificate/docs/README.md)
* [Terraform::Alicloud::CdnDomainConfig](../resources/alicloud/Terraform-Alicloud-CdnDomainConfig/docs/README.md)
* [Terraform::Alicloud::CdnDomainNew](../resources/alicloud/Terraform-Alicloud-CdnDomainNew/docs/README.md)
* [Terraform::Alicloud::CdnDomain](../resources/alicloud/Terraform-Alicloud-CdnDomain/docs/README.md)
* [Terraform::Alicloud::CenBandwidthLimit](../resources/alicloud/Terraform-Alicloud-CenBandwidthLimit/docs/README.md)
* [Terraform::Alicloud::CenBandwidthPackageAttachment](../resources/alicloud/Terraform-Alicloud-CenBandwidthPackageAttachment/docs/README.md)
* [Terraform::Alicloud::CenBandwidthPackage](../resources/alicloud/Terraform-Alicloud-CenBandwidthPackage/docs/README.md)
* [Terraform::Alicloud::CenFlowlog](../resources/alicloud/Terraform-Alicloud-CenFlowlog/docs/README.md)
* [Terraform::Alicloud::CenInstanceAttachment](../resources/alicloud/Terraform-Alicloud-CenInstanceAttachment/docs/README.md)
* [Terraform::Alicloud::CenInstanceGrant](../resources/alicloud/Terraform-Alicloud-CenInstanceGrant/docs/README.md)
* [Terraform::Alicloud::CenInstance](../resources/alicloud/Terraform-Alicloud-CenInstance/docs/README.md)
* [Terraform::Alicloud::CenRouteEntry](../resources/alicloud/Terraform-Alicloud-CenRouteEntry/docs/README.md)
* [Terraform::Alicloud::CloudConnectNetworkAttachment](../resources/alicloud/Terraform-Alicloud-CloudConnectNetworkAttachment/docs/README.md)
* [Terraform::Alicloud::CloudConnectNetworkGrant](../resources/alicloud/Terraform-Alicloud-CloudConnectNetworkGrant/docs/README.md)
* [Terraform::Alicloud::CloudConnectNetwork](../resources/alicloud/Terraform-Alicloud-CloudConnectNetwork/docs/README.md)
* [Terraform::Alicloud::CmsAlarm](../resources/alicloud/Terraform-Alicloud-CmsAlarm/docs/README.md)
* [Terraform::Alicloud::CmsSiteMonitor](../resources/alicloud/Terraform-Alicloud-CmsSiteMonitor/docs/README.md)
* [Terraform::Alicloud::CommonBandwidthPackageAttachment](../resources/alicloud/Terraform-Alicloud-CommonBandwidthPackageAttachment/docs/README.md)
* [Terraform::Alicloud::CommonBandwidthPackage](../resources/alicloud/Terraform-Alicloud-CommonBandwidthPackage/docs/README.md)
* [Terraform::Alicloud::ContainerCluster](../resources/alicloud/Terraform-Alicloud-ContainerCluster/docs/README.md)
* [Terraform::Alicloud::CopyImage](../resources/alicloud/Terraform-Alicloud-CopyImage/docs/README.md)
* [Terraform::Alicloud::CrNamespace](../resources/alicloud/Terraform-Alicloud-CrNamespace/docs/README.md)
* [Terraform::Alicloud::CrRepo](../resources/alicloud/Terraform-Alicloud-CrRepo/docs/README.md)
* [Terraform::Alicloud::CsApplication](../resources/alicloud/Terraform-Alicloud-CsApplication/docs/README.md)
* [Terraform::Alicloud::CsKubernetesAutoscaler](../resources/alicloud/Terraform-Alicloud-CsKubernetesAutoscaler/docs/README.md)
* [Terraform::Alicloud::CsKubernetes](../resources/alicloud/Terraform-Alicloud-CsKubernetes/docs/README.md)
* [Terraform::Alicloud::CsManagedKubernetes](../resources/alicloud/Terraform-Alicloud-CsManagedKubernetes/docs/README.md)
* [Terraform::Alicloud::CsServerlessKubernetes](../resources/alicloud/Terraform-Alicloud-CsServerlessKubernetes/docs/README.md)
* [Terraform::Alicloud::CsSwarm](../resources/alicloud/Terraform-Alicloud-CsSwarm/docs/README.md)
* [Terraform::Alicloud::DatahubProject](../resources/alicloud/Terraform-Alicloud-DatahubProject/docs/README.md)
* [Terraform::Alicloud::DatahubSubscription](../resources/alicloud/Terraform-Alicloud-DatahubSubscription/docs/README.md)
* [Terraform::Alicloud::DatahubTopic](../resources/alicloud/Terraform-Alicloud-DatahubTopic/docs/README.md)
* [Terraform::Alicloud::DbAccountPrivilege](../resources/alicloud/Terraform-Alicloud-DbAccountPrivilege/docs/README.md)
* [Terraform::Alicloud::DbAccount](../resources/alicloud/Terraform-Alicloud-DbAccount/docs/README.md)
* [Terraform::Alicloud::DbBackupPolicy](../resources/alicloud/Terraform-Alicloud-DbBackupPolicy/docs/README.md)
* [Terraform::Alicloud::DbConnection](../resources/alicloud/Terraform-Alicloud-DbConnection/docs/README.md)
* [Terraform::Alicloud::DbDatabase](../resources/alicloud/Terraform-Alicloud-DbDatabase/docs/README.md)
* [Terraform::Alicloud::DbInstance](../resources/alicloud/Terraform-Alicloud-DbInstance/docs/README.md)
* [Terraform::Alicloud::DbReadWriteSplittingConnection](../resources/alicloud/Terraform-Alicloud-DbReadWriteSplittingConnection/docs/README.md)
* [Terraform::Alicloud::DbReadonlyInstance](../resources/alicloud/Terraform-Alicloud-DbReadonlyInstance/docs/README.md)
* [Terraform::Alicloud::DdosbgpInstance](../resources/alicloud/Terraform-Alicloud-DdosbgpInstance/docs/README.md)
* [Terraform::Alicloud::DdoscooInstance](../resources/alicloud/Terraform-Alicloud-DdoscooInstance/docs/README.md)
* [Terraform::Alicloud::DiskAttachment](../resources/alicloud/Terraform-Alicloud-DiskAttachment/docs/README.md)
* [Terraform::Alicloud::Disk](../resources/alicloud/Terraform-Alicloud-Disk/docs/README.md)
* [Terraform::Alicloud::DnsGroup](../resources/alicloud/Terraform-Alicloud-DnsGroup/docs/README.md)
* [Terraform::Alicloud::DnsRecord](../resources/alicloud/Terraform-Alicloud-DnsRecord/docs/README.md)
* [Terraform::Alicloud::Dns](../resources/alicloud/Terraform-Alicloud-Dns/docs/README.md)
* [Terraform::Alicloud::DrdsInstance](../resources/alicloud/Terraform-Alicloud-DrdsInstance/docs/README.md)
* [Terraform::Alicloud::EipAssociation](../resources/alicloud/Terraform-Alicloud-EipAssociation/docs/README.md)
* [Terraform::Alicloud::Eip](../resources/alicloud/Terraform-Alicloud-Eip/docs/README.md)
* [Terraform::Alicloud::ElasticsearchInstance](../resources/alicloud/Terraform-Alicloud-ElasticsearchInstance/docs/README.md)
* [Terraform::Alicloud::EmrCluster](../resources/alicloud/Terraform-Alicloud-EmrCluster/docs/README.md)
* [Terraform::Alicloud::EssAlarm](../resources/alicloud/Terraform-Alicloud-EssAlarm/docs/README.md)
* [Terraform::Alicloud::EssAttachment](../resources/alicloud/Terraform-Alicloud-EssAttachment/docs/README.md)
* [Terraform::Alicloud::EssLifecycleHook](../resources/alicloud/Terraform-Alicloud-EssLifecycleHook/docs/README.md)
* [Terraform::Alicloud::EssNotification](../resources/alicloud/Terraform-Alicloud-EssNotification/docs/README.md)
* [Terraform::Alicloud::EssScalingConfiguration](../resources/alicloud/Terraform-Alicloud-EssScalingConfiguration/docs/README.md)
* [Terraform::Alicloud::EssScalingGroup](../resources/alicloud/Terraform-Alicloud-EssScalingGroup/docs/README.md)
* [Terraform::Alicloud::EssScalingRule](../resources/alicloud/Terraform-Alicloud-EssScalingRule/docs/README.md)
* [Terraform::Alicloud::EssScalinggroupVserverGroups](../resources/alicloud/Terraform-Alicloud-EssScalinggroupVserverGroups/docs/README.md)
* [Terraform::Alicloud::EssSchedule](../resources/alicloud/Terraform-Alicloud-EssSchedule/docs/README.md)
* [Terraform::Alicloud::EssScheduledTask](../resources/alicloud/Terraform-Alicloud-EssScheduledTask/docs/README.md)
* [Terraform::Alicloud::FcFunction](../resources/alicloud/Terraform-Alicloud-FcFunction/docs/README.md)
* [Terraform::Alicloud::FcService](../resources/alicloud/Terraform-Alicloud-FcService/docs/README.md)
* [Terraform::Alicloud::FcTrigger](../resources/alicloud/Terraform-Alicloud-FcTrigger/docs/README.md)
* [Terraform::Alicloud::ForwardEntry](../resources/alicloud/Terraform-Alicloud-ForwardEntry/docs/README.md)
* [Terraform::Alicloud::GpdbConnection](../resources/alicloud/Terraform-Alicloud-GpdbConnection/docs/README.md)
* [Terraform::Alicloud::GpdbInstance](../resources/alicloud/Terraform-Alicloud-GpdbInstance/docs/README.md)
* [Terraform::Alicloud::HavipAttachment](../resources/alicloud/Terraform-Alicloud-HavipAttachment/docs/README.md)
* [Terraform::Alicloud::Havip](../resources/alicloud/Terraform-Alicloud-Havip/docs/README.md)
* [Terraform::Alicloud::HbaseInstance](../resources/alicloud/Terraform-Alicloud-HbaseInstance/docs/README.md)
* [Terraform::Alicloud::ImageCopy](../resources/alicloud/Terraform-Alicloud-ImageCopy/docs/README.md)
* [Terraform::Alicloud::ImageExport](../resources/alicloud/Terraform-Alicloud-ImageExport/docs/README.md)
* [Terraform::Alicloud::ImageImport](../resources/alicloud/Terraform-Alicloud-ImageImport/docs/README.md)
* [Terraform::Alicloud::ImageSharePermission](../resources/alicloud/Terraform-Alicloud-ImageSharePermission/docs/README.md)
* [Terraform::Alicloud::Image](../resources/alicloud/Terraform-Alicloud-Image/docs/README.md)
* [Terraform::Alicloud::Instance](../resources/alicloud/Terraform-Alicloud-Instance/docs/README.md)
* [Terraform::Alicloud::KeyPairAttachment](../resources/alicloud/Terraform-Alicloud-KeyPairAttachment/docs/README.md)
* [Terraform::Alicloud::KeyPair](../resources/alicloud/Terraform-Alicloud-KeyPair/docs/README.md)
* [Terraform::Alicloud::KmsCiphertext](../resources/alicloud/Terraform-Alicloud-KmsCiphertext/docs/README.md)
* [Terraform::Alicloud::KmsKey](../resources/alicloud/Terraform-Alicloud-KmsKey/docs/README.md)
* [Terraform::Alicloud::KvstoreAccount](../resources/alicloud/Terraform-Alicloud-KvstoreAccount/docs/README.md)
* [Terraform::Alicloud::KvstoreBackupPolicy](../resources/alicloud/Terraform-Alicloud-KvstoreBackupPolicy/docs/README.md)
* [Terraform::Alicloud::KvstoreInstance](../resources/alicloud/Terraform-Alicloud-KvstoreInstance/docs/README.md)
* [Terraform::Alicloud::LaunchTemplate](../resources/alicloud/Terraform-Alicloud-LaunchTemplate/docs/README.md)
* [Terraform::Alicloud::LogMachineGroup](../resources/alicloud/Terraform-Alicloud-LogMachineGroup/docs/README.md)
* [Terraform::Alicloud::LogProject](../resources/alicloud/Terraform-Alicloud-LogProject/docs/README.md)
* [Terraform::Alicloud::LogStoreIndex](../resources/alicloud/Terraform-Alicloud-LogStoreIndex/docs/README.md)
* [Terraform::Alicloud::LogStore](../resources/alicloud/Terraform-Alicloud-LogStore/docs/README.md)
* [Terraform::Alicloud::LogtailAttachment](../resources/alicloud/Terraform-Alicloud-LogtailAttachment/docs/README.md)
* [Terraform::Alicloud::LogtailConfig](../resources/alicloud/Terraform-Alicloud-LogtailConfig/docs/README.md)
* [Terraform::Alicloud::MarketOrder](../resources/alicloud/Terraform-Alicloud-MarketOrder/docs/README.md)
* [Terraform::Alicloud::MnsQueue](../resources/alicloud/Terraform-Alicloud-MnsQueue/docs/README.md)
* [Terraform::Alicloud::MnsTopicSubscription](../resources/alicloud/Terraform-Alicloud-MnsTopicSubscription/docs/README.md)
* [Terraform::Alicloud::MnsTopic](../resources/alicloud/Terraform-Alicloud-MnsTopic/docs/README.md)
* [Terraform::Alicloud::MongodbInstance](../resources/alicloud/Terraform-Alicloud-MongodbInstance/docs/README.md)
* [Terraform::Alicloud::MongodbShardingInstance](../resources/alicloud/Terraform-Alicloud-MongodbShardingInstance/docs/README.md)
* [Terraform::Alicloud::NasAccessGroup](../resources/alicloud/Terraform-Alicloud-NasAccessGroup/docs/README.md)
* [Terraform::Alicloud::NasAccessRule](../resources/alicloud/Terraform-Alicloud-NasAccessRule/docs/README.md)
* [Terraform::Alicloud::NasFileSystem](../resources/alicloud/Terraform-Alicloud-NasFileSystem/docs/README.md)
* [Terraform::Alicloud::NasMountTarget](../resources/alicloud/Terraform-Alicloud-NasMountTarget/docs/README.md)
* [Terraform::Alicloud::NatGateway](../resources/alicloud/Terraform-Alicloud-NatGateway/docs/README.md)
* [Terraform::Alicloud::NetworkAclAttachment](../resources/alicloud/Terraform-Alicloud-NetworkAclAttachment/docs/README.md)
* [Terraform::Alicloud::NetworkAclEntries](../resources/alicloud/Terraform-Alicloud-NetworkAclEntries/docs/README.md)
* [Terraform::Alicloud::NetworkAcl](../resources/alicloud/Terraform-Alicloud-NetworkAcl/docs/README.md)
* [Terraform::Alicloud::NetworkInterfaceAttachment](../resources/alicloud/Terraform-Alicloud-NetworkInterfaceAttachment/docs/README.md)
* [Terraform::Alicloud::NetworkInterface](../resources/alicloud/Terraform-Alicloud-NetworkInterface/docs/README.md)
* [Terraform::Alicloud::OnsGroup](../resources/alicloud/Terraform-Alicloud-OnsGroup/docs/README.md)
* [Terraform::Alicloud::OnsInstance](../resources/alicloud/Terraform-Alicloud-OnsInstance/docs/README.md)
* [Terraform::Alicloud::OnsTopic](../resources/alicloud/Terraform-Alicloud-OnsTopic/docs/README.md)
* [Terraform::Alicloud::OssBucketObject](../resources/alicloud/Terraform-Alicloud-OssBucketObject/docs/README.md)
* [Terraform::Alicloud::OssBucket](../resources/alicloud/Terraform-Alicloud-OssBucket/docs/README.md)
* [Terraform::Alicloud::OtsInstanceAttachment](../resources/alicloud/Terraform-Alicloud-OtsInstanceAttachment/docs/README.md)
* [Terraform::Alicloud::OtsInstance](../resources/alicloud/Terraform-Alicloud-OtsInstance/docs/README.md)
* [Terraform::Alicloud::OtsTable](../resources/alicloud/Terraform-Alicloud-OtsTable/docs/README.md)
* [Terraform::Alicloud::PolardbAccountPrivilege](../resources/alicloud/Terraform-Alicloud-PolardbAccountPrivilege/docs/README.md)
* [Terraform::Alicloud::PolardbAccount](../resources/alicloud/Terraform-Alicloud-PolardbAccount/docs/README.md)
* [Terraform::Alicloud::PolardbBackupPolicy](../resources/alicloud/Terraform-Alicloud-PolardbBackupPolicy/docs/README.md)
* [Terraform::Alicloud::PolardbCluster](../resources/alicloud/Terraform-Alicloud-PolardbCluster/docs/README.md)
* [Terraform::Alicloud::PolardbDatabase](../resources/alicloud/Terraform-Alicloud-PolardbDatabase/docs/README.md)
* [Terraform::Alicloud::PolardbEndpointAddress](../resources/alicloud/Terraform-Alicloud-PolardbEndpointAddress/docs/README.md)
* [Terraform::Alicloud::PvtzZoneAttachment](../resources/alicloud/Terraform-Alicloud-PvtzZoneAttachment/docs/README.md)
* [Terraform::Alicloud::PvtzZoneRecord](../resources/alicloud/Terraform-Alicloud-PvtzZoneRecord/docs/README.md)
* [Terraform::Alicloud::PvtzZone](../resources/alicloud/Terraform-Alicloud-PvtzZone/docs/README.md)
* [Terraform::Alicloud::RamAccessKey](../resources/alicloud/Terraform-Alicloud-RamAccessKey/docs/README.md)
* [Terraform::Alicloud::RamAccountAlias](../resources/alicloud/Terraform-Alicloud-RamAccountAlias/docs/README.md)
* [Terraform::Alicloud::RamAccountPasswordPolicy](../resources/alicloud/Terraform-Alicloud-RamAccountPasswordPolicy/docs/README.md)
* [Terraform::Alicloud::RamAlias](../resources/alicloud/Terraform-Alicloud-RamAlias/docs/README.md)
* [Terraform::Alicloud::RamGroupMembership](../resources/alicloud/Terraform-Alicloud-RamGroupMembership/docs/README.md)
* [Terraform::Alicloud::RamGroupPolicyAttachment](../resources/alicloud/Terraform-Alicloud-RamGroupPolicyAttachment/docs/README.md)
* [Terraform::Alicloud::RamGroup](../resources/alicloud/Terraform-Alicloud-RamGroup/docs/README.md)
* [Terraform::Alicloud::RamLoginProfile](../resources/alicloud/Terraform-Alicloud-RamLoginProfile/docs/README.md)
* [Terraform::Alicloud::RamPolicy](../resources/alicloud/Terraform-Alicloud-RamPolicy/docs/README.md)
* [Terraform::Alicloud::RamRoleAttachment](../resources/alicloud/Terraform-Alicloud-RamRoleAttachment/docs/README.md)
* [Terraform::Alicloud::RamRolePolicyAttachment](../resources/alicloud/Terraform-Alicloud-RamRolePolicyAttachment/docs/README.md)
* [Terraform::Alicloud::RamRole](../resources/alicloud/Terraform-Alicloud-RamRole/docs/README.md)
* [Terraform::Alicloud::RamUserPolicyAttachment](../resources/alicloud/Terraform-Alicloud-RamUserPolicyAttachment/docs/README.md)
* [Terraform::Alicloud::RamUser](../resources/alicloud/Terraform-Alicloud-RamUser/docs/README.md)
* [Terraform::Alicloud::ReservedInstance](../resources/alicloud/Terraform-Alicloud-ReservedInstance/docs/README.md)
* [Terraform::Alicloud::RouteEntry](../resources/alicloud/Terraform-Alicloud-RouteEntry/docs/README.md)
* [Terraform::Alicloud::RouteTableAttachment](../resources/alicloud/Terraform-Alicloud-RouteTableAttachment/docs/README.md)
* [Terraform::Alicloud::RouteTable](../resources/alicloud/Terraform-Alicloud-RouteTable/docs/README.md)
* [Terraform::Alicloud::RouterInterfaceConnection](../resources/alicloud/Terraform-Alicloud-RouterInterfaceConnection/docs/README.md)
* [Terraform::Alicloud::RouterInterface](../resources/alicloud/Terraform-Alicloud-RouterInterface/docs/README.md)
* [Terraform::Alicloud::SagAclRule](../resources/alicloud/Terraform-Alicloud-SagAclRule/docs/README.md)
* [Terraform::Alicloud::SagAcl](../resources/alicloud/Terraform-Alicloud-SagAcl/docs/README.md)
* [Terraform::Alicloud::SagClientUser](../resources/alicloud/Terraform-Alicloud-SagClientUser/docs/README.md)
* [Terraform::Alicloud::SagDnatEntry](../resources/alicloud/Terraform-Alicloud-SagDnatEntry/docs/README.md)
* [Terraform::Alicloud::SagQosCar](../resources/alicloud/Terraform-Alicloud-SagQosCar/docs/README.md)
* [Terraform::Alicloud::SagQosPolicy](../resources/alicloud/Terraform-Alicloud-SagQosPolicy/docs/README.md)
* [Terraform::Alicloud::SagQos](../resources/alicloud/Terraform-Alicloud-SagQos/docs/README.md)
* [Terraform::Alicloud::SagSnatEntry](../resources/alicloud/Terraform-Alicloud-SagSnatEntry/docs/README.md)
* [Terraform::Alicloud::SecurityGroupRule](../resources/alicloud/Terraform-Alicloud-SecurityGroupRule/docs/README.md)
* [Terraform::Alicloud::SecurityGroup](../resources/alicloud/Terraform-Alicloud-SecurityGroup/docs/README.md)
* [Terraform::Alicloud::SlbAcl](../resources/alicloud/Terraform-Alicloud-SlbAcl/docs/README.md)
* [Terraform::Alicloud::SlbAttachment](../resources/alicloud/Terraform-Alicloud-SlbAttachment/docs/README.md)
* [Terraform::Alicloud::SlbBackendServer](../resources/alicloud/Terraform-Alicloud-SlbBackendServer/docs/README.md)
* [Terraform::Alicloud::SlbCaCertificate](../resources/alicloud/Terraform-Alicloud-SlbCaCertificate/docs/README.md)
* [Terraform::Alicloud::SlbDomainExtension](../resources/alicloud/Terraform-Alicloud-SlbDomainExtension/docs/README.md)
* [Terraform::Alicloud::SlbListener](../resources/alicloud/Terraform-Alicloud-SlbListener/docs/README.md)
* [Terraform::Alicloud::SlbMasterSlaveServerGroup](../resources/alicloud/Terraform-Alicloud-SlbMasterSlaveServerGroup/docs/README.md)
* [Terraform::Alicloud::SlbRule](../resources/alicloud/Terraform-Alicloud-SlbRule/docs/README.md)
* [Terraform::Alicloud::SlbServerCertificate](../resources/alicloud/Terraform-Alicloud-SlbServerCertificate/docs/README.md)
* [Terraform::Alicloud::SlbServerGroup](../resources/alicloud/Terraform-Alicloud-SlbServerGroup/docs/README.md)
* [Terraform::Alicloud::Slb](../resources/alicloud/Terraform-Alicloud-Slb/docs/README.md)
* [Terraform::Alicloud::SnapshotPolicy](../resources/alicloud/Terraform-Alicloud-SnapshotPolicy/docs/README.md)
* [Terraform::Alicloud::Snapshot](../resources/alicloud/Terraform-Alicloud-Snapshot/docs/README.md)
* [Terraform::Alicloud::SnatEntry](../resources/alicloud/Terraform-Alicloud-SnatEntry/docs/README.md)
* [Terraform::Alicloud::SslVpnClientCert](../resources/alicloud/Terraform-Alicloud-SslVpnClientCert/docs/README.md)
* [Terraform::Alicloud::SslVpnServer](../resources/alicloud/Terraform-Alicloud-SslVpnServer/docs/README.md)
* [Terraform::Alicloud::Subnet](../resources/alicloud/Terraform-Alicloud-Subnet/docs/README.md)
* [Terraform::Alicloud::Vpc](../resources/alicloud/Terraform-Alicloud-Vpc/docs/README.md)
* [Terraform::Alicloud::VpnConnection](../resources/alicloud/Terraform-Alicloud-VpnConnection/docs/README.md)
* [Terraform::Alicloud::VpnCustomerGateway](../resources/alicloud/Terraform-Alicloud-VpnCustomerGateway/docs/README.md)
* [Terraform::Alicloud::VpnGateway](../resources/alicloud/Terraform-Alicloud-VpnGateway/docs/README.md)
* [Terraform::Alicloud::VpnRouteEntry](../resources/alicloud/Terraform-Alicloud-VpnRouteEntry/docs/README.md)
* [Terraform::Alicloud::Vswitch](../resources/alicloud/Terraform-Alicloud-Vswitch/docs/README.md)
* [Terraform::Alicloud::YundunBastionhostInstance](../resources/alicloud/Terraform-Alicloud-YundunBastionhostInstance/docs/README.md)
* [Terraform::Alicloud::YundunDbauditInstance](../resources/alicloud/Terraform-Alicloud-YundunDbauditInstance/docs/README.md)