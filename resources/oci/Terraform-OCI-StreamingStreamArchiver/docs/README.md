# Terraform::OCI::StreamingStreamArchiver

This resource provides the Stream Archiver resource in Oracle Cloud Infrastructure Streaming service.

Starts the provisioning of a new stream archiver.
To track the progress of the provisioning, you can periodically call [GetArchiver](https://docs.cloud.oracle.com/iaas/api/#/en/streaming/20180418/Stream/GetArchiver).
In the response, the `lifecycleState` parameter of the [Stream](https://docs.cloud.oracle.com/iaas/api/#/en/streaming/20180418/Archiver) object tells you its current state.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::StreamingStreamArchiver",
    "Properties" : {
        "<a href="#batchrolloversizeinmbs" title="BatchRolloverSizeInMbs">BatchRolloverSizeInMbs</a>" : <i>Double</i>,
        "<a href="#batchrollovertimeinseconds" title="BatchRolloverTimeInSeconds">BatchRolloverTimeInSeconds</a>" : <i>Double</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#startposition" title="StartPosition">StartPosition</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#streamid" title="StreamId">StreamId</a>" : <i>String</i>,
        "<a href="#useexistingbucket" title="UseExistingBucket">UseExistingBucket</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::StreamingStreamArchiver
Properties:
    <a href="#batchrolloversizeinmbs" title="BatchRolloverSizeInMbs">BatchRolloverSizeInMbs</a>: <i>Double</i>
    <a href="#batchrollovertimeinseconds" title="BatchRolloverTimeInSeconds">BatchRolloverTimeInSeconds</a>: <i>Double</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#startposition" title="StartPosition">StartPosition</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#streamid" title="StreamId">StreamId</a>: <i>String</i>
    <a href="#useexistingbucket" title="UseExistingBucket">UseExistingBucket</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BatchRolloverSizeInMbs

(Updatable) The batch rollover size in megabytes.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BatchRolloverTimeInSeconds

(Updatable) The rollover time in seconds.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

(Updatable) The name of the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPosition

(Updatable) The start message.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

(Updatable) The target state for the instance pool. Could be set to RUNNING or STOPPED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamId

The OCID of the stream.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExistingBucket

(Updatable) The flag to create a new bucket or use existing one.

_Required_: Yes

_Type_: Boolean

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

#### Error

Returns the <code>Error</code> value.

#### Id

Returns the <code>Id</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

