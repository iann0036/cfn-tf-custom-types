# TF::GoogleBeta::GoogleOsConfigGuestPolicies ScriptRunDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedexitcodes" title="AllowedExitCodes">AllowedExitCodes</a>" : <i>[ Double, ... ]</i>,
    "<a href="#interpreter" title="Interpreter">Interpreter</a>" : <i>String</i>,
    "<a href="#script" title="Script">Script</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowedexitcodes" title="AllowedExitCodes">AllowedExitCodes</a>: <i>
      - Double</i>
<a href="#interpreter" title="Interpreter">Interpreter</a>: <i>String</i>
<a href="#script" title="Script">Script</a>: <i>String</i>
</pre>

## Properties

#### AllowedExitCodes

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interpreter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

