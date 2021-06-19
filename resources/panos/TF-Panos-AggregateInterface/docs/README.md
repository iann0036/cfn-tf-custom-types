# TF::Panos::AggregateInterface

This resource allows you to add/update/delete aggregate ethernet interfaces.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::AggregateInterface",
    "Properties" : {
        "<a href="#adjusttcpmss" title="AdjustTcpMss">AdjustTcpMss</a>" : <i>Boolean</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#createdhcpdefaultroute" title="CreateDhcpDefaultRoute">CreateDhcpDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#decryptforward" title="DecryptForward">DecryptForward</a>" : <i>Boolean</i>,
        "<a href="#dhcpdefaultroutemetric" title="DhcpDefaultRouteMetric">DhcpDefaultRouteMetric</a>" : <i>Double</i>,
        "<a href="#dhcpsendhostnameenable" title="DhcpSendHostnameEnable">DhcpSendHostnameEnable</a>" : <i>Boolean</i>,
        "<a href="#dhcpsendhostnamevalue" title="DhcpSendHostnameValue">DhcpSendHostnameValue</a>" : <i>String</i>,
        "<a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>" : <i>Boolean</i>,
        "<a href="#enableuntaggedsubinterface" title="EnableUntaggedSubinterface">EnableUntaggedSubinterface</a>" : <i>Boolean</i>,
        "<a href="#ipv4mssadjust" title="Ipv4MssAdjust">Ipv4MssAdjust</a>" : <i>Double</i>,
        "<a href="#ipv6enabled" title="Ipv6Enabled">Ipv6Enabled</a>" : <i>Boolean</i>,
        "<a href="#ipv6interfaceid" title="Ipv6InterfaceId">Ipv6InterfaceId</a>" : <i>String</i>,
        "<a href="#ipv6mssadjust" title="Ipv6MssAdjust">Ipv6MssAdjust</a>" : <i>Double</i>,
        "<a href="#lacpenable" title="LacpEnable">LacpEnable</a>" : <i>Boolean</i>,
        "<a href="#lacpfastfailover" title="LacpFastFailover">LacpFastFailover</a>" : <i>Boolean</i>,
        "<a href="#lacphaenablesamesystemmac" title="LacpHaEnableSameSystemMac">LacpHaEnableSameSystemMac</a>" : <i>Boolean</i>,
        "<a href="#lacphapassiveprenegotiation" title="LacpHaPassivePreNegotiation">LacpHaPassivePreNegotiation</a>" : <i>Boolean</i>,
        "<a href="#lacphasamesystemmacaddress" title="LacpHaSameSystemMacAddress">LacpHaSameSystemMacAddress</a>" : <i>String</i>,
        "<a href="#lacpmaxports" title="LacpMaxPorts">LacpMaxPorts</a>" : <i>Double</i>,
        "<a href="#lacpmode" title="LacpMode">LacpMode</a>" : <i>String</i>,
        "<a href="#lacpsystempriority" title="LacpSystemPriority">LacpSystemPriority</a>" : <i>Double</i>,
        "<a href="#lacptransmissionrate" title="LacpTransmissionRate">LacpTransmissionRate</a>" : <i>String</i>,
        "<a href="#lldpenable" title="LldpEnable">LldpEnable</a>" : <i>Boolean</i>,
        "<a href="#lldphapassiveprenegotiation" title="LldpHaPassivePreNegotiation">LldpHaPassivePreNegotiation</a>" : <i>Boolean</i>,
        "<a href="#lldpprofile" title="LldpProfile">LldpProfile</a>" : <i>String</i>,
        "<a href="#managementprofile" title="ManagementProfile">ManagementProfile</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netflowprofile" title="NetflowProfile">NetflowProfile</a>" : <i>String</i>,
        "<a href="#staticips" title="StaticIps">StaticIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::AggregateInterface
Properties:
    <a href="#adjusttcpmss" title="AdjustTcpMss">AdjustTcpMss</a>: <i>Boolean</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#createdhcpdefaultroute" title="CreateDhcpDefaultRoute">CreateDhcpDefaultRoute</a>: <i>Boolean</i>
    <a href="#decryptforward" title="DecryptForward">DecryptForward</a>: <i>Boolean</i>
    <a href="#dhcpdefaultroutemetric" title="DhcpDefaultRouteMetric">DhcpDefaultRouteMetric</a>: <i>Double</i>
    <a href="#dhcpsendhostnameenable" title="DhcpSendHostnameEnable">DhcpSendHostnameEnable</a>: <i>Boolean</i>
    <a href="#dhcpsendhostnamevalue" title="DhcpSendHostnameValue">DhcpSendHostnameValue</a>: <i>String</i>
    <a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>: <i>Boolean</i>
    <a href="#enableuntaggedsubinterface" title="EnableUntaggedSubinterface">EnableUntaggedSubinterface</a>: <i>Boolean</i>
    <a href="#ipv4mssadjust" title="Ipv4MssAdjust">Ipv4MssAdjust</a>: <i>Double</i>
    <a href="#ipv6enabled" title="Ipv6Enabled">Ipv6Enabled</a>: <i>Boolean</i>
    <a href="#ipv6interfaceid" title="Ipv6InterfaceId">Ipv6InterfaceId</a>: <i>String</i>
    <a href="#ipv6mssadjust" title="Ipv6MssAdjust">Ipv6MssAdjust</a>: <i>Double</i>
    <a href="#lacpenable" title="LacpEnable">LacpEnable</a>: <i>Boolean</i>
    <a href="#lacpfastfailover" title="LacpFastFailover">LacpFastFailover</a>: <i>Boolean</i>
    <a href="#lacphaenablesamesystemmac" title="LacpHaEnableSameSystemMac">LacpHaEnableSameSystemMac</a>: <i>Boolean</i>
    <a href="#lacphapassiveprenegotiation" title="LacpHaPassivePreNegotiation">LacpHaPassivePreNegotiation</a>: <i>Boolean</i>
    <a href="#lacphasamesystemmacaddress" title="LacpHaSameSystemMacAddress">LacpHaSameSystemMacAddress</a>: <i>String</i>
    <a href="#lacpmaxports" title="LacpMaxPorts">LacpMaxPorts</a>: <i>Double</i>
    <a href="#lacpmode" title="LacpMode">LacpMode</a>: <i>String</i>
    <a href="#lacpsystempriority" title="LacpSystemPriority">LacpSystemPriority</a>: <i>Double</i>
    <a href="#lacptransmissionrate" title="LacpTransmissionRate">LacpTransmissionRate</a>: <i>String</i>
    <a href="#lldpenable" title="LldpEnable">LldpEnable</a>: <i>Boolean</i>
    <a href="#lldphapassiveprenegotiation" title="LldpHaPassivePreNegotiation">LldpHaPassivePreNegotiation</a>: <i>Boolean</i>
    <a href="#lldpprofile" title="LldpProfile">LldpProfile</a>: <i>String</i>
    <a href="#managementprofile" title="ManagementProfile">ManagementProfile</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netflowprofile" title="NetflowProfile">NetflowProfile</a>: <i>String</i>
    <a href="#staticips" title="StaticIps">StaticIps</a>: <i>
      - String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### AdjustTcpMss

Adjust TCP MSS (default: false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

The interface comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDhcpDefaultRoute

Set to `true` to create a DHCP
default route.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DecryptForward

Set to `true` to enable decrypt forward.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDefaultRouteMetric

The metric for the DHCP default
route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSendHostnameEnable

For DHCP layer3 interfaces:
enable sending the firewall or a custom hostname to DHCP server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSendHostnameValue

For DHCP layer3 interfaces:
the interface hostname.  Leaving this unspecified with `dhcp_send_hostname_enable`
set means to send the system hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDhcp

Set to `true` to enable DHCP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableUntaggedSubinterface

Set to `true` to enable
untagged subinterfaces.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4MssAdjust

The IPv4 MSS adjust value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Enabled

Set to `true` to enable IPv6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6InterfaceId

The IPv6 interface ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6MssAdjust

The IPv6 MSS adjust value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpEnable

Enable LACP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpFastFailover

Enable LACP fast failover.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpHaEnableSameSystemMac

LACP HA enable same system MAC.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpHaPassivePreNegotiation

LACP HA passive pre-negotiation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpHaSameSystemMacAddress

LACP HA same system MAC address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpMaxPorts

LACP max ports.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpMode

LACP mode.  Valid values are `active` or `passive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpSystemPriority

LACP system priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LacpTransmissionRate

LACP transmission rate.  Valid values are `fast` or `slow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpEnable

Enable LLDP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpHaPassivePreNegotiation

LLDP HA passive pre-negotiation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LldpProfile

LLDP profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementProfile

The management profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The interface mode.  Valid values are `layer3` (default),
`layer2`, `virtual-wire`, `ha`, or `decrypt-mirror`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The MTU.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The interface's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowProfile

The netflow profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIps

List of static IPv4 addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys that will use this interface.  This should be
something like `vsys1` or `vsys3`.

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

