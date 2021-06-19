# TF::AWS::CodedeployDeploymentGroup TargetGroupPairInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>" : <i>[ <a href="prodtrafficroutedefinition.md">ProdTrafficRouteDefinition</a>, ... ]</i>,
    "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ <a href="targetgroupdefinition.md">TargetGroupDefinition</a>, ... ]</i>,
    "<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>" : <i>[ <a href="testtrafficroutedefinition.md">TestTrafficRouteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>: <i>
      - <a href="prodtrafficroutedefinition.md">ProdTrafficRouteDefinition</a></i>
<a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - <a href="targetgroupdefinition.md">TargetGroupDefinition</a></i>
<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>: <i>
      - <a href="testtrafficroutedefinition.md">TestTrafficRouteDefinition</a></i>
</pre>

## Properties

#### ProdTrafficRoute

_Required_: No

_Type_: List of <a href="prodtrafficroutedefinition.md">ProdTrafficRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No

_Type_: List of <a href="targetgroupdefinition.md">TargetGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTrafficRoute

_Required_: No

_Type_: List of <a href="testtrafficroutedefinition.md">TestTrafficRouteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

