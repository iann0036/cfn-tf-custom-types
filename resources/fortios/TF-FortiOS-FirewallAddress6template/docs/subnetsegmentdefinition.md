# TF::FortiOS::FirewallAddress6template SubnetSegmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bits" title="Bits">Bits</a>" : <i>Double</i>,
    "<a href="#exclusive" title="Exclusive">Exclusive</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ <a href="valuesdefinition.md">ValuesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bits" title="Bits">Bits</a>: <i>Double</i>
<a href="#exclusive" title="Exclusive">Exclusive</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#values" title="Values">Values</a>: <i>
      - <a href="valuesdefinition.md">ValuesDefinition</a></i>
</pre>

## Properties

#### Bits

Number of bits.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusive

Enable/disable exclusive value. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Subnet segment ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Subnet segment name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of <a href="valuesdefinition.md">ValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

