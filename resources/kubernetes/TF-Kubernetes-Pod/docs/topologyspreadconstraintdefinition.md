# TF::Kubernetes::Pod TopologySpreadConstraintDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxskew" title="MaxSkew">MaxSkew</a>" : <i>Double</i>,
    "<a href="#topologykey" title="TopologyKey">TopologyKey</a>" : <i>String</i>,
    "<a href="#whenunsatisfiable" title="WhenUnsatisfiable">WhenUnsatisfiable</a>" : <i>String</i>,
    "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ <a href="labelselectordefinition.md">LabelSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxskew" title="MaxSkew">MaxSkew</a>: <i>Double</i>
<a href="#topologykey" title="TopologyKey">TopologyKey</a>: <i>String</i>
<a href="#whenunsatisfiable" title="WhenUnsatisfiable">WhenUnsatisfiable</a>: <i>String</i>
<a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - <a href="labelselectordefinition.md">LabelSelectorDefinition</a></i>
</pre>

## Properties

#### MaxSkew

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhenUnsatisfiable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of <a href="labelselectordefinition.md">LabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

