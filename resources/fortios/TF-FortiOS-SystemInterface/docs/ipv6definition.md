# TF::FortiOS::SystemInterface Ipv6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoconf" title="Autoconf">Autoconf</a>" : <i>String</i>,
    "<a href="#cliconn6status" title="CliConn6Status">CliConn6Status</a>" : <i>Double</i>,
    "<a href="#dhcp6clientoptions" title="Dhcp6ClientOptions">Dhcp6ClientOptions</a>" : <i>String</i>,
    "<a href="#dhcp6informationrequest" title="Dhcp6InformationRequest">Dhcp6InformationRequest</a>" : <i>String</i>,
    "<a href="#dhcp6prefixdelegation" title="Dhcp6PrefixDelegation">Dhcp6PrefixDelegation</a>" : <i>String</i>,
    "<a href="#dhcp6prefixhint" title="Dhcp6PrefixHint">Dhcp6PrefixHint</a>" : <i>String</i>,
    "<a href="#dhcp6prefixhintplt" title="Dhcp6PrefixHintPlt">Dhcp6PrefixHintPlt</a>" : <i>Double</i>,
    "<a href="#dhcp6prefixhintvlt" title="Dhcp6PrefixHintVlt">Dhcp6PrefixHintVlt</a>" : <i>Double</i>,
    "<a href="#dhcp6relayip" title="Dhcp6RelayIp">Dhcp6RelayIp</a>" : <i>String</i>,
    "<a href="#dhcp6relayservice" title="Dhcp6RelayService">Dhcp6RelayService</a>" : <i>String</i>,
    "<a href="#dhcp6relaytype" title="Dhcp6RelayType">Dhcp6RelayType</a>" : <i>String</i>,
    "<a href="#icmp6sendredirect" title="Icmp6SendRedirect">Icmp6SendRedirect</a>" : <i>String</i>,
    "<a href="#interfaceidentifier" title="InterfaceIdentifier">InterfaceIdentifier</a>" : <i>String</i>,
    "<a href="#ip6address" title="Ip6Address">Ip6Address</a>" : <i>String</i>,
    "<a href="#ip6allowaccess" title="Ip6Allowaccess">Ip6Allowaccess</a>" : <i>String</i>,
    "<a href="#ip6defaultlife" title="Ip6DefaultLife">Ip6DefaultLife</a>" : <i>Double</i>,
    "<a href="#ip6dnsserveroverride" title="Ip6DnsServerOverride">Ip6DnsServerOverride</a>" : <i>String</i>,
    "<a href="#ip6hoplimit" title="Ip6HopLimit">Ip6HopLimit</a>" : <i>Double</i>,
    "<a href="#ip6linkmtu" title="Ip6LinkMtu">Ip6LinkMtu</a>" : <i>Double</i>,
    "<a href="#ip6manageflag" title="Ip6ManageFlag">Ip6ManageFlag</a>" : <i>String</i>,
    "<a href="#ip6maxinterval" title="Ip6MaxInterval">Ip6MaxInterval</a>" : <i>Double</i>,
    "<a href="#ip6mininterval" title="Ip6MinInterval">Ip6MinInterval</a>" : <i>Double</i>,
    "<a href="#ip6mode" title="Ip6Mode">Ip6Mode</a>" : <i>String</i>,
    "<a href="#ip6otherflag" title="Ip6OtherFlag">Ip6OtherFlag</a>" : <i>String</i>,
    "<a href="#ip6prefixmode" title="Ip6PrefixMode">Ip6PrefixMode</a>" : <i>String</i>,
    "<a href="#ip6reachabletime" title="Ip6ReachableTime">Ip6ReachableTime</a>" : <i>Double</i>,
    "<a href="#ip6retranstime" title="Ip6RetransTime">Ip6RetransTime</a>" : <i>Double</i>,
    "<a href="#ip6sendadv" title="Ip6SendAdv">Ip6SendAdv</a>" : <i>String</i>,
    "<a href="#ip6subnet" title="Ip6Subnet">Ip6Subnet</a>" : <i>String</i>,
    "<a href="#ip6upstreaminterface" title="Ip6UpstreamInterface">Ip6UpstreamInterface</a>" : <i>String</i>,
    "<a href="#ndcert" title="NdCert">NdCert</a>" : <i>String</i>,
    "<a href="#ndcgamodifier" title="NdCgaModifier">NdCgaModifier</a>" : <i>String</i>,
    "<a href="#ndmode" title="NdMode">NdMode</a>" : <i>String</i>,
    "<a href="#ndsecuritylevel" title="NdSecurityLevel">NdSecurityLevel</a>" : <i>Double</i>,
    "<a href="#ndtimestampdelta" title="NdTimestampDelta">NdTimestampDelta</a>" : <i>Double</i>,
    "<a href="#ndtimestampfuzz" title="NdTimestampFuzz">NdTimestampFuzz</a>" : <i>Double</i>,
    "<a href="#uniqueautoconfaddr" title="UniqueAutoconfAddr">UniqueAutoconfAddr</a>" : <i>String</i>,
    "<a href="#vrip6linklocal" title="Vrip6LinkLocal">Vrip6LinkLocal</a>" : <i>String</i>,
    "<a href="#vrrpvirtualmac6" title="VrrpVirtualMac6">VrrpVirtualMac6</a>" : <i>String</i>,
    "<a href="#ip6delegatedprefixlist" title="Ip6DelegatedPrefixList">Ip6DelegatedPrefixList</a>" : <i>[ <a href="ip6delegatedprefixlistdefinition.md">Ip6DelegatedPrefixListDefinition</a>, ... ]</i>,
    "<a href="#ip6extraaddr" title="Ip6ExtraAddr">Ip6ExtraAddr</a>" : <i>[ <a href="ip6extraaddrdefinition.md">Ip6ExtraAddrDefinition</a>, ... ]</i>,
    "<a href="#ip6prefixlist" title="Ip6PrefixList">Ip6PrefixList</a>" : <i>[ <a href="ip6prefixlistdefinition.md">Ip6PrefixListDefinition</a>, ... ]</i>,
    "<a href="#vrrp6" title="Vrrp6">Vrrp6</a>" : <i>[ <a href="vrrp6definition.md">Vrrp6Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoconf" title="Autoconf">Autoconf</a>: <i>String</i>
