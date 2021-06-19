# TF::AWS::EcsService LoadBalancerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containername" title="ContainerName">ContainerName</a>" : <i>String</i>,
    "<a href="#containerport" title="ContainerPort">ContainerPort</a>" : <i>Double</i>,
    "<a href="#elbname" title="ElbName">ElbName</a>" : <i>String</i>,
    "<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containername" title="ContainerName">ContainerName</a>: <i>String</i>
<a href="#containerport" title="ContainerPort">ContainerPort</a>: <i>Double</i>
<a href="#elbname" title="ElbName">ElbName</a>: <i>String</i>
<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>: <i>String</i>
</pre>

## Properties

#### ContainerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElbName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

