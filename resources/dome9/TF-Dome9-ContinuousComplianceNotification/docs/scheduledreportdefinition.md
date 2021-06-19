# TF::Dome9::ContinuousComplianceNotification ScheduledReportDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#emailsendingstate" title="EmailSendingState">EmailSendingState</a>" : <i>String</i>,
    "<a href="#scheduledata" title="ScheduleData">ScheduleData</a>" : <i>[ <a href="scheduledatadefinition.md">ScheduleDataDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#emailsendingstate" title="EmailSendingState">EmailSendingState</a>: <i>String</i>
<a href="#scheduledata" title="ScheduleData">ScheduleData</a>: <i>
      - <a href="scheduledatadefinition.md">ScheduleDataDefinition</a></i>
</pre>

## Properties

#### EmailSendingState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleData

_Required_: No

_Type_: List of <a href="scheduledatadefinition.md">ScheduleDataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

