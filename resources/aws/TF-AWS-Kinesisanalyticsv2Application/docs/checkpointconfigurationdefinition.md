# TF::AWS::Kinesisanalyticsv2Application CheckpointConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkpointinterval" title="CheckpointInterval">CheckpointInterval</a>" : <i>Double</i>,
    "<a href="#checkpointingenabled" title="CheckpointingEnabled">CheckpointingEnabled</a>" : <i>Boolean</i>,
    "<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>" : <i>String</i>,
    "<a href="#minpausebetweencheckpoints" title="MinPauseBetweenCheckpoints">MinPauseBetweenCheckpoints</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#checkpointinterval" title="CheckpointInterval">CheckpointInterval</a>: <i>Double</i>
<a href="#checkpointingenabled" title="CheckpointingEnabled">CheckpointingEnabled</a>: <i>Boolean</i>
<a href="#configurationtype" title="ConfigurationType">ConfigurationType</a>: <i>String</i>
<a href="#minpausebetweencheckpoints" title="MinPauseBetweenCheckpoints">MinPauseBetweenCheckpoints</a>: <i>Double</i>
</pre>

## Properties

#### CheckpointInterval

Describes the interval in milliseconds between checkpoint operations.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckpointingEnabled

Describes whether checkpointing is enabled for a Flink-based Kinesis Data Analytics application.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationType

Describes whether the application uses Kinesis Data Analytics' default checkpointing behavior. Valid values: `CUSTOM`, `DEFAULT`. Set this attribute to `CUSTOM` in order for any specified `checkpointing_enabled`, `checkpoint_interval`, or `min_pause_between_checkpoints` attribute values to be effective. If this attribute is set to `DEFAULT`, the application will always use the following values:
* `checkpointing_enabled = true`
* `checkpoint_interval = 60000`
* `min_pause_between_checkpoints = 5000`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPauseBetweenCheckpoints

Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

