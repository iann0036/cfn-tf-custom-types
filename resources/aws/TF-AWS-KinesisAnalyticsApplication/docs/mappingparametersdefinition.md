# TF::AWS::KinesisAnalyticsApplication MappingParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#csv" title="Csv">Csv</a>" : <i>[ <a href="csvdefinition.md">CsvDefinition</a>, ... ]</i>,
    "<a href="#json" title="Json">Json</a>" : <i>[ <a href="jsondefinition.md">JsonDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#csv" title="Csv">Csv</a>: <i>
      - <a href="csvdefinition.md">CsvDefinition</a></i>
<a href="#json" title="Json">Json</a>: <i>
      - <a href="jsondefinition.md">JsonDefinition</a></i>
</pre>

## Properties

#### Csv

_Required_: No

_Type_: List of <a href="csvdefinition.md">CsvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Json

_Required_: No

_Type_: List of <a href="jsondefinition.md">JsonDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

