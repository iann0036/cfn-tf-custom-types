# TF::AzureRM::MssqlDatabase

Manages a MS SQL Database.

~> **NOTE:** The Database Extended Auditing Policy Can be set inline here as well as with the [mssql_database_extended_auditing_policy resource](mssql_database_extended_auditing_policy.html) resource. You can only use one or the other and using both will cause a conflict.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MssqlDatabase",
    "Properties" : {
        "<a href="#autopausedelayinminutes" title="AutoPauseDelayInMinutes">AutoPauseDelayInMinutes</a>" : <i>Double</i>,
        "<a href="#collation" title="Collation">Collation</a>" : <i>String</i>,
        "<a href="#createmode" title="CreateMode">CreateMode</a>" : <i>String</i>,
        "<a href="#creationsourcedatabaseid" title="CreationSourceDatabaseId">CreationSourceDatabaseId</a>" : <i>String</i>,
        "<a href="#elasticpoolid" title="ElasticPoolId">ElasticPoolId</a>" : <i>String</i>,
        "<a href="#extendedauditingpolicy" title="ExtendedAuditingPolicy">ExtendedAuditingPolicy</a>" : <i>[ <a href="extendedauditingpolicydefinition.md">ExtendedAuditingPolicyDefinition</a>, ... ]</i>,
        "<a href="#geobackupenabled" title="GeoBackupEnabled">GeoBackupEnabled</a>" : <i>Boolean</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#maxsizegb" title="MaxSizeGb">MaxSizeGb</a>" : <i>Double</i>,
        "<a href="#mincapacity" title="MinCapacity">MinCapacity</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#readreplicacount" title="ReadReplicaCount">ReadReplicaCount</a>" : <i>Double</i>,
        "<a href="#readscale" title="ReadScale">ReadScale</a>" : <i>Boolean</i>,
        "<a href="#recoverdatabaseid" title="RecoverDatabaseId">RecoverDatabaseId</a>" : <i>String</i>,
        "<a href="#restoredroppeddatabaseid" title="RestoreDroppedDatabaseId">RestoreDroppedDatabaseId</a>" : <i>String</i>,
        "<a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>" : <i>String</i>,
        "<a href="#samplename" title="SampleName">SampleName</a>" : <i>String</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>String</i>,
        "<a href="#skuname" title="SkuName">SkuName</a>" : <i>String</i>,
        "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#zoneredundant" title="ZoneRedundant">ZoneRedundant</a>" : <i>Boolean</i>,
        "<a href="#longtermretentionpolicy" title="LongTermRetentionPolicy">LongTermRetentionPolicy</a>" : <i>[ <a href="longtermretentionpolicydefinition.md">LongTermRetentionPolicyDefinition</a>, ... ]</i>,
        "<a href="#shorttermretentionpolicy" title="ShortTermRetentionPolicy">ShortTermRetentionPolicy</a>" : <i>[ <a href="shorttermretentionpolicydefinition.md">ShortTermRetentionPolicyDefinition</a>, ... ]</i>,
        "<a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>" : <i>[ <a href="threatdetectionpolicydefinition.md">ThreatDetectionPolicyDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MssqlDatabase
Properties:
    <a href="#autopausedelayinminutes" title="AutoPauseDelayInMinutes">AutoPauseDelayInMinutes</a>: <i>Double</i>
    <a href="#collation" title="Collation">Collation</a>: <i>String</i>
    <a href="#createmode" title="CreateMode">CreateMode</a>: <i>String</i>
    <a href="#creationsourcedatabaseid" title="CreationSourceDatabaseId">CreationSourceDatabaseId</a>: <i>String</i>
    <a href="#elasticpoolid" title="ElasticPoolId">ElasticPoolId</a>: <i>String</i>
    <a href="#extendedauditingpolicy" title="ExtendedAuditingPolicy">ExtendedAuditingPolicy</a>: <i>
      - <a href="extendedauditingpolicydefinition.md">ExtendedAuditingPolicyDefinition</a></i>
    <a href="#geobackupenabled" title="GeoBackupEnabled">GeoBackupEnabled</a>: <i>Boolean</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#maxsizegb" title="MaxSizeGb">MaxSizeGb</a>: <i>Double</i>
    <a href="#mincapacity" title="MinCapacity">MinCapacity</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#readreplicacount" title="ReadReplicaCount">ReadReplicaCount</a>: <i>Double</i>
    <a href="#readscale" title="ReadScale">ReadScale</a>: <i>Boolean</i>
    <a href="#recoverdatabaseid" title="RecoverDatabaseId">RecoverDatabaseId</a>: <i>String</i>
    <a href="#restoredroppeddatabaseid" title="RestoreDroppedDatabaseId">RestoreDroppedDatabaseId</a>: <i>String</i>
    <a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>: <i>String</i>
    <a href="#samplename" title="SampleName">SampleName</a>: <i>String</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>String</i>
    <a href="#skuname" title="SkuName">SkuName</a>: <i>String</i>
    <a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#zoneredundant" title="ZoneRedundant">ZoneRedundant</a>: <i>Boolean</i>
    <a href="#longtermretentionpolicy" title="LongTermRetentionPolicy">LongTermRetentionPolicy</a>: <i>
      - <a href="longtermretentionpolicydefinition.md">LongTermRetentionPolicyDefinition</a></i>
    <a href="#shorttermretentionpolicy" title="ShortTermRetentionPolicy">ShortTermRetentionPolicy</a>: <i>
      - <a href="shorttermretentionpolicydefinition.md">ShortTermRetentionPolicyDefinition</a></i>
    <a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>: <i>
      - <a href="threatdetectionpolicydefinition.md">ThreatDetectionPolicyDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoPauseDelayInMinutes

Time in minutes after which database is automatically paused. A value of `-1` means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Collation

Specifies the collation of the database. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateMode

The create mode of the database. Possible values are `Copy`, `Default`, `OnlineSecondary`, `PointInTimeRestore`, `Recovery`, `Restore`, `RestoreExternalBackup`, `RestoreExternalBackupSecondary`, `RestoreLongTermRetentionBackup` and `Secondary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationSourceDatabaseId

The id of the source database to be referred to create the new database. This should only be used for databases with `create_mode` values that use another database as reference. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticPoolId

Specifies the ID of the elastic pool containing this database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedAuditingPolicy

A `extended_auditing_policy` block as defined below.

_Required_: No

_Type_: List of <a href="extendedauditingpolicydefinition.md">ExtendedAuditingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoBackupEnabled

A boolean that specifies if the Geo Backup Policy is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

Specifies the license type applied to this database. Possible values are `LicenseIncluded` and `BasePrice`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeGb

The max size of the database in gigabytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCapacity

Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Ms SQL Database. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadReplicaCount

The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadScale

If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecoverDatabaseId

The ID of the database to be recovered. This property is only applicable when the `create_mode` is `Recovery`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestoreDroppedDatabaseId

The ID of the database to be restored. This property is only applicable when the `create_mode` is `Restore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePointInTime

Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for `create_mode`= `PointInTimeRestore`  databases.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleName

Specifies the name of the sample schema to apply when creating this database. Possible value is `AdventureWorksLT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkuName

Specifies the name of the sku used by the database. Changing this forces a new resource to be created. For example, `GP_S_Gen5_2`,`HS_Gen4_1`,`BC_Gen5_2`, `ElasticPool`, `Basic`,`S0`, `P2` ,`DW100c`, `DS100`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

Specifies the storage account type used to store backups for this database. Changing this forces a new resource to be created.  Possible values are `GRS`, `LRS` and `ZRS`.  The default value is `GRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneRedundant

Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongTermRetentionPolicy

_Required_: No

_Type_: List of <a href="longtermretentionpolicydefinition.md">LongTermRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortTermRetentionPolicy

_Required_: No

_Type_: List of <a href="shorttermretentionpolicydefinition.md">ShortTermRetentionPolicyDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

