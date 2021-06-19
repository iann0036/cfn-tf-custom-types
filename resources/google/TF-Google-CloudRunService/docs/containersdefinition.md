# TF::Google::CloudRunService ContainersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#command" title="Command">Command</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#workingdir" title="WorkingDir">WorkingDir</a>" : <i>String</i>,
    "<a href="#env" title="Env">Env</a>" : <i>[ <a href="envdefinition.md">EnvDefinition</a>, ... ]</i>,
    "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ <a href="envfromdefinition.md">EnvFromDefinition</a>, ... ]</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#command" title="Command">Command</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#workingdir" title="WorkingDir">WorkingDir</a>: <i>String</i>
<a href="#env" title="Env">Env</a>: <i>
      - <a href="envdefinition.md">EnvDefinition</a></i>
<a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - <a href="envfromdefinition.md">EnvFromDefinition</a></i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
</pre>

## Properties

#### Args

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkingDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of <a href="envdefinition.md">EnvDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No

_Type_: List of <a href="envfromdefinition.md">EnvFromDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

