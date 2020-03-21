# Terraform::TencentCloud::MysqlBackupPolicy

Provides a mysql policy resource to create a backup policy.

~> **NOTE:** This attribute `backup_model` only support 'physical' in Terraform TencentCloud provider version 1.16.2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::MysqlBackupPolicy",
    "Properties" : {
        "<a href="#backupmodel" title="BackupModel">BackupModel</a>" : <i>String</i>,
        "<a href="#backuptime" title="BackupTime">BackupTime</a>" : <i>String</i>,
        "<a href="#mysqlid" title="MysqlId">MysqlId</a>" : <i>String</i>,
        "<a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::MysqlBackupPolicy
Properties:
    <a href="#backupmodel" title="BackupModel">BackupModel</a>: <i>String</i>
    <a href="#backuptime" title="BackupTime">BackupTime</a>: <i>String</i>
    <a href="#mysqlid" title="MysqlId">MysqlId</a>: <i>String</i>
    <a href="#retentionperiod" title="RetentionPeriod">RetentionPeriod</a>: <i>Double</i>
</pre>

## Properties

#### BackupModel

Backup method. Supported values include: 'physical' - physical backup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupTime

Instance backup time, in the format of "HH:mm-HH:mm". Time setting interval is four hours. Default to "02:00-06:00". The following value can be supported: 02:00-06:00, 06:00-10:00, 10:00-14:00, 14:00-18:00, 18:00-22:00, and 22:00-02:00.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MysqlId

Instance ID to which policies will be applied.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriod

Instance backup retention days. Valid values: [7-730]. And default value is 7.

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

#### BinlogPeriod

Returns the <code>BinlogPeriod</code> value.

