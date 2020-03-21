# Terraform::AWS::CloudwatchEventTarget EcsTarget

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
    "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ &lt;a href=&#34;ecstarget-networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;ecstarget-networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### Group

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinitionArn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;ecstarget-networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

