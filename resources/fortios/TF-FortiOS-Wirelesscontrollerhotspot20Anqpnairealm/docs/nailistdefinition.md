# TF::FortiOS::Wirelesscontrollerhotspot20Anqpnairealm NaiListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encoding" title="Encoding">Encoding</a>" : <i>String</i>,
    "<a href="#nairealm" title="NaiRealm">NaiRealm</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#eapmethod" title="EapMethod">EapMethod</a>" : <i>[ <a href="eapmethoddefinition.md">EapMethodDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#encoding" title="Encoding">Encoding</a>: <i>String</i>
<a href="#nairealm" title="NaiRealm">NaiRealm</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#eapmethod" title="EapMethod">EapMethod</a>: <i>
      - <a href="eapmethoddefinition.md">EapMethodDefinition</a></i>
</pre>

## Properties

#### Encoding

Enable/disable format in accordance with IETF RFC 4282. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NaiRealm

Configure NAI realms (delimited by a semi-colon character).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

NAI realm name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapMethod

_Required_: No

_Type_: List of <a href="eapmethoddefinition.md">EapMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

