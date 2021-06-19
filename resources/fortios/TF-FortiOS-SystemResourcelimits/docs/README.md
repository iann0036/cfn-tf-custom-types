# TF::FortiOS::SystemResourcelimits

Configure resource limits.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemResourcelimits",
    "Properties" : {
        "<a href="#customservice" title="CustomService">CustomService</a>" : <i>Double</i>,
        "<a href="#dialuptunnel" title="DialupTunnel">DialupTunnel</a>" : <i>Double</i>,
        "<a href="#firewalladdress" title="FirewallAddress">FirewallAddress</a>" : <i>Double</i>,
        "<a href="#firewalladdrgrp" title="FirewallAddrgrp">FirewallAddrgrp</a>" : <i>Double</i>,
        "<a href="#firewallpolicy" title="FirewallPolicy">FirewallPolicy</a>" : <i>Double</i>,
        "<a href="#ipsecphase1" title="IpsecPhase1">IpsecPhase1</a>" : <i>Double</i>,
        "<a href="#ipsecphase1interface" title="IpsecPhase1Interface">IpsecPhase1Interface</a>" : <i>Double</i>,
        "<a href="#ipsecphase2" title="IpsecPhase2">IpsecPhase2</a>" : <i>Double</i>,
        "<a href="#ipsecphase2interface" title="IpsecPhase2Interface">IpsecPhase2Interface</a>" : <i>Double</i>,
        "<a href="#logdiskquota" title="LogDiskQuota">LogDiskQuota</a>" : <i>Double</i>,
        "<a href="#onetimeschedule" title="OnetimeSchedule">OnetimeSchedule</a>" : <i>Double</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>Double</i>,
        "<a href="#recurringschedule" title="RecurringSchedule">RecurringSchedule</a>" : <i>Double</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>Double</i>,
        "<a href="#session" title="Session">Session</a>" : <i>Double</i>,
        "<a href="#sslvpn" title="Sslvpn">Sslvpn</a>" : <i>Double</i>,
        "<a href="#user" title="User">User</a>" : <i>Double</i>,
        "<a href="#usergroup" title="UserGroup">UserGroup</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemResourcelimits
Properties:
    <a href="#customservice" title="CustomService">CustomService</a>: <i>Double</i>
    <a href="#dialuptunnel" title="DialupTunnel">DialupTunnel</a>: <i>Double</i>
    <a href="#firewalladdress" title="FirewallAddress">FirewallAddress</a>: <i>Double</i>
    <a href="#firewalladdrgrp" title="FirewallAddrgrp">FirewallAddrgrp</a>: <i>Double</i>
    <a href="#firewallpolicy" title="FirewallPolicy">FirewallPolicy</a>: <i>Double</i>
    <a href="#ipsecphase1" title="IpsecPhase1">IpsecPhase1</a>: <i>Double</i>
    <a href="#ipsecphase1interface" title="IpsecPhase1Interface">IpsecPhase1Interface</a>: <i>Double</i>
    <a href="#ipsecphase2" title="IpsecPhase2">IpsecPhase2</a>: <i>Double</i>
    <a href="#ipsecphase2interface" title="IpsecPhase2Interface">IpsecPhase2Interface</a>: <i>Double</i>
    <a href="#logdiskquota" title="LogDiskQuota">LogDiskQuota</a>: <i>Double</i>
    <a href="#onetimeschedule" title="OnetimeSchedule">OnetimeSchedule</a>: <i>Double</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>Double</i>
    <a href="#recurringschedule" title="RecurringSchedule">RecurringSchedule</a>: <i>Double</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>Double</i>
    <a href="#session" title="Session">Session</a>: <i>Double</i>
    <a href="#sslvpn" title="Sslvpn">Sslvpn</a>: <i>Double</i>
    <a href="#user" title="User">User</a>: <i>Double</i>
    <a href="#usergroup" title="UserGroup">UserGroup</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### CustomService

Maximum number of firewall custom services.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialupTunnel

Maximum number of dial-up tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAddress

Maximum number of firewall addresses (IPv4, IPv6, multicast).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAddrgrp

Maximum number of firewall address groups (IPv4, IPv6).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallPolicy

Maximum number of firewall policies (IPv4, IPv6, policy46, policy64, DoS-policy4, DoS-policy6, multicast).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase1

Maximum number of VPN IPsec phase1 tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase1Interface

Maximum number of VPN IPsec phase1 interface tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase2

Maximum number of VPN IPsec phase2 tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase2Interface

Maximum number of VPN IPsec phase2 interface tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDiskQuota

Log disk quota in MB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnetimeSchedule

Maximum number of firewall one-time schedules.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Maximum number of concurrent proxy users.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurringSchedule

Maximum number of firewall recurring schedules.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Maximum number of firewall service groups.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Session

Maximum number of sessions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslvpn

Maximum number of SSL-VPN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Maximum number of local users.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroup

Maximum number of user groups.

_Required_: No

_Type_: Double

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

