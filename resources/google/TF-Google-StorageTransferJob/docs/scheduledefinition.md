# TF::Google::StorageTransferJob ScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>" : <i>[ <a href="scheduleenddatedefinition.md">ScheduleEndDateDefinition</a>, ... ]</i>,
    "<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>" : <i>[ <a href="schedulestartdatedefinition.md">ScheduleStartDateDefinition</a>, ... ]</i>,
    "<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>" : <i>[ <a href="starttimeofdaydefinition.md">StartTimeOfDayDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#scheduleenddate" title="ScheduleEndDate">ScheduleEndDate</a>: <i>
      - <a href="scheduleenddatedefinition.md">ScheduleEndDateDefinition</a></i>
<a href="#schedulestartdate" title="ScheduleStartDate">ScheduleStartDate</a>: <i>
      - <a href="schedulestartdatedefinition.md">ScheduleStartDateDefinition</a></i>
<a href="#starttimeofday" title="StartTimeOfDay">StartTimeOfDay</a>: <i>
      - <a href="starttimeofdaydefinition.md">StartTimeOfDayDefinition</a></i>
</pre>

## Properties

#### ScheduleEndDate

_Required_: No

_Type_: List of <a href="scheduleenddatedefinition.md">ScheduleEndDateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleStartDate

_Required_: No

_Type_: List of <a href="schedulestartdatedefinition.md">ScheduleStartDateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTimeOfDay

_Required_: No

_Type_: List of <a href="starttimeofdaydefinition.md">StartTimeOfDayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

