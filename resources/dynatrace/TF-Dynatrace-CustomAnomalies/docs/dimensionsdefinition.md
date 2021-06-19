# TF::Dynatrace::CustomAnomalies DimensionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ <a href="dimensiondefinition.md">DimensionDefinition</a>, ... ]</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>[ <a href="entitydefinition.md">EntityDefinition</a>, ... ]</i>,
    "<a href="#string" title="String">String</a>" : <i>[ <a href="stringdefinition.md">StringDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - <a href="dimensiondefinition.md">DimensionDefinition</a></i>
<a href="#entity" title="Entity">Entity</a>: <i>
      - <a href="entitydefinition.md">EntityDefinition</a></i>
<a href="#string" title="String">String</a>: <i>
      - <a href="stringdefinition.md">StringDefinition</a></i>
</pre>

## Properties

#### Dimension

_Required_: No

_Type_: List of <a href="dimensiondefinition.md">DimensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No

_Type_: List of <a href="entitydefinition.md">EntityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### String

_Required_: No

_Type_: List of <a href="stringdefinition.md">StringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

