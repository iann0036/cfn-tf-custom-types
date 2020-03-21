# Terraform::AWS::CodedeployDeploymentGroup LoadBalancerInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#elbinfo" title="ElbInfo">ElbInfo</a>" : <i>[ <a href="loadbalancerinfo-elbinfo.md">ElbInfo</a>, ... ]</i>,
    "<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>" : <i>[ <a href="loadbalancerinfo-targetgroupinfo.md">TargetGroupInfo</a>, ... ]</i>,
    "<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>" : <i>[ <a href="loadbalancerinfo-targetgrouppairinfo.md">TargetGroupPairInfo</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#elbinfo" title="ElbInfo">ElbInfo</a>: <i>
      - <a href="loadbalancerinfo-elbinfo.md">ElbInfo</a></i>
<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>: <i>
      - <a href="loadbalancerinfo-targetgroupinfo.md">TargetGroupInfo</a></i>
<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>: <i>
      - <a href="loadbalancerinfo-targetgrouppairinfo.md">TargetGroupPairInfo</a></i>
</pre>

## Properties

#### ElbInfo

_Required_: No

_Type_: List of <a href="loadbalancerinfo-elbinfo.md">ElbInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInfo

_Required_: No

_Type_: List of <a href="loadbalancerinfo-targetgroupinfo.md">TargetGroupInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupPairInfo

_Required_: No

_Type_: List of <a href="loadbalancerinfo-targetgrouppairinfo.md">TargetGroupPairInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

