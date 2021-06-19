# TF::FortiOS::FmgFirewallSecurityPolicy

This resource supports Create/Read/Update/Delete firewall security policy on FortiManager which could be installed to the FortiGate later

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgFirewallSecurityPolicy",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#adom" title="Adom">Adom</a>" : <i>String</i>,
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>[ String, ... ]</i>,
        "<a href="#avprofile" title="AvProfile">AvProfile</a>" : <i>[ String, ... ]</i>,
        "<a href="#capturepacket" title="CapturePacket">CapturePacket</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>" : <i>[ String, ... ]</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ String, ... ]</i>,
        "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>[ String, ... ]</i>,
        "<a href="#fixedport" title="Fixedport">Fixedport</a>" : <i>String</i>,
        "<a href="#fsso" title="Fsso">Fsso</a>" : <i>String</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#inbound" title="Inbound">Inbound</a>" : <i>String</i>,
        "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>String</i>,
        "<a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>" : <i>[ String, ... ]</i>,
        "<a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>" : <i>[ String, ... ]</i>,
        "<a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>" : <i>String</i>,
        "<a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>" : <i>[ String, ... ]</i>,
        "<a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>" : <i>[ String, ... ]</i>,
        "<a href="#ippool" title="Ippool">Ippool</a>" : <i>String</i>,
        "<a href="#ipssensor" title="IpsSensor">IpsSensor</a>" : <i>[ String, ... ]</i>,
        "<a href="#logtraffic" title="Logtraffic">Logtraffic</a>" : <i>String</i>,
        "<a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nat" title="Nat">Nat</a>" : <i>String</i>,
        "<a href="#packagename" title="PackageName">PackageName</a>" : <i>String</i>,
        "<a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>" : <i>[ String, ... ]</i>,
        "<a href="#poolname" title="Poolname">Poolname</a>" : <i>[ String, ... ]</i>,
        "<a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>" : <i>[ String, ... ]</i>,
        "<a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#profiletype" title="ProfileType">ProfileType</a>" : <i>String</i>,
        "<a href="#rsso" title="Rsso">Rsso</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ String, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ String, ... ]</i>,
        "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ String, ... ]</i>,
        "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>[ String, ... ]</i>,
        "<a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>" : <i>[ String, ... ]</i>,
        "<a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>" : <i>[ String, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>,
        "<a href="#utmstatus" title="UtmStatus">UtmStatus</a>" : <i>String</i>,
        "<a href="#vpntunnel" title="VpnTunnel">VpnTunnel</a>" : <i>[ String, ... ]</i>,
        "<a href="#wafprofile" title="WafProfile">WafProfile</a>" : <i>[ String, ... ]</i>,
        "<a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgFirewallSecurityPolicy
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#adom" title="Adom">Adom</a>: <i>String</i>
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>
      - String</i>
    <a href="#avprofile" title="AvProfile">AvProfile</a>: <i>
      - String</i>
    <a href="#capturepacket" title="CapturePacket">CapturePacket</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#dnsfilterprofile" title="DnsfilterProfile">DnsfilterProfile</a>: <i>
      - String</i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - String</i>
    <a href="#dstintf" title="Dstintf">Dstintf</a>: <i>
      - String</i>
    <a href="#fixedport" title="Fixedport">Fixedport</a>: <i>String</i>
    <a href="#fsso" title="Fsso">Fsso</a>: <i>String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#inbound" title="Inbound">Inbound</a>: <i>String</i>
    <a href="#internetservice" title="InternetService">InternetService</a>: <i>String</i>
    <a href="#internetserviceid" title="InternetServiceId">InternetServiceId</a>: <i>
      - String</i>
    <a href="#internetservicename" title="InternetServiceName">InternetServiceName</a>: <i>
      - String</i>
    <a href="#internetservicesrc" title="InternetServiceSrc">InternetServiceSrc</a>: <i>String</i>
    <a href="#internetservicesrcid" title="InternetServiceSrcId">InternetServiceSrcId</a>: <i>
      - String</i>
    <a href="#internetservicesrcname" title="InternetServiceSrcName">InternetServiceSrcName</a>: <i>
      - String</i>
    <a href="#ippool" title="Ippool">Ippool</a>: <i>String</i>
    <a href="#ipssensor" title="IpsSensor">IpsSensor</a>: <i>
      - String</i>
    <a href="#logtraffic" title="Logtraffic">Logtraffic</a>: <i>String</i>
    <a href="#logtrafficstart" title="LogtrafficStart">LogtrafficStart</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nat" title="Nat">Nat</a>: <i>String</i>
    <a href="#packagename" title="PackageName">PackageName</a>: <i>String</i>
    <a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>: <i>
      - String</i>
    <a href="#poolname" title="Poolname">Poolname</a>: <i>
      - String</i>
    <a href="#profilegroup" title="ProfileGroup">ProfileGroup</a>: <i>
      - String</i>
    <a href="#profileprotocoloptions" title="ProfileProtocolOptions">ProfileProtocolOptions</a>: <i>
      - String</i>
    <a href="#profiletype" title="ProfileType">ProfileType</a>: <i>String</i>
    <a href="#rsso" title="Rsso">Rsso</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - String</i>
    <a href="#service" title="Service">Service</a>: <i>
      - String</i>
    <a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - String</i>
    <a href="#srcintf" title="Srcintf">Srcintf</a>: <i>
      - String</i>
    <a href="#trafficshaper" title="TrafficShaper">TrafficShaper</a>: <i>
      - String</i>
    <a href="#trafficshaperreverse" title="TrafficShaperReverse">TrafficShaperReverse</a>: <i>
      - String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
    <a href="#utmstatus" title="UtmStatus">UtmStatus</a>: <i>String</i>
    <a href="#vpntunnel" title="VpnTunnel">VpnTunnel</a>: <i>
      - String</i>
    <a href="#wafprofile" title="WafProfile">WafProfile</a>: <i>
      - String</i>
    <a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>: <i>
      - String</i>
</pre>

## Properties

#### Action

Policy action, default is deny. Enum: [allow, deny, ipsec].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Adom

ADOM name. default is 'root'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationList

Name of an existing Application list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvProfile

Name of an existing Antivirus profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapturePacket

Enable/disable capture packets.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsfilterProfile

Name of an existing DNS filter profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

Destination address and adress group names.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

Outgoing interface.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fixedport

Enable/disable to prevent source NAT from changing a session's source port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fsso

Enable/disable Fortinet Single Sign-On.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

Names of user groups that can authenticate with this policy.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inbound

Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. Enum: [disable, enable].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Enable/disable use of Destination Internet Services for this policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceId

Destination Internet Service ID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceName

Destination Internet Service Name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrc

Enable/disable use of Source Internet Services for this policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcId

Source Internet Service ID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceSrcName

Source Internet Service Name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ippool

Enable/disable to use IP Pools for source NAT.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSensor

Name of an existing IPS sensor.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logtraffic

Enable or disable logging. Enum: [disable, all, utm].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogtrafficStart

Record logs when a session starts and ends. Enum: [disable, enable].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat

Enable/disable source NAT.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageName

The package name which the policy will be added to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerIpShaper

Per-IP traffic shaper.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Poolname

IP Pool names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileGroup

Name of profile group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileProtocolOptions

Name of an existing Protocol options profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileType

Determine whether the firewall policy allows security profile groups or single profiles only. Enum: [single, group].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rsso

Enable/disable RADIUS Single Sign-On.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

Schedule name.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Service and service group names.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

Source address and adress group names.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

Incoming interface.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaper

Traffic shaper.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficShaperReverse

Reverse traffic shaper.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

Names of individual users that can authenticate with this policy.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtmStatus

Enable/disable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnTunnel

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafProfile

Name of an existing Web application firewall profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterProfile

Name of an existing Web filter profile.

_Required_: No

_Type_: List of String

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

