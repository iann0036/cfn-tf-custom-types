# Terraform::OCI::DatabaseAutonomousDataWarehouseBackup

This resource provides the Autonomous Data Warehouse Backup resource in Oracle Cloud Infrastructure Database service.

Creates a new Autonomous Data Warehouse backup for the specified database based on the provided request parameters.

**IMPORTANT:** This resource is being **deprecated**, use `oci_database_autonomous_database_backup` instead.
Refer to the [Deprecation Guide](#deprecation-guide) below on how to rename and migrate existing resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::DatabaseAutonomousDataWarehouseBackup",
    "Properties" : {
        "<a href="#autonomousdatawarehouseid" title="AutonomousDataWarehouseId">AutonomousDataWarehouseId</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::DatabaseAutonomousDataWarehouseBackup
Properties:
    <a href="#autonomousdatawarehouseid" title="AutonomousDataWarehouseId">AutonomousDataWarehouseId</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutonomousDataWarehouseId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Autonomous Data Warehouse backup.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The user-friendly name for the backup. The name does not have to be unique.

_Required_: Yes

_Type_: String

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

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsAutomatic

Returns the <code>IsAutomatic</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeEnded

Returns the <code>TimeEnded</code> value.

#### TimeStarted

Returns the <code>TimeStarted</code> value.

#### Type

Returns the <code>Type</code> value.

