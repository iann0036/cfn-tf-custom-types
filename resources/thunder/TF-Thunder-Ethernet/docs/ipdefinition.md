# TF::Thunder::Ethernet IpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dhcp" title="Dhcp">Dhcp</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#addresslist" title="AddressList">AddressList</a>" : <i>[ <a href="addresslistdefinition.md">AddressListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dhcp" title="Dhcp">Dhcp</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#addresslist" title="AddressList">AddressList</a>: <i>
      - <a href="addresslistdefinition.md">AddressListDefinition</a></i>
</pre>

## Properties

#### Dhcp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressList

_Required_: No

_Type_: List of <a href="addresslistdefinition.md">AddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

