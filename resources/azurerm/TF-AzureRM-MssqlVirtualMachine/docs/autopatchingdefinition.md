# TF::AzureRM::MssqlVirtualMachine AutoPatchingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>" : <i>String</i>,
    "<a href="#maintenancewindowdurationinminutes" title="MaintenanceWindowDurationInMinutes">MaintenanceWindowDurationInMinutes</a>" : <i>Double</i>,
    "<a href="#maintenancewindowstartinghour" title="MaintenanceWindowStartingHour">MaintenanceWindowStartingHour</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dayofweek" title="DayOfWeek">DayOfWeek</a>: <i>String</i>
<a href="#maintenancewindowdurationinminutes" title="MaintenanceWindowDurationInMinutes">MaintenanceWindowDurationInMinutes</a>: <i>Double</i>
<a href="#maintenancewindowstartinghour" title="MaintenanceWindowStartingHour">MaintenanceWindowStartingHour</a>: <i>Double</i>
</pre>

## Properties

#### DayOfWeek

The day of week to apply the patch on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowDurationInMinutes

The size of the Maintenance Window in minutes.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowStartingHour

The Hour, in the Virtual Machine Time-Zone when the patching maintenance window should begin.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

