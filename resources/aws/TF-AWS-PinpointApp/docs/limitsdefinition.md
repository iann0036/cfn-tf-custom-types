# TF::AWS::PinpointApp LimitsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#daily" title="Daily">Daily</a>" : <i>Double</i>,
    "<a href="#maximumduration" title="MaximumDuration">MaximumDuration</a>" : <i>Double</i>,
    "<a href="#messagespersecond" title="MessagesPerSecond">MessagesPerSecond</a>" : <i>Double</i>,
    "<a href="#total" title="Total">Total</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#daily" title="Daily">Daily</a>: <i>Double</i>
<a href="#maximumduration" title="MaximumDuration">MaximumDuration</a>: <i>Double</i>
<a href="#messagespersecond" title="MessagesPerSecond">MessagesPerSecond</a>: <i>Double</i>
<a href="#total" title="Total">Total</a>: <i>Double</i>
</pre>

## Properties

#### Daily

The maximum number of messages that the campaign can send daily.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumDuration

The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessagesPerSecond

The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Total

The maximum total number of messages that the campaign can send.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

