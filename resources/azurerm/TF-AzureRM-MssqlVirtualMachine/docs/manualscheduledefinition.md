# TF::AzureRM::MssqlVirtualMachine ManualScheduleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fullbackupfrequency" title="FullBackupFrequency">FullBackupFrequency</a>" : <i>String</i>,
    "<a href="#fullbackupstarthour" title="FullBackupStartHour">FullBackupStartHour</a>" : <i>Double</i>,
    "<a href="#fullbackupwindowinhours" title="FullBackupWindowInHours">FullBackupWindowInHours</a>" : <i>Double</i>,
    "<a href="#logbackupfrequencyinminutes" title="LogBackupFrequencyInMinutes">LogBackupFrequencyInMinutes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#fullbackupfrequency" title="FullBackupFrequency">FullBackupFrequency</a>: <i>String</i>
<a href="#fullbackupstarthour" title="FullBackupStartHour">FullBackupStartHour</a>: <i>Double</i>
<a href="#fullbackupwindowinhours" title="FullBackupWindowInHours">FullBackupWindowInHours</a>: <i>Double</i>
<a href="#logbackupfrequencyinminutes" title="LogBackupFrequencyInMinutes">LogBackupFrequencyInMinutes</a>: <i>Double</i>
</pre>

## Properties

#### FullBackupFrequency

Frequency of full backups. Valid values include `Daily` or `Weekly`. Required when `backup_schedule_automated` is false.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullBackupStartHour

Start hour of a given day during which full backups can take place. Valid values are from `0` to `23`. Required when `backup_schedule_automated` is false.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullBackupWindowInHours

Duration of the time window of a given day during which full backups can take place, in hours. Valid values are between `1` and `23`. Required when `backup_schedule_automated` is false.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackupFrequencyInMinutes

Frequency of log backups, in minutes. Valid values are from `5` to `60`. Required when `backup_schedule_automated` is false.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

