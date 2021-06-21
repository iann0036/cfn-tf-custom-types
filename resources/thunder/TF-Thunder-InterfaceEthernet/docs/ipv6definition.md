# TF::Thunder::InterfaceEthernet Ipv6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inside" title="Inside">Inside</a>" : <i>Double</i>,
    "<a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>" : <i>Double</i>,
    "<a href="#outside" title="Outside">Outside</a>" : <i>Double</i>,
    "<a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#accesslistcfg" title="AccessListCfg">AccessListCfg</a>" : <i>[ <a href="accesslistcfgdefinition.md">AccessListCfgDefinition</a>, ... ]</i>,
    "<a href="#addresslist" title="AddressList">AddressList</a>" : <i>[ <a href="addresslistdefinition.md">AddressListDefinition</a>, ... ]</i>,
    "<a href="#ospf" title="Ospf">Ospf</a>" : <i>[ <a href="ospfdefinition.md">OspfDefinition</a>, ... ]</i>,
    "<a href="#rip" title="Rip">Rip</a>" : <i>[ <a href="ripdefinition.md">RipDefinition</a>, ... ]</i>,
    "<a href="#router" title="Router">Router</a>" : <i>[ <a href="routerdefinition.md">RouterDefinition</a>, ... ]</i>,
    "<a href="#routeradver" title="RouterAdver">RouterAdver</a>" : <i>[ <a href="routeradverdefinition.md">RouterAdverDefinition</a>, ... ]</i>,
    "<a href="#statefulfirewall" title="StatefulFirewall">StatefulFirewall</a>" : <i>[ <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inside" title="Inside">Inside</a>: <i>Double</i>
<a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>: <i>Double</i>
<a href="#outside" title="Outside">Outside</a>: <i>Double</i>
<a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#accesslistcfg" title="AccessListCfg">AccessListCfg</a>: <i>
      - <a href="accesslistcfgdefinition.md">AccessListCfgDefinition</a></i>
<a href="#addresslist" title="AddressList">AddressList</a>: <i>
      - <a href="addresslistdefinition.md">AddressListDefinition</a></i>
<a href="#ospf" title="Ospf">Ospf</a>: <i>
      - <a href="ospfdefinition.md">OspfDefinition</a></i>
<a href="#rip" title="Rip">Rip</a>: <i>
      - <a href="ripdefinition.md">RipDefinition</a></i>
<a href="#router" title="Router">Router</a>: <i>
      - <a href="routerdefinition.md">RouterDefinition</a></i>
<a href="#routeradver" title="RouterAdver">RouterAdver</a>: <i>
      - <a href="routeradverdefinition.md">RouterAdverDefinition</a></i>
<a href="#statefulfirewall" title="StatefulFirewall">StatefulFirewall</a>: <i>
      - <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a></i>
</pre>

## Properties

#### Inside

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Enable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outside

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TtlIgnore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessListCfg

_Required_: No

_Type_: List of <a href="accesslistcfgdefinition.md">AccessListCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressList

_Required_: No

_Type_: List of <a href="addresslistdefinition.md">AddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf

_Required_: No

_Type_: List of <a href="ospfdefinition.md">OspfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rip

_Required_: No

_Type_: List of <a href="ripdefinition.md">RipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: No

_Type_: List of <a href="routerdefinition.md">RouterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterAdver

_Required_: No

_Type_: List of <a href="routeradverdefinition.md">RouterAdverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulFirewall

_Required_: No

_Type_: List of <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
