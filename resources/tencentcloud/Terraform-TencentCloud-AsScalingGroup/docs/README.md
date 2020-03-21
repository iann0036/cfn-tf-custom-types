# Terraform::TencentCloud::AsScalingGroup

Provides a resource to create a group of AS (Auto scaling) instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::AsScalingGroup",
    "Properties" : {
        "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
        "<a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>" : <i>Double</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#loadbalancerids" title="LoadBalancerIds">LoadBalancerIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>String</i>,
        "<a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>" : <i>[ <a href="forwardbalancerids.md">ForwardBalancerIds</a>, ... ]</i>,
        "<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>" : <i>[ <a href="targetattribute.md">TargetAttribute</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::AsScalingGroup
Properties:
    <a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
    <a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>: <i>Double</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#loadbalancerids" title="LoadBalancerIds">LoadBalancerIds</a>: <i>
      - String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>String</i>
    <a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>: <i>
      - String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>: <i>
      - <a href="forwardbalancerids.md">ForwardBalancerIds</a></i>
    <a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>: <i>
      - <a href="targetattribute.md">TargetAttribute</a></i>
</pre>

## Properties

#### ConfigurationId

An available ID for a launch configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCooldown

Default cooldown time in second, and default value is 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

Desired volume of CVM instances, which is between max_size and min_size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerIds

ID list of traditional load balancers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Maximum number of CVM instances (0~2000).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

Minimum number of CVM instances (0~2000).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Specifies to which project the scaling group belongs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

Available values for retry policies include IMMEDIATE_RETRY and INCREMENTAL_INTERVALS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupName

Name of a scaling group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

ID list of subnet, and for VPC it is required.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of a scaling group.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationPolicies

Available values for termination policies include OLDEST_INSTANCE and NEWEST_INSTANCE.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of VPC network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

List of available zones, for Basic network it is required.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardBalancerIds

_Required_: No

_Type_: List of <a href="forwardbalancerids.md">ForwardBalancerIds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAttribute

_Required_: No

_Type_: List of <a href="targetattribute.md">TargetAttribute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### InstanceCount

Returns the <code>InstanceCount</code> value.

#### Status

Returns the <code>Status</code> value.

