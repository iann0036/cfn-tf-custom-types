# TF::AVI::Hardwaresecuritymodulegroup NethsmDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#esn" title="Esn">Esn</a>" : <i>String</i>,
    "<a href="#keyhash" title="Keyhash">Keyhash</a>" : <i>String</i>,
    "<a href="#moduleid" title="ModuleId">ModuleId</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#remoteport" title="RemotePort">RemotePort</a>" : <i>Double</i>,
    "<a href="#remoteip" title="RemoteIp">RemoteIp</a>" : <i>[ <a href="remoteipdefinition.md">RemoteIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#esn" title="Esn">Esn</a>: <i>String</i>
<a href="#keyhash" title="Keyhash">Keyhash</a>: <i>String</i>
<a href="#moduleid" title="ModuleId">ModuleId</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#remoteport" title="RemotePort">RemotePort</a>: <i>Double</i>
<a href="#remoteip" title="RemoteIp">RemoteIp</a>: <i>
      - <a href="remoteipdefinition.md">RemoteIpDefinition</a></i>
</pre>

## Properties

#### Esn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keyhash

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModuleId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemotePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIp

_Required_: No

_Type_: List of <a href="remoteipdefinition.md">RemoteIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

