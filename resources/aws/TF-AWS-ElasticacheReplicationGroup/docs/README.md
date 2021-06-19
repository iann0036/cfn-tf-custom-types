# TF::AWS::ElasticacheReplicationGroup

Provides an ElastiCache Replication Group resource.

For working with a [Memcached cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html) or a
[single-node Redis instance (Cluster Mode Disabled)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html),
see the [`aws_elasticache_cluster` resource](/docs/providers/aws/r/elasticache_cluster.html).

~> **Note:** When you change an attribute, such as `engine_version`, by
default the ElastiCache API applies it in the next maintenance window. Because
of this, Terraform may report a difference in its planning phase because the
actual modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change
immediately. Using `apply_immediately` can result in a brief downtime as
servers reboots.
See the AWS Documentation on
[Modifying an ElastiCache Cache Cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Modify.html)
for more information.

~> **...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElasticacheReplicationGroup",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#atrestencryptionenabled" title="AtRestEncryptionEnabled">AtRestEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#authtoken" title="AuthToken">AuthToken</a>" : <i>String</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#automaticfailoverenabled" title="AutomaticFailoverEnabled">AutomaticFailoverEnabled</a>" : <i>Boolean</i>,
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#finalsnapshotidentifier" title="FinalSnapshotIdentifier">FinalSnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#globalreplicationgroupid" title="GlobalReplicationGroupId">GlobalReplicationGroupId</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>String</i>,
        "<a href="#multiazenabled" title="MultiAzEnabled">MultiAzEnabled</a>" : <i>Boolean</i>,
        "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
        "<a href="#notificationtopicarn" title="NotificationTopicArn">NotificationTopicArn</a>" : <i>String</i>,
        "<a href="#numbercacheclusters" title="NumberCacheClusters">NumberCacheClusters</a>" : <i>Double</i>,
        "<a href="#parametergroupname" title="ParameterGroupName">ParameterGroupName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#replicationgroupdescription" title="ReplicationGroupDescription">ReplicationGroupDescription</a>" : <i>String</i>,
        "<a href="#replicationgroupid" title="ReplicationGroupId">ReplicationGroupId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#snapshotarns" title="SnapshotArns">SnapshotArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>,
        "<a href="#snapshotretentionlimit" title="SnapshotRetentionLimit">SnapshotRetentionLimit</a>" : <i>Double</i>,
        "<a href="#snapshotwindow" title="SnapshotWindow">SnapshotWindow</a>" : <i>String</i>,
        "<a href="#subnetgroupname" title="SubnetGroupName">SubnetGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#transitencryptionenabled" title="TransitEncryptionEnabled">TransitEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#clustermode" title="ClusterMode">ClusterMode</a>" : <i>[ <a href="clustermodedefinition.md">ClusterModeDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElasticacheReplicationGroup
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#atrestencryptionenabled" title="AtRestEncryptionEnabled">AtRestEncryptionEnabled</a>: <i>Boolean</i>
    <a href="#authtoken" title="AuthToken">AuthToken</a>: <i>String</i>
    <a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>: <i>Boolean</i>
    <a href="#automaticfailoverenabled" title="AutomaticFailoverEnabled">AutomaticFailoverEnabled</a>: <i>Boolean</i>
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#finalsnapshotidentifier" title="FinalSnapshotIdentifier">FinalSnapshotIdentifier</a>: <i>String</i>
    <a href="#globalreplicationgroupid" title="GlobalReplicationGroupId">GlobalReplicationGroupId</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>String</i>
    <a href="#multiazenabled" title="MultiAzEnabled">MultiAzEnabled</a>: <i>Boolean</i>
    <a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
    <a href="#notificationtopicarn" title="NotificationTopicArn">NotificationTopicArn</a>: <i>String</i>
    <a href="#numbercacheclusters" title="NumberCacheClusters">NumberCacheClusters</a>: <i>Double</i>
    <a href="#parametergroupname" title="ParameterGroupName">ParameterGroupName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#replicationgroupdescription" title="ReplicationGroupDescription">ReplicationGroupDescription</a>: <i>String</i>
    <a href="#replicationgroupid" title="ReplicationGroupId">ReplicationGroupId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>: <i>
      - String</i>
    <a href="#snapshotarns" title="SnapshotArns">SnapshotArns</a>: <i>
      - String</i>
    <a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
    <a href="#snapshotretentionlimit" title="SnapshotRetentionLimit">SnapshotRetentionLimit</a>: <i>Double</i>
    <a href="#snapshotwindow" title="SnapshotWindow">SnapshotWindow</a>: <i>String</i>
    <a href="#subnetgroupname" title="SubnetGroupName">SubnetGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#transitencryptionenabled" title="TransitEncryptionEnabled">TransitEncryptionEnabled</a>: <i>Boolean</i>
    <a href="#clustermode" title="ClusterMode">ClusterMode</a>: <i>
      - <a href="clustermodedefinition.md">ClusterModeDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtRestEncryptionEnabled

Whether to enable encryption at rest.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthToken

The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. This parameter is currently not supported by the AWS API. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticFailoverEnabled

Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If enabled, `number_cache_clusters` must be greater than 1. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

The name of the cache engine to be used for the clusters in this replication group. The only valid value is `redis`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

The version number of the cache engine to be used for the cache clusters in this replication group. If the version is 6 or higher, only the major version can be set, e.g. `6.x`, otherwise, specify the full version desired, e.g. `5.0.6`. The actual engine version used is returned in the attribute `engine_version_actual`, [defined below](#engine_version_actual).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FinalSnapshotIdentifier

The name of your final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster. If omitted, no final snapshot will be made.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalReplicationGroupId

The ID of the global replication group to which this replication group should belong. If this parameter is specified, the replication group is added to the specified global replication group as a secondary replication group; otherwise, the replication group is not part of any global replication group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if `at_rest_encryption_enabled = true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiAzEnabled

Specifies whether to enable Multi-AZ Support for the replication group. If `true`, `automatic_failover_enabled` must also be enabled. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

The instance class to be used. See AWS documentation for information on [supported node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html) and [guidance on selecting node types](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/nodes-select-size.html). Required unless `global_replication_group_id` is set. Cannot be set if `global_replication_group_id` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberCacheClusters

The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications. One of `number_cache_clusters` or `cluster_mode` is required.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterGroupName

The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used. To enable "cluster mode", i.e. data sharding, use a parameter group that has the parameter `cluster-enabled` set to true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationGroupDescription

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupNames

A list of cache security group names to associate with this replication group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotRetentionLimit

The number of days for which ElastiCache will retain automatic cache cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off. Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro cache nodes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotWindow

The daily time range (in UTC) during which ElastiCache will begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetGroupName

The name of the cache subnet group to be used for the replication group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. Adding tags to this resource will add or overwrite any existing tags on the clusters in the replication group and not to the group itself. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitEncryptionEnabled

Whether to enable encryption in transit.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMode

_Required_: No

_Type_: List of <a href="clustermodedefinition.md">ClusterModeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ClusterEnabled

Returns the <code>ClusterEnabled</code> value.

#### ConfigurationEndpointAddress

Returns the <code>ConfigurationEndpointAddress</code> value.

#### EngineVersionActual

Returns the <code>EngineVersionActual</code> value.

#### Id

Returns the <code>Id</code> value.

#### MemberClusters

Returns the <code>MemberClusters</code> value.

#### PrimaryEndpointAddress

Returns the <code>PrimaryEndpointAddress</code> value.

#### ReaderEndpointAddress

Returns the <code>ReaderEndpointAddress</code> value.

