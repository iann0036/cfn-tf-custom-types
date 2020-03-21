# Terraform::AWS::CodedeployDeploymentGroup LoadBalancerInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#elbinfo" title="ElbInfo">ElbInfo</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;, ... ]</i>,
    "<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;, ... ]</i>,
    "<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#elbinfo" title="ElbInfo">ElbInfo</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;</i>
<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;</i>
<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;</i>
</pre>

## Properties

#### ElbInfo

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInfo

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupPairInfo

_Required_: No
_Type_: List of &lt;a href=&#34;loadbalancerinfo-targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

