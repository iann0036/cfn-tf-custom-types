# TF::AWS::KinesisAnalyticsApplication InputsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>" : <i>[ <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a>, ... ]</i>,
    "<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>" : <i>[ <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a>, ... ]</i>,
    "<a href="#parallelism" title="Parallelism">Parallelism</a>" : <i>[ <a href="parallelismdefinition.md">ParallelismDefinition</a>, ... ]</i>,
    "<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>" : <i>[ <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#schema" title="Schema">Schema</a>" : <i>[ <a href="schemadefinition.md">SchemaDefinition</a>, ... ]</i>,
    "<a href="#startingpositionconfiguration" title="StartingPositionConfiguration">StartingPositionConfiguration</a>" : <i>[ <a href="startingpositionconfigurationdefinition.md">StartingPositionConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#kinesisfirehose" title="KinesisFirehose">KinesisFirehose</a>: <i>
      - <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a></i>
<a href="#kinesisstream" title="KinesisStream">KinesisStream</a>: <i>
      - <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a></i>
<a href="#parallelism" title="Parallelism">Parallelism</a>: <i>
      - <a href="parallelismdefinition.md">ParallelismDefinition</a></i>
<a href="#processingconfiguration" title="ProcessingConfiguration">ProcessingConfiguration</a>: <i>
      - <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a></i>
<a href="#schema" title="Schema">Schema</a>: <i>
      - <a href="schemadefinition.md">SchemaDefinition</a></i>
<a href="#startingpositionconfiguration" title="StartingPositionConfiguration">StartingPositionConfiguration</a>: <i>
      - <a href="startingpositionconfigurationdefinition.md">StartingPositionConfigurationDefinition</a></i>
</pre>

## Properties

#### NamePrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehose

_Required_: No

_Type_: List of <a href="kinesisfirehosedefinition.md">KinesisFirehoseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStream

_Required_: No

_Type_: List of <a href="kinesisstreamdefinition.md">KinesisStreamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parallelism

_Required_: No

_Type_: List of <a href="parallelismdefinition.md">ParallelismDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessingConfiguration

_Required_: No

_Type_: List of <a href="processingconfigurationdefinition.md">ProcessingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schema

_Required_: No

_Type_: List of <a href="schemadefinition.md">SchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartingPositionConfiguration

_Required_: No

_Type_: List of <a href="startingpositionconfigurationdefinition.md">StartingPositionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

