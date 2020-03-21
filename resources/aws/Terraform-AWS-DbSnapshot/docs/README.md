# Terraform::AWS::DbSnapshot

CloudFormation equivalent of aws_db_snapshot

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DbSnapshot",
    "Properties" : {
        "<a href="#dbinstanceidentifier" title="DbInstanceIdentifier">DbInstanceIdentifier</a>" : <i>String</i>,
        "<a href="#dbsnapshotidentifier" title="DbSnapshotIdentifier">DbSnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DbSnapshot
Properties:
    <a href="#dbinstanceidentifier" title="DbInstanceIdentifier">DbInstanceIdentifier</a>: <i>String</i>
    <a href="#dbsnapshotidentifier" title="DbSnapshotIdentifier">DbSnapshotIdentifier</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### DbInstanceIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSnapshotIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

#### AllocatedStorage

Returns the <code>AllocatedStorage</code> value.

#### AvailabilityZone

Returns the <code>AvailabilityZone</code> value.

#### DbSnapshotArn

Returns the <code>DbSnapshotArn</code> value.

#### Encrypted

Returns the <code>Encrypted</code> value.

#### Engine

Returns the <code>Engine</code> value.

#### EngineVersion

Returns the <code>EngineVersion</code> value.

#### Iops

Returns the <code>Iops</code> value.

#### KmsKeyId

Returns the <code>KmsKeyId</code> value.

#### LicenseModel

Returns the <code>LicenseModel</code> value.

#### OptionGroupName

Returns the <code>OptionGroupName</code> value.

#### Port

Returns the <code>Port</code> value.

#### SnapshotType

Returns the <code>SnapshotType</code> value.

#### SourceDbSnapshotIdentifier

Returns the <code>SourceDbSnapshotIdentifier</code> value.

#### SourceRegion

Returns the <code>SourceRegion</code> value.

#### Status

Returns the <code>Status</code> value.

#### StorageType

Returns the <code>StorageType</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

