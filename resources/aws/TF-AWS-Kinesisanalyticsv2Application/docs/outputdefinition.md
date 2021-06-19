# TF::AWS::Kinesisanalyticsv2Application OutputDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#destinationschema" title="DestinationSchema">DestinationSchema</a>" : <i>[ <a href="destinationschemadefinition.md">DestinationSchemaDefinition</a>, ... ]</i>,
    "<a href="#kinesisfirehoseoutput" title="KinesisFirehoseOutput">KinesisFirehoseOutput</a>" : <i>[ <a href="kinesisfirehoseoutputdefinition.md">KinesisFirehoseOutputDefinition</a>, ... ]</i>,
    "<a href="#kinesisstreamsoutput" title="KinesisStreamsOutput">KinesisStreamsOutput</a>" : <i>[ <a href="kinesisstreamsoutputdefinition.md">KinesisStreamsOutputDefinition</a>, ... ]</i>,
    "<a href="#lambdaoutput" title="LambdaOutput">LambdaOutput</a>" : <i>[ <a href="lambdaoutputdefinition.md">LambdaOutputDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#destinationschema" title="DestinationSchema">DestinationSchema</a>: <i>
      - <a href="destinationschemadefinition.md">DestinationSchemaDefinition</a></i>
<a href="#kinesisfirehoseoutput" title="KinesisFirehoseOutput">KinesisFirehoseOutput</a>: <i>
      - <a href="kinesisfirehoseoutputdefinition.md">KinesisFirehoseOutputDefinition</a></i>
<a href="#kinesisstreamsoutput" title="KinesisStreamsOutput">KinesisStreamsOutput</a>: <i>
      - <a href="kinesisstreamsoutputdefinition.md">KinesisStreamsOutputDefinition</a></i>
<a href="#lambdaoutput" title="LambdaOutput">LambdaOutput</a>: <i>
      - <a href="lambdaoutputdefinition.md">LambdaOutputDefinition</a></i>
</pre>

## Properties

#### Name

The name of the in-application stream.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationSchema

_Required_: No

_Type_: List of <a href="destinationschemadefinition.md">DestinationSchemaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisFirehoseOutput

_Required_: No

_Type_: List of <a href="kinesisfirehoseoutputdefinition.md">KinesisFirehoseOutputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStreamsOutput

_Required_: No

_Type_: List of <a href="kinesisstreamsoutputdefinition.md">KinesisStreamsOutputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaOutput

_Required_: No

_Type_: List of <a href="lambdaoutputdefinition.md">LambdaOutputDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

