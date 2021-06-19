# TF::AzureRM::PostgresqlServer

Manages a PostgreSQL Server.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::PostgresqlServer",
    "Properties" : {
        "<a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>" : <i>String</i>,
        "<a href="#administratorloginpassword" title="AdministratorLoginPassword">AdministratorLoginPassword</a>" : <i>String</i>,
        "<a href="#autogrowenabled" title="AutoGrowEnabled">AutoGrowEnabled</a>" : <i>Boolean</i>,
        "<a href="#backupretentiondays" title="BackupRetentionDays">BackupRetentionDays</a>" : <i>Double</i>,
        "<a href="#createmode" title="CreateMode">CreateMode</a>" : <i>String</i>,
        "<a href="#creationsourceserverid" title="CreationSourceServerId">CreationSourceServerId</a>" : <i>String</i>,
        "<a href="#georedundantbackupenabled" title="GeoRedundantBackupEnabled">GeoRedundantBackupEnabled</a>" : <i>Boolean</i>,
        "<a href="#infrastructureencryptionenabled" title="InfrastructureEncryptionEnabled">InfrastructureEncryptionEnabled</a>" : <i>Boolean</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#sslenforcement" title="SslEnforcement">SslEnforcement</a>" : <i>String</i>,
        "<a href="#sslenforcementenabled" title="SslEnforcementEnabled">SslEnforcementEnabled</a>" : <i>Boolean</i>,
        "<a href="#sslminimaltlsversionenforced" title="SslMinimalTlsVersionEnforced">SslMinimalTlsVersionEnforced</a>" : <i>String</i>,
        "<a href="#storagemb" title="StorageMb">StorageMb</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>[ <a href="identitydefinition.md">IdentityDefinition</a>, ... ]</i>,
        "<a href="#storageprofile" title="StorageProfile">StorageProfile</a>" : <i>[ <a href="storageprofiledefinition.md">StorageProfileDefinition</a>, ... ]</i>,
        "<a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>" : <i>[ <a href="threatdetectionpolicydefinition.md">ThreatDetectionPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::PostgresqlServer
Properties:
    <a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>: <i>String</i>
    <a href="#administratorloginpassword" title="AdministratorLoginPassword">AdministratorLoginPassword</a>: <i>String</i>
    <a href="#autogrowenabled" title="AutoGrowEnabled">AutoGrowEnabled</a>: <i>Boolean</i>
    <a href="#backupretentiondays" title="BackupRetentionDays">BackupRetentionDays</a>: <i>Double</i>
    <a href="#createmode" title="CreateMode">CreateMode</a>: <i>String</i>
    <a href="#creationsourceserverid" title="CreationSourceServerId">CreationSourceServerId</a>: <i>String</i>
    <a href="#georedundantbackupenabled" title="GeoRedundantBackupEnabled">GeoRedundantBackupEnabled</a>: <i>Boolean</i>
    <a href="#infrastructureencryptionenabled" title="InfrastructureEncryptionEnabled">InfrastructureEncryptionEnabled</a>: <i>Boolean</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicnetworkaccessenabled" title="PublicNetworkAccessEnabled">PublicNetworkAccessEnabled</a>: <i>Boolean</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#sslenforcement" title="SslEnforcement">SslEnforcement</a>: <i>String</i>
    <a href="#sslenforcementenabled" title="SslEnforcementEnabled">SslEnforcementEnabled</a>: <i>Boolean</i>
    <a href="#sslminimaltlsversionenforced" title="SslMinimalTlsVersionEnforced">SslMinimalTlsVersionEnforced</a>: <i>String</i>
    <a href="#storagemb" title="StorageMb">StorageMb</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#identity" title="Identity">Identity</a>: <i>
      - <a href="identitydefinition.md">IdentityDefinition</a></i>
    <a href="#storageprofile" title="StorageProfile">StorageProfile</a>: <i>
      - <a href="storageprofiledefinition.md">StorageProfileDefinition</a></i>
    <a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>: <i>
      - <a href="threatdetectionpolicydefinition.md">ThreatDetectionPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdministratorLogin

The Administrator Login for the PostgreSQL Server. Required when `create_mode` is `Default`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdministratorLoginPassword

The Password associated with the `administrator_login` for the PostgreSQL Server. Required when `create_mode` is `Default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoGrowEnabled

Enable/Disable auto-growing of the storage. Storage auto-grow prevents your server from running out of storage and becoming read-only. If storage auto grow is enabled, the storage automatically grows without impacting the workload. The default value if not explicitly specified is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupRetentionDays

Backup retention days for the server, supported values are between `7` and `35` days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateMode

The creation mode. Can be used to restore or replicate existing servers. Possible values are `Default`, `Replica`, `GeoRestore`, and `PointInTimeRestore`. Defaults to `Default.`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationSourceServerId

For creation modes other then default the source server ID to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoRedundantBackupEnabled

Turn Geo-redundant server backups on/off. This allows you to choose between locally redundant or geo-redundant backup storage in the General Purpose and Memory Optimized tiers. When the backups are stored in geo-redundant backup storage, they are not only stored within the region in which your server is hosted, but are also replicated to a paired data center. This provides better protection and ability to restore your server in a different region in the event of a disaster. This is not support for the Basic tier. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfrastructureEncryptionEnabled

Whether or not infrastructure is encrypted for this server. Defaults to `false`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicNetworkAccessEnabled

Whether or not public network access is allowed for this server. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePointInTime

When `create_mode` is `PointInTimeRestore` the point in time to restore from `creation_source_server_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. `B_Gen4_1`, `GP_Gen5_8`). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/singleserver/servers/create#sku).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslEnforcement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslEnforcementEnabled

Specifies if SSL should be enforced on connections. Possible values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinimalTlsVersionEnforced

The mimimun TLS version to support on the sever. Possible values are `TLSEnforcementDisabled`, `TLS1_0`, `TLS1_1`, and `TLS1_2`. Defaults to `TLSEnforcementDisabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageMb

Max storage allowed for a server. Possible values are between `5120` MB(5GB) and `1048576` MB(1TB) for the Basic SKU and between `5120` MB(5GB) and `16777216` MB(16TB) for General Purpose/Memory Optimized SKUs. For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#StorageProfile).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specifies the version of PostgreSQL to use. Valid values are `9.5`, `9.6`, `10`, `10.0`, and `11`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

_Required_: No

_Type_: List of <a href="identitydefinition.md">IdentityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProfile

_Required_: No

_Type_: List of <a href="storageprofiledefinition.md">StorageProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatDetectionPolicy

_Required_: No

_Type_: List of <a href="threatdetectionpolicydefinition.md">ThreatDetectionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fqdn

Returns the <code>Fqdn</code> value.

#### Id

Returns the <code>Id</code> value.

