# Terraform::Alicloud::DbBackupPolicy

CloudFormation equivalent of alicloud_db_backup_policy

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveBackupKeepPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArchiveBackupRetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPeriod

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBackupLog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighSpaceUsageProtection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogRetentionHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogRetentionSpace

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackupFrequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogBackupRetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogRetentionPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupPeriod

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

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

