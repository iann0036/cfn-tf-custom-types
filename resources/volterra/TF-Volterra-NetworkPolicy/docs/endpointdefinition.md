# TF::Volterra::NetworkPolicy EndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#any" title="Any">Any</a>" : <i>Boolean</i>,
    "<a href="#insideendpoints" title="InsideEndpoints">InsideEndpoints</a>" : <i>Boolean</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#outsideendpoints" title="OutsideEndpoints">OutsideEndpoints</a>" : <i>Boolean</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ <a href="labelselectordefinition.md">LabelSelectorDefinition</a>, ... ]</i>,
    "<a href="#prefixlist" title="PrefixList">PrefixList</a>" : <i>[ <a href="prefixlistdefinition.md">PrefixListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#any" title="Any">Any</a>: <i>Boolean</i>
<a href="#insideendpoints" title="InsideEndpoints">InsideEndpoints</a>: <i>Boolean</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#outsideendpoints" title="OutsideEndpoints">OutsideEndpoints</a>: <i>Boolean</i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - <a href="labelselectordefinition.md">LabelSelectorDefinition</a></i>
<a href="#prefixlist" title="PrefixList">PrefixList</a>: <i>
      - <a href="prefixlistdefinition.md">PrefixListDefinition</a></i>
</pre>

## Properties

#### Any

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideEndpoints

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideEndpoints

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of <a href="labelselectordefinition.md">LabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixList

_Required_: No

_Type_: List of <a href="prefixlistdefinition.md">PrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