<a href="#cliconn6status" title="CliConn6Status">CliConn6Status</a>: <i>Double</i>
<a href="#dhcp6clientoptions" title="Dhcp6ClientOptions">Dhcp6ClientOptions</a>: <i>String</i>
<a href="#dhcp6informationrequest" title="Dhcp6InformationRequest">Dhcp6InformationRequest</a>: <i>String</i>
<a href="#dhcp6prefixdelegation" title="Dhcp6PrefixDelegation">Dhcp6PrefixDelegation</a>: <i>String</i>
<a href="#dhcp6prefixhint" title="Dhcp6PrefixHint">Dhcp6PrefixHint</a>: <i>String</i>
<a href="#dhcp6prefixhintplt" title="Dhcp6PrefixHintPlt">Dhcp6PrefixHintPlt</a>: <i>Double</i>
<a href="#dhcp6prefixhintvlt" title="Dhcp6PrefixHintVlt">Dhcp6PrefixHintVlt</a>: <i>Double</i>
<a href="#dhcp6relayip" title="Dhcp6RelayIp">Dhcp6RelayIp</a>: <i>String</i>
<a href="#dhcp6relayservice" title="Dhcp6RelayService">Dhcp6RelayService</a>: <i>String</i>
<a href="#dhcp6relaytype" title="Dhcp6RelayType">Dhcp6RelayType</a>: <i>String</i>
<a href="#icmp6sendredirect" title="Icmp6SendRedirect">Icmp6SendRedirect</a>: <i>String</i>
<a href="#interfaceidentifier" title="InterfaceIdentifier">InterfaceIdentifier</a>: <i>String</i>
<a href="#ip6address" title="Ip6Address">Ip6Address</a>: <i>String</i>
<a href="#ip6allowaccess" title="Ip6Allowaccess">Ip6Allowaccess</a>: <i>String</i>
<a href="#ip6defaultlife" title="Ip6DefaultLife">Ip6DefaultLife</a>: <i>Double</i>
<a href="#ip6dnsserveroverride" title="Ip6DnsServerOverride">Ip6DnsServerOverride</a>: <i>String</i>
<a href="#ip6hoplimit" title="Ip6HopLimit">Ip6HopLimit</a>: <i>Double</i>
<a href="#ip6linkmtu" title="Ip6LinkMtu">Ip6LinkMtu</a>: <i>Double</i>
<a href="#ip6manageflag" title="Ip6ManageFlag">Ip6ManageFlag</a>: <i>String</i>
<a href="#ip6maxinterval" title="Ip6MaxInterval">Ip6MaxInterval</a>: <i>Double</i>
<a href="#ip6mininterval" title="Ip6MinInterval">Ip6MinInterval</a>: <i>Double</i>
<a href="#ip6mode" title="Ip6Mode">Ip6Mode</a>: <i>String</i>
<a href="#ip6otherflag" title="Ip6OtherFlag">Ip6OtherFlag</a>: <i>String</i>
<a href="#ip6prefixmode" title="Ip6PrefixMode">Ip6PrefixMode</a>: <i>String</i>
<a href="#ip6reachabletime" title="Ip6ReachableTime">Ip6ReachableTime</a>: <i>Double</i>
<a href="#ip6retranstime" title="Ip6RetransTime">Ip6RetransTime</a>: <i>Double</i>
<a href="#ip6sendadv" title="Ip6SendAdv">Ip6SendAdv</a>: <i>String</i>
<a href="#ip6subnet" title="Ip6Subnet">Ip6Subnet</a>: <i>String</i>
<a href="#ip6upstreaminterface" title="Ip6UpstreamInterface">Ip6UpstreamInterface</a>: <i>String</i>
<a href="#ndcert" title="NdCert">NdCert</a>: <i>String</i>
<a href="#ndcgamodifier" title="NdCgaModifier">NdCgaModifier</a>: <i>String</i>
<a href="#ndmode" title="NdMode">NdMode</a>: <i>String</i>
<a href="#ndsecuritylevel" title="NdSecurityLevel">NdSecurityLevel</a>: <i>Double</i>
<a href="#ndtimestampdelta" title="NdTimestampDelta">NdTimestampDelta</a>: <i>Double</i>
<a href="#ndtimestampfuzz" title="NdTimestampFuzz">NdTimestampFuzz</a>: <i>Double</i>
<a href="#uniqueautoconfaddr" title="UniqueAutoconfAddr">UniqueAutoconfAddr</a>: <i>String</i>
<a href="#vrip6linklocal" title="Vrip6LinkLocal">Vrip6LinkLocal</a>: <i>String</i>
<a href="#vrrpvirtualmac6" title="VrrpVirtualMac6">VrrpVirtualMac6</a>: <i>String</i>
<a href="#ip6delegatedprefixlist" title="Ip6DelegatedPrefixList">Ip6DelegatedPrefixList</a>: <i>
      - <a href="ip6delegatedprefixlistdefinition.md">Ip6DelegatedPrefixListDefinition</a></i>
