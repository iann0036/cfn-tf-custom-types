# TF::Volterra::K8sClusterRole ResourceListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apigroups" title="ApiGroups">ApiGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#resourceinstances" title="ResourceInstances">ResourceInstances</a>" : <i>[ String, ... ]</i>,
    "<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#verbs" title="Verbs">Verbs</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apigroups" title="ApiGroups">ApiGroups</a>: <i>
      - String</i>
<a href="#resourceinstances" title="ResourceInstances">ResourceInstances</a>: <i>
      - String</i>
<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>: <i>
      - String</i>
<a href="#verbs" title="Verbs">Verbs</a>: <i>
      - String</i>
</pre>

## Properties

#### ApiGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceInstances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Verbs

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

