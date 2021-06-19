# TF::GoogleBeta::GoogleComputeResourcePolicy ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a>, ... ]</i>,
    "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a>, ... ]</i>,
    "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a></i>
<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a></i>
<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a></i>
</pre>

## Properties

#### DailySchedule

_Required_: No

_Type_: List of <a href="dailyscheduledefinition.md">DailyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No

_Type_: List of <a href="hourlyscheduledefinition.md">HourlyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No

_Type_: List of <a href="weeklyscheduledefinition.md">WeeklyScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

