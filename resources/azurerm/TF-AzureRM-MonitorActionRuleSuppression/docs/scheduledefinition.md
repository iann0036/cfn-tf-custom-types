# TF::AzureRM::MonitorActionRuleSuppression ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enddateutc" title="EndDateUtc">EndDateUtc</a>" : <i>String</i>,
    "<a href="#recurrencemonthly" title="RecurrenceMonthly">RecurrenceMonthly</a>" : <i>[ Double, ... ]</i>,
    "<a href="#recurrenceweekly" title="RecurrenceWeekly">RecurrenceWeekly</a>" : <i>[ String, ... ]</i>,
    "<a href="#startdateutc" title="StartDateUtc">StartDateUtc</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enddateutc" title="EndDateUtc">EndDateUtc</a>: <i>String</i>
<a href="#recurrencemonthly" title="RecurrenceMonthly">RecurrenceMonthly</a>: <i>
      - Double</i>
<a href="#recurrenceweekly" title="RecurrenceWeekly">RecurrenceWeekly</a>: <i>
      - String</i>
<a href="#startdateutc" title="StartDateUtc">StartDateUtc</a>: <i>String</i>
</pre>

## Properties

#### EndDateUtc

specifies the recurrence UTC end datetime (Y-m-d'T'H:M:S'Z').

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceMonthly

specifies the list of dayOfMonth to recurrence. Possible values are between `1` - `31`. Required if `recurrence_type` is `Monthly`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceWeekly

specifies the list of dayOfWeek to recurrence. Possible values are `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` and  `Saturday`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDateUtc

specifies the recurrence UTC start datetime (Y-m-d'T'H:M:S'Z').

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

