# TF::AWS::Kinesisanalyticsv2Application InputDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
    "<a href="#inputparallelism" title="InputParallelism">InputParallelism</a>" : <i>[ <a href="inputparallelismdefinition.md">InputParallelismDefinition</a>, ... ]</i>,
    "<a href="#inputprocessingconfiguration" title="InputProcessingConfiguration">InputProcessingConfiguration</a>" : <i>[ <a href="inputprocessingconfigurationdefinition.md">InputProcessingConfigurationDefinition</a>, ... ]</i>,
    "<a href="#inputschema" title="InputSchema">InputSchema</a>" : <i>[ <a href="inputschemadefinition.md">InputSchemaDefinition</a>, ... ]</i>,
    "<a href="#inputstartingpositionconfiguration" title="InputStartingPositionConfiguration">InputStartingPositionConfiguration</a>" : <i>[ <a href="inputstartingpositionconfigurationdefinition.md">InputStartingPositionConfigurationDefinition</a>, ... ]</i>,
    "<a href="#kinesisfirehoseinput" title="KinesisFirehoseInput">KinesisFirehoseInput</a>" : <i>[ <a href="kinesisfirehoseinputdefinition.md">KinesisFirehoseInputDefinition</a>, ... ]</i>,
    "<a href="#kinesisstreamsinput" title="KinesisStreamsInput">KinesisStreamsInput</a>" : <i>[ <a href="kinesisstreamsinputdefinition.md">KinesisStreamsInputDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
<a href="#inputparallelism" title="InputParallelism">InputParallelism</a>: <i>
      - <a href="inputparallelismdefinition.md">InputParallelismDefinition</a></i>
<a href="#inputprocessingconfiguration" title="InputProcessingConfiguration">InputProcessingConfiguration</a>: <i>
      - <a href="inputprocessingconfigurationdefinition.md">InputProcessingConfigurationDefinition</a></i>
<a href="#inputschema" title="InputSchema">InputSchema</a>: <i>
      - <a href="inputschemadefinition.md">InputSchemaDefinition</a></i>
<a href="#inputstartingpositionconfiguration" title="InputStartingPositionConfiguration">InputStartingPositionConfiguration</a>: <i>
      - <a href="inputstartingpositionconfigurationdefinition.md">InputStartingPositionConfigurationDefinition</a></i>
<a href="#kinesisfirehoseinput" title="KinesisFirehoseInput">KinesisFirehoseInput</a>: <i>
      - <a href="kinesisfirehoseinputdefinition.md">KinesisFirehoseInputDefinition</a></i>
<a href="#kinesisstreamsinput" title="KinesisStreamsInput">KinesisStreamsInput</a>: <i>
      - <a href="kinesisstreamsinputdefinition.md">KinesisStreamsInputDefinition</a></i>
</pre>

## Properties

#### NamePrefix

The name prefix to use when creating an in-application stream.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputParallelism

_Required_: No

_Type_: List of <a href="inputparallelismdefinition.md">InputParallelismDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputProcessingConfiguration

_Required_: No

_Type_: List of <a href="inputprocessingconfigurationdefinition.md">InputProcessingConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputSchema

_Required_: No

_Type_: List of <a href="inputschemadefinition.md">InputSchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputStartingPositionConfiguration

_Required_: No

_Type_: List of <a href="inputstartingpositionconfigurationdefinition.md">InputStartingPositionConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehoseInput

_Required_: No

_Type_: List of <a href="kinesisfirehoseinputdefinition.md">KinesisFirehoseInputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStreamsInput

_Required_: No

_Type_: List of <a href="kinesisstreamsinputdefinition.md">KinesisStreamsInputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

