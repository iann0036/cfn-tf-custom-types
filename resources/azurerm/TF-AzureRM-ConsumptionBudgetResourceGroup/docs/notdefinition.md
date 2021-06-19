# TF::AzureRM::ConsumptionBudgetResourceGroup NotDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ <a href="dimensiondefinition.md">DimensionDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - <a href="dimensiondefinition.md">DimensionDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Dimension

_Required_: No

_Type_: List of <a href="dimensiondefinition.md">DimensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

