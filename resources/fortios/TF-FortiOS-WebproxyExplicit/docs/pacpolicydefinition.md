# TF::FortiOS::WebproxyExplicit PacPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
    "<a href="#pacfiledata" title="PacFileData">PacFileData</a>" : <i>String</i>,
    "<a href="#pacfilename" title="PacFileName">PacFileName</a>" : <i>String</i>,
    "<a href="#policyid" title="Policyid">Policyid</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
    "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>,
    "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>[ <a href="srcaddr6definition.md">Srcaddr6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comments" title="Comments">Comments</a>: <i>String</i>
<a href="#pacfiledata" title="PacFileData">PacFileData</a>: <i>String</i>
<a href="#pacfilename" title="PacFileName">PacFileName</a>: <i>String</i>
<a href="#policyid" title="Policyid">Policyid</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
<a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>
      - <a href="srcaddr6definition.md">Srcaddr6Definition</a></i>
</pre>

## Properties

#### Comments

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileData

PAC file contents enclosed in quotes (maximum of 256K bytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileName

Pac file name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policyid

Policy ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

_Required_: No

_Type_: List of <a href="srcaddr6definition.md">Srcaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

