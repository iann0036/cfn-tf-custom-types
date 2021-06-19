# TF::AVI::Image SeInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hash" title="Hash">Hash</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#build" title="Build">Build</a>" : <i>[ <a href="builddefinition.md">BuildDefinition</a>, ... ]</i>,
    "<a href="#patch" title="Patch">Patch</a>" : <i>[ <a href="patchdefinition.md">PatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hash" title="Hash">Hash</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#build" title="Build">Build</a>: <i>
      - <a href="builddefinition.md">BuildDefinition</a></i>
<a href="#patch" title="Patch">Patch</a>: <i>
      - <a href="patchdefinition.md">PatchDefinition</a></i>
</pre>

## Properties

#### Hash

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Build

_Required_: No

_Type_: List of <a href="builddefinition.md">BuildDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Patch

_Required_: No

_Type_: List of <a href="patchdefinition.md">PatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

