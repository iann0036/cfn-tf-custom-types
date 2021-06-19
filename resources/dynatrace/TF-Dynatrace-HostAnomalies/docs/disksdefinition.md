# TF::Dynatrace::HostAnomalies DisksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inodes" title="Inodes">Inodes</a>" : <i>[ <a href="inodesdefinition.md">InodesDefinition</a>, ... ]</i>,
    "<a href="#space" title="Space">Space</a>" : <i>[ <a href="spacedefinition.md">SpaceDefinition</a>, ... ]</i>,
    "<a href="#speed" title="Speed">Speed</a>" : <i>[ <a href="speeddefinition.md">SpeedDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inodes" title="Inodes">Inodes</a>: <i>
      - <a href="inodesdefinition.md">InodesDefinition</a></i>
<a href="#space" title="Space">Space</a>: <i>
      - <a href="spacedefinition.md">SpaceDefinition</a></i>
<a href="#speed" title="Speed">Speed</a>: <i>
      - <a href="speeddefinition.md">SpeedDefinition</a></i>
</pre>

## Properties

#### Inodes

_Required_: No

_Type_: List of <a href="inodesdefinition.md">InodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

_Required_: No

_Type_: List of <a href="spacedefinition.md">SpaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Speed

_Required_: No

_Type_: List of <a href="speeddefinition.md">SpeedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

