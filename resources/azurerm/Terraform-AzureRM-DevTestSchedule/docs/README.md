# Terraform::AzureRM::DevTestSchedule

Manages automated startup and shutdown schedules for Azure Dev Test Lab.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::DevTestSchedule",
    "Properties" : {
        "<a href="#labname" title="LabName">LabName</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tasktype" title="TaskType">TaskType</a>" : <i>String</i>,
        "<a href="#timezoneid" title="TimeZoneId">TimeZoneId</a>" : <i>String</i>,
        "<a href="#dailyrecurrence" title="DailyRecurrence">DailyRecurrence</a>" : <i>[ <a href="dailyrecurrence.md">DailyRecurrence</a>, ... ]</i>,
        "<a href="#hourlyrecurrence" title="HourlyRecurrence">HourlyRecurrence</a>" : <i>[ <a href="hourlyrecurrence.md">HourlyRecurrence</a>, ... ]</i>,
        "<a href="#notificationsettings" title="NotificationSettings">NotificationSettings</a>" : <i>[ <a href="notificationsettings.md">NotificationSettings</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#weeklyrecurrence" title="WeeklyRecurrence">WeeklyRecurrence</a>" : <i>[ <a href="weeklyrecurrence.md">WeeklyRecurrence</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::DevTestSchedule
Properties:
    <a href="#labname" title="LabName">LabName</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tasktype" title="TaskType">TaskType</a>: <i>String</i>
    <a href="#timezoneid" title="TimeZoneId">TimeZoneId</a>: <i>String</i>
    <a href="#dailyrecurrence" title="DailyRecurrence">DailyRecurrence</a>: <i>
      - <a href="dailyrecurrence.md">DailyRecurrence</a></i>
    <a href="#hourlyrecurrence" title="HourlyRecurrence">HourlyRecurrence</a>: <i>
      - <a href="hourlyrecurrence.md">HourlyRecurrence</a></i>
    <a href="#notificationsettings" title="NotificationSettings">NotificationSettings</a>: <i>
      - <a href="notificationsettings.md">NotificationSettings</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#weeklyrecurrence" title="WeeklyRecurrence">WeeklyRecurrence</a>: <i>
      - <a href="weeklyrecurrence.md">WeeklyRecurrence</a></i>
</pre>

## Properties

#### LabName

The name of the dev test lab. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the schedule is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the dev test lab schedule. Valid value for name depends on the `task_type`. For instance for task_type `LabVmsStartupTask` the name needs to be `LabVmAutoStart`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the dev test lab schedule. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the notification. Possible values are `Enabled` and `Disabled`. Defaults to `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskType

The task type of the schedule. Possible values include `LabVmsShutdownTask` and `LabVmAutoStart`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZoneId

The time zone ID (e.g. Pacific Standard time).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyRecurrence

_Required_: No

_Type_: List of <a href="dailyrecurrence.md">DailyRecurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourlyRecurrence

_Required_: No

_Type_: List of <a href="hourlyrecurrence.md">HourlyRecurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationSettings

_Required_: No

_Type_: List of <a href="notificationsettings.md">NotificationSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyRecurrence

_Required_: No

_Type_: List of <a href="weeklyrecurrence.md">WeeklyRecurrence</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

