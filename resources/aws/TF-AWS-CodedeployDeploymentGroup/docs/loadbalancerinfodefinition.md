# TF::AWS::CodedeployDeploymentGroup LoadBalancerInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#elbinfo" title="ElbInfo">ElbInfo</a>" : <i>[ <a href="elbinfodefinition.md">ElbInfoDefinition</a>, ... ]</i>,
    "<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>" : <i>[ <a href="targetgroupinfodefinition.md">TargetGroupInfoDefinition</a>, ... ]</i>,
    "<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>" : <i>[ <a href="targetgrouppairinfodefinition.md">TargetGroupPairInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#elbinfo" title="ElbInfo">ElbInfo</a>: <i>
      - <a href="elbinfodefinition.md">ElbInfoDefinition</a></i>
<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>: <i>
      - <a href="targetgroupinfodefinition.md">TargetGroupInfoDefinition</a></i>
<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>: <i>
      - <a href="targetgrouppairinfodefinition.md">TargetGroupPairInfoDefinition</a></i>
</pre>

## Properties

#### ElbInfo

_Required_: No

_Type_: List of <a href="elbinfodefinition.md">ElbInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInfo

_Required_: No

_Type_: List of <a href="targetgroupinfodefinition.md">TargetGroupInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupPairInfo

_Required_: No

_Type_: List of <a href="targetgrouppairinfodefinition.md">TargetGroupPairInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

