# TF::StackPath::ComputeWorkload ContainerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
    "<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>" : <i>[ <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>[ <a href="portdefinition.md">PortDefinition</a>, ... ]</i>,
    "<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>" : <i>[ <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>,
    "<a href="#volumemount" title="VolumeMount">VolumeMount</a>" : <i>[ <a href="volumemountdefinition.md">VolumeMountDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
<a href="#livenessprobe" title="LivenessProbe">LivenessProbe</a>: <i>
      - <a href="livenessprobedefinition.md">LivenessProbeDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>
      - <a href="portdefinition.md">PortDefinition</a></i>
<a href="#readinessprobe" title="ReadinessProbe">ReadinessProbe</a>: <i>
      - <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a></i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
<a href="#volumemount" title="VolumeMount">VolumeMount</a>: <i>
      - <a href="volumemountdefinition.md">VolumeMountDefinition</a></i>
</pre>

## Properties

#### Command

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessProbe

_Required_: No

_Type_: List of <a href="livenessprobedefinition.md">LivenessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: List of <a href="portdefinition.md">PortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadinessProbe

_Required_: No

_Type_: List of <a href="readinessprobedefinition.md">ReadinessProbeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMount

_Required_: No

_Type_: List of <a href="volumemountdefinition.md">VolumeMountDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

