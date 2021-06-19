# TF::Scaleway::K8sCluster AutoUpgradeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#maintenancewindowday" title="MaintenanceWindowDay">MaintenanceWindowDay</a>" : <i>String</i>,
    "<a href="#maintenancewindowstarthour" title="MaintenanceWindowStartHour">MaintenanceWindowStartHour</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#maintenancewindowday" title="MaintenanceWindowDay">MaintenanceWindowDay</a>: <i>String</i>
<a href="#maintenancewindowstarthour" title="MaintenanceWindowStartHour">MaintenanceWindowStartHour</a>: <i>Double</i>
</pre>

## Properties

#### Enable

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowDay

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindowStartHour

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

