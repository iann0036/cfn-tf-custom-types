# Terraform::AWS::EcsTaskDefinition

Manages a revision of an ECS task definition to be used in `aws_ecs_service`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EcsTaskDefinition",
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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>" : <i>String</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ <a href="placementconstraints.md">PlacementConstraints</a>, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ <a href="proxyconfiguration.md">ProxyConfiguration</a>, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volume.md">Volume</a>, ... ]</i>,
        "<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>" : <i>[ <a href="dockervolumeconfiguration.md">DockerVolumeConfiguration</a>, ... ]</i>,
        "<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>" : <i>[ <a href="efsvolumeconfiguration.md">EfsVolumeConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EcsTaskDefinition
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
      - <a href="tags.md">Tags</a></i>
    <a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>: <i>String</i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - <a href="placementconstraints.md">PlacementConstraints</a></i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - <a href="proxyconfiguration.md">ProxyConfiguration</a></i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volume.md">Volume</a></i>
    <a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>: <i>
      - <a href="dockervolumeconfiguration.md">DockerVolumeConfiguration</a></i>
    <a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>: <i>
      - <a href="efsvolumeconfiguration.md">EfsVolumeConfiguration</a></i>
</pre>

## Properties

#### ContainerDefinitions

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Family

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpcMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PidMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiresCompatibilities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of <a href="placementconstraints.md">PlacementConstraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of <a href="proxyconfiguration.md">ProxyConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerVolumeConfiguration

_Required_: No

_Type_: List of <a href="dockervolumeconfiguration.md">DockerVolumeConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfsVolumeConfiguration

_Required_: No

_Type_: List of <a href="efsvolumeconfiguration.md">EfsVolumeConfiguration</a>

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

