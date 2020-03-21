# Terraform::TencentCloud::KubernetesAsScalingGroup AutoScalingGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultcooldown" title="DefaultCooldown">DefaultCooldown</a>" : <i>Double</i>,
    "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
    "<a href="#loadbalancerids" title="LoadBalancerIds">LoadBalancerIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
    "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
    "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>String</i>,
    "<a href="#scalinggroupname" title="ScalingGroupName">ScalingGroupName</a>" : <i>String</i>,
    "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="autoscalinggroup-tags.md">Tags</a>, ... ]</i>,
    "<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>" : <i>[ String, ... ]</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
    "<a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>" : <i>[ <a href="autoscalinggroup-forwardbalancerids.md">ForwardBalancerIds</a>, ... ]</i>
}
</pre>

### YAML

<pre>
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
      - <a href="autoscalinggroup-tags.md">Tags</a></i>
<a href="#terminationpolicies" title="TerminationPolicies">TerminationPolicies</a>: <i>
      - String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
<a href="#forwardbalancerids" title="ForwardBalancerIds">ForwardBalancerIds</a>: <i>
      - <a href="autoscalinggroup-forwardbalancerids.md">ForwardBalancerIds</a></i>
</pre>

## Properties

#### DefaultCooldown

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of <a href="autoscalinggroup-tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminationPolicies

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardBalancerIds

_Required_: No
_Type_: List of <a href="autoscalinggroup-forwardbalancerids.md">ForwardBalancerIds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

