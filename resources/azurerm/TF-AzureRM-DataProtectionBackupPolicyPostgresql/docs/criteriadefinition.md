# TF::AzureRM::DataProtectionBackupPolicyPostgresql CriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#absolutecriteria" title="AbsoluteCriteria">AbsoluteCriteria</a>" : <i>String</i>,
    "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ String, ... ]</i>,
    "<a href="#monthsofyear" title="MonthsOfYear">MonthsOfYear</a>" : <i>[ String, ... ]</i>,
    "<a href="#scheduledbackuptimes" title="ScheduledBackupTimes">ScheduledBackupTimes</a>" : <i>[ String, ... ]</i>,
    "<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#absolutecriteria" title="AbsoluteCriteria">AbsoluteCriteria</a>: <i>String</i>
<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - String</i>
<a href="#monthsofyear" title="MonthsOfYear">MonthsOfYear</a>: <i>
      - String</i>
<a href="#scheduledbackuptimes" title="ScheduledBackupTimes">ScheduledBackupTimes</a>: <i>
      - String</i>
<a href="#weeksofmonth" title="WeeksOfMonth">WeeksOfMonth</a>: <i>
      - String</i>
</pre>

## Properties

#### AbsoluteCriteria

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysOfWeek

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthsOfYear

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledBackupTimes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeksOfMonth

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

