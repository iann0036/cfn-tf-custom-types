# Terraform::AzureRM::MysqlServer StorageProfile

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

Defines whether autogrow is enabled or disabled for the storage. Valid values are `Enabled` or `Disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionDays

Backup retention days for the server, supported values are between `7` and `35` days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRedundantBackup

Enable Geo-redundant or not for server backup. Valid values for this property are `Enabled` or `Disabled`, not supported for the `basic` tier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageMb

Max storage allowed for a server. Possible values are between `5120` MB(5GB) and `1048576` MB(1TB) for the Basic SKU and between `5120` MB(5GB) and `4194304` MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#StorageProfile).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

