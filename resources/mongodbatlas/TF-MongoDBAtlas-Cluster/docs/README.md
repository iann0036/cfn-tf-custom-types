# TF::MongoDBAtlas::Cluster

`mongodbatlas_cluster` provides a Cluster resource. The resource lets you create, edit and delete clusters. The resource requires your Project ID.

-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

-> **NOTE:** A network container is created for a cluster to reside in if one does not yet exist in the project.  To  use this automatically created container with another resource, such as peering, the `container_id` is exported after creation.

~> **IMPORTANT:**
<br> &#8226; Free tier cluster creation (M0) is not supported via API or by this Provider.
<br> &#8226; Shared tier clusters (M2, M5) cannot be upgraded to higher tiers via API or by this Provider.
<br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).   
<br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::Cluster",
    "Properties" : {
        "<a href="#autoscalingcomputeenabled" title="AutoScalingComputeEnabled">AutoScalingComputeEnabled</a>" : <i>Boolean</i>,
        "<a href="#autoscalingcomputescaledownenabled" title="AutoScalingComputeScaleDownEnabled">AutoScalingComputeScaleDownEnabled</a>" : <i>Boolean</i>,
        "<a href="#autoscalingdiskgbenabled" title="AutoScalingDiskGbEnabled">AutoScalingDiskGbEnabled</a>" : <i>Boolean</i>,
        "<a href="#backingprovidername" title="BackingProviderName">BackingProviderName</a>" : <i>String</i>,
        "<a href="#backupenabled" title="BackupEnabled">BackupEnabled</a>" : <i>Boolean</i>,
        "<a href="#biconnector" title="BiConnector">BiConnector</a>" : <i>[ <a href="biconnectordefinition.md">BiConnectorDefinition</a>, ... ]</i>,
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>String</i>,
        "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
        "<a href="#encryptionatrestprovider" title="EncryptionAtRestProvider">EncryptionAtRestProvider</a>" : <i>String</i>,
        "<a href="#mongodbmajorversion" title="MongoDbMajorVersion">MongoDbMajorVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numshards" title="NumShards">NumShards</a>" : <i>Double</i>,
        "<a href="#pitenabled" title="PitEnabled">PitEnabled</a>" : <i>Boolean</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providerautoscalingcomputemaxinstancesize" title="ProviderAutoScalingComputeMaxInstanceSize">ProviderAutoScalingComputeMaxInstanceSize</a>" : <i>String</i>,
        "<a href="#providerautoscalingcomputemininstancesize" title="ProviderAutoScalingComputeMinInstanceSize">ProviderAutoScalingComputeMinInstanceSize</a>" : <i>String</i>,
        "<a href="#providerbackupenabled" title="ProviderBackupEnabled">ProviderBackupEnabled</a>" : <i>Boolean</i>,
        "<a href="#providerdiskiops" title="ProviderDiskIops">ProviderDiskIops</a>" : <i>Double</i>,
        "<a href="#providerdisktypename" title="ProviderDiskTypeName">ProviderDiskTypeName</a>" : <i>String</i>,
        "<a href="#providerencryptebsvolume" title="ProviderEncryptEbsVolume">ProviderEncryptEbsVolume</a>" : <i>Boolean</i>,
        "<a href="#providerinstancesizename" title="ProviderInstanceSizeName">ProviderInstanceSizeName</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#providerregionname" title="ProviderRegionName">ProviderRegionName</a>" : <i>String</i>,
        "<a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>" : <i>String</i>,
        "<a href="#replicationfactor" title="ReplicationFactor">ReplicationFactor</a>" : <i>Double</i>,
        "<a href="#advancedconfiguration" title="AdvancedConfiguration">AdvancedConfiguration</a>" : <i>[ <a href="advancedconfigurationdefinition.md">AdvancedConfigurationDefinition</a>, ... ]</i>,
        "<a href="#biconnectorconfig" title="BiConnectorConfig">BiConnectorConfig</a>" : <i>[ <a href="biconnectorconfigdefinition.md">BiConnectorConfigDefinition</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#replicationspecs" title="ReplicationSpecs">ReplicationSpecs</a>" : <i>[ <a href="replicationspecsdefinition.md">ReplicationSpecsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::Cluster
Properties:
    <a href="#autoscalingcomputeenabled" title="AutoScalingComputeEnabled">AutoScalingComputeEnabled</a>: <i>Boolean</i>
    <a href="#autoscalingcomputescaledownenabled" title="AutoScalingComputeScaleDownEnabled">AutoScalingComputeScaleDownEnabled</a>: <i>Boolean</i>
    <a href="#autoscalingdiskgbenabled" title="AutoScalingDiskGbEnabled">AutoScalingDiskGbEnabled</a>: <i>Boolean</i>
    <a href="#backingprovidername" title="BackingProviderName">BackingProviderName</a>: <i>String</i>
    <a href="#backupenabled" title="BackupEnabled">BackupEnabled</a>: <i>Boolean</i>
    <a href="#biconnector" title="BiConnector">BiConnector</a>: <i>
      - <a href="biconnectordefinition.md">BiConnectorDefinition</a></i>
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>String</i>
    <a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
    <a href="#encryptionatrestprovider" title="EncryptionAtRestProvider">EncryptionAtRestProvider</a>: <i>String</i>
    <a href="#mongodbmajorversion" title="MongoDbMajorVersion">MongoDbMajorVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numshards" title="NumShards">NumShards</a>: <i>Double</i>
    <a href="#pitenabled" title="PitEnabled">PitEnabled</a>: <i>Boolean</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#providerautoscalingcomputemaxinstancesize" title="ProviderAutoScalingComputeMaxInstanceSize">ProviderAutoScalingComputeMaxInstanceSize</a>: <i>String</i>
    <a href="#providerautoscalingcomputemininstancesize" title="ProviderAutoScalingComputeMinInstanceSize">ProviderAutoScalingComputeMinInstanceSize</a>: <i>String</i>
    <a href="#providerbackupenabled" title="ProviderBackupEnabled">ProviderBackupEnabled</a>: <i>Boolean</i>
    <a href="#providerdiskiops" title="ProviderDiskIops">ProviderDiskIops</a>: <i>Double</i>
    <a href="#providerdisktypename" title="ProviderDiskTypeName">ProviderDiskTypeName</a>: <i>String</i>
    <a href="#providerencryptebsvolume" title="ProviderEncryptEbsVolume">ProviderEncryptEbsVolume</a>: <i>Boolean</i>
    <a href="#providerinstancesizename" title="ProviderInstanceSizeName">ProviderInstanceSizeName</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#providerregionname" title="ProviderRegionName">ProviderRegionName</a>: <i>String</i>
    <a href="#providervolumetype" title="ProviderVolumeType">ProviderVolumeType</a>: <i>String</i>
    <a href="#replicationfactor" title="ReplicationFactor">ReplicationFactor</a>: <i>Double</i>
    <a href="#advancedconfiguration" title="AdvancedConfiguration">AdvancedConfiguration</a>: <i>
      - <a href="advancedconfigurationdefinition.md">AdvancedConfigurationDefinition</a></i>
    <a href="#biconnectorconfig" title="BiConnectorConfig">BiConnectorConfig</a>: <i>
      - <a href="biconnectorconfigdefinition.md">BiConnectorConfigDefinition</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#replicationspecs" title="ReplicationSpecs">ReplicationSpecs</a>: <i>
      - <a href="replicationspecsdefinition.md">ReplicationSpecsDefinition</a></i>
</pre>

## Properties

#### AutoScalingComputeEnabled

Specifies whether cluster tier auto-scaling is enabled. The default is false.
- Set to `true` to enable cluster tier auto-scaling. If enabled, you must specify a value for `providerSettings.autoScaling.compute.maxInstanceSize`.
- Set to `false` to disable cluster tier auto-scaling.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingComputeScaleDownEnabled

Set to `true` to enable the cluster tier to scale down. This option is only available if `autoScaling.compute.enabled` is `true`.
- If this option is enabled, you must specify a value for `providerSettings.autoScaling.compute.minInstanceSize`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingDiskGbEnabled

Specifies whether disk auto-scaling is enabled. The default is true.
- Set to `true` to enable disk auto-scaling.
- Set to `false` to disable disk auto-scaling.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackingProviderName

Cloud service provider on which the server for a multi-tenant cluster is provisioned.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupEnabled

Legacy Backup - Set to true to enable Atlas legacy backups for the cluster.
**Important** - MongoDB deprecated the Legacy Backup feature. Clusters that use Legacy Backup can continue to use it. MongoDB recommends using [Cloud Backups](https://docs.atlas.mongodb.com/backup/cloud-backup/overview/).
* Any net new Atlas clusters of any type do not support this parameter. These clusters must use Cloud Backup, `provider_backup_enabled`, to enable Cloud Backup.  If you create a new Atlas cluster and set `backup_enabled` to true, the Provider will respond with an error.  This change doesn’t affect existing clusters that use legacy backups.
* Setting this value to false to disable legacy backups for the cluster will let Atlas delete any stored snapshots. In order to preserve the legacy backups snapshots, disable the legacy backups and enable the cloud backups in the single **terraform apply** action.
```
backup_enabled = "false"
provider_backup_enabled = "true"
```
* The default value is false.  M10 and above only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BiConnector

Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See [BI Connector](#bi-connector) below for more details. **DEPRECATED** Use `bi_connector_config` instead.

_Required_: No

_Type_: List of <a href="biconnectordefinition.md">BiConnectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterType

Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

Capacity, in gigabytes, of the host’s root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
* The minimum disk size for dedicated clusters is 10GB for AWS and GCP. If you specify diskSizeGB with a lower disk size, Atlas defaults to the minimum disk size value.
* Note: The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require additional storage space beyond this limitation, consider upgrading your cluster to a higher tier.
* Cannot be used with clusters with local NVMe SSDs
* Cannot be used with Azure clusters.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionAtRestProvider

Possible values are AWS, GCP, AZURE or NONE.  Only needed if you desire to manage the keys, see [Encryption at Rest using Customer Key Management](https://docs.atlas.mongodb.com/security-aws-kms/) for complete documentation.  You must configure encryption at rest for the Atlas project before enabling it on any cluster in the project. For complete documentation on configuring Encryption at Rest, see Encryption at Rest using Customer Key Management. Requires M10 or greater. and for legacy backups, backup_enabled, to be false or omitted. **Note: Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default**.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoDbMajorVersion

Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: `3.6`, `4.0`, or `4.2`. You must set this value to `4.2` if `provider_instance_size_name` is either M2 or M5.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumShards

Selects whether the cluster is a replica set or a sharded cluster. If you use the replicationSpecs parameter, you must set num_shards.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PitEnabled

- Flag that indicates if the cluster uses Continuous Cloud Backup. If set to true, provider_backup_enabled must also be set to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to create the database user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderAutoScalingComputeMaxInstanceSize

Maximum instance size to which your cluster can automatically scale (e.g., M40). Required if `autoScaling.compute.enabled` is `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderAutoScalingComputeMinInstanceSize

Minimum instance size to which your cluster can automatically scale (e.g., M10). Required if `autoScaling.compute.scaleDownEnabled` is `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderBackupEnabled

Flag indicating if the cluster uses Cloud Backup for backups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderDiskIops

The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected `provider_instance_size_name` and `disk_size_gb`.  This setting requires that `provider_instance_size_name` to be M30 or greater and cannot be used with clusters with local NVMe SSDs.  The default value for `provider_disk_iops` is the same as the cluster tier's Standard IOPS value, as viewable in the Atlas console.  It is used in cases where a higher number of IOPS is needed and possible.  If a value is submitted that is lower or equal to the default IOPS value for the cluster tier Atlas ignores the requested value and uses the default.  More details available under the providerSettings.diskIOPS parameter: [MongoDB API Clusters](https://docs.atlas.mongodb.com/reference/api/clusters-create-one/)
* You do not need to configure IOPS for a STANDARD disk configuration but only for a PROVISIONED configuration.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderDiskTypeName

Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P15 - 256GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at https://docs.atlas.mongodb.com/reference/api/clusters-create-one/.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderEncryptEbsVolume

**(Deprecated) The Flag is always true.** Flag that indicates whether the Amazon EBS encryption feature encrypts the host's root volume for both data at rest within the volume and for data moving between the volume and the cluster. Note: This setting is always enabled for clusters with local NVMe SSDs. **Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default.**.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderInstanceSizeName

Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See [Create a Cluster](https://docs.atlas.mongodb.com/reference/api/clusters-create-one/) `providerSettings.instanceSizeName` for valid values and default resources.
**Note** free tier (M0) creation is not supported by the Atlas API and hence not supported by this provider.).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

Cloud service provider on which the servers are provisioned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderRegionName

Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the **Atlas region name**, see the reference list for [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderVolumeType

The type of the volume. The possible values are: `STANDARD` and `PROVISIONED`.  `PROVISIONED` is ONLY required if setting IOPS higher than the default instance IOPS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationFactor

Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedConfiguration

_Required_: No

_Type_: List of <a href="advancedconfigurationdefinition.md">AdvancedConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BiConnectorConfig

_Required_: No

_Type_: List of <a href="biconnectorconfigdefinition.md">BiConnectorConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationSpecs

_Required_: No

_Type_: List of <a href="replicationspecsdefinition.md">ReplicationSpecsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterId

Returns the <code>ClusterId</code> value.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### ContainerId

Returns the <code>ContainerId</code> value.

#### Id

Returns the <code>Id</code> value.

#### MongoDbVersion

Returns the <code>MongoDbVersion</code> value.

#### MongoUri

Returns the <code>MongoUri</code> value.

#### MongoUriUpdated

Returns the <code>MongoUriUpdated</code> value.

#### MongoUriWithOptions

Returns the <code>MongoUriWithOptions</code> value.

#### Paused

Returns the <code>Paused</code> value.

#### ProviderEncryptEbsVolumeFlag

Returns the <code>ProviderEncryptEbsVolumeFlag</code> value.

#### SnapshotBackupPolicy

Returns the <code>SnapshotBackupPolicy</code> value.

#### SrvAddress

Returns the <code>SrvAddress</code> value.

#### StateName

Returns the <code>StateName</code> value.

