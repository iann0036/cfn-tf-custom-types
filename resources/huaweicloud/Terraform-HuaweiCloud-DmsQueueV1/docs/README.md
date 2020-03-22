# Terraform::HuaweiCloud::DmsQueueV1

Manages a DMS queue in the huaweicloud DMS Service.

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

Indicates the basic information about a queue. The queue
description must be 0 to 160 characters in length, and does not contain angle
brackets (<) and (>).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConsumeCount

This parameter is mandatory only when redrive_policy is
set to enable. This parameter indicates the maximum number of allowed message consumption
failures. When a message fails to be consumed after the number of consumption attempts of
this message reaches this value, DMS stores this message into the dead letter queue.
The max_consume_count value range is 1–100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Indicates the unique name of a queue. A string of 1 to 64
characters that contain a-z, A-Z, 0-9, hyphens (-), and underscores (_).
The name cannot be modified once specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueMode

Indicates the queue type. It only support 'NORMAL' and 'FIFO'.
NORMAL: Standard queue. Best-effort ordering. Messages might be retrieved in an order
different from which they were sent. Select standard queues when throughput is important.
FIFO: First-ln-First-out (FIFO) queue. FIFO delivery. Messages are retrieved in the
order they were sent. Select FIFO queues when the order of messages is important.
Default value: NORMAL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedrivePolicy

Indicates whether to enable dead letter messages.
Dead letter messages indicate messages that cannot be normally consumed.
The redrive_policy should be set to 'enable' or 'disable'. The default value is 'disable'.

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

#### Id

Returns the <code>Id</code> value.

#### MaxMsgSizeByte

Returns the <code>MaxMsgSizeByte</code> value.

#### ProducedMessages

Returns the <code>ProducedMessages</code> value.

#### Reservation

Returns the <code>Reservation</code> value.

