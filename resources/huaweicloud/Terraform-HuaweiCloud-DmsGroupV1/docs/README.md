# Terraform::HuaweiCloud::DmsGroupV1

CloudFormation equivalent of huaweicloud_dms_group_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DmsGroupV1",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#availabledeadletters" title="AvailableDeadletters">AvailableDeadletters</a>" : <i>Double</i>,
        "<a href="#availablemessages" title="AvailableMessages">AvailableMessages</a>" : <i>Double</i>,
        "<a href="#consumedmessages" title="ConsumedMessages">ConsumedMessages</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#produceddeadletters" title="ProducedDeadletters">ProducedDeadletters</a>" : <i>Double</i>,
        "<a href="#producedmessages" title="ProducedMessages">ProducedMessages</a>" : <i>Double</i>,
        "<a href="#queueid" title="QueueId">QueueId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DmsGroupV1
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#availabledeadletters" title="AvailableDeadletters">AvailableDeadletters</a>: <i>Double</i>
    <a href="#availablemessages" title="AvailableMessages">AvailableMessages</a>: <i>Double</i>
    <a href="#consumedmessages" title="ConsumedMessages">ConsumedMessages</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#produceddeadletters" title="ProducedDeadletters">ProducedDeadletters</a>: <i>Double</i>
    <a href="#producedmessages" title="ProducedMessages">ProducedMessages</a>: <i>Double</i>
    <a href="#queueid" title="QueueId">QueueId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableDeadletters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableMessages

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsumedMessages

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProducedDeadletters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProducedMessages

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueId

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

Returns the &lt;code&gt;AvailableDeadletters&lt;/code&gt; value.

#### AvailableMessages

Returns the &lt;code&gt;AvailableMessages&lt;/code&gt; value.

#### ConsumedMessages

Returns the &lt;code&gt;ConsumedMessages&lt;/code&gt; value.

#### ProducedDeadletters

Returns the &lt;code&gt;ProducedDeadletters&lt;/code&gt; value.

#### ProducedMessages

Returns the &lt;code&gt;ProducedMessages&lt;/code&gt; value.

