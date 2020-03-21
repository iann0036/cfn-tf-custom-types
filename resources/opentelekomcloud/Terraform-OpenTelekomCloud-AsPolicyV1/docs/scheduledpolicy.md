# Terraform::OpenTelekomCloud::AsPolicyV1 ScheduledPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#launchtime" title="LaunchTime">LaunchTime</a>" : <i>String</i>,
    "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
    "<a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#launchtime" title="LaunchTime">LaunchTime</a>: <i>String</i>
<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
<a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
</pre>

## Properties

#### EndTime

The end time of the scaling action triggered periodically.
The time format complies with UTC. This argument is mandatory when `scaling_policy_type`
is set to `RECURRENCE`. The time format is YYYY-MM-DDThh:mmZ.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTime

The time when the scaling action is triggered. If `scaling_policy_type`
is set to `SCHEDULED`, the time format is YYYY-MM-DDThh:mmZ. If `scaling_policy_type` is set to
`RECURRENCE`, the time format is hh:mm.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

The periodic triggering type. This argument is mandatory when
`scaling_policy_type` is set to `RECURRENCE`. The options include `Daily`, `Weekly`, and `Monthly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceValue

The frequency at which scaling actions are triggered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

The start time of the scaling action triggered periodically.
The time format complies with UTC. The current time is used by default. The time
format is YYYY-MM-DDThh:mmZ.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

