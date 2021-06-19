# TF::Thunder::SnmpServerEnableTraps RoutingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bgp" title="Bgp">Bgp</a>" : <i>[ <a href="bgpdefinition.md">BgpDefinition</a>, ... ]</i>,
    "<a href="#isis" title="Isis">Isis</a>" : <i>[ <a href="isisdefinition.md">IsisDefinition</a>, ... ]</i>,
    "<a href="#ospf" title="Ospf">Ospf</a>" : <i>[ <a href="ospfdefinition.md">OspfDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bgp" title="Bgp">Bgp</a>: <i>
      - <a href="bgpdefinition.md">BgpDefinition</a></i>
<a href="#isis" title="Isis">Isis</a>: <i>
      - <a href="isisdefinition.md">IsisDefinition</a></i>
<a href="#ospf" title="Ospf">Ospf</a>: <i>
      - <a href="ospfdefinition.md">OspfDefinition</a></i>
</pre>

## Properties

#### Bgp

_Required_: No

_Type_: List of <a href="bgpdefinition.md">BgpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isis

_Required_: No

_Type_: List of <a href="isisdefinition.md">IsisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf

_Required_: No

_Type_: List of <a href="ospfdefinition.md">OspfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

