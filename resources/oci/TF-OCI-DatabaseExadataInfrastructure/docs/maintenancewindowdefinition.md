# TF::OCI::DatabaseExadataInfrastructure MaintenanceWindowDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>" : <i>[ Double, ... ]</i>,
    "<a href="#leadtimeinweeks" title="LeadTimeInWeeks">LeadTimeInWeeks</a>" : <i>Double</i>,
    "<a href="#preference" title="Preference">Preference</a>" : <i>String</i>,
    "<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>" : <i>[ Double, ... ]</i>,
    "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a>, ... ]</i>,
    "<a href="#months" title="Months">Months</a>" : <i>[ <a href="monthsdefinition.md">MonthsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>: <i>
      - Double</i>
<a href="#leadtimeinweeks" title="LeadTimeInWeeks">LeadTimeInWeeks</a>: <i>Double</i>
<a href="#preference" title="Preference">Preference</a>: <i>String</i>
<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>: <i>
      - Double</i>
<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a></i>
<a href="#months" title="Months">Months</a>: <i>
      - <a href="monthsdefinition.md">MonthsDefinition</a></i>
</pre>

## Properties

#### HoursOfDay

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeadTimeInWeeks

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeksOfMonth

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysOfWeek

_Required_: No

_Type_: List of <a href="daysofweekdefinition.md">DaysOfWeekDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Months

_Required_: No

_Type_: List of <a href="monthsdefinition.md">MonthsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

