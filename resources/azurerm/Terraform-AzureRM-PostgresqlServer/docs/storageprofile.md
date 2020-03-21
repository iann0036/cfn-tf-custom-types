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

Enable/Disable auto-growing of the storage. Valid values for this property are `Enabled` or `Disabled`. Storage auto-grow prevents your server from running out of storage and becoming read-only. If storage auto grow is enabled, the storage automatically grows without impacting the workload. The default value if not explicitly specified is `Enabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionDays

Backup retention days for the server, supported values are between `7` and `35` days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRedundantBackup

Enable/Disable Geo-redundant for server backup. Valid values for this property are `Enabled` or `Disabled`, not supported for the `basic` tier.  This allows you to choose between locally redundant or geo-redundant backup storage in the General Purpose and Memory Optimized tiers. When the backups are stored in geo-redundant backup storage, they are not only stored within the region in which your server is hosted, but are also replicated to a paired data center. This provides better protection and ability to restore your server in a different region in the event of a disaster. The Basic tier only offers locally redundant backup storage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageMb

Max storage allowed for a server. Possible values are between `5120` MB(5GB) and `1048576` MB(1TB) for the Basic SKU and between `5120` MB(5GB) and `4194304` MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#StorageProfile).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

