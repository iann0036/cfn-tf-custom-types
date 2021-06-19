# TF::AWS::Kinesisanalyticsv2ApplicationSnapshot

Manages a Kinesis Analytics v2 Application Snapshot.
Snapshots are the AWS implementation of [Flink Savepoints](https://ci.apache.org/projects/flink/flink-docs-release-1.11/ops/state/savepoints.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Kinesisanalyticsv2ApplicationSnapshot",
    "Properties" : {
        "<a href="#applicationname" title="ApplicationName">ApplicationName</a>" : <i>String</i>,
        "<a href="#snapshotname" title="SnapshotName">SnapshotName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Kinesisanalyticsv2ApplicationSnapshot
Properties:
    <a href="#applicationname" title="ApplicationName">ApplicationName</a>: <i>String</i>
    <a href="#snapshotname" title="SnapshotName">SnapshotName</a>: <i>String</i>
</pre>

## Properties

#### ApplicationName

The name of an existing  [Kinesis Analytics v2 Application](/docs/providers/aws/r/kinesisanalyticsv2_application.html). Note that the application must be running for a snapshot to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotName

The name of the application snapshot.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApplicationVersionId

Returns the <code>ApplicationVersionId</code> value.

#### Id

Returns the <code>Id</code> value.

#### SnapshotCreationTimestamp

Returns the <code>SnapshotCreationTimestamp</code> value.

