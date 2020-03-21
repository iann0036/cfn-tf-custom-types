# Terraform::TencentCloud::KubernetesAsScalingGroup AutoScalingGroup ForwardBalancerIds

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
    "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>" : <i>[ &lt;a href=&#34;autoscalinggroup-forwardbalancerids-targetattribute.md&#34;&gt;TargetAttribute&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>: <i>
      - &lt;a href=&#34;autoscalinggroup-forwardbalancerids-targetattribute.md&#34;&gt;TargetAttribute&lt;/a&gt;</i>
</pre>

## Properties

#### ListenerId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAttribute

_Required_: No
_Type_: List of &lt;a href=&#34;autoscalinggroup-forwardbalancerids-targetattribute.md&#34;&gt;TargetAttribute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

