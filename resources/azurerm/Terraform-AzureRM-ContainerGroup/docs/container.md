# Terraform::AzureRM::ContainerGroup Container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commands" title="Commands">Commands</a>" : <i>[ String, ... ]</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="container-environmentvariables.md">EnvironmentVariables</a>, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>" : <i>[ <a href="container-secureenvironmentvariables.md">SecureEnvironmentVariables</a>, ... ]</i>,
    "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ <a href="container-gpu.md">Gpu</a>, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="container-livenessprobe.md">LivenessProbe</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="container-ports.md">Ports</a>, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="container-readinessprobe.md">ReadinessProbe</a>, ... ]</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="container-volume.md">Volume</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commands" title="Commands">Commands</a>: <i>
      - String</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="container-environmentvariables.md">EnvironmentVariables</a></i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#memory" title="Memory">Memory</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>: <i>
      - <a href="container-secureenvironmentvariables.md">SecureEnvironmentVariables</a></i>
<a href="#gpu" title="Gpu">Gpu</a>: <i>
      - <a href="container-gpu.md">Gpu</a></i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="container-livenessprobe.md">LivenessProbe</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="container-ports.md">Ports</a></i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="container-readinessprobe.md">ReadinessProbe</a></i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="container-volume.md">Volume</a></i>
</pre>

## Properties

#### Commands

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

_Required_: No
_Type_: List of <a href="container-environmentvariables.md">EnvironmentVariables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureEnvironmentVariables

_Required_: No
_Type_: List of <a href="container-secureenvironmentvariables.md">SecureEnvironmentVariables</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No
_Type_: List of <a href="container-gpu.md">Gpu</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No
_Type_: List of <a href="container-livenessprobe.md">LivenessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No
_Type_: List of <a href="container-ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No
_Type_: List of <a href="container-readinessprobe.md">ReadinessProbe</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No
_Type_: List of <a href="container-volume.md">Volume</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

