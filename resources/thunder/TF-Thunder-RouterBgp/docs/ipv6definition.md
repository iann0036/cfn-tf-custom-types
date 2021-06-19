# TF::Thunder::RouterBgp Ipv6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autosummary" title="AutoSummary">AutoSummary</a>" : <i>Double</i>,
    "<a href="#maximumpathsvalue" title="MaximumPathsValue">MaximumPathsValue</a>" : <i>Double</i>,
    "<a href="#originate" title="Originate">Originate</a>" : <i>Double</i>,
    "<a href="#synchronization" title="Synchronization">Synchronization</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#aggregateaddresslist" title="AggregateAddressList">AggregateAddressList</a>" : <i>[ <a href="aggregateaddresslistdefinition.md">AggregateAddressListDefinition</a>, ... ]</i>,
    "<a href="#bgp" title="Bgp">Bgp</a>" : <i>[ <a href="bgpdefinition.md">BgpDefinition</a>, ... ]</i>,
    "<a href="#distance" title="Distance">Distance</a>" : <i>[ <a href="distancedefinition.md">DistanceDefinition</a>, ... ]</i>,
    "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
    "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autosummary" title="AutoSummary">AutoSummary</a>: <i>Double</i>
<a href="#maximumpathsvalue" title="MaximumPathsValue">MaximumPathsValue</a>: <i>Double</i>
<a href="#originate" title="Originate">Originate</a>: <i>Double</i>
<a href="#synchronization" title="Synchronization">Synchronization</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#aggregateaddresslist" title="AggregateAddressList">AggregateAddressList</a>: <i>
      - <a href="aggregateaddresslistdefinition.md">AggregateAddressListDefinition</a></i>
<a href="#bgp" title="Bgp">Bgp</a>: <i>
      - <a href="bgpdefinition.md">BgpDefinition</a></i>
<a href="#distance" title="Distance">Distance</a>: <i>
      - <a href="distancedefinition.md">DistanceDefinition</a></i>
<a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
<a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
</pre>

## Properties

#### AutoSummary

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumPathsValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Originate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Synchronization

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregateAddressList

_Required_: No

_Type_: List of <a href="aggregateaddresslistdefinition.md">AggregateAddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bgp

_Required_: No

_Type_: List of <a href="bgpdefinition.md">BgpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

_Required_: No

_Type_: List of <a href="distancedefinition.md">DistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

