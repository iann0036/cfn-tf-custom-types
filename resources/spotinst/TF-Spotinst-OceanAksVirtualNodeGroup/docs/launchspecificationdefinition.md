# TF::Spotinst::OceanAksVirtualNodeGroup LaunchSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#osdisk" title="OsDisk">OsDisk</a>" : <i>[ <a href="osdiskdefinition.md">OsDiskDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#osdisk" title="OsDisk">OsDisk</a>: <i>
      - <a href="osdiskdefinition.md">OsDiskDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### OsDisk

_Required_: No

_Type_: List of <a href="osdiskdefinition.md">OsDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

