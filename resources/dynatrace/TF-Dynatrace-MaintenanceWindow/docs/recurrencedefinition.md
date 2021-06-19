# TF::Dynatrace::MaintenanceWindow RecurrenceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>" : <i>Double</i>,
    "<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>" : <i>String</i>,
    "<a href="#durationminutes" title="DurationMinutes">DurationMinutes</a>" : <i>Double</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>: <i>Double</i>
<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>: <i>String</i>
<a href="#durationminutes" title="DurationMinutes">DurationMinutes</a>: <i>Double</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
</pre>

## Properties

#### DayOfMonth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfWeek

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DurationMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

