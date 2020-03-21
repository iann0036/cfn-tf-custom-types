# Terraform::OCI::DatabaseAutonomousDatabase

This resource provides the Autonomous Database resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Database.
Note: `whitelisted_ips` cannot be used during creation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseAutonomousDatabase",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>" : <i>String</i>,
        "<a href="#autonomousdatabasebackupid" title="AutonomousDatabaseBackupId">AutonomousDatabaseBackupId</a>" : <i>String</i>,
        "<a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>" : <i>String</i>,
        "<a href="#clonetype" title="CloneType">CloneType</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>" : <i>Double</i>,
        "<a href="#datasafestatus" title="DataSafeStatus">DataSafeStatus</a>" : <i>String</i>,
        "<a href="#datastoragesizeintbs" title="DataStorageSizeInTbs">DataStorageSizeInTbs</a>" : <i>Double</i>,
        "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#dbworkload" title="DbWorkload">DbWorkload</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>" : <i>Boolean</i>,
        "<a href="#isdedicated" title="IsDedicated">IsDedicated</a>" : <i>Boolean</i>,
        "<a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>" : <i>Boolean</i>,
        "<a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>" : <i>Boolean</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceid" title="SourceId">SourceId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#timestamp" title="Timestamp">Timestamp</a>" : <i>String</i>,
        "<a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseAutonomousDatabase
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#autonomouscontainerdatabaseid" title="AutonomousContainerDatabaseId">AutonomousContainerDatabaseId</a>: <i>String</i>
    <a href="#autonomousdatabasebackupid" title="AutonomousDatabaseBackupId">AutonomousDatabaseBackupId</a>: <i>String</i>
    <a href="#autonomousdatabaseid" title="AutonomousDatabaseId">AutonomousDatabaseId</a>: <i>String</i>
    <a href="#clonetype" title="CloneType">CloneType</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#cpucorecount" title="CpuCoreCount">CpuCoreCount</a>: <i>Double</i>
    <a href="#datasafestatus" title="DataSafeStatus">DataSafeStatus</a>: <i>String</i>
    <a href="#datastoragesizeintbs" title="DataStorageSizeInTbs">DataStorageSizeInTbs</a>: <i>Double</i>
    <a href="#dbname" title="DbName">DbName</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#dbworkload" title="DbWorkload">DbWorkload</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>: <i>Boolean</i>
    <a href="#isdedicated" title="IsDedicated">IsDedicated</a>: <i>Boolean</i>
    <a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>: <i>Boolean</i>
    <a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>: <i>Boolean</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceid" title="SourceId">SourceId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#timestamp" title="Timestamp">Timestamp</a>: <i>String</i>
    <a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminPassword

(Updatable) The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (") or the username "admin", regardless of casing.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousContainerDatabaseId

The Autonomous Container Database [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousDatabaseBackupId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source Autonomous Database Backup that you will clone to create a new Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousDatabaseId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create a new Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloneType

The Autonomous Database clone type.
* `FULL` - This option creates a new database that includes all source database data.
* `METADATA` - This option creates a new database that includes the source database schema and select metadata, but not the source database data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment of the Autonomous Database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCoreCount

(Updatable) The number of OCPU cores to be made available to the database. This input is ignored for Always Free resources.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSafeStatus

(Updatable) Target status of the Data Safe registration for this Autonomous Database. Could be set to REGISTERED or NOT_REGISTERED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInTbs

(Updatable) The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. This input is ignored for Always Free resources.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

A valid Oracle Database version for Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

The Autonomous Database workload type. The following values are valid:
* OLTP - indicates an Autonomous Transaction Processing database
* DW - indicates an Autonomous Data Warehouse database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The user-friendly name for the Autonomous Database. The name does not have to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoScalingEnabled

(Updatable) Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`. Note that auto scaling is available for databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI) only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDedicated

True if the database is on [dedicated Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adbddoverview.htm).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFreeTier

(Updatable) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPreviewVersionWithServiceTermsAccepted

If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

(Updatable) The Oracle license model that applies to the Oracle Autonomous Database. Note that when provisioning an Autonomous Database on [dedicated Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adbddoverview.htm), this attribute must be null because the attribute is already set at the  Autonomous Exadata Infrastructure level. When using [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

(Updatable) A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:**
* Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpointLabel

The private endpoint label for the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning an existing Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create a new Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timestamp

The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhitelistedIps

(Updatable) The client IP access control list (ACL). This feature is available for databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI) only. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID. To add the whitelist VCN specific subnet or IP, use a semicoln ';' as a deliminator to add the VCN specific subnets or IPs. Example: `["1.1.1.1","1.1.1.0/24","ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw","ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw;1.1.1.1","ocid1.vcn.oc1.sea.aaaaaaaard2hfx2nn3e5xeo6j6o62jga44xjizkw;1.1.0.0/16"]`. To remove all whitelisted IPs, set the field to a list with an empty string `[""]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### ConnectionUrls

Returns the <code>ConnectionUrls</code> value.

#### IsPreview

Returns the <code>IsPreview</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### PrivateEndpoint

Returns the <code>PrivateEndpoint</code> value.

#### ServiceConsoleUrl

Returns the <code>ServiceConsoleUrl</code> value.

#### State

Returns the <code>State</code> value.

#### SystemTags

Returns the <code>SystemTags</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeDeletionOfFreeAutonomousDatabase

Returns the <code>TimeDeletionOfFreeAutonomousDatabase</code> value.

#### TimeMaintenanceBegin

Returns the <code>TimeMaintenanceBegin</code> value.

#### TimeMaintenanceEnd

Returns the <code>TimeMaintenanceEnd</code> value.

#### TimeReclamationOfFreeAutonomousDatabase

Returns the <code>TimeReclamationOfFreeAutonomousDatabase</code> value.

#### UsedDataStorageSizeInTbs

Returns the <code>UsedDataStorageSizeInTbs</code> value.

