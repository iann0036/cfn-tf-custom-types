# TF::FortiOS::SystemReplacemsggroup TrafficQuotaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buffer" title="Buffer">Buffer</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#header" title="Header">Header</a>" : <i>String</i>,
    "<a href="#msgtype" title="MsgType">MsgType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#buffer" title="Buffer">Buffer</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#header" title="Header">Header</a>: <i>String</i>
<a href="#msgtype" title="MsgType">MsgType</a>: <i>String</i>
</pre>

## Properties

#### Buffer

Message string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Format flag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

Header flag. Valid values: `none`, `http`, `8bit`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsgType

Message type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

