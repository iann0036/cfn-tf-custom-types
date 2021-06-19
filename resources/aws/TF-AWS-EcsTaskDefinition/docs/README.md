# TF::AWS::EcsTaskDefinition

Manages a revision of an ECS task definition to be used in `aws_ecs_service`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EcsTaskDefinition",
    "Properties" : {
        "<a href="#containerdefinitions" title="ContainerDefinitions">ContainerDefinitions</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#family" title="Family">Family</a>" : <i>String</i>,
        "<a href="#ipcmode" title="IpcMode">IpcMode</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>String</i>,
        "<a href="#networkmode" title="NetworkMode">NetworkMode</a>" : <i>String</i>,
        "<a href="#pidmode" title="PidMode">PidMode</a>" : <i>String</i>,
        "<a href="#requirescompatibilities" title="RequiresCompatibilities">RequiresCompatibilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>" : <i>String</i>,
        "<a href="#ephemeralstorage" title="EphemeralStorage">EphemeralStorage</a>" : <i>[ <a href="ephemeralstoragedefinition.md">EphemeralStorageDefinition</a>, ... ]</i>,
        "<a href="#inferenceaccelerator" title="InferenceAccelerator">InferenceAccelerator</a>" : <i>[ <a href="inferenceacceleratordefinition.md">InferenceAcceleratorDefinition</a>, ... ]</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a>, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volumedefinition.md">VolumeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EcsTaskDefinition
Properties:
    <a href="#containerdefinitions" title="ContainerDefinitions">ContainerDefinitions</a>: <i>String</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>String</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#family" title="Family">Family</a>: <i>String</i>
    <a href="#ipcmode" title="IpcMode">IpcMode</a>: <i>String</i>
    <a href="#memory" title="Memory">Memory</a>: <i>String</i>
    <a href="#networkmode" title="NetworkMode">NetworkMode</a>: <i>String</i>
    <a href="#pidmode" title="PidMode">PidMode</a>: <i>String</i>
    <a href="#requirescompatibilities" title="RequiresCompatibilities">RequiresCompatibilities</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>: <i>String</i>
    <a href="#ephemeralstorage" title="EphemeralStorage">EphemeralStorage</a>: <i>
      - <a href="ephemeralstoragedefinition.md">EphemeralStorageDefinition</a></i>
    <a href="#inferenceaccelerator" title="InferenceAccelerator">InferenceAccelerator</a>: <i>
      - <a href="inferenceacceleratordefinition.md">InferenceAcceleratorDefinition</a></i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a></i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volumedefinition.md">VolumeDefinition</a></i>
</pre>

## Properties

#### ContainerDefinitions

A list of valid [container definitions](http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a single valid JSON document. Please note that you should only provide values that are part of the container definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

Number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

ARN of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

A unique name for your task definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpcMode

IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

Amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMode

Docker networking mode to use for the containers in the task. Valid values are `none`, `bridge`, `awsvpc`, and `host`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidMode

Process namespace to use for the containers in the task. The valid values are `host` and `task`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresCompatibilities

Set of launch types required by the task. The valid values are `EC2` and `FARGATE`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskRoleArn

ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralStorage

_Required_: No

_Type_: List of <a href="ephemeralstoragedefinition.md">EphemeralStorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InferenceAccelerator

_Required_: No

_Type_: List of <a href="inferenceacceleratordefinition.md">InferenceAcceleratorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volumedefinition.md">VolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Revision

Returns the <code>Revision</code> value.

