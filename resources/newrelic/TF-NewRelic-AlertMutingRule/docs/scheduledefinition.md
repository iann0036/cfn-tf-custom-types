# TF::NewRelic::AlertMutingRule ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endrepeat" title="EndRepeat">EndRepeat</a>" : <i>String</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#repeat" title="Repeat">Repeat</a>" : <i>String</i>,
    "<a href="#repeatcount" title="RepeatCount">RepeatCount</a>" : <i>Double</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
    "<a href="#weeklyrepeatdays" title="WeeklyRepeatDays">WeeklyRepeatDays</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#endrepeat" title="EndRepeat">EndRepeat</a>: <i>String</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#repeat" title="Repeat">Repeat</a>: <i>String</i>
<a href="#repeatcount" title="RepeatCount">RepeatCount</a>: <i>Double</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
<a href="#weeklyrepeatdays" title="WeeklyRepeatDays">WeeklyRepeatDays</a>: <i>
      - String</i>
</pre>

## Properties

#### EndRepeat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repeat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepeatCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyRepeatDays

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

