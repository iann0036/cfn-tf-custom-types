# TF::Alicloud::AutoProvisioningGroup

Provides a ECS auto provisioning group resource which is a solution that uses preemptive instances and pay_as_you_go instances to rapidly deploy clusters.

-> **NOTE:** Available in 1.79.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::AutoProvisioningGroup",
    "Properties" : {
        "<a href="#autoprovisioninggroupname" title="AutoProvisioningGroupName">AutoProvisioningGroupName</a>" : <i>String</i>,
        "<a href="#autoprovisioninggrouptype" title="AutoProvisioningGroupType">AutoProvisioningGroupType</a>" : <i>String</i>,
        "<a href="#defaulttargetcapacitytype" title="DefaultTargetCapacityType">DefaultTargetCapacityType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>" : <i>String</i>,
        "<a href="#launchtemplateid" title="LaunchTemplateId">LaunchTemplateId</a>" : <i>String</i>,
        "<a href="#launchtemplateversion" title="LaunchTemplateVersion">LaunchTemplateVersion</a>" : <i>String</i>,
        "<a href="#maxspotprice" title="MaxSpotPrice">MaxSpotPrice</a>" : <i>Double</i>,
        "<a href="#payasyougoallocationstrategy" title="PayAsYouGoAllocationStrategy">PayAsYouGoAllocationStrategy</a>" : <i>String</i>,
        "<a href="#payasyougotargetcapacity" title="PayAsYouGoTargetCapacity">PayAsYouGoTargetCapacity</a>" : <i>String</i>,
        "<a href="#spotallocationstrategy" title="SpotAllocationStrategy">SpotAllocationStrategy</a>" : <i>String</i>,
        "<a href="#spotinstanceinterruptionbehavior" title="SpotInstanceInterruptionBehavior">SpotInstanceInterruptionBehavior</a>" : <i>String</i>,
        "<a href="#spotinstancepoolstousecount" title="SpotInstancePoolsToUseCount">SpotInstancePoolsToUseCount</a>" : <i>Double</i>,
        "<a href="#spottargetcapacity" title="SpotTargetCapacity">SpotTargetCapacity</a>" : <i>String</i>,
        "<a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>" : <i>Boolean</i>,
        "<a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>" : <i>Boolean</i>,
        "<a href="#totaltargetcapacity" title="TotalTargetCapacity">TotalTargetCapacity</a>" : <i>String</i>,
        "<a href="#validfrom" title="ValidFrom">ValidFrom</a>" : <i>String</i>,
        "<a href="#validuntil" title="ValidUntil">ValidUntil</a>" : <i>String</i>,
        "<a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>" : <i>[ <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::AutoProvisioningGroup
Properties:
    <a href="#autoprovisioninggroupname" title="AutoProvisioningGroupName">AutoProvisioningGroupName</a>: <i>String</i>
    <a href="#autoprovisioninggrouptype" title="AutoProvisioningGroupType">AutoProvisioningGroupType</a>: <i>String</i>
    <a href="#defaulttargetcapacitytype" title="DefaultTargetCapacityType">DefaultTargetCapacityType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>: <i>String</i>
    <a href="#launchtemplateid" title="LaunchTemplateId">LaunchTemplateId</a>: <i>String</i>
    <a href="#launchtemplateversion" title="LaunchTemplateVersion">LaunchTemplateVersion</a>: <i>String</i>
    <a href="#maxspotprice" title="MaxSpotPrice">MaxSpotPrice</a>: <i>Double</i>
    <a href="#payasyougoallocationstrategy" title="PayAsYouGoAllocationStrategy">PayAsYouGoAllocationStrategy</a>: <i>String</i>
    <a href="#payasyougotargetcapacity" title="PayAsYouGoTargetCapacity">PayAsYouGoTargetCapacity</a>: <i>String</i>
    <a href="#spotallocationstrategy" title="SpotAllocationStrategy">SpotAllocationStrategy</a>: <i>String</i>
    <a href="#spotinstanceinterruptionbehavior" title="SpotInstanceInterruptionBehavior">SpotInstanceInterruptionBehavior</a>: <i>String</i>
    <a href="#spotinstancepoolstousecount" title="SpotInstancePoolsToUseCount">SpotInstancePoolsToUseCount</a>: <i>Double</i>
    <a href="#spottargetcapacity" title="SpotTargetCapacity">SpotTargetCapacity</a>: <i>String</i>
    <a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>: <i>Boolean</i>
    <a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>: <i>Boolean</i>
    <a href="#totaltargetcapacity" title="TotalTargetCapacity">TotalTargetCapacity</a>: <i>String</i>
    <a href="#validfrom" title="ValidFrom">ValidFrom</a>: <i>String</i>
    <a href="#validuntil" title="ValidUntil">ValidUntil</a>: <i>String</i>
    <a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>: <i>
      - <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a></i>
</pre>

## Properties

#### AutoProvisioningGroupName

The name of the auto provisioning group to be created. It must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoProvisioningGroupType

The type of the auto provisioning group. Valid values:`request` and `maintain`,Default value: `maintain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTargetCapacityType

The type of supplemental instances. When the total value of `PayAsYouGoTargetCapacity` and `SpotTargetCapacity` is smaller than the value of TotalTargetCapacity, the auto provisioning group will create instances of the specified type to meet the capacity requirements. Valid values:`PayAsYouGo`: Pay-as-you-go instances; `Spot`: Preemptible instances, Default value: `Spot`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the auto provisioning group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcessCapacityTerminationPolicy

The shutdown policy for excess preemptible instances followed when the capacity of the auto provisioning group exceeds the target capacity. Valid values: `no-termination` and `termination`,Default value: `no-termination`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateId

The ID of the instance launch template associated with the auto provisioning group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateVersion

The version of the instance launch template associated with the auto provisioning group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSpotPrice

The global maximum price for preemptible instances in the auto provisioning group. If both the `MaxSpotPrice` and `LaunchTemplateConfig.N.MaxPrice` parameters are specified, the maximum price is the lower value of the two.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayAsYouGoAllocationStrategy

The scale-out policy for pay-as-you-go instances. Valid values: `lowest-price` and `prioritized`,Default value: `lowest-price`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayAsYouGoTargetCapacity

The target capacity of pay-as-you-go instances in the auto provisioning group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotAllocationStrategy

The scale-out policy for preemptible instances. Valid values:`lowest-price` and `diversified`,Default value: `lowest-price`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstanceInterruptionBehavior

The default behavior after preemptible instances are shut down. Value values: `stop` and `terminate`,Default value: `stop`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstancePoolsToUseCount

This parameter takes effect when the `SpotAllocationStrategy` parameter is set to `lowest-price`. The auto provisioning group selects instance types of the lowest cost to create instances.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotTargetCapacity

The target capacity of preemptible instances in the auto provisioning group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstances

Specifies whether to release instances of the auto provisioning group. Valid values:`false` and `true`, default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstancesWithExpiration

The shutdown policy for preemptible instances when the auto provisioning group expires. Valid values: `false` and `true`, default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalTargetCapacity

The total target capacity of the auto provisioning group. The target capacity consists of the following three parts:PayAsYouGoTargetCapacity,SpotTargetCapacity and the supplemental capacity besides PayAsYouGoTargetCapacity and SpotTargetCapacity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidFrom

The time when the auto provisioning group is started. The period of time between this point in time and the point in time specified by the `valid_until` parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group is immediately started after creation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidUntil

The time when the auto provisioning group expires. The period of time between this point in time and the point in time specified by the `valid_from` parameter is the effective time period of the auto provisioning group.By default, an auto provisioning group never expires.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateConfig

_Required_: No

_Type_: List of <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

