# TF::OCI::DatabaseMaintenanceRun

This resource provides the Maintenance Run resource in Oracle Cloud Infrastructure Database service.

Updates the properties of a maintenance run, such as the state of a maintenance run.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseMaintenanceRun",
    "Properties" : {
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#ispatchnowenabled" title="IsPatchNowEnabled">IsPatchNowEnabled</a>" : <i>Boolean</i>,
        "<a href="#maintenancerunid" title="MaintenanceRunId">MaintenanceRunId</a>" : <i>String</i>,
        "<a href="#patchid" title="PatchId">PatchId</a>" : <i>String</i>,
        "<a href="#patchingmode" title="PatchingMode">PatchingMode</a>" : <i>String</i>,
        "<a href="#timescheduled" title="TimeScheduled">TimeScheduled</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseMaintenanceRun
Properties:
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#ispatchnowenabled" title="IsPatchNowEnabled">IsPatchNowEnabled</a>: <i>Boolean</i>
    <a href="#maintenancerunid" title="MaintenanceRunId">MaintenanceRunId</a>: <i>String</i>
    <a href="#patchid" title="PatchId">PatchId</a>: <i>String</i>
    <a href="#patchingmode" title="PatchingMode">PatchingMode</a>: <i>String</i>
    <a href="#timescheduled" title="TimeScheduled">TimeScheduled</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### IsEnabled

(Updatable) If `FALSE`, skips the maintenance run.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPatchNowEnabled

(Updatable) If set to `TRUE`, starts patching immediately.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceRunId

The maintenance run OCID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the patch to be applied in the maintenance run.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchingMode

(Updatable) Maintenance method, it will be either "ROLLING" or "NONROLLING". Default value is ROLLING.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeScheduled

(Updatable) The scheduled date and time of the maintenance run to update.

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

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Description

Returns the <code>Description</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### MaintenanceSubtype

Returns the <code>MaintenanceSubtype</code> value.

#### MaintenanceType

Returns the <code>MaintenanceType</code> value.

#### PatchFailureCount

Returns the <code>PatchFailureCount</code> value.

#### PeerMaintenanceRunId

Returns the <code>PeerMaintenanceRunId</code> value.

#### State

Returns the <code>State</code> value.

#### TargetResourceId

Returns the <code>TargetResourceId</code> value.

#### TargetResourceType

Returns the <code>TargetResourceType</code> value.

#### TimeEnded

Returns the <code>TimeEnded</code> value.

#### TimeStarted

Returns the <code>TimeStarted</code> value.

