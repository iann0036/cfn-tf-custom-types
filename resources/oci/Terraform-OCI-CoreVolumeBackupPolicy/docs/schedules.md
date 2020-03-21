# Terraform::OCI::CoreVolumeBackupPolicy Schedules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backuptype" title="BackupType">BackupType</a>" : <i>String</i>,
    "<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>" : <i>Double</i>,
    "<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>" : <i>String</i>,
    "<a href="#hourofday" title="HourOfDay">HourOfDay</a>" : <i>Double</i>,
    "<a href="#month" title="Month">Month</a>" : <i>String</i>,
    "<a href="#offsetseconds" title="OffsetSeconds">OffsetSeconds</a>" : <i>Double</i>,
    "<a href="#offsettype" title="OffsetType">OffsetType</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>String</i>,
    "<a href="#retentionseconds" title="RetentionSeconds">RetentionSeconds</a>" : <i>Double</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backuptype" title="BackupType">BackupType</a>: <i>String</i>
<a href="#dayofmonth" title="DayOfMonth">DayOfMonth</a>: <i>Double</i>
<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>: <i>String</i>
<a href="#hourofday" title="HourOfDay">HourOfDay</a>: <i>Double</i>
<a href="#month" title="Month">Month</a>: <i>String</i>
<a href="#offsetseconds" title="OffsetSeconds">OffsetSeconds</a>: <i>Double</i>
<a href="#offsettype" title="OffsetType">OffsetType</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>String</i>
<a href="#retentionseconds" title="RetentionSeconds">RetentionSeconds</a>: <i>Double</i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
</pre>

## Properties

#### BackupType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfMonth

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DayOfWeek

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HourOfDay

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Month

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffsetSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffsetType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionSeconds

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

