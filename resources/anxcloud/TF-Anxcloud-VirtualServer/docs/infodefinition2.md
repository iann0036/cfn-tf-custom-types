# TF::Anxcloud::VirtualServer InfoDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ipv4" title="IpV4">IpV4</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipv6" title="IpV6">IpV6</a>" : <i>[ String, ... ]</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#nic" title="Nic">Nic</a>" : <i>Double</i>,
    "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ipv4" title="IpV4">IpV4</a>: <i>
      - String</i>
<a href="#ipv6" title="IpV6">IpV6</a>: <i>
      - String</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#nic" title="Nic">Nic</a>: <i>Double</i>
<a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpV4

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpV6

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nic

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

