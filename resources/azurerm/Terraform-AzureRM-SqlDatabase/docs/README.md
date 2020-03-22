# Terraform::AzureRM::SqlDatabase

Allows you to manage an Azure SQL Database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::SqlDatabase",
    "Properties" : {
        "<a href="#collation" title="Collation">Collation</a>" : <i>String</i>,
        "<a href="#createmode" title="CreateMode">CreateMode</a>" : <i>String</i>,
        "<a href="#edition" title="Edition">Edition</a>" : <i>String</i>,
        "<a href="#elasticpoolname" title="ElasticPoolName">ElasticPoolName</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxsizebytes" title="MaxSizeBytes">MaxSizeBytes</a>" : <i>String</i>,
        "<a href="#maxsizegb" title="MaxSizeGb">MaxSizeGb</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#readscale" title="ReadScale">ReadScale</a>" : <i>Boolean</i>,
        "<a href="#requestedserviceobjectiveid" title="RequestedServiceObjectiveId">RequestedServiceObjectiveId</a>" : <i>String</i>,
        "<a href="#requestedserviceobjectivename" title="RequestedServiceObjectiveName">RequestedServiceObjectiveName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#sourcedatabasedeletiondate" title="SourceDatabaseDeletionDate">SourceDatabaseDeletionDate</a>" : <i>String</i>,
        "<a href="#sourcedatabaseid" title="SourceDatabaseId">SourceDatabaseId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#zoneredundant" title="ZoneRedundant">ZoneRedundant</a>" : <i>Boolean</i>,
        "<a href="#extendedauditingpolicy" title="ExtendedAuditingPolicy">ExtendedAuditingPolicy</a>" : <i>[ <a href="extendedauditingpolicy.md">ExtendedAuditingPolicy</a>, ... ]</i>,
        "<a href="#import" title="Import">Import</a>" : <i>[ <a href="import.md">Import</a>, ... ]</i>,
        "<a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>" : <i>[ <a href="threatdetectionpolicy.md">ThreatDetectionPolicy</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::SqlDatabase
Properties:
    <a href="#collation" title="Collation">Collation</a>: <i>String</i>
    <a href="#createmode" title="CreateMode">CreateMode</a>: <i>String</i>
    <a href="#edition" title="Edition">Edition</a>: <i>String</i>
    <a href="#elasticpoolname" title="ElasticPoolName">ElasticPoolName</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxsizebytes" title="MaxSizeBytes">MaxSizeBytes</a>: <i>String</i>
    <a href="#maxsizegb" title="MaxSizeGb">MaxSizeGb</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#readscale" title="ReadScale">ReadScale</a>: <i>Boolean</i>
    <a href="#requestedserviceobjectiveid" title="RequestedServiceObjectiveId">RequestedServiceObjectiveId</a>: <i>String</i>
    <a href="#requestedserviceobjectivename" title="RequestedServiceObjectiveName">RequestedServiceObjectiveName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#restorepointintime" title="RestorePointInTime">RestorePointInTime</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#sourcedatabasedeletiondate" title="SourceDatabaseDeletionDate">SourceDatabaseDeletionDate</a>: <i>String</i>
    <a href="#sourcedatabaseid" title="SourceDatabaseId">SourceDatabaseId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#zoneredundant" title="ZoneRedundant">ZoneRedundant</a>: <i>Boolean</i>
    <a href="#extendedauditingpolicy" title="ExtendedAuditingPolicy">ExtendedAuditingPolicy</a>: <i>
      - <a href="extendedauditingpolicy.md">ExtendedAuditingPolicy</a></i>
    <a href="#import" title="Import">Import</a>: <i>
      - <a href="import.md">Import</a></i>
    <a href="#threatdetectionpolicy" title="ThreatDetectionPolicy">ThreatDetectionPolicy</a>: <i>
      - <a href="threatdetectionpolicy.md">ThreatDetectionPolicy</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Collation

The name of the collation. Applies only if `create_mode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateMode

Specifies how to create the database. Valid values are: `Default`, `Copy`, `OnlineSecondary`, `NonReadableSecondary`,  `PointInTimeRestore`, `Recovery`, `Restore` or `RestoreLongTermRetentionBackup`. Must be `Default` to create a new database. Defaults to `Default`. Please see [Azure SQL Database REST API](https://docs.microsoft.com/en-us/rest/api/sql/databases/createorupdate#createmode).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Edition

The edition of the database to be created. Applies only if `create_mode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, `DataWarehouse`, `Business`, `BusinessCritical`, `Free`, `GeneralPurpose`, `Hyperscale`, `Premium`, `PremiumRS`, `Standard`, `Stretch`, `System`, `System2`, or `Web`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticPoolName

The name of the elastic database pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeBytes

The maximum size that the database can grow to. Applies only if `create_mode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSizeGb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadScale

Read-only connections will be redirected to a high-available replica. Please see [Use read-only replicas to load-balance read-only query workloads](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-read-scale-out).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedServiceObjectiveId

A GUID/UUID corresponding to a configured Service Level Objective for the Azure SQL database which can be used to configure a performance level.
.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedServiceObjectiveName

The service objective name for the database. Valid values depend on edition and location and may include `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`. You can list the available names with the cli: ```shell az sql db list-editions -l westus --edition Standard -o table ```. For further information please see [Azure CLI - az sql db](https://docs.microsoft.com/en-us/cli/azure/sql/db?view=azure-cli-latest#az-sql-db-list-editions).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePointInTime

The point in time for the restore. Only applies if `create_mode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

The name of the SQL Server on which to create the database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatabaseDeletionDate

The deletion date time of the source database. Only applies to deleted databases where `create_mode` is `PointInTimeRestore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDatabaseId

The URI of the source database if `create_mode` value is not `Default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneRedundant

Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedAuditingPolicy

_Required_: No

_Type_: List of <a href="extendedauditingpolicy.md">ExtendedAuditingPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Import

_Required_: No

_Type_: List of <a href="import.md">Import</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatDetectionPolicy

_Required_: No

_Type_: List of <a href="threatdetectionpolicy.md">ThreatDetectionPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### DefaultSecondaryLocation

Returns the <code>DefaultSecondaryLocation</code> value.

#### Encryption

Returns the <code>Encryption</code> value.

#### Id

Returns the <code>Id</code> value.

