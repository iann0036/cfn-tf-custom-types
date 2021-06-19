# TF::FortiOS::VpnIpsecPhase2interface

Configure VPN autokey tunnel.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnIpsecPhase2interface",
    "Properties" : {
        "<a href="#addroute" title="AddRoute">AddRoute</a>" : <i>String</i>,
        "<a href="#autodiscoveryforwarder" title="AutoDiscoveryForwarder">AutoDiscoveryForwarder</a>" : <i>String</i>,
        "<a href="#autodiscoverysender" title="AutoDiscoverySender">AutoDiscoverySender</a>" : <i>String</i>,
        "<a href="#autonegotiate" title="AutoNegotiate">AutoNegotiate</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dhcpipsec" title="DhcpIpsec">DhcpIpsec</a>" : <i>String</i>,
        "<a href="#dhgrp" title="Dhgrp">Dhgrp</a>" : <i>String</i>,
        "<a href="#diffserv" title="Diffserv">Diffserv</a>" : <i>String</i>,
        "<a href="#diffservcode" title="Diffservcode">Diffservcode</a>" : <i>String</i>,
        "<a href="#dstaddrtype" title="DstAddrType">DstAddrType</a>" : <i>String</i>,
        "<a href="#dstendip" title="DstEndIp">DstEndIp</a>" : <i>String</i>,
        "<a href="#dstendip6" title="DstEndIp6">DstEndIp6</a>" : <i>String</i>,
        "<a href="#dstname" title="DstName">DstName</a>" : <i>String</i>,
        "<a href="#dstname6" title="DstName6">DstName6</a>" : <i>String</i>,
        "<a href="#dstport" title="DstPort">DstPort</a>" : <i>Double</i>,
        "<a href="#dststartip" title="DstStartIp">DstStartIp</a>" : <i>String</i>,
        "<a href="#dststartip6" title="DstStartIp6">DstStartIp6</a>" : <i>String</i>,
        "<a href="#dstsubnet" title="DstSubnet">DstSubnet</a>" : <i>String</i>,
        "<a href="#dstsubnet6" title="DstSubnet6">DstSubnet6</a>" : <i>String</i>,
        "<a href="#encapsulation" title="Encapsulation">Encapsulation</a>" : <i>String</i>,
        "<a href="#initiatortsnarrow" title="InitiatorTsNarrow">InitiatorTsNarrow</a>" : <i>String</i>,
        "<a href="#ipv4df" title="Ipv4Df">Ipv4Df</a>" : <i>String</i>,
        "<a href="#keepalive" title="Keepalive">Keepalive</a>" : <i>String</i>,
        "<a href="#keylifetype" title="KeylifeType">KeylifeType</a>" : <i>String</i>,
        "<a href="#keylifekbs" title="Keylifekbs">Keylifekbs</a>" : <i>Double</i>,
        "<a href="#keylifeseconds" title="Keylifeseconds">Keylifeseconds</a>" : <i>Double</i>,
        "<a href="#l2tp" title="L2tp">L2tp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pfs" title="Pfs">Pfs</a>" : <i>String</i>,
        "<a href="#phase1name" title="Phase1name">Phase1name</a>" : <i>String</i>,
        "<a href="#proposal" title="Proposal">Proposal</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
        "<a href="#replay" title="Replay">Replay</a>" : <i>String</i>,
        "<a href="#routeoverlap" title="RouteOverlap">RouteOverlap</a>" : <i>String</i>,
        "<a href="#singlesource" title="SingleSource">SingleSource</a>" : <i>String</i>,
        "<a href="#srcaddrtype" title="SrcAddrType">SrcAddrType</a>" : <i>String</i>,
        "<a href="#srcendip" title="SrcEndIp">SrcEndIp</a>" : <i>String</i>,
        "<a href="#srcendip6" title="SrcEndIp6">SrcEndIp6</a>" : <i>String</i>,
        "<a href="#srcname" title="SrcName">SrcName</a>" : <i>String</i>,
        "<a href="#srcname6" title="SrcName6">SrcName6</a>" : <i>String</i>,
        "<a href="#srcport" title="SrcPort">SrcPort</a>" : <i>Double</i>,
        "<a href="#srcstartip" title="SrcStartIp">SrcStartIp</a>" : <i>String</i>,
        "<a href="#srcstartip6" title="SrcStartIp6">SrcStartIp6</a>" : <i>String</i>,
        "<a href="#srcsubnet" title="SrcSubnet">SrcSubnet</a>" : <i>String</i>,
        "<a href="#srcsubnet6" title="SrcSubnet6">SrcSubnet6</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnIpsecPhase2interface
Properties:
    <a href="#addroute" title="AddRoute">AddRoute</a>: <i>String</i>
    <a href="#autodiscoveryforwarder" title="AutoDiscoveryForwarder">AutoDiscoveryForwarder</a>: <i>String</i>
    <a href="#autodiscoverysender" title="AutoDiscoverySender">AutoDiscoverySender</a>: <i>String</i>
    <a href="#autonegotiate" title="AutoNegotiate">AutoNegotiate</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dhcpipsec" title="DhcpIpsec">DhcpIpsec</a>: <i>String</i>
    <a href="#dhgrp" title="Dhgrp">Dhgrp</a>: <i>String</i>
    <a href="#diffserv" title="Diffserv">Diffserv</a>: <i>String</i>
    <a href="#diffservcode" title="Diffservcode">Diffservcode</a>: <i>String</i>
    <a href="#dstaddrtype" title="DstAddrType">DstAddrType</a>: <i>String</i>
    <a href="#dstendip" title="DstEndIp">DstEndIp</a>: <i>String</i>
    <a href="#dstendip6" title="DstEndIp6">DstEndIp6</a>: <i>String</i>
    <a href="#dstname" title="DstName">DstName</a>: <i>String</i>
    <a href="#dstname6" title="DstName6">DstName6</a>: <i>String</i>
    <a href="#dstport" title="DstPort">DstPort</a>: <i>Double</i>
    <a href="#dststartip" title="DstStartIp">DstStartIp</a>: <i>String</i>
    <a href="#dststartip6" title="DstStartIp6">DstStartIp6</a>: <i>String</i>
    <a href="#dstsubnet" title="DstSubnet">DstSubnet</a>: <i>String</i>
    <a href="#dstsubnet6" title="DstSubnet6">DstSubnet6</a>: <i>String</i>
    <a href="#encapsulation" title="Encapsulation">Encapsulation</a>: <i>String</i>
    <a href="#initiatortsnarrow" title="InitiatorTsNarrow">InitiatorTsNarrow</a>: <i>String</i>
    <a href="#ipv4df" title="Ipv4Df">Ipv4Df</a>: <i>String</i>
    <a href="#keepalive" title="Keepalive">Keepalive</a>: <i>String</i>
    <a href="#keylifetype" title="KeylifeType">KeylifeType</a>: <i>String</i>
    <a href="#keylifekbs" title="Keylifekbs">Keylifekbs</a>: <i>Double</i>
    <a href="#keylifeseconds" title="Keylifeseconds">Keylifeseconds</a>: <i>Double</i>
    <a href="#l2tp" title="L2tp">L2tp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pfs" title="Pfs">Pfs</a>: <i>String</i>
    <a href="#phase1name" title="Phase1name">Phase1name</a>: <i>String</i>
    <a href="#proposal" title="Proposal">Proposal</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
    <a href="#replay" title="Replay">Replay</a>: <i>String</i>
    <a href="#routeoverlap" title="RouteOverlap">RouteOverlap</a>: <i>String</i>
    <a href="#singlesource" title="SingleSource">SingleSource</a>: <i>String</i>
    <a href="#srcaddrtype" title="SrcAddrType">SrcAddrType</a>: <i>String</i>
    <a href="#srcendip" title="SrcEndIp">SrcEndIp</a>: <i>String</i>
    <a href="#srcendip6" title="SrcEndIp6">SrcEndIp6</a>: <i>String</i>
    <a href="#srcname" title="SrcName">SrcName</a>: <i>String</i>
    <a href="#srcname6" title="SrcName6">SrcName6</a>: <i>String</i>
    <a href="#srcport" title="SrcPort">SrcPort</a>: <i>Double</i>
    <a href="#srcstartip" title="SrcStartIp">SrcStartIp</a>: <i>String</i>
    <a href="#srcstartip6" title="SrcStartIp6">SrcStartIp6</a>: <i>String</i>
    <a href="#srcsubnet" title="SrcSubnet">SrcSubnet</a>: <i>String</i>
    <a href="#srcsubnet6" title="SrcSubnet6">SrcSubnet6</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AddRoute

Enable/disable automatic route addition. Valid values: `phase1`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDiscoveryForwarder

Enable/disable forwarding short-cut messages. Valid values: `phase1`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoDiscoverySender

Enable/disable sending short-cut messages. Valid values: `phase1`, `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoNegotiate

Enable/disable IPsec SA auto-negotiation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpIpsec

Enable/disable DHCP-IPsec. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhgrp

Phase2 DH group. Valid values: `1`, `2`, `5`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `27`, `28`, `29`, `30`, `31`, `32`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffserv

Enable/disable applying DSCP value to the IPsec tunnel outer IP header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffservcode

DSCP value to be applied to the IPsec tunnel outer IP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstAddrType

Remote proxy ID type. Valid values: `subnet`, `range`, `ip`, `name`, `subnet6`, `range6`, `ip6`, `name6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstEndIp

Remote proxy ID IPv4 end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstEndIp6

Remote proxy ID IPv6 end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstName

Remote proxy ID name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstName6

Remote proxy ID name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPort

Quick mode destination port (1 - 65535 or 0 for all).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstStartIp

Remote proxy ID IPv4 start.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstStartIp6

Remote proxy ID IPv6 start.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstSubnet

Remote proxy ID IPv4 subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstSubnet6

Remote proxy ID IPv6 subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encapsulation

ESP encapsulation mode. Valid values: `tunnel-mode`, `transport-mode`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitiatorTsNarrow

Enable/disable traffic selector narrowing for IKEv2 initiator. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Df

Enable/disable setting and resetting of IPv4 'Don't Fragment' bit. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keepalive

Enable/disable keep alive. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeylifeType

Keylife type. Valid values: `seconds`, `kbs`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keylifekbs

Phase2 key life in number of bytes of traffic (5120 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keylifeseconds

Phase2 key life in time in seconds (120 - 172800).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2tp

Enable/disable L2TP over IPsec. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IPsec tunnel name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pfs

Enable/disable PFS feature. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1name

Phase 1 determines the options required for phase 2.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proposal

Phase2 proposal. Valid values: `null-md5`, `null-sha1`, `null-sha256`, `null-sha384`, `null-sha512`, `des-null`, `des-md5`, `des-sha1`, `des-sha256`, `des-sha384`, `des-sha512`, `3des-null`, `3des-md5`, `3des-sha1`, `3des-sha256`, `3des-sha384`, `3des-sha512`, `aes128-null`, `aes128-md5`, `aes128-sha1`, `aes128-sha256`, `aes128-sha384`, `aes128-sha512`, `aes128gcm`, `aes192-null`, `aes192-md5`, `aes192-sha1`, `aes192-sha256`, `aes192-sha384`, `aes192-sha512`, `aes256-null`, `aes256-md5`, `aes256-sha1`, `aes256-sha256`, `aes256-sha384`, `aes256-sha512`, `aes256gcm`, `chacha20poly1305`, `aria128-null`, `aria128-md5`, `aria128-sha1`, `aria128-sha256`, `aria128-sha384`, `aria128-sha512`, `aria192-null`, `aria192-md5`, `aria192-sha1`, `aria192-sha256`, `aria192-sha384`, `aria192-sha512`, `aria256-null`, `aria256-md5`, `aria256-sha1`, `aria256-sha256`, `aria256-sha384`, `aria256-sha512`, `seed-null`, `seed-md5`, `seed-sha1`, `seed-sha256`, `seed-sha384`, `seed-sha512`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Quick mode protocol selector (1 - 255 or 0 for all).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replay

Enable/disable replay detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteOverlap

Action for overlapping routes. Valid values: `use-old`, `use-new`, `allow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSource

Enable/disable single source IP restriction. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcAddrType

Local proxy ID type. Valid values: `subnet`, `range`, `ip`, `name`, `subnet6`, `range6`, `ip6`, `name6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcEndIp

Local proxy ID end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcEndIp6

Local proxy ID IPv6 end.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcName

Local proxy ID name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcName6

Local proxy ID name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPort

Quick mode source port (1 - 65535 or 0 for all).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcStartIp

Local proxy ID start.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcStartIp6

Local proxy ID IPv6 start.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcSubnet

Local proxy ID subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcSubnet6

Local proxy ID IPv6 subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

