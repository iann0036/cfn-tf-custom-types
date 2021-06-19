# TF::AVI::Hardwaresecuritymodulegroup HsmDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#cloudhsm" title="Cloudhsm">Cloudhsm</a>" : <i>[ <a href="cloudhsmdefinition.md">CloudhsmDefinition</a>, ... ]</i>,
    "<a href="#nethsm" title="Nethsm">Nethsm</a>" : <i>[ <a href="nethsmdefinition.md">NethsmDefinition</a>, ... ]</i>,
    "<a href="#rfs" title="Rfs">Rfs</a>" : <i>[ <a href="rfsdefinition.md">RfsDefinition</a>, ... ]</i>,
    "<a href="#sluna" title="Sluna">Sluna</a>" : <i>[ <a href="slunadefinition.md">SlunaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#cloudhsm" title="Cloudhsm">Cloudhsm</a>: <i>
      - <a href="cloudhsmdefinition.md">CloudhsmDefinition</a></i>
<a href="#nethsm" title="Nethsm">Nethsm</a>: <i>
      - <a href="nethsmdefinition.md">NethsmDefinition</a></i>
<a href="#rfs" title="Rfs">Rfs</a>: <i>
      - <a href="rfsdefinition.md">RfsDefinition</a></i>
<a href="#sluna" title="Sluna">Sluna</a>: <i>
      - <a href="slunadefinition.md">SlunaDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cloudhsm

_Required_: No

_Type_: List of <a href="cloudhsmdefinition.md">CloudhsmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nethsm

_Required_: No

_Type_: List of <a href="nethsmdefinition.md">NethsmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfs

_Required_: No

_Type_: List of <a href="rfsdefinition.md">RfsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sluna

_Required_: No

_Type_: List of <a href="slunadefinition.md">SlunaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

