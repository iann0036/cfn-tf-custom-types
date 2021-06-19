# TF::GoogleBeta::GoogleSqlDatabaseInstance BackupConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#binarylogenabled" title="BinaryLogEnabled">BinaryLogEnabled</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#pointintimerecoveryenabled" title="PointInTimeRecoveryEnabled">PointInTimeRecoveryEnabled</a>" : <i>Boolean</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#transactionlogretentiondays" title="TransactionLogRetentionDays">TransactionLogRetentionDays</a>" : <i>Double</i>,
    "<a href="#backupretentionsettings" title="BackupRetentionSettings">BackupRetentionSettings</a>" : <i>[ <a href="backupretentionsettingsdefinition.md">BackupRetentionSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#binarylogenabled" title="BinaryLogEnabled">BinaryLogEnabled</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#pointintimerecoveryenabled" title="PointInTimeRecoveryEnabled">PointInTimeRecoveryEnabled</a>: <i>Boolean</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#transactionlogretentiondays" title="TransactionLogRetentionDays">TransactionLogRetentionDays</a>: <i>Double</i>
<a href="#backupretentionsettings" title="BackupRetentionSettings">BackupRetentionSettings</a>: <i>
      - <a href="backupretentionsettingsdefinition.md">BackupRetentionSettingsDefinition</a></i>
</pre>

## Properties

#### BinaryLogEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointInTimeRecoveryEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransactionLogRetentionDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionSettings

_Required_: No

_Type_: List of <a href="backupretentionsettingsdefinition.md">BackupRetentionSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

