# TF::GoogleBeta::GoogleContainerCluster MaintenancePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>" : <i>[ <a href="dailymaintenancewindowdefinition.md">DailyMaintenanceWindowDefinition</a>, ... ]</i>,
    "<a href="#maintenanceexclusion" title="MaintenanceExclusion">MaintenanceExclusion</a>" : <i>[ <a href="maintenanceexclusiondefinition.md">MaintenanceExclusionDefinition</a>, ... ]</i>,
    "<a href="#recurringwindow" title="RecurringWindow">RecurringWindow</a>" : <i>[ <a href="recurringwindowdefinition.md">RecurringWindowDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>: <i>
      - <a href="dailymaintenancewindowdefinition.md">DailyMaintenanceWindowDefinition</a></i>
<a href="#maintenanceexclusion" title="MaintenanceExclusion">MaintenanceExclusion</a>: <i>
      - <a href="maintenanceexclusiondefinition.md">MaintenanceExclusionDefinition</a></i>
<a href="#recurringwindow" title="RecurringWindow">RecurringWindow</a>: <i>
      - <a href="recurringwindowdefinition.md">RecurringWindowDefinition</a></i>
</pre>

## Properties

#### DailyMaintenanceWindow

_Required_: No

_Type_: List of <a href="dailymaintenancewindowdefinition.md">DailyMaintenanceWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceExclusion

_Required_: No

_Type_: List of <a href="maintenanceexclusiondefinition.md">MaintenanceExclusionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurringWindow

_Required_: No

_Type_: List of <a href="recurringwindowdefinition.md">RecurringWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

