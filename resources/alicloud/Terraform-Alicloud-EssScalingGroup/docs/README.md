# Terraform::Alicloud::EssScalingGroup

Provides a ESS scaling group resource which is a collection of ECS instances with the same application scenarios.

It defines the maximum and minimum numbers of ECS instances in the group, and their associated Server Load Balancer instances, RDS instances, and other attributes.

-> **NOTE:** You can launch an ESS scaling group for a VPC network via specifying parameter `vswitch_ids`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::EssScalingGroup",
    "Properties" : {
        "<a href="#dbinstanceids" title="DbInstanceIds">DbInstanceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>" : <i>Double</i>,
        "<a href="#loadbalancerids" title="LoadbalancerIds">LoadbalancerIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#multiazpolicy" title="MultiAzPolicy">MultiAzPolicy</a>" : <i>String</i>,
        "<a href="#ondemandbasecapacity" title="OnDemandBaseCapacity">OnDemandBaseCapacity</a>" : <i>Double</i>,
        "<a href="#ondemandpercentageabovebasecapacity" title="OnDemandPercentageAboveBaseCapacity">OnDemandPercentageAboveBaseCapacity</a>" : <i>Double</i>,
        "<a href="#removalpolicies" title="RemovalPolicies">RemovalPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>" : <i>String</i>,
        "<a href="#spotinstancepools" title="SpotInstancePools">SpotInstancePools</a>" : <i>Double</i>,
        "<a href="#spotinstanceremedy" title="SpotInstanceRemedy">SpotInstanceRemedy</a>" : <i>Boolean</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#vswitchids" title="VswitchIds">VswitchIds</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::EssScalingGroup
Properties:
    <a href="#dbinstanceids" title="DbInstanceIds">DbInstanceIds</a>: <i>
      - String</i>
    <a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>: <i>Double</i>
    <a href="#loadbalancerids" title="LoadbalancerIds">LoadbalancerIds</a>: <i>
      - String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#multiazpolicy" title="MultiAzPolicy">MultiAzPolicy</a>: <i>String</i>
    <a href="#ondemandbasecapacity" title="OnDemandBaseCapacity">OnDemandBaseCapacity</a>: <i>Double</i>
    <a href="#ondemandpercentageabovebasecapacity" title="OnDemandPercentageAboveBaseCapacity">OnDemandPercentageAboveBaseCapacity</a>: <i>Double</i>
    <a href="#removalpolicies" title="RemovalPolicies">RemovalPolicies</a>: <i>
      - String</i>
    <a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>: <i>String</i>
    <a href="#spotinstancepools" title="SpotInstancePools">SpotInstancePools</a>: <i>Double</i>
    <a href="#spotinstanceremedy" title="SpotInstanceRemedy">SpotInstanceRemedy</a>: <i>Boolean</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#vswitchids" title="VswitchIds">VswitchIds</a>: <i>
      - String</i>
</pre>

## Properties

#### DbInstanceIds

If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.
- The specified RDS instance must be in running status.
- The specified RDS instance’s whitelist must have room for more IP addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCooldown

Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerIds

If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.
- The Server Load Balancer instance must be enabled.
- At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
targeting your `alicloud_slb_listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
- The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
- The default weight of an ECS instance attached to the Server Load Balancer instance is 50.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Maximum number of ECS instances in the scaling group. Value range: [0, 1000].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

Minimum number of ECS instances in the scaling group. Value range: [0, 1000].

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiAzPolicy

Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandBaseCapacity

The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandPercentageAboveBaseCapacity

Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemovalPolicies

RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:
- OldestInstance: removes the first ECS instance attached to the scaling group.
- NewestInstance: removes the first ECS instance attached to the scaling group.
- OldestScalingConfiguration: removes the ECS instance with the oldest scaling configuration.
- Default values: OldestScalingConfiguration and OldestInstance. You can enter up to two removal policies.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupName

Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores `_`, hyphens `-`, and decimal points `.`. If this parameter is not specified, the default value is ScalingGroupId.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstancePools

The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstanceRemedy

Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

It has been deprecated from version 1.7.1 and new field 'vswitch_ids' replaces it.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchIds

List of virtual switch IDs in which the ecs instances to be launched.

_Required_: No

_Type_: List of String

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

