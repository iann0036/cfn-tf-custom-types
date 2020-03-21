# Terraform::HuaweiCloud::DmsQueueV1

CloudFormation equivalent of huaweicloud_dms_queue_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DmsQueueV1",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#maxconsumecount" title="MaxConsumeCount">MaxConsumeCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#queuemode" title="QueueMode">QueueMode</a>" : <i>String</i>,
        "<a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>" : <i>String</i>,
        "<a href="#retentionhours" title="RetentionHours">RetentionHours</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DmsQueueV1
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#maxconsumecount" title="MaxConsumeCount">MaxConsumeCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#queuemode" title="QueueMode">QueueMode</a>: <i>String</i>
    <a href="#redrivepolicy" title="RedrivePolicy">RedrivePolicy</a>: <i>String</i>
    <a href="#retentionhours" title="RetentionHours">RetentionHours</a>: <i>Double</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConsumeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedrivePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### GroupCount

Returns the <code>GroupCount</code> value.

#### MaxMsgSizeByte

Returns the <code>MaxMsgSizeByte</code> value.

#### ProducedMessages

Returns the <code>ProducedMessages</code> value.

#### Reservation

Returns the <code>Reservation</code> value.

