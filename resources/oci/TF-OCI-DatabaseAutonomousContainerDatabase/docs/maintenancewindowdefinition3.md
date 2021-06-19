# TF::OCI::DatabaseAutonomousContainerDatabase MaintenanceWindowDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>,
    "<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>" : <i>[ Double, ... ]</i>,
    "<a href="#leadtimeinweeks" title="LeadTimeInWeeks">LeadTimeInWeeks</a>" : <i>Double</i>,
    "<a href="#months" title="Months">Months</a>" : <i>[ <a href="maintenancewindowdefinition2.md">MaintenanceWindowDefinition2</a>, ... ]</i>,
    "<a href="#preference" title="Preference">Preference</a>" : <i>String</i>,
    "<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>" : <i>[ Double, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
<a href="#hoursofday" title="HoursOfDay">HoursOfDay</a>: <i>
      - Double</i>
<a href="#leadtimeinweeks" title="LeadTimeInWeeks">LeadTimeInWeeks</a>: <i>Double</i>
<a href="#months" title="Months">Months</a>: <i>
      - <a href="maintenancewindowdefinition2.md">MaintenanceWindowDefinition2</a></i>
<a href="#preference" title="Preference">Preference</a>: <i>String</i>
<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>: <i>
      - Double</i>
</pre>

## Properties

#### DaysOfWeek

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoursOfDay

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeadTimeInWeeks

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Months

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition2.md">MaintenanceWindowDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeksOfMonth

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

