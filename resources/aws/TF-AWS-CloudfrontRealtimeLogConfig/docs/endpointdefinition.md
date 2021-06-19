# TF::AWS::CloudfrontRealtimeLogConfig EndpointDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#streamtype" title="StreamType">StreamType</a>" : <i>String</i>,
    "<a href="#kinesisstreamconfig" title="KinesisStreamConfig">KinesisStreamConfig</a>" : <i>[ <a href="kinesisstreamconfigdefinition.md">KinesisStreamConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#streamtype" title="StreamType">StreamType</a>: <i>String</i>
<a href="#kinesisstreamconfig" title="KinesisStreamConfig">KinesisStreamConfig</a>: <i>
      - <a href="kinesisstreamconfigdefinition.md">KinesisStreamConfigDefinition</a></i>
</pre>

## Properties

#### StreamType

The type of data stream where real-time log data is sent. The only valid value is `Kinesis`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KinesisStreamConfig

_Required_: No

_Type_: List of <a href="kinesisstreamconfigdefinition.md">KinesisStreamConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

