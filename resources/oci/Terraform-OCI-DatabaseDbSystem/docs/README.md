# Terraform::OCI::DatabaseDbSystem

This resource provides the Db System resource in Oracle Cloud Infrastructure Database service.

Creates a new DB system in the specified compartment and availability domain. The Oracle
Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.

An initial database is created on the DB system based on the request parameters you provide and some default
options. For detailed information about default options, see the following:

- [Bare metal and virtual machine DB system default options](https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/creatingDBsystem.htm#DefaultOptionsfortheInitialDatabase)
- [Exadata DB system default options](https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/exacreatingDBsystem.htm#DefaultOptionsfortheInitialDatabase)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseDbSystem",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupsubnetid" title="BackupSubnetId">BackupSubnetId</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#datastoragepercentage" title="DataStoragePercentage">DataStoragePercentage</a>" : <i>Double</i>,
        "<a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>" : <i>Double</i>,
        "<a href="#databaseedition" title="DatabaseEdition">DatabaseEdition</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#diskredundancy" title="DiskRedundancy">DiskRedundancy</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#faultdomains" title="FaultDomains">FaultDomains</a>" : <i>[ String, ... ]</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#shape" title="Shape">Shape</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sparsediskgroup" title="SparseDiskgroup">SparseDiskgroup</a>" : <i>Boolean</i>,
        "<a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#dbhome" title="DbHome">DbHome</a>" : <i>[ <a href="dbhome.md">DbHome</a>, ... ]</i>,
        "<a href="#dbsystemoptions" title="DbSystemOptions">DbSystemOptions</a>" : <i>[ <a href="dbsystemoptions.md">DbSystemOptions</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="database.md">Database</a>, ... ]</i>,
        "<a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>" : <i>[ <a href="dbbackupconfig.md">DbBackupConfig</a>, ... ]</i>,
        "<a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>" : <i>[ <a href="backupdestinationdetails.md">BackupDestinationDetails</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseDbSystem
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>: <i>
      - String</i>
    <a href="#backupsubnetid" title="BackupSubnetId">BackupSubnetId</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#datastoragepercentage" title="DataStoragePercentage">DataStoragePercentage</a>: <i>Double</i>
    <a href="#datastoragesizeingb" title="DataStorageSizeInGb">DataStorageSizeInGb</a>: <i>Double</i>
    <a href="#databaseedition" title="DatabaseEdition">DatabaseEdition</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#diskredundancy" title="DiskRedundancy">DiskRedundancy</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#faultdomains" title="FaultDomains">FaultDomains</a>: <i>
      - String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#shape" title="Shape">Shape</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sparsediskgroup" title="SparseDiskgroup">SparseDiskgroup</a>: <i>Boolean</i>
    <a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>: <i>
      - String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#dbhome" title="DbHome">DbHome</a>: <i>
      - <a href="dbhome.md">DbHome</a></i>
    <a href="#dbsystemoptions" title="DbSystemOptions">DbSystemOptions</a>: <i>
      - <a href="dbsystemoptions.md">DbSystemOptions</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="database.md">Database</a></i>
    <a href="#dbbackupconfig" title="DbBackupConfig">DbBackupConfig</a>: <i>
      - <a href="dbbackupconfig.md">DbBackupConfig</a></i>
    <a href="#backupdestinationdetails" title="BackupDestinationDetails">BackupDestinationDetails</a>: <i>
      - <a href="backupdestinationdetails.md">BackupDestinationDetails</a></i>
</pre>

## Properties

#### AvailabilityDomain

The availability domain where the DB system is located.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupNetworkNsgIds

(Updatable) A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata DB systems.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupSubnetId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated with. Applicable only to Exadata DB systems.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment the DB system  belongs in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

(Updatable) The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:
* BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36.
* BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52.
* Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
* Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
* Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
* Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
* Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
* Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
* Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStoragePercentage

The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInGb

(Updatable) Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and software volume.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseEdition

The Oracle Database Edition that applies to all the databases on the DB system. Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskRedundancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparseDiskgroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKeys

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbHome

_Required_: No

_Type_: List of <a href="dbhome.md">DbHome</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbSystemOptions

_Required_: No

_Type_: List of <a href="dbsystemoptions.md">DbSystemOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="database.md">Database</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbBackupConfig

_Required_: No

_Type_: List of <a href="dbbackupconfig.md">DbBackupConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupDestinationDetails

_Required_: No

_Type_: List of <a href="backupdestinationdetails.md">BackupDestinationDetails</a>

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

#### IormConfigCache

Returns the <code>IormConfigCache</code> value.

#### LastPatchHistoryEntryId

Returns the <code>LastPatchHistoryEntryId</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### ListenerPort

Returns the <code>ListenerPort</code> value.

#### RecoStorageSizeInGb

Returns the <code>RecoStorageSizeInGb</code> value.

#### ScanDnsRecordId

Returns the <code>ScanDnsRecordId</code> value.

#### ScanIpIds

Returns the <code>ScanIpIds</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### Version

Returns the <code>Version</code> value.

#### VipIds

Returns the <code>VipIds</code> value.

