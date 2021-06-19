# TF::AWS::CloudwatchEventTarget EcsTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#launchtype" title="LaunchType">LaunchType</a>" : <i>String</i>,
    "<a href="#platformversion" title="PlatformVersion">PlatformVersion</a>" : <i>String</i>,
    "<a href="#taskcount" title="TaskCount">TaskCount</a>" : <i>Double</i>,
    "<a href="#taskdefinitionarn" title="TaskDefinitionArn">TaskDefinitionArn</a>" : <i>String</i>,
    "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#launchtype" title="LaunchType">LaunchType</a>: <i>String</i>
<a href="#platformversion" title="PlatformVersion">PlatformVersion</a>: <i>String</i>
<a href="#taskcount" title="TaskCount">TaskCount</a>: <i>Double</i>
<a href="#taskdefinitionarn" title="TaskDefinitionArn">TaskDefinitionArn</a>: <i>String</i>
<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a></i>
</pre>

## Properties

#### Group

Specifies an ECS task group for the task. The maximum length is 255 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchType

Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values include: an empty string `""` (to specify no launch type), `EC2`, or `FARGATE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformVersion

Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskCount

The number of tasks to create based on the TaskDefinition. The default is 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinitionArn

The ARN of the task definition to use if the event target is an Amazon ECS cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

