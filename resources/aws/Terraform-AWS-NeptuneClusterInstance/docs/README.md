# Terraform::AWS::NeptuneClusterInstance

A Cluster Instance Resource defines attributes that are specific to a single instance in a Neptune Cluster.

You can simply add neptune instances and Neptune manages the replication. You can use the [count][1]
meta-parameter to make multiple instances and join them all to the same Neptune Cluster, or you may specify different Cluster Instance resources with various `instance_class` sizes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::NeptuneClusterInstance",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>" : <i>String</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
        "<a href="#identifierprefix" title="IdentifierPrefix">IdentifierPrefix</a>" : <i>String</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#neptuneparametergroupname" title="NeptuneParameterGroupName">NeptuneParameterGroupName</a>" : <i>String</i>,
        "<a href="#neptunesubnetgroupname" title="NeptuneSubnetGroupName">NeptuneSubnetGroupName</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#preferredbackupwindow" title="PreferredBackupWindow">PreferredBackupWindow</a>" : <i>String</i>,
        "<a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>" : <i>String</i>,
        "<a href="#promotiontier" title="PromotionTier">PromotionTier</a>" : <i>Double</i>,
        "<a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::NeptuneClusterInstance
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>: <i>String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
    <a href="#identifierprefix" title="IdentifierPrefix">IdentifierPrefix</a>: <i>String</i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#neptuneparametergroupname" title="NeptuneParameterGroupName">NeptuneParameterGroupName</a>: <i>String</i>
    <a href="#neptunesubnetgroupname" title="NeptuneSubnetGroupName">NeptuneSubnetGroupName</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#preferredbackupwindow" title="PreferredBackupWindow">PreferredBackupWindow</a>: <i>String</i>
    <a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>: <i>String</i>
    <a href="#promotiontier" title="PromotionTier">PromotionTier</a>: <i>Double</i>
    <a href="#publiclyaccessible" title="PubliclyAccessible">PubliclyAccessible</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any instance modifications
are applied immediately, or during the next maintenance window. Default is`false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

Indicates that minor engine upgrades will be applied automatically to the instance during the maintenance window. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

The EC2 Availability Zone that the neptune instance is created in.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIdentifier

The identifier of the [`aws_neptune_cluster`](/docs/providers/aws/r/neptune_cluster.html) in which to launch this instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

The name of the database engine to be used for the neptune instance. Defaults to `neptune`. Valid Values: `neptune`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

The neptune engine version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

The indentifier for the neptune instance, if omitted, Terraform will assign a random, unique identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentifierPrefix

Creates a unique identifier beginning with the specified prefix. Conflicts with `identifier`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

The instance class to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeptuneParameterGroupName

The name of the neptune parameter group to associate with this instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeptuneSubnetGroupName

A subnet group to associate with this neptune instance. **NOTE:** This must match the `neptune_subnet_group_name` of the attached [`aws_neptune_cluster`](/docs/providers/aws/r/neptune_cluster.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port on which the DB accepts connections. Defaults to `8182`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupWindow

The daily time range during which automated backups are created if automated backups are enabled. Eg: "04:00-09:00".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredMaintenanceWindow

The window to perform maintenance in.
Syntax: "ddd:hh24:mi-ddd:hh24:mi". Eg: "Mon:00:00-Mon:03:00".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PromotionTier

Default 0. Failover Priority setting on instance level. The reader who has lower tier has higher priority to get promoter to writer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PubliclyAccessible

Bool to control if instance is publicly accessible. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the instance.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Address

Returns the <code>Address</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### DbiResourceId

Returns the <code>DbiResourceId</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### KmsKeyArn

Returns the <code>KmsKeyArn</code> value.

#### StorageEncrypted

Returns the <code>StorageEncrypted</code> value.

#### Writer

Returns the <code>Writer</code> value.

