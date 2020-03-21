# Terraform::AzureRM::AutomationSchedule

Manages a Automation Schedule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::AutomationSchedule",
    "Properties" : {
        "<a href="#automationaccountname" title="AutomationAccountName">AutomationAccountName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expirytime" title="ExpiryTime">ExpiryTime</a>" : <i>String</i>,
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>String</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#monthdays" title="MonthDays">MonthDays</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#weekdays" title="WeekDays">WeekDays</a>" : <i>[ String, ... ]</i>,
        "<a href="#monthlyoccurrence" title="MonthlyOccurrence">MonthlyOccurrence</a>" : <i>[ <a href="monthlyoccurrence.md">MonthlyOccurrence</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::AutomationSchedule
Properties:
    <a href="#automationaccountname" title="AutomationAccountName">AutomationAccountName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expirytime" title="ExpiryTime">ExpiryTime</a>: <i>String</i>
    <a href="#frequency" title="Frequency">Frequency</a>: <i>String</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#monthdays" title="MonthDays">MonthDays</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#weekdays" title="WeekDays">WeekDays</a>: <i>
      - String</i>
    <a href="#monthlyoccurrence" title="MonthlyOccurrence">MonthlyOccurrence</a>: <i>
      - <a href="monthlyoccurrence.md">MonthlyOccurrence</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutomationAccountName

The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for this Schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiryTime

The end time of the schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthDays

List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Schedule. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeekDays

List of days of the week that the job should execute on. Only valid when frequency is `Week`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlyOccurrence

_Required_: No

_Type_: List of <a href="monthlyoccurrence.md">MonthlyOccurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

