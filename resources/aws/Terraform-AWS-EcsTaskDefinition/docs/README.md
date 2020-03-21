# Terraform::AWS::EcsTaskDefinition

CloudFormation equivalent of aws_ecs_task_definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EcsTaskDefinition",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#containerdefinitions" title="ContainerDefinitions">ContainerDefinitions</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>String</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#family" title="Family">Family</a>" : <i>String</i>,
        "<a href="#ipcmode" title="IpcMode">IpcMode</a>" : <i>String</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>String</i>,
        "<a href="#networkmode" title="NetworkMode">NetworkMode</a>" : <i>String</i>,
        "<a href="#pidmode" title="PidMode">PidMode</a>" : <i>String</i>,
        "<a href="#requirescompatibilities" title="RequiresCompatibilities">RequiresCompatibilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>" : <i>String</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ &lt;a href=&#34;proxyconfiguration.md&#34;&gt;ProxyConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#volume" title="Volume">Volume</a>" : <i>[ &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;, ... ]</i>,
        "<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>" : <i>[ &lt;a href=&#34;dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>" : <i>[ &lt;a href=&#34;efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EcsTaskDefinition
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
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
    <a href="#revision" title="Revision">Revision</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#taskrolearn" title="TaskRoleArn">TaskRoleArn</a>: <i>String</i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;</i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - &lt;a href=&#34;proxyconfiguration.md&#34;&gt;ProxyConfiguration&lt;/a&gt;</i>
    <a href="#volume" title="Volume">Volume</a>: <i>
      - &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;</i>
    <a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>: <i>
      - &lt;a href=&#34;dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;</i>
    <a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>: <i>
      - &lt;a href=&#34;efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Revision

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;proxyconfiguration.md&#34;&gt;ProxyConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of &lt;a href=&#34;volume.md&#34;&gt;Volume&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerVolumeConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfsVolumeConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.

