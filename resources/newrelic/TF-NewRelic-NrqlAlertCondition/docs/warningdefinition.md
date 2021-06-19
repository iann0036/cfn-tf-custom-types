# TF::NewRelic::NrqlAlertCondition WarningDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#thresholdduration" title="ThresholdDuration">ThresholdDuration</a>" : <i>Double</i>,
    "<a href="#thresholdoccurrences" title="ThresholdOccurrences">ThresholdOccurrences</a>" : <i>String</i>,
    "<a href="#timefunction" title="TimeFunction">TimeFunction</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#thresholdduration" title="ThresholdDuration">ThresholdDuration</a>: <i>Double</i>
<a href="#thresholdoccurrences" title="ThresholdOccurrences">ThresholdOccurrences</a>: <i>String</i>
<a href="#timefunction" title="TimeFunction">TimeFunction</a>: <i>String</i>
</pre>

## Properties

#### Duration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdDuration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdOccurrences

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFunction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

