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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BridgeOpts

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cnames

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpTag

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceMaster

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DefaultGateway

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Mtu

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Secondaries

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6StaticRoutes

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutes

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtBridge

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

