# Terraform::AWS::ElasticacheReplicationGroup

CloudFormation equivalent of aws_elasticache_replication_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElasticacheReplicationGroup",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#atrestencryptionenabled" title="AtRestEncryptionEnabled">AtRestEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#authtoken" title="AuthToken">AuthToken</a>" : <i>String</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#automaticfailoverenabled" title="AutomaticFailoverEnabled">AutomaticFailoverEnabled</a>" : <i>Boolean</i>,
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>String</i>,
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#transitencryptionenabled" title="TransitEncryptionEnabled">TransitEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#clustermode" title="ClusterMode">ClusterMode</a>" : <i>[ <a href="clustermode.md">ClusterMode</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElasticacheReplicationGroup
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
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>String</i>
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
      - <a href="tags.md">Tags</a></i>
    <a href="#transitencryptionenabled" title="TransitEncryptionEnabled">TransitEncryptionEnabled</a>: <i>Boolean</i>
    <a href="#clustermode" title="ClusterMode">ClusterMode</a>: <i>
      - <a href="clustermode.md">ClusterMode</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApplyImmediately

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtRestEncryptionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticFailoverEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberCacheClusters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParameterGroupName

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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotRetentionLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitEncryptionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMode

_Required_: No

_Type_: List of <a href="clustermode.md">ClusterMode</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConfigurationEndpointAddress

Returns the <code>ConfigurationEndpointAddress</code> value.

#### Id

Returns the <code>Id</code> value.

#### MemberClusters

Returns the <code>MemberClusters</code> value.

#### PrimaryEndpointAddress

Returns the <code>PrimaryEndpointAddress</code> value.

