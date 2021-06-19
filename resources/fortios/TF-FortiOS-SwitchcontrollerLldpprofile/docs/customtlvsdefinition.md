# TF::FortiOS::SwitchcontrollerLldpprofile CustomTlvsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#informationstring" title="InformationString">InformationString</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#oui" title="Oui">Oui</a>" : <i>String</i>,
    "<a href="#subtype" title="Subtype">Subtype</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#informationstring" title="InformationString">InformationString</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#oui" title="Oui">Oui</a>: <i>String</i>
<a href="#subtype" title="Subtype">Subtype</a>: <i>Double</i>
</pre>

## Properties

#### InformationString

Organizationally defined information string (0 - 507 hexadecimal bytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

TLV name (not sent).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oui

Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtype

Organizationally defined subtype (0 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

