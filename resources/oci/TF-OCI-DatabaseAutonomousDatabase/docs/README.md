# TF::OCI::DatabaseAutonomousDatabase

This resource provides the Autonomous Database resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Database.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseAutonomousDatabase",
    "Properties" : {
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#areprimarywhitelistedipsused" title="ArePrimaryWhitelistedIpsUsed">ArePrimaryWhitelistedIpsUsed</a>" : <i>Boolean</i>,
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
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#isaccesscontrolenabled" title="IsAccessControlEnabled">IsAccessControlEnabled</a>" : <i>Boolean</i>,
        "<a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>" : <i>Boolean</i>,
        "<a href="#isdataguardenabled" title="IsDataGuardEnabled">IsDataGuardEnabled</a>" : <i>Boolean</i>,
        "<a href="#isdedicated" title="IsDedicated">IsDedicated</a>" : <i>Boolean</i>,
        "<a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>" : <i>Boolean</i>,
        "<a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>" : <i>Boolean</i>,
        "<a href="#isrefreshableclone" title="IsRefreshableClone">IsRefreshableClone</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#licensemodel" title="LicenseModel">LicenseModel</a>" : <i>String</i>,
        "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#openmode" title="OpenMode">OpenMode</a>" : <i>String</i>,
        "<a href="#operationsinsightsstatus" title="OperationsInsightsStatus">OperationsInsightsStatus</a>" : <i>String</i>,
        "<a href="#permissionlevel" title="PermissionLevel">PermissionLevel</a>" : <i>String</i>,
        "<a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>" : <i>String</i>,
        "<a href="#refreshablemode" title="RefreshableMode">RefreshableMode</a>" : <i>String</i>,
        "<a href="#rotatekeytrigger" title="RotateKeyTrigger">RotateKeyTrigger</a>" : <i>Boolean</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceid" title="SourceId">SourceId</a>" : <i>String</i>,
        "<a href="#standbywhitelistedips" title="StandbyWhitelistedIps">StandbyWhitelistedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#switchoverto" title="SwitchoverTo">SwitchoverTo</a>" : <i>String</i>,
        "<a href="#timestamp" title="Timestamp">Timestamp</a>" : <i>String</i>,
        "<a href="#vaultid" title="VaultId">VaultId</a>" : <i>String</i>,
        "<a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#customercontacts" title="CustomerContacts">CustomerContacts</a>" : <i>[ <a href="customercontactsdefinition.md">CustomerContactsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseAutonomousDatabase
Properties:
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#areprimarywhitelistedipsused" title="ArePrimaryWhitelistedIpsUsed">ArePrimaryWhitelistedIpsUsed</a>: <i>Boolean</i>
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
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#isaccesscontrolenabled" title="IsAccessControlEnabled">IsAccessControlEnabled</a>: <i>Boolean</i>
    <a href="#isautoscalingenabled" title="IsAutoScalingEnabled">IsAutoScalingEnabled</a>: <i>Boolean</i>
    <a href="#isdataguardenabled" title="IsDataGuardEnabled">IsDataGuardEnabled</a>: <i>Boolean</i>
    <a href="#isdedicated" title="IsDedicated">IsDedicated</a>: <i>Boolean</i>
    <a href="#isfreetier" title="IsFreeTier">IsFreeTier</a>: <i>Boolean</i>
    <a href="#ispreviewversionwithservicetermsaccepted" title="IsPreviewVersionWithServiceTermsAccepted">IsPreviewVersionWithServiceTermsAccepted</a>: <i>Boolean</i>
    <a href="#isrefreshableclone" title="IsRefreshableClone">IsRefreshableClone</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#licensemodel" title="LicenseModel">LicenseModel</a>: <i>String</i>
    <a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
    <a href="#openmode" title="OpenMode">OpenMode</a>: <i>String</i>
    <a href="#operationsinsightsstatus" title="OperationsInsightsStatus">OperationsInsightsStatus</a>: <i>String</i>
    <a href="#permissionlevel" title="PermissionLevel">PermissionLevel</a>: <i>String</i>
    <a href="#privateendpointlabel" title="PrivateEndpointLabel">PrivateEndpointLabel</a>: <i>String</i>
    <a href="#refreshablemode" title="RefreshableMode">RefreshableMode</a>: <i>String</i>
    <a href="#rotatekeytrigger" title="RotateKeyTrigger">RotateKeyTrigger</a>: <i>Boolean</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceid" title="SourceId">SourceId</a>: <i>String</i>
    <a href="#standbywhitelistedips" title="StandbyWhitelistedIps">StandbyWhitelistedIps</a>: <i>
      - String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#switchoverto" title="SwitchoverTo">SwitchoverTo</a>: <i>String</i>
    <a href="#timestamp" title="Timestamp">Timestamp</a>: <i>String</i>
    <a href="#vaultid" title="VaultId">VaultId</a>: <i>String</i>
    <a href="#whitelistedips" title="WhitelistedIps">WhitelistedIps</a>: <i>
      - String</i>
    <a href="#customercontacts" title="CustomerContacts">CustomerContacts</a>: <i>
      - <a href="customercontactsdefinition.md">CustomerContactsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AdminPassword

(Updatable) The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (") or the username "admin", regardless of casing. The password is mandatory if source value is "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "DATABASE" or "NONE".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArePrimaryWhitelistedIpsUsed

(Updatable) This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled. It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby. It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.

_Required_: No

_Type_: Boolean

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

(Updatable) Status of the Data Safe registration for this Autonomous Database. Could be REGISTERED or NOT_REGISTERED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataStorageSizeInTbs

(Updatable) The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. This input is ignored for Always Free resources.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

(Updatable) A valid Oracle Database version for Autonomous Database.`db_workload` AJD and APEX are only supported for `db_version` `19c` and above.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbWorkload

(Updatable) The Autonomous Database workload type. The following values are valid:
* OLTP - indicates an Autonomous Transaction Processing database
* DW - indicates an Autonomous Data Warehouse database
* AJD - indicates an Autonomous JSON Database
* APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type. *Note: `db_workload` can only be updated from AJD to OLTP or from a free OLTP to AJD.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The user-friendly name for the Autonomous Database. The name does not have to be unique.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAccessControlEnabled

(Updatable) Indicates if the database-level access control is enabled. If disabled, database access is defined by the network security rules. If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional, if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console. When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoScalingEnabled

(Updatable) Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDataGuardEnabled

(Updatable) Indicates whether the Autonomous Database has Data Guard enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDedicated

True if the database is on [dedicated Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adbddoverview.htm).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFreeTier

(Updatable) Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled. When `db_workload` is `AJD` or `APEX` it cannot be `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPreviewVersionWithServiceTermsAccepted

If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRefreshableClone

(Updatable) True for creating a refreshable clone and False for detaching the clone from source Autonomous Database. Detaching is one time operation and clone becomes a regular Autonomous Database.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseModel

(Updatable) The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud. License Included allows you to subscribe to new Oracle Database software licenses and the Database service. Note that when provisioning an Autonomous Database on [dedicated Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adbddoverview.htm), this attribute must be null because the attribute is already set at the Autonomous Exadata Infrastructure level. When using [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`. It is a required field when `db_workload` is AJD and needs to be set to `LICENSE_INCLUDED` as AJD does not support default `license_model` value `BRING_YOUR_OWN_LICENSE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

(Updatable) A list of the [OCIDs](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see [Security Rules](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securityrules.htm). **NsgIds restrictions:**
* Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationsInsightsStatus

(Updatable) Status of Operations Insights for this Autonomous Database. Values supported are `ENABLED` and `NOT_ENABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateEndpointLabel

(Updatable) The private endpoint label for the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshableMode

(Updatable) The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotateKeyTrigger

(Updatable) An optional property when flipped triggers rotation of KMS key. It is only applicable on dedicated databases i.e. where `is_dedicated` is true.

_Required_: No

_Type_: Boolean

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

#### StandbyWhitelistedIps

(Updatable) The client IP access control list (ACL). This feature is available for autonomous databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI) and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

(Updatable) The current state of the Autonomous Database. Could be set to AVAILABLE or STOPPED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchoverTo

It is applicable only when `is_data_guard_enabled` is true. Could be set to `PRIMARY` or `STANDBY`. Default value is `PRIMARY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timestamp

The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure [vault](https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhitelistedIps

(Updatable) The client IP access control list (ACL). This feature is available for autonomous databases on [shared Exadata infrastructure](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adboverview.htm#AEI) and on Exadata Cloud@Customer. Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerContacts

_Required_: No

_Type_: List of <a href="customercontactsdefinition.md">CustomerContactsDefinition</a>

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

#### ApexDetails

Returns the <code>ApexDetails</code> value.

#### AvailableUpgradeVersions

Returns the <code>AvailableUpgradeVersions</code> value.

#### BackupConfig

Returns the <code>BackupConfig</code> value.

#### ConnectionStrings

Returns the <code>ConnectionStrings</code> value.

#### ConnectionUrls

Returns the <code>ConnectionUrls</code> value.

#### DataStorageSizeInGb

Returns the <code>DataStorageSizeInGb</code> value.

#### FailedDataRecoveryInSeconds

Returns the <code>FailedDataRecoveryInSeconds</code> value.

#### Id

Returns the <code>Id</code> value.

#### InfrastructureType

Returns the <code>InfrastructureType</code> value.

#### IsPreview

Returns the <code>IsPreview</code> value.

#### KeyHistoryEntry

Returns the <code>KeyHistoryEntry</code> value.

#### KeyStoreId

Returns the <code>KeyStoreId</code> value.

#### KeyStoreWalletName

Returns the <code>KeyStoreWalletName</code> value.

#### KmsKeyLifecycleDetails

Returns the <code>KmsKeyLifecycleDetails</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### PrivateEndpoint

Returns the <code>PrivateEndpoint</code> value.

#### PrivateEndpointIp

Returns the <code>PrivateEndpointIp</code> value.

#### RefreshableStatus

Returns the <code>RefreshableStatus</code> value.

#### Role

Returns the <code>Role</code> value.

#### ServiceConsoleUrl

Returns the <code>ServiceConsoleUrl</code> value.

#### StandbyDb

Returns the <code>StandbyDb</code> value.

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

#### TimeOfLastFailover

Returns the <code>TimeOfLastFailover</code> value.

#### TimeOfLastRefresh

Returns the <code>TimeOfLastRefresh</code> value.

#### TimeOfLastRefreshPoint

Returns the <code>TimeOfLastRefreshPoint</code> value.

#### TimeOfLastSwitchover

Returns the <code>TimeOfLastSwitchover</code> value.

#### TimeOfNextRefresh

Returns the <code>TimeOfNextRefresh</code> value.

#### TimeReclamationOfFreeAutonomousDatabase

Returns the <code>TimeReclamationOfFreeAutonomousDatabase</code> value.

#### UsedDataStorageSizeInTbs

Returns the <code>UsedDataStorageSizeInTbs</code> value.

