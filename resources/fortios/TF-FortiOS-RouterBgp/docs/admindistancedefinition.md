# TF::FortiOS::RouterBgp AdminDistanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#distance" title="Distance">Distance</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#neighbourprefix" title="NeighbourPrefix">NeighbourPrefix</a>" : <i>String</i>,
    "<a href="#routelist" title="RouteList">RouteList</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#distance" title="Distance">Distance</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#neighbourprefix" title="NeighbourPrefix">NeighbourPrefix</a>: <i>String</i>
<a href="#routelist" title="RouteList">RouteList</a>: <i>String</i>
</pre>

## Properties

#### Distance

Administrative distance to apply (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighbourPrefix

Neighbor address prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteList

Access list of routes to apply new distance to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

