# TF::FortiOS::RouterKeychain KeyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceptlifetime" title="AcceptLifetime">AcceptLifetime</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#keystring" title="KeyString">KeyString</a>" : <i>String</i>,
    "<a href="#sendlifetime" title="SendLifetime">SendLifetime</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acceptlifetime" title="AcceptLifetime">AcceptLifetime</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#keystring" title="KeyString">KeyString</a>: <i>String</i>
<a href="#sendlifetime" title="SendLifetime">SendLifetime</a>: <i>String</i>
</pre>

## Properties

#### AcceptLifetime

Lifetime of received authentication key (format: hh:mm:ss day month year).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Key ID (0 - 2147483647).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyString

Password for the key (max. = 35 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendLifetime

Lifetime of sent authentication key (format: hh:mm:ss day month year).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

