# Terraform::AzureRM::PostgresqlServer StorageProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autogrow" title="AutoGrow">AutoGrow</a>" : <i>String</i>,
    "<a href="#backupretentiondays" title="BackupRetentionDays">BackupRetentionDays</a>" : <i>Double</i>,
    "<a href="#georedundantbackup" title="GeoRedundantBackup">GeoRedundantBackup</a>" : <i>String</i>,
    "<a href="#storagemb" title="StorageMb">StorageMb</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#autogrow" title="AutoGrow">AutoGrow</a>: <i>String</i>
<a href="#backupretentiondays" title="BackupRetentionDays">BackupRetentionDays</a>: <i>Double</i>
<a href="#georedundantbackup" title="GeoRedundantBackup">GeoRedundantBackup</a>: <i>String</i>
<a href="#storagemb" title="StorageMb">StorageMb</a>: <i>Double</i>
</pre>

## Properties

#### AutoGrow

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionDays

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRedundantBackup

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageMb

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

