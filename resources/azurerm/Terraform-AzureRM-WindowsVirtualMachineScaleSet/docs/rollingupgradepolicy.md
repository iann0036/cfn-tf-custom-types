# Terraform::AzureRM::WindowsVirtualMachineScaleSet RollingUpgradePolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxbatchinstancepercent" title="MaxBatchInstancePercent">MaxBatchInstancePercent</a>" : <i>Double</i>,
    "<a href="#maxunhealthyinstancepercent" title="MaxUnhealthyInstancePercent">MaxUnhealthyInstancePercent</a>" : <i>Double</i>,
    "<a href="#maxunhealthyupgradedinstancepercent" title="MaxUnhealthyUpgradedInstancePercent">MaxUnhealthyUpgradedInstancePercent</a>" : <i>Double</i>,
    "<a href="#pausetimebetweenbatches" title="PauseTimeBetweenBatches">PauseTimeBetweenBatches</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#maxbatchinstancepercent" title="MaxBatchInstancePercent">MaxBatchInstancePercent</a>: <i>Double</i>
<a href="#maxunhealthyinstancepercent" title="MaxUnhealthyInstancePercent">MaxUnhealthyInstancePercent</a>: <i>Double</i>
<a href="#maxunhealthyupgradedinstancepercent" title="MaxUnhealthyUpgradedInstancePercent">MaxUnhealthyUpgradedInstancePercent</a>: <i>Double</i>
<a href="#pausetimebetweenbatches" title="PauseTimeBetweenBatches">PauseTimeBetweenBatches</a>: <i>String</i>
</pre>

## Properties

#### MaxBatchInstancePercent

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnhealthyInstancePercent

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnhealthyUpgradedInstancePercent

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PauseTimeBetweenBatches

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

