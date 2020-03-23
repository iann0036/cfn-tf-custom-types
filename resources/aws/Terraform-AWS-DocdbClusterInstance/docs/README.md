# Terraform::AWS::DocdbClusterInstance

Provides an DocDB Cluster Resource Instance. A Cluster Instance Resource defines
attributes that are specific to a single instance in a [DocDB Cluster][1].

You do not designate a primary and subsequent replicas. Instead, you simply add DocDB
Instances and DocDB manages the replication. You can use the [count][3]
meta-parameter to make multiple instances and join them all to the same DocDB
Cluster, or you may specify different Cluster Instance resources with various
`instance_class` sizes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DocdbClusterInstance",
    "Properties" : {
        "<a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>" : <i>Boolean</i>,
        "<a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cacertidentifier" title="CaCertIdentifier">CaCertIdentifier</a>" : <i>String</i>,
        "<a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>" : <i>String</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
        "<a href="#identifierprefix" title="IdentifierPrefix">IdentifierPrefix</a>" : <i>String</i>,
        "<a href="#instanceclass" title="InstanceClass">InstanceClass</a>" : <i>String</i>,
        "<a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>" : <i>String</i>,
        "<a href="#promotiontier" title="PromotionTier">PromotionTier</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DocdbClusterInstance
Properties:
    <a href="#applyimmediately" title="ApplyImmediately">ApplyImmediately</a>: <i>Boolean</i>
    <a href="#autominorversionupgrade" title="AutoMinorVersionUpgrade">AutoMinorVersionUpgrade</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cacertidentifier" title="CaCertIdentifier">CaCertIdentifier</a>: <i>String</i>
    <a href="#clusteridentifier" title="ClusterIdentifier">ClusterIdentifier</a>: <i>String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
    <a href="#identifierprefix" title="IdentifierPrefix">IdentifierPrefix</a>: <i>String</i>
    <a href="#instanceclass" title="InstanceClass">InstanceClass</a>: <i>String</i>
    <a href="#preferredmaintenancewindow" title="PreferredMaintenanceWindow">PreferredMaintenanceWindow</a>: <i>String</i>
    <a href="#promotiontier" title="PromotionTier">PromotionTier</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ApplyImmediately

Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is`false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMinorVersionUpgrade

Indicates that minor engine upgrades will be applied automatically to the DB instance during the maintenance window. Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

The EC2 Availability Zone that the DB instance is created in. See [docs](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_CreateDBInstance.html) about the details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertIdentifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIdentifier

The identifier of the [`aws_docdb_cluster`](/docs/providers/aws/r/docdb_cluster.html) in which to launch this instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

The name of the database engine to be used for the DocDB instance. Defaults to `docdb`. Valid Values: `docdb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identifier

The indentifier for the DocDB instance, if omitted, Terraform will assign a random, unique identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentifierPrefix

Creates a unique identifier beginning with the specified prefix. Conflicts with `identifer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceClass

The instance class to use. For details on CPU and memory, see [Scaling for DocDB Instances][2]. DocDB currently
supports the below instance classes. Please see [AWS Documentation][4] for complete details.
- db.r4.large
- db.r4.xlarge
- db.r4.2xlarge
- db.r4.4xlarge
- db.r4.8xlarge
- db.r4.16xlarge.

_Required_: Yes

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

#### Arn

Returns the <code>Arn</code> value.

#### DbSubnetGroupName

Returns the <code>DbSubnetGroupName</code> value.

#### DbiResourceId

Returns the <code>DbiResourceId</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### EngineVersion

Returns the <code>EngineVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### KmsKeyId

Returns the <code>KmsKeyId</code> value.

#### Port

Returns the <code>Port</code> value.

#### PreferredBackupWindow

Returns the <code>PreferredBackupWindow</code> value.

#### PubliclyAccessible

Returns the <code>PubliclyAccessible</code> value.

#### StorageEncrypted

Returns the <code>StorageEncrypted</code> value.

#### Writer

Returns the <code>Writer</code> value.

