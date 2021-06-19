# TF::GoogleBeta::GoogleOsConfigPatchDeployment WindowsExecStepConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedsuccesscodes" title="AllowedSuccessCodes">AllowedSuccessCodes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#interpreter" title="Interpreter">Interpreter</a>" : <i>String</i>,
    "<a href="#localpath" title="LocalPath">LocalPath</a>" : <i>String</i>,
    "<a href="#gcsobject" title="GcsObject">GcsObject</a>" : <i>[ <a href="gcsobjectdefinition.md">GcsObjectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowedsuccesscodes" title="AllowedSuccessCodes">AllowedSuccessCodes</a>: <i>
      - Double</i>
<a href="#interpreter" title="Interpreter">Interpreter</a>: <i>String</i>
<a href="#localpath" title="LocalPath">LocalPath</a>: <i>String</i>
<a href="#gcsobject" title="GcsObject">GcsObject</a>: <i>
      - <a href="gcsobjectdefinition.md">GcsObjectDefinition</a></i>
</pre>

## Properties

#### AllowedSuccessCodes

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interpreter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsObject

_Required_: No

_Type_: List of <a href="gcsobjectdefinition.md">GcsObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