<a href="#ip6extraaddr" title="Ip6ExtraAddr">Ip6ExtraAddr</a>: <i>
      - <a href="ip6extraaddrdefinition.md">Ip6ExtraAddrDefinition</a></i>
<a href="#ip6prefixlist" title="Ip6PrefixList">Ip6PrefixList</a>: <i>
      - <a href="ip6prefixlistdefinition.md">Ip6PrefixListDefinition</a></i>
<a href="#vrrp6" title="Vrrp6">Vrrp6</a>: <i>
      - <a href="vrrp6definition.md">Vrrp6Definition</a></i>
</pre>

## Properties

#### Autoconf

Enable/disable address auto config. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CliConn6Status

CLI IPv6 connection status.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6ClientOptions

DHCPv6 client options. Valid values: `rapid`, `iapd`, `iana`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6InformationRequest

Enable/disable DHCPv6 information request. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6PrefixDelegation

Enable/disable DHCPv6 prefix delegation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6PrefixHint

DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6PrefixHintPlt

DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6PrefixHintVlt

DHCPv6 prefix hint valid life time (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6RelayIp

DHCPv6 relay IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6RelayService

Enable/disable DHCPv6 relay. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp6RelayType

DHCPv6 relay type. Valid values: `regular`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmp6SendRedirect

Enable/disable sending of ICMPv6 redirects. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceIdentifier

IPv6 interface identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Address

Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Allowaccess

Allow management access to the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6DefaultLife

Default life (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6DnsServerOverride

Enable/disable using the DNS server acquired by DHCP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6HopLimit

Hop limit (0 means unspecified).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6LinkMtu

IPv6 link MTU.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6ManageFlag

Enable/disable the managed flag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6MaxInterval

IPv6 maximum interval (4 to 1800 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6MinInterval

IPv6 minimum interval (3 to 1350 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Mode

Addressing mode (static, DHCP, delegated). Valid values: `static`, `dhcp`, `pppoe`, `delegated`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6OtherFlag

Enable/disable the other IPv6 flag. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6PrefixMode

Assigning a prefix from DHCP or RA. Valid values: `dhcp6`, `ra`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6ReachableTime

IPv6 reachable time (milliseconds; 0 means unspecified).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6RetransTime

IPv6 retransmit time (milliseconds; 0 means unspecified).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6SendAdv

Enable/disable sending advertisements about the interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6Subnet

Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6UpstreamInterface

Interface name providing delegated information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdCert

Neighbor discovery certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdCgaModifier

Neighbor discovery CGA modifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdMode

Neighbor discovery mode. Valid values: `basic`, `SEND-compatible`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdSecurityLevel

Neighbor discovery security level (0 - 7; 0 = least secure, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdTimestampDelta

Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NdTimestampFuzz

Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UniqueAutoconfAddr

Enable/disable unique auto config address. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrip6LinkLocal

Link-local IPv6 address of virtual router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpVirtualMac6

Enable/disable virtual MAC for VRRP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6DelegatedPrefixList

_Required_: No

_Type_: List of <a href="ip6delegatedprefixlistdefinition.md">Ip6DelegatedPrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6ExtraAddr

_Required_: No

_Type_: List of <a href="ip6extraaddrdefinition.md">Ip6ExtraAddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip6PrefixList

_Required_: No

_Type_: List of <a href="ip6prefixlistdefinition.md">Ip6PrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrrp6

_Required_: No

_Type_: List of <a href="vrrp6definition.md">Vrrp6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

