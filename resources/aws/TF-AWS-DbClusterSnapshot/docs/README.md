# TF::AWS::DbClusterSnapshot

Manages an RDS database cluster snapshot for Aurora clusters. For managing RDS database instance snapshots, see the [`aws_db_snapshot` resource](/docs/providers/aws/r/db_snapshot.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DbClusterSnapshot",
    "Properties" : {
        "<a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>" : <i>String</i>,
        "<a href="#dbclustersnapshotidentifier" title="DbClusterSnapshotIdentifier">DbClusterSnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DbClusterSnapshot
Properties:
    <a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>: <i>String</i>
    <a href="#dbclustersnapshotidentifier" title="DbClusterSnapshotIdentifier">DbClusterSnapshotIdentifier</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DbClusterIdentifier

The DB Cluster Identifier from which to take the snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterSnapshotIdentifier

The Identifier for the snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the DB cluster. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

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

#### AllocatedStorage

Returns the <code>AllocatedStorage</code> value.

#### AvailabilityZones

Returns the <code>AvailabilityZones</code> value.

#### DbClusterSnapshotArn

Returns the <code>DbClusterSnapshotArn</code> value.

#### Engine

Returns the <code>Engine</code> value.

#### EngineVersion

Returns the <code>EngineVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### KmsKeyId

Returns the <code>KmsKeyId</code> value.

#### LicenseModel

Returns the <code>LicenseModel</code> value.

#### Port

Returns the <code>Port</code> value.

#### SnapshotType

Returns the <code>SnapshotType</code> value.

#### SourceDbClusterSnapshotArn

Returns the <code>SourceDbClusterSnapshotArn</code> value.

#### Status

Returns the <code>Status</code> value.

#### StorageEncrypted

Returns the <code>StorageEncrypted</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

