# TF::AWS::Macie2ClassificationJob ScheduleFrequencyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>" : <i>Boolean</i>,
    "<a href="#monthlyschedule" title="MonthlySchedule">MonthlySchedule</a>" : <i>Double</i>,
    "<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dailyschedule" title="DailySchedule">DailySchedule</a>: <i>Boolean</i>
<a href="#monthlyschedule" title="MonthlySchedule">MonthlySchedule</a>: <i>Double</i>
<a href="#weeklyschedule" title="WeeklySchedule">WeeklySchedule</a>: <i>String</i>
</pre>

## Properties

#### DailySchedule

Specifies a daily recurrence pattern for running the job.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlySchedule

Specifies a monthly recurrence pattern for running the job.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklySchedule

Specifies a weekly recurrence pattern for running the job.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

