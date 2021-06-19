# TF::Thunder::RouterOspf DistanceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#distancevalue" title="DistanceValue">DistanceValue</a>" : <i>Double</i>,
    "<a href="#distanceospf" title="DistanceOspf">DistanceOspf</a>" : <i>[ <a href="distanceospfdefinition.md">DistanceOspfDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#distancevalue" title="DistanceValue">DistanceValue</a>: <i>Double</i>
<a href="#distanceospf" title="DistanceOspf">DistanceOspf</a>: <i>
      - <a href="distanceospfdefinition.md">DistanceOspfDefinition</a></i>
</pre>

## Properties

#### DistanceValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceOspf

_Required_: No

_Type_: List of <a href="distanceospfdefinition.md">DistanceOspfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

