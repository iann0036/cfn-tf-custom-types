# Terraform::AzureRM::RedisCache RedisConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aofbackupenabled" title="AofBackupEnabled">AofBackupEnabled</a>" : <i>Boolean</i>,
    "<a href="#aofstorageconnectionstring0" title="AofStorageConnectionString0">AofStorageConnectionString0</a>" : <i>String</i>,
    "<a href="#aofstorageconnectionstring1" title="AofStorageConnectionString1">AofStorageConnectionString1</a>" : <i>String</i>,
    "<a href="#enableauthentication" title="EnableAuthentication">EnableAuthentication</a>" : <i>Boolean</i>,
    "<a href="#maxfragmentationmemoryreserved" title="MaxfragmentationmemoryReserved">MaxfragmentationmemoryReserved</a>" : <i>Double</i>,
    "<a href="#maxmemorydelta" title="MaxmemoryDelta">MaxmemoryDelta</a>" : <i>Double</i>,
    "<a href="#maxmemorypolicy" title="MaxmemoryPolicy">MaxmemoryPolicy</a>" : <i>String</i>,
    "<a href="#maxmemoryreserved" title="MaxmemoryReserved">MaxmemoryReserved</a>" : <i>Double</i>,
    "<a href="#notifykeyspaceevents" title="NotifyKeyspaceEvents">NotifyKeyspaceEvents</a>" : <i>String</i>,
    "<a href="#rdbbackupenabled" title="RdbBackupEnabled">RdbBackupEnabled</a>" : <i>Boolean</i>,
    "<a href="#rdbbackupfrequency" title="RdbBackupFrequency">RdbBackupFrequency</a>" : <i>Double</i>,
    "<a href="#rdbbackupmaxsnapshotcount" title="RdbBackupMaxSnapshotCount">RdbBackupMaxSnapshotCount</a>" : <i>Double</i>,
    "<a href="#rdbstorageconnectionstring" title="RdbStorageConnectionString">RdbStorageConnectionString</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aofbackupenabled" title="AofBackupEnabled">AofBackupEnabled</a>: <i>Boolean</i>
<a href="#aofstorageconnectionstring0" title="AofStorageConnectionString0">AofStorageConnectionString0</a>: <i>String</i>
<a href="#aofstorageconnectionstring1" title="AofStorageConnectionString1">AofStorageConnectionString1</a>: <i>String</i>
<a href="#enableauthentication" title="EnableAuthentication">EnableAuthentication</a>: <i>Boolean</i>
<a href="#maxfragmentationmemoryreserved" title="MaxfragmentationmemoryReserved">MaxfragmentationmemoryReserved</a>: <i>Double</i>
<a href="#maxmemorydelta" title="MaxmemoryDelta">MaxmemoryDelta</a>: <i>Double</i>
<a href="#maxmemorypolicy" title="MaxmemoryPolicy">MaxmemoryPolicy</a>: <i>String</i>
<a href="#maxmemoryreserved" title="MaxmemoryReserved">MaxmemoryReserved</a>: <i>Double</i>
<a href="#notifykeyspaceevents" title="NotifyKeyspaceEvents">NotifyKeyspaceEvents</a>: <i>String</i>
<a href="#rdbbackupenabled" title="RdbBackupEnabled">RdbBackupEnabled</a>: <i>Boolean</i>
<a href="#rdbbackupfrequency" title="RdbBackupFrequency">RdbBackupFrequency</a>: <i>Double</i>
<a href="#rdbbackupmaxsnapshotcount" title="RdbBackupMaxSnapshotCount">RdbBackupMaxSnapshotCount</a>: <i>Double</i>
<a href="#rdbstorageconnectionstring" title="RdbStorageConnectionString">RdbStorageConnectionString</a>: <i>String</i>
</pre>

## Properties

#### AofBackupEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AofStorageConnectionString0

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AofStorageConnectionString1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAuthentication

If set to `false`, the Redis instance will be accessible without authentication. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxfragmentationmemoryReserved

Value in megabytes reserved to accommodate for memory fragmentation. Defaults are shown below.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxmemoryDelta

The max-memory delta for this Redis instance. Defaults are shown below.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxmemoryPolicy

How Redis will select what to remove when `maxmemory` is reached. Defaults are shown below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxmemoryReserved

Value in megabytes reserved for non-cache usage e.g. failover. Defaults are shown below.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyKeyspaceEvents

Keyspace notifications allows clients to subscribe to Pub/Sub channels in order to receive events affecting the Redis data set in some way. [Reference](https://redis.io/topics/notifications#configuration).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdbBackupEnabled

Is Backup Enabled? Only supported on Premium SKU's.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdbBackupFrequency

The Backup Frequency in Minutes. Only supported on Premium SKU's. Possible values are: `15`, `30`, `60`, `360`, `720` and `1440`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdbBackupMaxSnapshotCount

The maximum number of snapshots to create as a backup. Only supported for Premium SKU's.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdbStorageConnectionString

The Connection String to the Storage Account. Only supported for Premium SKU's. In the format: `DefaultEndpointsProtocol=https;BlobEndpoint=${azurerm_storage_account.example.primary_blob_endpoint};AccountName=${azurerm_storage_account.example.name};AccountKey=${azurerm_storage_account.example.primary_access_key}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

