# Terraform::AWS::SpotFleetRequest

Provides an EC2 Spot Fleet Request resource. This allows a fleet of Spot
instances to be requested on the Spot market.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SpotFleetRequest",
    "Properties" : {
        "<a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>" : <i>String</i>,
        "<a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>" : <i>String</i>,
        "<a href="#fleettype" title="FleetType">FleetType</a>" : <i>String</i>,
        "<a href="#iamfleetrole" title="IamFleetRole">IamFleetRole</a>" : <i>String</i>,
        "<a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>" : <i>String</i>,
        "<a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>" : <i>Double</i>,
        "<a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>" : <i>[ String, ... ]</i>,
        "<a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>" : <i>Boolean</i>,
        "<a href="#spotprice" title="SpotPrice">SpotPrice</a>" : <i>String</i>,
        "<a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>" : <i>Double</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>" : <i>Boolean</i>,
        "<a href="#validfrom" title="ValidFrom">ValidFrom</a>" : <i>String</i>,
        "<a href="#validuntil" title="ValidUntil">ValidUntil</a>" : <i>String</i>,
        "<a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>" : <i>Boolean</i>,
        "<a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>" : <i>[ <a href="launchspecification.md">LaunchSpecification</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevice.md">EbsBlockDevice</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>, ... ]</i>,
        "<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>" : <i>[ <a href="rootblockdevice.md">RootBlockDevice</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SpotFleetRequest
Properties:
    <a href="#allocationstrategy" title="AllocationStrategy">AllocationStrategy</a>: <i>String</i>
    <a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>: <i>String</i>
    <a href="#fleettype" title="FleetType">FleetType</a>: <i>String</i>
    <a href="#iamfleetrole" title="IamFleetRole">IamFleetRole</a>: <i>String</i>
    <a href="#instanceinterruptionbehaviour" title="InstanceInterruptionBehaviour">InstanceInterruptionBehaviour</a>: <i>String</i>
    <a href="#instancepoolstousecount" title="InstancePoolsToUseCount">InstancePoolsToUseCount</a>: <i>Double</i>
    <a href="#loadbalancers" title="LoadBalancers">LoadBalancers</a>: <i>
      - String</i>
    <a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>: <i>Boolean</i>
    <a href="#spotprice" title="SpotPrice">SpotPrice</a>: <i>String</i>
    <a href="#targetcapacity" title="TargetCapacity">TargetCapacity</a>: <i>Double</i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>: <i>Boolean</i>
    <a href="#validfrom" title="ValidFrom">ValidFrom</a>: <i>String</i>
    <a href="#validuntil" title="ValidUntil">ValidUntil</a>: <i>String</i>
    <a href="#waitforfulfillment" title="WaitForFulfillment">WaitForFulfillment</a>: <i>Boolean</i>
    <a href="#launchspecification" title="LaunchSpecification">LaunchSpecification</a>: <i>
      - <a href="launchspecification.md">LaunchSpecification</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevice.md">EbsBlockDevice</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a></i>
    <a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>: <i>
      - <a href="rootblockdevice.md">RootBlockDevice</a></i>
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

The end date and time of the request, in UTC [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.8) format(for example, YYYY-MM-DDTHH:MM:SSZ). At this point, no new Spot instance requests are placed or enabled to fulfill the request. Defaults to 24 hours.

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

_Type_: List of <a href="launchspecification.md">LaunchSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevice.md">EbsBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootBlockDevice

_Required_: No

_Type_: List of <a href="rootblockdevice.md">RootBlockDevice</a>

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

