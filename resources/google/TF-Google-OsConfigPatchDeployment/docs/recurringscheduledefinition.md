# TF::Google::OsConfigPatchDeployment RecurringScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#monthly" title="Monthly">Monthly</a>" : <i>[ <a href="monthlydefinition.md">MonthlyDefinition</a>, ... ]</i>,
    "<a href="#timeofday" title="TimeOfDay">TimeOfDay</a>" : <i>[ <a href="timeofdaydefinition.md">TimeOfDayDefinition</a>, ... ]</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>[ <a href="timezonedefinition.md">TimeZoneDefinition</a>, ... ]</i>,
    "<a href="#weekly" title="Weekly">Weekly</a>" : <i>[ <a href="weeklydefinition.md">WeeklyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#monthly" title="Monthly">Monthly</a>: <i>
      - <a href="monthlydefinition.md">MonthlyDefinition</a></i>
<a href="#timeofday" title="TimeOfDay">TimeOfDay</a>: <i>
      - <a href="timeofdaydefinition.md">TimeOfDayDefinition</a></i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>
      - <a href="timezonedefinition.md">TimeZoneDefinition</a></i>
<a href="#weekly" title="Weekly">Weekly</a>: <i>
      - <a href="weeklydefinition.md">WeeklyDefinition</a></i>
</pre>

## Properties

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monthly

_Required_: No

_Type_: List of <a href="monthlydefinition.md">MonthlyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeOfDay

_Required_: No

_Type_: List of <a href="timeofdaydefinition.md">TimeOfDayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No

_Type_: List of <a href="timezonedefinition.md">TimeZoneDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weekly

_Required_: No

_Type_: List of <a href="weeklydefinition.md">WeeklyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

