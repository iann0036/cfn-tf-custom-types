# TF::AWS::Ec2Fleet SpotOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>" : <i>String</i>,
    "<a href="#instanceinterruptionbehavior" title="InstanceInterruptionBehavior">InstanceInterruptionBehavior</a>" : <i>String</i>,
    "<a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>" : <i>Double</i>,
    "<a href="#maintenancestrategies" title="MaintenanceStrategies">MaintenanceStrategies</a>" : <i>[ <a href="maintenancestrategiesdefinition.md">MaintenanceStrategiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>: <i>String</i>
<a href="#instanceinterruptionbehavior" title="InstanceInterruptionBehavior">InstanceInterruptionBehavior</a>: <i>String</i>
<a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>: <i>Double</i>
<a href="#maintenancestrategies" title="MaintenanceStrategies">MaintenanceStrategies</a>: <i>
      - <a href="maintenancestrategiesdefinition.md">MaintenanceStrategiesDefinition</a></i>
</pre>

## Properties

#### AllocationStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInterruptionBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolsToUseCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceStrategies

_Required_: No

_Type_: List of <a href="maintenancestrategiesdefinition.md">MaintenanceStrategiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

