# TF::AzureRM::ContainerGroup ContainerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#commands" title="Commands">Commands</a>" : <i>[ String, ... ]</i>,
    "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
    "<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>" : <i>[ <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>" : <i>[ <a href="secureenvironmentvariablesdefinition.md">SecureEnvironmentVariablesDefinition</a>, ... ]</i>,
    "<a href="#gpu" title="Gpu">Gpu</a>" : <i>[ <a href="gpudefinition.md">GpuDefinition</a>, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>, ... ]</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volumedefinition.md">VolumeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#commands" title="Commands">Commands</a>: <i>
      - String</i>
<a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
<a href="#environmentvariables" title="EnvironmentVariables">EnvironmentVariables</a>: <i>
      - <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a></i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#memory" title="Memory">Memory</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#secureenvironmentvariables" title="SecureEnvironmentVariables">SecureEnvironmentVariables</a>: <i>
      - <a href="secureenvironmentvariablesdefinition.md">SecureEnvironmentVariablesDefinition</a></i>
<a href="#gpu" title="Gpu">Gpu</a>: <i>
      - <a href="gpudefinition.md">GpuDefinition</a></i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="livenessprobedefinition.md">LivenessProbeDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a></i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volumedefinition.md">VolumeDefinition</a></i>
</pre>

## Properties

#### Commands

A list of commands which should be run on the container. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

The required number of CPU cores of the containers. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariables

A list of environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="environmentvariablesdefinition.md">EnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The container image name. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

The required memory of the containers in GB. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Container. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureEnvironmentVariables

A list of sensitive environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="secureenvironmentvariablesdefinition.md">SecureEnvironmentVariablesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gpu

_Required_: No

_Type_: List of <a href="gpudefinition.md">GpuDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: No

_Type_: List of <a href="volumedefinition.md">VolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

