# TF::FortiOS::RouterBgp NeighborRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#maxneighbornum" title="MaxNeighborNum">MaxNeighborNum</a>" : <i>Double</i>,
    "<a href="#neighborgroup" title="NeighborGroup">NeighborGroup</a>" : <i>[ <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a>, ... ]</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#maxneighbornum" title="MaxNeighborNum">MaxNeighborNum</a>: <i>Double</i>
<a href="#neighborgroup" title="NeighborGroup">NeighborGroup</a>: <i>
      - <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a></i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
</pre>

## Properties

#### Id

Neighbor range ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNeighborNum

Maximum number of neighbors.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborGroup

_Required_: No

_Type_: List of <a href="neighborgroupdefinition.md">NeighborGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Neighbor range prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

