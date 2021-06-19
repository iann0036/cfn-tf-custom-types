# TF::FortiOS::FirewallInternetservicecustom EntryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
    "<a href="#dst" title="Dst">Dst</a>" : <i>[ <a href="dstdefinition.md">DstDefinition</a>, ... ]</i>,
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>[ <a href="portrangedefinition.md">PortRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
<a href="#dst" title="Dst">Dst</a>: <i>
      - <a href="dstdefinition.md">DstDefinition</a></i>
<a href="#portrange" title="PortRange">PortRange</a>: <i>
      - <a href="portrangedefinition.md">PortRangeDefinition</a></i>
</pre>

## Properties

#### Id

Entry ID(1-255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Integer value for the protocol type as defined by IANA (0 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst

_Required_: No

_Type_: List of <a href="dstdefinition.md">DstDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

_Required_: No

_Type_: List of <a href="portrangedefinition.md">PortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

