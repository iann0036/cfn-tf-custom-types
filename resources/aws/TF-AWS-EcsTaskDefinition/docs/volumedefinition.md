# TF::AWS::EcsTaskDefinition VolumeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>" : <i>[ <a href="dockervolumeconfigurationdefinition.md">DockerVolumeConfigurationDefinition</a>, ... ]</i>,
    "<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>" : <i>[ <a href="efsvolumeconfigurationdefinition.md">EfsVolumeConfigurationDefinition</a>, ... ]</i>,
    "<a href="#fsxwindowsfileservervolumeconfiguration" title="FsxWindowsFileServerVolumeConfiguration">FsxWindowsFileServerVolumeConfiguration</a>" : <i>[ <a href="fsxwindowsfileservervolumeconfigurationdefinition.md">FsxWindowsFileServerVolumeConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#dockervolumeconfiguration" title="DockerVolumeConfiguration">DockerVolumeConfiguration</a>: <i>
      - <a href="dockervolumeconfigurationdefinition.md">DockerVolumeConfigurationDefinition</a></i>
<a href="#efsvolumeconfiguration" title="EfsVolumeConfiguration">EfsVolumeConfiguration</a>: <i>
      - <a href="efsvolumeconfigurationdefinition.md">EfsVolumeConfigurationDefinition</a></i>
<a href="#fsxwindowsfileservervolumeconfiguration" title="FsxWindowsFileServerVolumeConfiguration">FsxWindowsFileServerVolumeConfiguration</a>: <i>
      - <a href="fsxwindowsfileservervolumeconfigurationdefinition.md">FsxWindowsFileServerVolumeConfigurationDefinition</a></i>
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

_Type_: List of <a href="dockervolumeconfigurationdefinition.md">DockerVolumeConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EfsVolumeConfiguration

_Required_: No

_Type_: List of <a href="efsvolumeconfigurationdefinition.md">EfsVolumeConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FsxWindowsFileServerVolumeConfiguration

_Required_: No

_Type_: List of <a href="fsxwindowsfileservervolumeconfigurationdefinition.md">FsxWindowsFileServerVolumeConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

