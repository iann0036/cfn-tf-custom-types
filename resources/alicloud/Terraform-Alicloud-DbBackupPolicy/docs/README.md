# Terraform::Alicloud::DbBackupPolicy

Provides an RDS instance backup policy resource and used to configure instance backup policy.

-> **NOTE:** Each DB instance has a backup policy and it will be set default values when destroying the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::DbBackupPolicy",
    "Properties" : {
        "<a href="#archivebackupkeepcount" title="ArchiveBackupKeepCount">ArchiveBackupKeepCount</a>" : <i>Double</i>,
        "<a href="#archivebackupkeeppolicy" title="ArchiveBackupKeepPolicy">ArchiveBackupKeepPolicy</a>" : <i>String</i>,
        "<a href="#archivebackupretentionperiod" title="ArchiveBackupRetentionPeriod">ArchiveBackupRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#backupperiod" title="BackupPeriod">BackupPeriod</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupretentionperiod" title="BackupRetentionPeriod">BackupRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#backuptime" title="BackupTime">BackupTime</a>" : <i>String</i>,
        "<a href="#compresstype" title="CompressType">CompressType</a>" : <i>String</i>,
        "<a href="#enablebackuplog" title="EnableBackupLog">EnableBackupLog</a>" : <i>Boolean</i>,
        "<a href="#highspaceusageprotection" title="HighSpaceUsageProtection">HighSpaceUsageProtection</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#locallogretentionhours" title="LocalLogRetentionHours">LocalLogRetentionHours</a>" : <i>Double</i>,
        "<a href="#locallogretentionspace" title="LocalLogRetentionSpace">LocalLogRetentionSpace</a>" : <i>Double</i>,
        "<a href="#logbackup" title="LogBackup">LogBackup</a>" : <i>Boolean</i>,
        "<a href="#logbackupfrequency" title="LogBackupFrequency">LogBackupFrequency</a>" : <i>String</i>,
        "<a href="#logbackupretentionperiod" title="LogBackupRetentionPeriod">LogBackupRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#logretentionperiod" title="LogRetentionPeriod">LogRetentionPeriod</a>" : <i>Double</i>,
        "<a href="#preferredbackupperiod" title="PreferredBackupPeriod">PreferredBackupPeriod</a>" : <i>[ String, ... ]</i>,
        "<a href="#preferredbackuptime" title="PreferredBackupTime">PreferredBackupTime</a>" : <i>String</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::DbBackupPolicy
Properties:
    <a href="#archivebackupkeepcount" title="ArchiveBackupKeepCount">ArchiveBackupKeepCount</a>: <i>Double</i>
    <a href="#archivebackupkeeppolicy" title="ArchiveBackupKeepPolicy">ArchiveBackupKeepPolicy</a>: <i>String</i>
    <a href="#archivebackupretentionperiod" title="ArchiveBackupRetentionPeriod">ArchiveBackupRetentionPeriod</a>: <i>Double</i>
    <a href="#backupperiod" title="BackupPeriod">BackupPeriod</a>: <i>
      - String</i>
    <a href="#backupretentionperiod" title="BackupRetentionPeriod">BackupRetentionPeriod</a>: <i>Double</i>
    <a href="#backuptime" title="BackupTime">BackupTime</a>: <i>String</i>
    <a href="#compresstype" title="CompressType">CompressType</a>: <i>String</i>
    <a href="#enablebackuplog" title="EnableBackupLog">EnableBackupLog</a>: <i>Boolean</i>
    <a href="#highspaceusageprotection" title="HighSpaceUsageProtection">HighSpaceUsageProtection</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#locallogretentionhours" title="LocalLogRetentionHours">LocalLogRetentionHours</a>: <i>Double</i>
    <a href="#locallogretentionspace" title="LocalLogRetentionSpace">LocalLogRetentionSpace</a>: <i>Double</i>
    <a href="#logbackup" title="LogBackup">LogBackup</a>: <i>Boolean</i>
    <a href="#logbackupfrequency" title="LogBackupFrequency">LogBackupFrequency</a>: <i>String</i>
    <a href="#logbackupretentionperiod" title="LogBackupRetentionPeriod">LogBackupRetentionPeriod</a>: <i>Double</i>
    <a href="#logretentionperiod" title="LogRetentionPeriod">LogRetentionPeriod</a>: <i>Double</i>
    <a href="#preferredbackupperiod" title="PreferredBackupPeriod">PreferredBackupPeriod</a>: <i>
      - String</i>
    <a href="#preferredbackuptime" title="PreferredBackupTime">PreferredBackupTime</a>: <i>String</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
</pre>

## Properties

#### ArchiveBackupKeepCount

Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveBackupKeepPolicy

Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveBackupRetentionPeriod

Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPeriod

It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionPeriod

Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupTime

It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressType

The compress type of instance policy. Valid values are `1`, `4`, `8`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackupLog

Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighSpaceUsageProtection

Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The Id of instance that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogRetentionHours

Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogRetentionSpace

Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackup

It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackupFrequency

Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackupRetentionPeriod

Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetentionPeriod

It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupPeriod

DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupTime

DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

