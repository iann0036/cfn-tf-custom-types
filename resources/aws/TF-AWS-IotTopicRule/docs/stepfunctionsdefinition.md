# TF::AWS::IotTopicRule StepFunctionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#executionnameprefix" title="ExecutionNamePrefix">ExecutionNamePrefix</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#statemachinename" title="StateMachineName">StateMachineName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#executionnameprefix" title="ExecutionNamePrefix">ExecutionNamePrefix</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#statemachinename" title="StateMachineName">StateMachineName</a>: <i>String</i>
</pre>

## Properties

#### ExecutionNamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StateMachineName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

