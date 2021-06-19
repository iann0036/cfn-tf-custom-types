# TF::OCI::DatabaseAutonomousContainerDatabase

This resource provides the Autonomous Container Database resource in Oracle Cloud Infrastructure Database service.

Creates an Autonomous Container Database in the specified Autonomous Exadata Infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseAutonomousContainerDatabase",
    "Properties" : {
        "<a href="#autonomousexadatainfrastructureid" title="AutonomousExadataInfrastructureId">AutonomousExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#autonomousvmclusterid" title="AutonomousVmClusterId">AutonomousVmClusterId</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#keystoreid" title="KeyStoreId">KeyStoreId</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#patchmodel" title="PatchModel">PatchModel</a>" : <i>String</i>,
        "<a href="#peerautonomouscontainerdatabasecompartmentid" title="PeerAutonomousContainerDatabaseCompartmentId">PeerAutonomousContainerDatabaseCompartmentId</a>" : <i>String</i>,
        "<a href="#peerautonomouscontainerdatabasedisplayname" title="PeerAutonomousContainerDatabaseDisplayName">PeerAutonomousContainerDatabaseDisplayName</a>" : <i>String</i>,
        "<a href="#peerautonomousexadatainfrastructureid" title="PeerAutonomousExadataInfrastructureId">PeerAutonomousExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#peerautonomousvmclusterid" title="PeerAutonomousVmClusterId">PeerAutonomousVmClusterId</a>" : <i>String</i>,
        "<a href="#peerdbuniquename" title="PeerDbUniqueName">PeerDbUniqueName</a>" : <i>String</i>,
        "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
        "<a href="#rotatekeytrigger" title="RotateKeyTrigger">RotateKeyTrigger</a>" : <i>Boolean</i>,
        "<a href="#servicelevelagreementtype" title="ServiceLevelAgreementType">ServiceLevelAgreementType</a>" : <i>String</i>,
        "<a href="#standbymaintenancebufferindays" title="StandbyMaintenanceBufferInDays">StandbyMaintenanceBufferInDays</a>" : <i>Double</i>,
        "<a href="#vaultid" title="VaultId">VaultId</a>" : <i>String</i>,
        "<a href="#backupconfig" title="BackupConfig">BackupConfig</a>" : <i>[ <a href="backupconfigdefinition.md">BackupConfigDefinition</a>, ... ]</i>,
        "<a href="#maintenancewindowdetails" title="MaintenanceWindowDetails">MaintenanceWindowDetails</a>" : <i>[ <a href="maintenancewindowdetailsdefinition.md">MaintenanceWindowDetailsDefinition</a>, ... ]</i>,
        "<a href="#peerautonomouscontainerdatabasebackupconfig" title="PeerAutonomousContainerDatabaseBackupConfig">PeerAutonomousContainerDatabaseBackupConfig</a>" : <i>[ <a href="peerautonomouscontainerdatabasebackupconfigdefinition.md">PeerAutonomousContainerDatabaseBackupConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseAutonomousContainerDatabase
Properties:
    <a href="#autonomousexadatainfrastructureid" title="AutonomousExadataInfrastructureId">AutonomousExadataInfrastructureId</a>: <i>String</i>
    <a href="#autonomousvmclusterid" title="AutonomousVmClusterId">AutonomousVmClusterId</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#dbuniquename" title="DbUniqueName">DbUniqueName</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#keystoreid" title="KeyStoreId">KeyStoreId</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#patchmodel" title="PatchModel">PatchModel</a>: <i>String</i>
    <a href="#peerautonomouscontainerdatabasecompartmentid" title="PeerAutonomousContainerDatabaseCompartmentId">PeerAutonomousContainerDatabaseCompartmentId</a>: <i>String</i>
    <a href="#peerautonomouscontainerdatabasedisplayname" title="PeerAutonomousContainerDatabaseDisplayName">PeerAutonomousContainerDatabaseDisplayName</a>: <i>String</i>
    <a href="#peerautonomousexadatainfrastructureid" title="PeerAutonomousExadataInfrastructureId">PeerAutonomousExadataInfrastructureId</a>: <i>String</i>
    <a href="#peerautonomousvmclusterid" title="PeerAutonomousVmClusterId">PeerAutonomousVmClusterId</a>: <i>String</i>
    <a href="#peerdbuniquename" title="PeerDbUniqueName">PeerDbUniqueName</a>: <i>String</i>
    <a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
    <a href="#rotatekeytrigger" title="RotateKeyTrigger">RotateKeyTrigger</a>: <i>Boolean</i>
    <a href="#servicelevelagreementtype" title="ServiceLevelAgreementType">ServiceLevelAgreementType</a>: <i>String</i>
    <a href="#standbymaintenancebufferindays" title="StandbyMaintenanceBufferInDays">StandbyMaintenanceBufferInDays</a>: <i>Double</i>
    <a href="#vaultid" title="VaultId">VaultId</a>: <i>String</i>
    <a href="#backupconfig" title="BackupConfig">BackupConfig</a>: <i>
      - <a href="backupconfigdefinition.md">BackupConfigDefinition</a></i>
    <a href="#maintenancewindowdetails" title="MaintenanceWindowDetails">MaintenanceWindowDetails</a>: <i>
      - <a href="maintenancewindowdetailsdefinition.md">MaintenanceWindowDetailsDefinition</a></i>
    <a href="#peerautonomouscontainerdatabasebackupconfig" title="PeerAutonomousContainerDatabaseBackupConfig">PeerAutonomousContainerDatabaseBackupConfig</a>: <i>
      - <a href="peerautonomouscontainerdatabasebackupconfigdefinition.md">PeerAutonomousContainerDatabaseBackupConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutonomousExadataInfrastructureId

The OCID of the Autonomous Exadata Infrastructure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonomousVmClusterId

The OCID of the Autonomous VM Cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Autonomous Container Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbUniqueName

The `DB_UNIQUE_NAME` of the Oracle Database being backed up.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The display name for the Autonomous Container Database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyStoreId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the key store.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchModel

(Updatable) Database Patch model preference.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAutonomousContainerDatabaseCompartmentId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where the standby Autonomous Container Database will be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAutonomousContainerDatabaseDisplayName

The display name for the peer Autonomous Container Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAutonomousExadataInfrastructureId

The OCID of the peer Autonomous Exadata Infrastructure for autonomous dataguard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAutonomousVmClusterId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the peer Autonomous VM cluster for Autonomous Data Guard. Required to enable Data Guard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerDbUniqueName

The `DB_UNIQUE_NAME` of the peer Autonomous Container Database in a Data Guard association.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

The protection mode of this Autonomous Data Guard association. For more information, see [Oracle Data Guard Protection Modes](http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000) in the Oracle Data Guard documentation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotateKeyTrigger

(Updatable) An optional property when flipped triggers rotation of KMS key. It is only applicable on dedicated container databases i.e. where `autonomous_exadata_infrastructure_id` is set.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelAgreementType

The service level agreement type of the Autonomous Container Database. The default is STANDARD. For an autonomous dataguard Autonomous Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandbyMaintenanceBufferInDays

(Updatable) The scheduling detail for the quarterly maintenance window of standby Autonomous Container Database. This value represents the number of days before the primary database maintenance schedule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure [vault](https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfig

_Required_: No

_Type_: List of <a href="backupconfigdefinition.md">BackupConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowDetails

_Required_: No

_Type_: List of <a href="maintenancewindowdetailsdefinition.md">MaintenanceWindowDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAutonomousContainerDatabaseBackupConfig

_Required_: No

_Type_: List of <a href="peerautonomouscontainerdatabasebackupconfigdefinition.md">PeerAutonomousContainerDatabaseBackupConfigDefinition</a>

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

#### DbVersion

Returns the <code>DbVersion</code> value.

#### Id

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the backup destination.
* `internet_proxy` - (Optional) Proxy URL to connect to object store.
* `type` - (Required) Type of the database backup destination.
* `vpc_password` - (Optional) For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
* `vpc_user` - (Optional) For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.
* `recovery_window_in_days` - (Optional) Number of days between the current and the earliest point of recoverability covered by automatic backups. This value applies to automatic backups. After a new automatic backup has been created, Oracle removes old automatic backups that are created before the window. When the value is updated, it is applied to all existing automatic backups.

#### InfrastructureType

Returns the <code>InfrastructureType</code> value.

#### KeyStoreWalletName

Returns the <code>KeyStoreWalletName</code> value.

#### LastMaintenanceRunId

Returns the <code>LastMaintenanceRunId</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MaintenanceWindow

Returns the <code>MaintenanceWindow</code> value.

#### NextMaintenanceRunId

Returns the <code>NextMaintenanceRunId</code> value.

#### PatchId

Returns the <code>PatchId</code> value.

#### Role

Returns the <code>Role</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

