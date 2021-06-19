# TF::FortiOS::SystemVdomproperty

Configure VDOM property.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemVdomproperty",
    "Properties" : {
        "<a href="#customservice" title="CustomService">CustomService</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dialuptunnel" title="DialupTunnel">DialupTunnel</a>" : <i>String</i>,
        "<a href="#firewalladdress" title="FirewallAddress">FirewallAddress</a>" : <i>String</i>,
        "<a href="#firewalladdrgrp" title="FirewallAddrgrp">FirewallAddrgrp</a>" : <i>String</i>,
        "<a href="#firewallpolicy" title="FirewallPolicy">FirewallPolicy</a>" : <i>String</i>,
        "<a href="#ipsecphase1" title="IpsecPhase1">IpsecPhase1</a>" : <i>String</i>,
        "<a href="#ipsecphase1interface" title="IpsecPhase1Interface">IpsecPhase1Interface</a>" : <i>String</i>,
        "<a href="#ipsecphase2" title="IpsecPhase2">IpsecPhase2</a>" : <i>String</i>,
        "<a href="#ipsecphase2interface" title="IpsecPhase2Interface">IpsecPhase2Interface</a>" : <i>String</i>,
        "<a href="#logdiskquota" title="LogDiskQuota">LogDiskQuota</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#onetimeschedule" title="OnetimeSchedule">OnetimeSchedule</a>" : <i>String</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#recurringschedule" title="RecurringSchedule">RecurringSchedule</a>" : <i>String</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>String</i>,
        "<a href="#session" title="Session">Session</a>" : <i>String</i>,
        "<a href="#snmpindex" title="SnmpIndex">SnmpIndex</a>" : <i>Double</i>,
        "<a href="#sslvpn" title="Sslvpn">Sslvpn</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usergroup" title="UserGroup">UserGroup</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemVdomproperty
Properties:
    <a href="#customservice" title="CustomService">CustomService</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dialuptunnel" title="DialupTunnel">DialupTunnel</a>: <i>String</i>
    <a href="#firewalladdress" title="FirewallAddress">FirewallAddress</a>: <i>String</i>
    <a href="#firewalladdrgrp" title="FirewallAddrgrp">FirewallAddrgrp</a>: <i>String</i>
    <a href="#firewallpolicy" title="FirewallPolicy">FirewallPolicy</a>: <i>String</i>
    <a href="#ipsecphase1" title="IpsecPhase1">IpsecPhase1</a>: <i>String</i>
    <a href="#ipsecphase1interface" title="IpsecPhase1Interface">IpsecPhase1Interface</a>: <i>String</i>
    <a href="#ipsecphase2" title="IpsecPhase2">IpsecPhase2</a>: <i>String</i>
    <a href="#ipsecphase2interface" title="IpsecPhase2Interface">IpsecPhase2Interface</a>: <i>String</i>
    <a href="#logdiskquota" title="LogDiskQuota">LogDiskQuota</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#onetimeschedule" title="OnetimeSchedule">OnetimeSchedule</a>: <i>String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#recurringschedule" title="RecurringSchedule">RecurringSchedule</a>: <i>String</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>String</i>
    <a href="#session" title="Session">Session</a>: <i>String</i>
    <a href="#snmpindex" title="SnmpIndex">SnmpIndex</a>: <i>Double</i>
    <a href="#sslvpn" title="Sslvpn">Sslvpn</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usergroup" title="UserGroup">UserGroup</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### CustomService

Maximum guaranteed number of firewall custom services.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialupTunnel

Maximum guaranteed number of dial-up tunnels.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAddress

Maximum guaranteed number of firewall addresses (IPv4, IPv6, multicast).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAddrgrp

Maximum guaranteed number of firewall address groups (IPv4, IPv6).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallPolicy

Maximum guaranteed number of firewall policies (IPv4, IPv6, policy46, policy64, DoS-policy4, DoS-policy6, multicast).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase1

Maximum guaranteed number of VPN IPsec phase 1 tunnels.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase1Interface

Maximum guaranteed number of VPN IPsec phase1 interface tunnels.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase2

Maximum guaranteed number of VPN IPsec phase 2 tunnels.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPhase2Interface

Maximum guaranteed number of VPN IPsec phase2 interface tunnels.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDiskQuota

Log disk quota in MB (range depends on how much disk space is available).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

VDOM name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnetimeSchedule

Maximum guaranteed number of firewall one-time schedules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Maximum guaranteed number of concurrent proxy users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurringSchedule

Maximum guaranteed number of firewall recurring schedules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Maximum guaranteed number of firewall service groups.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Session

Maximum guaranteed number of sessions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpIndex

Permanent SNMP Index of the virtual domain (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslvpn

Maximum guaranteed number of SSL-VPNs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Maximum guaranteed number of local users.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroup

Maximum guaranteed number of user groups.

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

