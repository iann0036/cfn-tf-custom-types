# TF::FortiOS::RouterOspf RangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertise" title="Advertise">Advertise</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#substitute" title="Substitute">Substitute</a>" : <i>String</i>,
    "<a href="#substitutestatus" title="SubstituteStatus">SubstituteStatus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#advertise" title="Advertise">Advertise</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#substitute" title="Substitute">Substitute</a>: <i>String</i>
<a href="#substitutestatus" title="SubstituteStatus">SubstituteStatus</a>: <i>String</i>
</pre>

## Properties

#### Advertise

Enable/disable advertise status. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Range entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Substitute

Substitute prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubstituteStatus

Enable/disable substitute status. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

