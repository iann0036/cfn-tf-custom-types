# TF::FortiOS::VpnsslwebPortal SplitDnsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>" : <i>String</i>,
    "<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>" : <i>String</i>,
    "<a href="#domains" title="Domains">Domains</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>" : <i>String</i>,
    "<a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>: <i>String</i>
<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>: <i>String</i>
<a href="#domains" title="Domains">Domains</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>: <i>String</i>
<a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>: <i>String</i>
</pre>

## Properties

#### DnsServer1

DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer2

DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

Split DNS domains used for SSL-VPN clients separated by comma(,).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer1

IPv6 DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer2

IPv6 DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

