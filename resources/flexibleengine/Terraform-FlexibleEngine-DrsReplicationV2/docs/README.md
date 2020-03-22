# Terraform::FlexibleEngine::DrsReplicationV2

Manages a V2 replication resource within FlexibleEngine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::DrsReplicationV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#prioritystation" title="PriorityStation">PriorityStation</a>" : <i>String</i>,
        "<a href="#replicationmodel" title="ReplicationModel">ReplicationModel</a>" : <i>String</i>,
        "<a href="#volumeids" title="VolumeIds">VolumeIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::DrsReplicationV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#prioritystation" title="PriorityStation">PriorityStation</a>: <i>String</i>
    <a href="#replicationmodel" title="ReplicationModel">ReplicationModel</a>: <i>String</i>
    <a href="#volumeids" title="VolumeIds">VolumeIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

The description of the EVS replication pair. The description can contain a maximum of 255 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the EVS replication pair. The name can contain a maximum of 255 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityStation

The primary AZ of the EVS replication pair. That is the AZ where the production disk belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationModel

The type of the EVS replication pair. Currently only type hypermetro is supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeIds

An array of one or more IDs of the EVS disks used to create the EVS replication pair.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### FailureDetail

Returns the <code>FailureDetail</code> value.

#### FaultLevel

Returns the <code>FaultLevel</code> value.

#### Id

Returns the <code>Id</code> value.

#### Progress

Returns the <code>Progress</code> value.

#### RecordMetadata

Returns the <code>RecordMetadata</code> value.

#### ReplicationConsistencyGroupId

Returns the <code>ReplicationConsistencyGroupId</code> value.

#### ReplicationStatus

Returns the <code>ReplicationStatus</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

