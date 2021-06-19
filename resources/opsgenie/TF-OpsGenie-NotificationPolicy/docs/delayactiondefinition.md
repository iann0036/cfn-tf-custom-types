# TF::OpsGenie::NotificationPolicy DelayActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delayoption" title="DelayOption">DelayOption</a>" : <i>String</i>,
    "<a href="#untilhour" title="UntilHour">UntilHour</a>" : <i>Double</i>,
    "<a href="#untilminute" title="UntilMinute">UntilMinute</a>" : <i>Double</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ <a href="durationdefinition.md">DurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#delayoption" title="DelayOption">DelayOption</a>: <i>String</i>
<a href="#untilhour" title="UntilHour">UntilHour</a>: <i>Double</i>
<a href="#untilminute" title="UntilMinute">UntilMinute</a>: <i>Double</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - <a href="durationdefinition.md">DurationDefinition</a></i>
</pre>

## Properties

#### DelayOption

Defines until what day to delay or for what duration. Possible values are: `for-duration`, `next-time`, `next-weekday`, `next-monday`, `next-tuesday`, `next-wednesday`, `next-thursday`, `next-friday`, `next-saturday`, `next-sunday`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilHour

Until what hour notifications will be delayed. If `delay_option` is set to antyhing else then `for-duration` this has to be set.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilMinute

Until what minute on `until_hour` notifications will be delayed. If `delay_option` is set to antyhing else then `for-duration` this has to be set.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: List of <a href="durationdefinition.md">DurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

