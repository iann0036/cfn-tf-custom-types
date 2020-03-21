# Terraform::HuaweiCloud::DmsGroupV1

Manages a DMS group in the huaweicloud DMS Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DmsGroupV1",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#queueid" title="QueueId">QueueId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DmsGroupV1
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#queueid" title="QueueId">QueueId</a>: <i>String</i>
</pre>

## Properties

#### Name

Indicates the unique name of a group. A string of 1 to 64
characters that contain a-z, A-Z, 0-9, hyphens (-), and underscores (_).
The name cannot be modified once specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueId

Indicates the ID of a specified queue.

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

#### AvailableDeadletters

Returns the <code>AvailableDeadletters</code> value.

#### AvailableMessages

Returns the <code>AvailableMessages</code> value.

#### ConsumedMessages

Returns the <code>ConsumedMessages</code> value.

#### ProducedDeadletters

Returns the <code>ProducedDeadletters</code> value.

#### ProducedMessages

Returns the <code>ProducedMessages</code> value.

