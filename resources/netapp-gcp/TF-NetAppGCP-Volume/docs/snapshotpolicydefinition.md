# TF::NetAppGCP::Volume SnapshotPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a>, ... ]</i>,
    "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a>, ... ]</i>,
    "<a href="#monthlyschedule" title="MonthlySchedule">MonthlySchedule</a>" : <i>[ <a href="monthlyscheduledefinition.md">MonthlyScheduleDefinition</a>, ... ]</i>,
    "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a></i>
<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a></i>
<a href="#monthlyschedule" title="MonthlySchedule">MonthlySchedule</a>: <i>
      - <a href="monthlyscheduledefinition.md">MonthlyScheduleDefinition</a></i>
<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailySchedule

_Required_: No

_Type_: List of <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No

_Type_: List of <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlySchedule

_Required_: No

_Type_: List of <a href="monthlyscheduledefinition.md">MonthlyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No

_Type_: List of <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

