# TF::GoogleBeta::GoogleOsConfigPatchDeployment MonthlyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#monthday" title="MonthDay">MonthDay</a>" : <i>Double</i>,
    "<a href="#weekdayofmonth" title="WeekDayOfMonth">WeekDayOfMonth</a>" : <i>[ <a href="weekdayofmonthdefinition.md">WeekDayOfMonthDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#monthday" title="MonthDay">MonthDay</a>: <i>Double</i>
<a href="#weekdayofmonth" title="WeekDayOfMonth">WeekDayOfMonth</a>: <i>
      - <a href="weekdayofmonthdefinition.md">WeekDayOfMonthDefinition</a></i>
</pre>

## Properties

#### MonthDay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeekDayOfMonth

_Required_: No

_Type_: List of <a href="weekdayofmonthdefinition.md">WeekDayOfMonthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

