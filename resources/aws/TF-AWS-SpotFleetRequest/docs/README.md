# TF::AWS::SpotFleetRequest

Provides an EC2 Spot Fleet Request resource. This allows a fleet of Spot
instances to be requested on the Spot market.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SpotFleetRequest",
    "Properties" : {
        "<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>" : <i>String</i>,
        "<a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>" : <i>String</i>,
        "<a href="#fleettype" title="FleetType">FleetType</a>" : <i>String</i>,
        "<a href="#iamfleetrole" title="IamFleetRole">IamFleetRole</a>" : <i>String</i>,
        "<a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>" : <i>String</i>,
        "<a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>" : <i>Double</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ String, ... ]</i>,
        "<a href="#ondemandallocationstrategy" title="OnDemandAllocationStrategy">OnDemandAllocationStrategy</a>" : <i>String</i>,
        "<a href="#ondemandmaxtotalprice" title="OnDemandMaxTotalPrice">OnDemandMaxTotalPrice</a>" : <i>String</i>,
        "<a href="#ondemandtargetcapacity" title="OnDemandTargetCapacity">OnDemandTargetCapacity</a>" : <i>Double</i>,
        "<a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>" : <i>Boolean</i>,
        "<a href="#spotprice" title="SpotPrice">SpotPrice</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>" : <i>Double</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>" : <i>Boolean</i>,
        "<a href="#validfrom" title="ValidFrom">ValidFrom</a>" : <i>String</i>,
        "<a href="#validuntil" title="ValidUntil">ValidUntil</a>" : <i>String</i>,
        "<a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>" : <i>Boolean</i>,
        "<a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>" : <i>[ <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a>, ... ]</i>,
        "<a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>" : <i>[ <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>, ... ]</i>,
        "<a href="#spotmaintenancestrategies" title="SpotMaintenanceStrategies">SpotMaintenanceStrategies</a>" : <i>[ <a href="spotmaintenancestrategiesdefinition.md">SpotMaintenanceStrategiesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SpotFleetRequest
Properties:
    <a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>: <i>String</i>
    <a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>: <i>String</i>
    <a href="#fleettype" title="FleetType">FleetType</a>: <i>String</i>
    <a href="#iamfleetrole" title="IamFleetRole">IamFleetRole</a>: <i>String</i>
    <a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>: <i>String</i>
    <a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>: <i>Double</i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - String</i>
    <a href="#ondemandallocationstrategy" title="OnDemandAllocationStrategy">OnDemandAllocationStrategy</a>: <i>String</i>
    <a href="#ondemandmaxtotalprice" title="OnDemandMaxTotalPrice">OnDemandMaxTotalPrice</a>: <i>String</i>
    <a href="#ondemandtargetcapacity" title="OnDemandTargetCapacity">OnDemandTargetCapacity</a>: <i>Double</i>
    <a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>: <i>Boolean</i>
    <a href="#spotprice" title="SpotPrice">SpotPrice</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>: <i>Double</i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>: <i>Boolean</i>
    <a href="#validfrom" title="ValidFrom">ValidFrom</a>: <i>String</i>
    <a href="#validuntil" title="ValidUntil">ValidUntil</a>: <i>String</i>
    <a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>: <i>Boolean</i>
    <a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>: <i>
      - <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a></i>
    <a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>: <i>
      - <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a></i>
    <a href="#spotmaintenancestrategies" title="SpotMaintenanceStrategies">SpotMaintenanceStrategies</a>: <i>
      - <a href="spotmaintenancestrategiesdefinition.md">SpotMaintenanceStrategiesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllocationStrategy

Indicates how to allocate the target capacity across
the Spot pools specified by the Spot fleet request. The default is
`lowestPrice`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcessCapacityTerminationPolicy

Indicates whether running Spot
instances should be terminated if the target capacity of the Spot fleet
request is decreased below the current size of the Spot fleet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetType

The type of fleet request. Indicates whether the Spot Fleet only requests the target
capacity or also attempts to maintain it. Default is `maintain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamFleetRole

Grants the Spot fleet permission to terminate
Spot instances on your behalf when you cancel its Spot fleet request using
CancelSpotFleetRequests or when the Spot fleet request expires, if you set
terminateInstancesWithExpiration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInterruptionBehaviour

Indicates whether a Spot
instance stops or terminates when it is interrupted. Default is
`terminate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolsToUseCount

The number of Spot pools across which to allocate your target Spot capacity.
Valid only when `allocation_strategy` is set to `lowestPrice`. Spot Fleet selects
the cheapest Spot pools and evenly allocates your target Spot capacity across
the number of Spot pools that you specify.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandAllocationStrategy

The order of the launch template overrides to use in fulfilling On-Demand capacity. the possible values are: `lowestPrice` and `prioritized`. the default is `lowestPrice`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandMaxTotalPrice

The maximum amount per hour for On-Demand Instances that you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandTargetCapacity

The number of On-Demand units to request. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceUnhealthyInstances

Indicates whether Spot fleet should replace unhealthy instances. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPrice

The maximum bid price per unit hour.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCapacity

The number of units to request. You can choose to set the
target capacity in terms of instances or a performance characteristic that is
important to your application workload, such as vCPUs, memory, or I/O.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstancesWithExpiration

Indicates whether running Spot
instances should be terminated when the Spot fleet request expires.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidFrom

The start date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). The default is to start fulfilling the request immediately.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidUntil

The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForFulfillment

If set, Terraform will
wait for the Spot Request to be fulfilled, and will throw an error if the
timeout of 10m is reached.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchSpecification

_Required_: No

_Type_: List of <a href="launchspecificationdefinition.md">LaunchSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateConfig

_Required_: No

_Type_: List of <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotMaintenanceStrategies

_Required_: No

_Type_: List of <a href="spotmaintenancestrategiesdefinition.md">SpotMaintenanceStrategiesDefinition</a>

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

#### ClientToken

Returns the <code>ClientToken</code> value.

#### Id

Returns the <code>Id</code> value.

#### SpotRequestState

Returns the <code>SpotRequestState</code> value.

