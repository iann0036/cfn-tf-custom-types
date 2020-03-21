# Terraform::TencentCloud::AsScalingGroup ForwardBalancerIds

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
    "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
    "<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>" : <i>[ <a href="forwardbalancerids-targetattribute.md">TargetAttribute</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
<a href="#targetattribute" title="TargetAttribute">TargetAttribute</a>: <i>
      - <a href="forwardbalancerids-targetattribute.md">TargetAttribute</a></i>
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

_Type_: List of <a href="forwardbalancerids-targetattribute.md">TargetAttribute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

