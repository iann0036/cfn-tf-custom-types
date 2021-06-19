# TF::AzureRM::WindowsVirtualMachineScaleSet RollingUpgradePolicyDefinition

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

The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnhealthyInstancePercent

The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnhealthyUpgradedInstancePercent

The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PauseTimeBetweenBatches

The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

