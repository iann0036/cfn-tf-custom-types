# TF::Alicloud::EciContainerGroup ContainersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#commands" title="Commands">Commands</a>" : <i>[ String, ... ]</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#gpu" title="Gpu">Gpu</a>" : <i>Double</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>" : <i>String</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
    "<a href="#environmentvars" title="EnvironmentVars">EnvironmentVars</a>" : <i>[ <a href="environmentvarsdefinition.md">EnvironmentVarsDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>,
    "<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>" : <i>[ <a href="volumemountsdefinition.md">VolumeMountsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#commands" title="Commands">Commands</a>: <i>
      - String</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#gpu" title="Gpu">Gpu</a>: <i>Double</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#imagepullpolicy" title="ImagePullPolicy">ImagePullPolicy</a>: <i>String</i>
<a href="#memory" title="Memory">Memory</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
<a href="#environmentvars" title="EnvironmentVars">EnvironmentVars</a>: <i>
      - <a href="environmentvarsdefinition.md">EnvironmentVarsDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>: <i>
      - <a href="volumemountsdefinition.md">VolumeMountsDefinition</a></i>
</pre>

## Properties

#### Args

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Commands

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVars

_Required_: No

_Type_: List of <a href="environmentvarsdefinition.md">EnvironmentVarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMounts

_Required_: No

_Type_: List of <a href="volumemountsdefinition.md">VolumeMountsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

