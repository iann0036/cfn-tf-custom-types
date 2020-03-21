# Terraform::OCI::DatabaseAutonomousContainerDatabase

This resource provides the Autonomous Container Database resource in Oracle Cloud Infrastructure Database service.

Create a new Autonomous Container Database in the specified Autonomous Exadata Infrastructure.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseAutonomousContainerDatabase",
    "Properties" : {
        "<a href="#autonomousexadatainfrastructureid" title="AutonomousExadataInfrastructureId">AutonomousExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#patchmodel" title="PatchModel">PatchModel</a>" : <i>String</i>,
        "<a href="#servicelevelagreementtype" title="ServiceLevelAgreementType">ServiceLevelAgreementType</a>" : <i>String</i>,
        "<a href="#backupconfig" title="BackupConfig">BackupConfig</a>" : <i>[ <a href="backupconfig.md">BackupConfig</a>, ... ]</i>,
        "<a href="#maintenancewindowdetails" title="MaintenanceWindowDetails">MaintenanceWindowDetails</a>" : <i>[ <a href="maintenancewindowdetails.md">MaintenanceWindowDetails</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>" : <i>[ <a href="daysofweek.md">DaysOfWeek</a>, ... ]</i>,
        "<a href="#months" title="Months">Months</a>" : <i>[ <a href="months.md">Months</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseAutonomousContainerDatabase
Properties:
    <a href="#autonomousexadatainfrastructureid" title="AutonomousExadataInfrastructureId">AutonomousExadataInfrastructureId</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#patchmodel" title="PatchModel">PatchModel</a>: <i>String</i>
    <a href="#servicelevelagreementtype" title="ServiceLevelAgreementType">ServiceLevelAgreementType</a>: <i>String</i>
    <a href="#backupconfig" title="BackupConfig">BackupConfig</a>: <i>
      - <a href="backupconfig.md">BackupConfig</a></i>
    <a href="#maintenancewindowdetails" title="MaintenanceWindowDetails">MaintenanceWindowDetails</a>: <i>
      - <a href="maintenancewindowdetails.md">MaintenanceWindowDetails</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#daysofweek" title="DaysOfWeek">DaysOfWeek</a>: <i>
      - <a href="daysofweek.md">DaysOfWeek</a></i>
    <a href="#months" title="Months">Months</a>: <i>
      - <a href="months.md">Months</a></i>
</pre>

## Properties

#### AutonomousExadataInfrastructureId

The OCID of the Autonomous Exadata Infrastructure.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the Autonomous Container Database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) The display name for the Autonomous Container Database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchModel

(Updatable) Database Patch model preference.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceLevelAgreementType

The service level agreement type of the Autonomous Container Database. The default is STANDARD. For a mission critical Autonomous Container Database, the specified Autonomous Exadata Infrastructure must be associated with a remote Autonomous Exadata Infrastructure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupConfig

_Required_: No

_Type_: List of <a href="backupconfig.md">BackupConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowDetails

_Required_: No

_Type_: List of <a href="maintenancewindowdetails.md">MaintenanceWindowDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DaysOfWeek

_Required_: No

_Type_: List of <a href="daysofweek.md">DaysOfWeek</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Months

_Required_: No

_Type_: List of <a href="months.md">Months</a>

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

#### LastMaintenanceRunId

Returns the <code>LastMaintenanceRunId</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MaintenanceWindow

Returns the <code>MaintenanceWindow</code> value.

#### NextMaintenanceRunId

Returns the <code>NextMaintenanceRunId</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

