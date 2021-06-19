# TF::GoogleBeta::GoogleComputeInstanceGroupManager StatusDefinition4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isstable" title="IsStable">IsStable</a>" : <i>Boolean</i>,
    "<a href="#stateful" title="Stateful">Stateful</a>" : <i>[ <a href="statusdefinition2.md">StatusDefinition2</a>, ... ]</i>,
    "<a href="#versiontarget" title="VersionTarget">VersionTarget</a>" : <i>[ <a href="statusdefinition3.md">StatusDefinition3</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isstable" title="IsStable">IsStable</a>: <i>Boolean</i>
<a href="#stateful" title="Stateful">Stateful</a>: <i>
      - <a href="statusdefinition2.md">StatusDefinition2</a></i>
<a href="#versiontarget" title="VersionTarget">VersionTarget</a>: <i>
      - <a href="statusdefinition3.md">StatusDefinition3</a></i>
</pre>

## Properties

#### IsStable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

_Required_: No

_Type_: List of <a href="statusdefinition2.md">StatusDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionTarget

_Required_: No

_Type_: List of <a href="statusdefinition3.md">StatusDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

