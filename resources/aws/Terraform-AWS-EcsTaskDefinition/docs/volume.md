# Terraform::AWS::EcsTaskDefinition Volume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>" : <i>[ &lt;a href=&#34;volume-dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;, ... ]</i>,
    "<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>" : <i>[ &lt;a href=&#34;volume-efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>: <i>
      - &lt;a href=&#34;volume-dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;</i>
<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>: <i>
      - &lt;a href=&#34;volume-efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### HostPath

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerVolumeConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;volume-dockervolumeconfiguration.md&#34;&gt;DockerVolumeConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfsVolumeConfiguration

_Required_: No
_Type_: List of &lt;a href=&#34;volume-efsvolumeconfiguration.md&#34;&gt;EfsVolumeConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

