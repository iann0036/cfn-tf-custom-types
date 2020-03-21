# Terraform::Cobbler::System Interface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bondingopts" title="BondingOpts">BondingOpts</a>" : <i>String</i>,
    "<a href="#bridgeopts" title="BridgeOpts">BridgeOpts</a>" : <i>String</i>,
    "<a href="#cnames" title="Cnames">Cnames</a>" : <i>[ String, ... ]</i>,
    "<a href="#dhcptag" title="DhcpTag">DhcpTag</a>" : <i>String</i>,
    "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
    "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
    "<a href="#interfacemaster" title="InterfaceMaster">InterfaceMaster</a>" : <i>String</i>,
    "<a href="#interfacetype" title="InterfaceType">InterfaceType</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
    "<a href="#ipv6defaultgateway" title="Ipv6DefaultGateway">Ipv6DefaultGateway</a>" : <i>String</i>,
    "<a href="#ipv6mtu" title="Ipv6Mtu">Ipv6Mtu</a>" : <i>String</i>,
    "<a href="#ipv6secondaries" title="Ipv6Secondaries">Ipv6Secondaries</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipv6staticroutes" title="Ipv6StaticRoutes">Ipv6StaticRoutes</a>" : <i>[ String, ... ]</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#management" title="Management">Management</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
    "<a href="#static" title="Static">Static</a>" : <i>Boolean</i>,
    "<a href="#staticroutes" title="StaticRoutes">StaticRoutes</a>" : <i>[ String, ... ]</i>,
    "<a href="#virtbridge" title="VirtBridge">VirtBridge</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bondingopts" title="BondingOpts">BondingOpts</a>: <i>String</i>
<a href="#bridgeopts" title="BridgeOpts">BridgeOpts</a>: <i>String</i>
<a href="#cnames" title="Cnames">Cnames</a>: <i>
      - String</i>
<a href="#dhcptag" title="DhcpTag">DhcpTag</a>: <i>String</i>
<a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
<a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
<a href="#interfacemaster" title="InterfaceMaster">InterfaceMaster</a>: <i>String</i>
<a href="#interfacetype" title="InterfaceType">InterfaceType</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
<a href="#ipv6defaultgateway" title="Ipv6DefaultGateway">Ipv6DefaultGateway</a>: <i>String</i>
<a href="#ipv6mtu" title="Ipv6Mtu">Ipv6Mtu</a>: <i>String</i>
<a href="#ipv6secondaries" title="Ipv6Secondaries">Ipv6Secondaries</a>: <i>
      - String</i>
<a href="#ipv6staticroutes" title="Ipv6StaticRoutes">Ipv6StaticRoutes</a>: <i>
      - String</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#management" title="Management">Management</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
<a href="#static" title="Static">Static</a>: <i>Boolean</i>
<a href="#staticroutes" title="StaticRoutes">StaticRoutes</a>: <i>
      - String</i>
<a href="#virtbridge" title="VirtBridge">VirtBridge</a>: <i>String</i>
</pre>

## Properties

#### BondingOpts

Options for bonded interfaces.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BridgeOpts

Options for bridge interfaces.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnames

Canonical name records.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpTag

DHCP tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

DNS name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Per-interface gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceMaster

The master interface when slave.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceType

The type of interface: na, master,
slave, bond, bond_slave, bridge, bridge_slave, bonded_bridge_slave.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The IP address of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

The IPv6 address of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DefaultGateway

The default gateawy for the
IPv6 address / interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Mtu

The MTU of the IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Secondaries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6StaticRoutes

Static routes for the IPv6
interface.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

The MAC address of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

Whether this interface is a management
interface.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The device name of the interface. ex: eth0.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

The IPv4 netmask of the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

Whether the interface should be static or
DHCP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutes

Static routes for the interface.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtBridge

The virtual bridge to attach to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

