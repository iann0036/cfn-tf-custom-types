# TF::OCI::ContainerengineNodePool NodeConfigDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#placementconfigs" title="PlacementConfigs">PlacementConfigs</a>" : <i>[ <a href="placementconfigsdefinition.md">PlacementConfigsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#placementconfigs" title="PlacementConfigs">PlacementConfigs</a>: <i>
      - <a href="placementconfigsdefinition.md">PlacementConfigsDefinition</a></i>
</pre>

## Properties

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConfigs

_Required_: No

_Type_: List of <a href="placementconfigsdefinition.md">PlacementConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

