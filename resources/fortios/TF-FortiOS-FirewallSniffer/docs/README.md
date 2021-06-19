# TF::FortiOS::FirewallSniffer

Configure sniffer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallSniffer",
    "Properties" : {
        "<a href="#applicationlist" title="ApplicationList">ApplicationList</a>" : <i>String</i>,
        "<a href="#applicationliststatus" title="ApplicationListStatus">ApplicationListStatus</a>" : <i>String</i>,
        "<a href="#avprofile" title="AvProfile">AvProfile</a>" : <i>String</i>,
        "<a href="#avprofilestatus" title="AvProfileStatus">AvProfileStatus</a>" : <i>String</i>,
        "<a href="#dlpsensor" title="DlpSensor">DlpSensor</a>" : <i>String</i>,
        "<a href="#dlpsensorstatus" title="DlpSensorStatus">DlpSensorStatus</a>" : <i>String</i>,
        "<a href="#dsri" title="Dsri">Dsri</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>" : <i>String</i>,
        "<a href="#emailfilterprofilestatus" title="EmailfilterProfileStatus">EmailfilterProfileStatus</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipthreatfeedstatus" title="IpThreatfeedStatus">IpThreatfeedStatus</a>" : <i>String</i>,
        "<a href="#ipsdosstatus" title="IpsDosStatus">IpsDosStatus</a>" : <i>String</i>,
        "<a href="#ipssensor" title="IpsSensor">IpsSensor</a>" : <i>String</i>,
        "<a href="#ipssensorstatus" title="IpsSensorStatus">IpsSensorStatus</a>" : <i>String</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
        "<a href="#logtraffic" title="Logtraffic">Logtraffic</a>" : <i>String</i>,
        "<a href="#maxpacketcount" title="MaxPacketCount">MaxPacketCount</a>" : <i>Double</i>,
        "<a href="#nonip" title="NonIp">NonIp</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#scanbotnetconnections" title="ScanBotnetConnections">ScanBotnetConnections</a>" : <i>String</i>,
        "<a href="#spamfilterprofile" title="SpamfilterProfile">SpamfilterProfile</a>" : <i>String</i>,
        "<a href="#spamfilterprofilestatus" title="SpamfilterProfileStatus">SpamfilterProfileStatus</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>,
        "<a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>" : <i>String</i>,
        "<a href="#webfilterprofilestatus" title="WebfilterProfileStatus">WebfilterProfileStatus</a>" : <i>String</i>,
        "<a href="#anomaly" title="Anomaly">Anomaly</a>" : <i>[ <a href="anomalydefinition.md">AnomalyDefinition</a>, ... ]</i>,
        "<a href="#ipthreatfeed" title="IpThreatfeed">IpThreatfeed</a>" : <i>[ <a href="ipthreatfeeddefinition.md">IpThreatfeedDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallSniffer
Properties:
    <a href="#applicationlist" title="ApplicationList">ApplicationList</a>: <i>String</i>
    <a href="#applicationliststatus" title="ApplicationListStatus">ApplicationListStatus</a>: <i>String</i>
    <a href="#avprofile" title="AvProfile">AvProfile</a>: <i>String</i>
    <a href="#avprofilestatus" title="AvProfileStatus">AvProfileStatus</a>: <i>String</i>
    <a href="#dlpsensor" title="DlpSensor">DlpSensor</a>: <i>String</i>
    <a href="#dlpsensorstatus" title="DlpSensorStatus">DlpSensorStatus</a>: <i>String</i>
    <a href="#dsri" title="Dsri">Dsri</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#emailfilterprofile" title="EmailfilterProfile">EmailfilterProfile</a>: <i>String</i>
    <a href="#emailfilterprofilestatus" title="EmailfilterProfileStatus">EmailfilterProfileStatus</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipthreatfeedstatus" title="IpThreatfeedStatus">IpThreatfeedStatus</a>: <i>String</i>
    <a href="#ipsdosstatus" title="IpsDosStatus">IpsDosStatus</a>: <i>String</i>
    <a href="#ipssensor" title="IpsSensor">IpsSensor</a>: <i>String</i>
    <a href="#ipssensorstatus" title="IpsSensorStatus">IpsSensorStatus</a>: <i>String</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
    <a href="#logtraffic" title="Logtraffic">Logtraffic</a>: <i>String</i>
    <a href="#maxpacketcount" title="MaxPacketCount">MaxPacketCount</a>: <i>Double</i>
    <a href="#nonip" title="NonIp">NonIp</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#scanbotnetconnections" title="ScanBotnetConnections">ScanBotnetConnections</a>: <i>String</i>
    <a href="#spamfilterprofile" title="SpamfilterProfile">SpamfilterProfile</a>: <i>String</i>
    <a href="#spamfilterprofilestatus" title="SpamfilterProfileStatus">SpamfilterProfileStatus</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
    <a href="#webfilterprofile" title="WebfilterProfile">WebfilterProfile</a>: <i>String</i>
    <a href="#webfilterprofilestatus" title="WebfilterProfileStatus">WebfilterProfileStatus</a>: <i>String</i>
    <a href="#anomaly" title="Anomaly">Anomaly</a>: <i>
      - <a href="anomalydefinition.md">AnomalyDefinition</a></i>
    <a href="#ipthreatfeed" title="IpThreatfeed">IpThreatfeed</a>: <i>
      - <a href="ipthreatfeeddefinition.md">IpThreatfeedDefinition</a></i>
</pre>

## Properties

#### ApplicationList

Name of an existing application list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationListStatus

Enable/disable application control profile. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvProfile

Name of an existing antivirus profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvProfileStatus

Enable/disable antivirus profile. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DlpSensor

Name of an existing DLP sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DlpSensorStatus

Enable/disable DLP sensor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dsri

Enable/disable DSRI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailfilterProfile

Name of an existing email filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailfilterProfileStatus

Enable/disable emailfilter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

Sniffer ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

Hosts to filter for in sniffer traffic (Format examples: 1.1.1.1, 2.2.2.0/24, 3.3.3.3/255.255.255.0, 4.4.4.0-4.4.4.240).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface name that traffic sniffing will take place on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpThreatfeedStatus

Enable/disable IP threat feed. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsDosStatus

Enable/disable IPS DoS anomaly detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSensor

Name of an existing IPS sensor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSensorStatus

Enable/disable IPS sensor. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

Enable/disable sniffing IPv6 packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logtraffic

Either log all sessions, only sessions that have a security profile applied, or disable all logging for this policy. Valid values: `all`, `utm`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPacketCount

Maximum packet count (1 - 1000000, default = 10000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonIp

Enable/disable sniffing non-IP packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Ports to sniff (Format examples: 10, :20, 30:40, 50-, 100-200).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Integer value for the protocol type as defined by IANA (0 - 255).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanBotnetConnections

Enable/disable scanning of connections to Botnet servers. Valid values: `disable`, `block`, `monitor`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamfilterProfile

Name of an existing spam filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamfilterProfileStatus

Enable/disable spam filter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the active status of the sniffer. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

List of VLANs to sniff.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterProfile

Name of an existing web filter profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterProfileStatus

Enable/disable web filter profile. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Anomaly

_Required_: No

_Type_: List of <a href="anomalydefinition.md">AnomalyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpThreatfeed

_Required_: No

_Type_: List of <a href="ipthreatfeeddefinition.md">IpThreatfeedDefinition</a>

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

