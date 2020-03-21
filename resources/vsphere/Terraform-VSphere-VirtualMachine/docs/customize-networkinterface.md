# Terraform::VSphere::VirtualMachine Customize NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsdomain" title="DnsDomain">DnsDomain</a>" : <i>String</i>,
    "<a href="#dnsserverlist" title="DnsServerList">DnsServerList</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
    "<a href="#ipv4netmask" title="Ipv4Netmask">Ipv4Netmask</a>" : <i>Double</i>,
    "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
    "<a href="#ipv6netmask" title="Ipv6Netmask">Ipv6Netmask</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dnsdomain" title="DnsDomain">DnsDomain</a>: <i>String</i>
<a href="#dnsserverlist" title="DnsServerList">DnsServerList</a>: <i>
      - String</i>
<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
<a href="#ipv4netmask" title="Ipv4Netmask">Ipv4Netmask</a>: <i>Double</i>
<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
<a href="#ipv6netmask" title="Ipv6Netmask">Ipv6Netmask</a>: <i>Double</i>
</pre>

## Properties

#### DnsDomain

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServerList

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Netmask

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Netmask

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

