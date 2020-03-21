# Terraform::PagerDuty::Schedule Layer Restriction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#durationseconds" title="DurationSeconds">DurationSeconds</a>" : <i>Double</i>,
    "<a href="#startdayofweek" title="StartDayOfWeek">StartDayOfWeek</a>" : <i>Double</i>,
    "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#durationseconds" title="DurationSeconds">DurationSeconds</a>: <i>Double</i>
<a href="#startdayofweek" title="StartDayOfWeek">StartDayOfWeek</a>: <i>Double</i>
<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DurationSeconds

The duration of the restriction in `seconds`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDayOfWeek

Number of the day when restriction starts. From 1 to 7 where 1 is Monday and 7 is Sunday.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

The start time in `HH:mm:ss` format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Can be `daily_restriction` or `weekly_restriction`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

