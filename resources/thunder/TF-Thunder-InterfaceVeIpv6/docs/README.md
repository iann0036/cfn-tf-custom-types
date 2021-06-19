# TF::Thunder::InterfaceVeIpv6

`thunder_interface_ve_ipv6` Provides details about thunder interface ve ipv6

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::InterfaceVeIpv6",
    "Properties" : {
        "<a href="#ifnum" title="Ifnum">Ifnum</a>" : <i>Double</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>Double</i>,
        "<a href="#inside" title="Inside">Inside</a>" : <i>Double</i>,
        "<a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>" : <i>Double</i>,
        "<a href="#outside" title="Outside">Outside</a>" : <i>Double</i>,
        "<a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#v6aclname" title="V6AclName">V6AclName</a>" : <i>String</i>,
        "<a href="#addresslist" title="AddressList">AddressList</a>" : <i>[ <a href="addresslistdefinition.md">AddressListDefinition</a>, ... ]</i>,
        "<a href="#ospf" title="Ospf">Ospf</a>" : <i>[ <a href="ospfdefinition.md">OspfDefinition</a>, ... ]</i>,
        "<a href="#rip" title="Rip">Rip</a>" : <i>[ <a href="ripdefinition.md">RipDefinition</a>, ... ]</i>,
        "<a href="#router" title="Router">Router</a>" : <i>[ <a href="routerdefinition.md">RouterDefinition</a>, ... ]</i>,
        "<a href="#routeradver" title="RouterAdver">RouterAdver</a>" : <i>[ <a href="routeradverdefinition.md">RouterAdverDefinition</a>, ... ]</i>,
        "<a href="#statefulfirewall" title="StatefulFirewall">StatefulFirewall</a>" : <i>[ <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::InterfaceVeIpv6
Properties:
    <a href="#ifnum" title="Ifnum">Ifnum</a>: <i>Double</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>Double</i>
    <a href="#inside" title="Inside">Inside</a>: <i>Double</i>
    <a href="#ipv6enable" title="Ipv6Enable">Ipv6Enable</a>: <i>Double</i>
    <a href="#outside" title="Outside">Outside</a>: <i>Double</i>
    <a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#v6aclname" title="V6AclName">V6AclName</a>: <i>String</i>
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

#### Ifnum

Interface no.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

ACL applied on incoming packets to this interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inside

Inside (private) interface for stateful firewall.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Enable

Enable IPv6 processing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outside

Outside (public) interface for stateful firewall.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TtlIgnore

Ignore TTL decrement for a received packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V6AclName

Apply ACL rules to incoming packets on this interface (Named Access List).

_Required_: No

_Type_: String

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

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

