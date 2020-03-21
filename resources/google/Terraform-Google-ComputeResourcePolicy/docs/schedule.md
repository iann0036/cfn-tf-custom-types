# Terraform::Google::ComputeResourcePolicy Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>[ <a href="schedule-dailyschedule.md">DailySchedule</a>, ... ]</i>,
    "<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>" : <i>[ <a href="schedule-hourlyschedule.md">HourlySchedule</a>, ... ]</i>,
    "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>[ <a href="schedule-weeklyschedule.md">WeeklySchedule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>
      - <a href="schedule-dailyschedule.md">DailySchedule</a></i>
<a href="#hourlyschedule" title="HourlySchedule">HourlySchedule</a>: <i>
      - <a href="schedule-hourlyschedule.md">HourlySchedule</a></i>
<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>
      - <a href="schedule-weeklyschedule.md">WeeklySchedule</a></i>
</pre>

## Properties

#### DailySchedule

_Required_: No
_Type_: List of <a href="schedule-dailyschedule.md">DailySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlySchedule

_Required_: No
_Type_: List of <a href="schedule-hourlyschedule.md">HourlySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

_Required_: No
_Type_: List of <a href="schedule-weeklyschedule.md">WeeklySchedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

