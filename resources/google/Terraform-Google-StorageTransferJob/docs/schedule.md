# Terraform::Google::StorageTransferJob Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>" : <i>[ <a href="schedule-scheduleenddate.md">ScheduleEndDate</a>, ... ]</i>,
    "<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>" : <i>[ <a href="schedule-schedulestartdate.md">ScheduleStartDate</a>, ... ]</i>,
    "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>[ <a href="schedule-starttimeofday.md">StartTimeOfDay</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>: <i>
      - <a href="schedule-scheduleenddate.md">ScheduleEndDate</a></i>
<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>: <i>
      - <a href="schedule-schedulestartdate.md">ScheduleStartDate</a></i>
<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>
      - <a href="schedule-starttimeofday.md">StartTimeOfDay</a></i>
</pre>

## Properties

#### ScheduleEndDate

_Required_: No
_Type_: List of <a href="schedule-scheduleenddate.md">ScheduleEndDate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleStartDate

_Required_: No
_Type_: List of <a href="schedule-schedulestartdate.md">ScheduleStartDate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

_Required_: No
_Type_: List of <a href="schedule-starttimeofday.md">StartTimeOfDay</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

