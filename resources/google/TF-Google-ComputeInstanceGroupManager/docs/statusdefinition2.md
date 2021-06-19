# TF::Google::ComputeInstanceGroupManager StatusDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hasstatefulconfig" title="HasStatefulConfig">HasStatefulConfig</a>" : <i>Boolean</i>,
    "<a href="#perinstanceconfigs" title="PerInstanceConfigs">PerInstanceConfigs</a>" : <i>[ <a href="statusdefinition.md">StatusDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hasstatefulconfig" title="HasStatefulConfig">HasStatefulConfig</a>: <i>Boolean</i>
<a href="#perinstanceconfigs" title="PerInstanceConfigs">PerInstanceConfigs</a>: <i>
      - <a href="statusdefinition.md">StatusDefinition</a></i>
</pre>

## Properties

#### HasStatefulConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerInstanceConfigs

_Required_: No

_Type_: List of <a href="statusdefinition.md">StatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

