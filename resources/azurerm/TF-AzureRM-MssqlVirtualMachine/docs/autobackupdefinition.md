# TF::AzureRM::MssqlVirtualMachine AutoBackupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptionenabled" title="EncryptionEnabled">EncryptionEnabled</a>" : <i>Boolean</i>,
    "<a href="#encryptionpassword" title="EncryptionPassword">EncryptionPassword</a>" : <i>String</i>,
    "<a href="#retentionperiodindays" title="RetentionPeriodInDays">RetentionPeriodInDays</a>" : <i>Double</i>,
    "<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>" : <i>String</i>,
    "<a href="#storageblobendpoint" title="StorageBlobEndpoint">StorageBlobEndpoint</a>" : <i>String</i>,
    "<a href="#systemdatabasesbackupenabled" title="SystemDatabasesBackupEnabled">SystemDatabasesBackupEnabled</a>" : <i>Boolean</i>,
    "<a href="#manualschedule" title="ManualSchedule">ManualSchedule</a>" : <i>[ <a href="manualscheduledefinition.md">ManualScheduleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encryptionenabled" title="EncryptionEnabled">EncryptionEnabled</a>: <i>Boolean</i>
<a href="#encryptionpassword" title="EncryptionPassword">EncryptionPassword</a>: <i>String</i>
<a href="#retentionperiodindays" title="RetentionPeriodInDays">RetentionPeriodInDays</a>: <i>Double</i>
<a href="#storageaccountaccesskey" title="StorageAccountAccessKey">StorageAccountAccessKey</a>: <i>String</i>
<a href="#storageblobendpoint" title="StorageBlobEndpoint">StorageBlobEndpoint</a>: <i>String</i>
<a href="#systemdatabasesbackupenabled" title="SystemDatabasesBackupEnabled">SystemDatabasesBackupEnabled</a>: <i>Boolean</i>
<a href="#manualschedule" title="ManualSchedule">ManualSchedule</a>: <i>
      - <a href="manualscheduledefinition.md">ManualScheduleDefinition</a></i>
</pre>

## Properties

#### EncryptionEnabled

Enable or disable encryption for backups. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionPassword

Encryption password to use. Must be specified when encryption is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPeriodInDays

Retention period of backups, in days. Valid values are from `1` to `30`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountAccessKey

Access key for the storage account where backups will be kept.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageBlobEndpoint

Blob endpoint for the storage account where backups will be kept.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDatabasesBackupEnabled

Include or exclude system databases from auto backup. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualSchedule

_Required_: No

_Type_: List of <a href="manualscheduledefinition.md">ManualScheduleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

