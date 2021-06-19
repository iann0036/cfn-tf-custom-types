# TF::OCI::DatabaseCloudVmCluster

This resource provides the Cloud Vm Cluster resource in Oracle Cloud Infrastructure Database service.

Creates a cloud VM cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseCloudVmCluster",
    "Properties" : {
        "<a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupsubnetid" title="BackupSubnetId">BackupSubnetId</a>" : <i>String</i>,
        "<a href="#cloudexadatainfrastructureid" title="CloudExadataInfrastructureId">CloudExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#createasync" title="CreateAsync">CreateAsync</a>" : <i>Boolean</i>,
        "<a href="#datastoragepercentage" title="DataStoragePercentage">DataStoragePercentage</a>" : <i>Double</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#giversion" title="GiVersion">GiVersion</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#islocalbackupenabled" title="IsLocalBackupEnabled">IsLocalBackupEnabled</a>" : <i>Boolean</i>,
        "<a href="#issparsediskgroupenabled" title="IsSparseDiskgroupEnabled">IsSparseDiskgroupEnabled</a>" : <i>Boolean</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseCloudVmCluster
Properties:
    <a href="#backupnetworknsgids" title="BackupNetworkNsgIds">BackupNetworkNsgIds</a>: <i>
      - String</i>
    <a href="#backupsubnetid" title="BackupSubnetId">BackupSubnetId</a>: <i>String</i>
    <a href="#cloudexadatainfrastructureid" title="CloudExadataInfrastructureId">CloudExadataInfrastructureId</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#createasync" title="CreateAsync">CreateAsync</a>: <i>Boolean</i>
    <a href="#datastoragepercentage" title="DataStoragePercentage">DataStoragePercentage</a>: <i>Double</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#giversion" title="GiVersion">GiVersion</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#islocalbackupenabled" title="IsLocalBackupEnabled">IsLocalBackupEnabled</a>: <i>Boolean</i>
    <a href="#issparsediskgroupenabled" title="IsSparseDiskgroupEnabled">IsSparseDiskgroupEnabled</a>: <i>Boolean</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#sshpublickeys" title="SshPublicKeys">SshPublicKeys</a>: <i>
      - String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BackupNetworkNsgIds

(Updatable) A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata systems.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupSubnetId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup network subnet associated with the cloud VM cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudExadataInfrastructureId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

(Updatable) The number of CPU cores to enable for a cloud VM cluster. Valid values depend on the specified shape:
* Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
* Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
* Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
* Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
* Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
* Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
* Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateAsync

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStoragePercentage

The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40, 60 and 80. The default is 80 percent assigned to DATA storage. See [Storage Configuration](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm#Exadata) in the Exadata documentation for details on the impact of the configuration settings on storage.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The user-friendly name for the cloud VM cluster. The name does not need to be unique.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

A domain name used for the cloud VM cluster. If the Oracle-provided internet and VCN resolver is enabled for the specified subnet, the domain name for the subnet is used (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted. Applies to Exadata Cloud Service instances only.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GiVersion

A valid Oracle Grid Infrastructure (GI) software version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname for the cloud VM cluster. The hostname must begin with an alphabetic character, and can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB systems, and 12 characters for Exadata systems.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsLocalBackupEnabled

If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is not available in the cloud VM cluster.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSparseDiskgroupEnabled

If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

(Updatable) The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

(Updatable) A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:**
* Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKeys

(Updatable) The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet associated with the cloud VM cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

The time zone to use for the cloud VM cluster. For details, see [Time Zones](https://docs.cloud.oracle.com/iaas/Content/Database/References/timezones.htm).

_Required_: No

_Type_: String

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

#### AvailabilityDomain

Returns the <code>AvailabilityDomain</code> value.

#### DiskRedundancy

Returns the <code>DiskRedundancy</code> value.

#### Id

Returns the <code>Id</code> value.

#### IormConfigCache

Returns the <code>IormConfigCache</code> value.

#### LastUpdateHistoryEntryId

Returns the <code>LastUpdateHistoryEntryId</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### ListenerPort

Returns the <code>ListenerPort</code> value.

#### NodeCount

Returns the <code>NodeCount</code> value.

#### ScanDnsName

Returns the <code>ScanDnsName</code> value.

#### ScanDnsRecordId

Returns the <code>ScanDnsRecordId</code> value.

#### ScanIpIds

Returns the <code>ScanIpIds</code> value.

#### Shape

Returns the <code>Shape</code> value.

#### State

Returns the <code>State</code> value.

#### StorageSizeInGbs

Returns the <code>StorageSizeInGbs</code> value.

#### SystemVersion

Returns the <code>SystemVersion</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VipIds

Returns the <code>VipIds</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.

