# Terraform::AWS::CodedeployDeploymentGroup TargetGroupPairInfo

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>" : <i>[ <a href="targetgrouppairinfo-prodtrafficroute.md">ProdTrafficRoute</a>, ... ]</i>,
    "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ <a href="targetgrouppairinfo-targetgroup.md">TargetGroup</a>, ... ]</i>,
    "<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>" : <i>[ <a href="targetgrouppairinfo-testtrafficroute.md">TestTrafficRoute</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>: <i>
      - <a href="targetgrouppairinfo-prodtrafficroute.md">ProdTrafficRoute</a></i>
<a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - <a href="targetgrouppairinfo-targetgroup.md">TargetGroup</a></i>
<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>: <i>
      - <a href="targetgrouppairinfo-testtrafficroute.md">TestTrafficRoute</a></i>
</pre>

## Properties

#### ProdTrafficRoute

_Required_: No

_Type_: List of <a href="targetgrouppairinfo-prodtrafficroute.md">ProdTrafficRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No

_Type_: List of <a href="targetgrouppairinfo-targetgroup.md">TargetGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTrafficRoute

_Required_: No

_Type_: List of <a href="targetgrouppairinfo-testtrafficroute.md">TestTrafficRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

