# TF::GoogleBeta::GoogleComputeReservation SpecificReservationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#instanceproperties" title="InstanceProperties">InstanceProperties</a>" : <i>[ <a href="instancepropertiesdefinition.md">InstancePropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#instanceproperties" title="InstanceProperties">InstanceProperties</a>: <i>
      - <a href="instancepropertiesdefinition.md">InstancePropertiesDefinition</a></i>
</pre>

## Properties

#### Count

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProperties

_Required_: No

_Type_: List of <a href="instancepropertiesdefinition.md">InstancePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

