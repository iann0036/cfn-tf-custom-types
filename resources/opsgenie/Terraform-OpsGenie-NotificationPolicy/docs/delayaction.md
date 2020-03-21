# Terraform::OpsGenie::NotificationPolicy DelayAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delayoption" title="DelayOption">DelayOption</a>" : <i>String</i>,
    "<a href="#untilhour" title="UntilHour">UntilHour</a>" : <i>Double</i>,
    "<a href="#untilminute" title="UntilMinute">UntilMinute</a>" : <i>Double</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ <a href="delayaction-duration.md">Duration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#delayoption" title="DelayOption">DelayOption</a>: <i>String</i>
<a href="#untilhour" title="UntilHour">UntilHour</a>: <i>Double</i>
<a href="#untilminute" title="UntilMinute">UntilMinute</a>: <i>Double</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - <a href="delayaction-duration.md">Duration</a></i>
</pre>

## Properties

#### DelayOption

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilHour

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntilMinute

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No
_Type_: List of <a href="delayaction-duration.md">Duration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

