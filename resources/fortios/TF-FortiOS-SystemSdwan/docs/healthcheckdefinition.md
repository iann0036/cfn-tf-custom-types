# TF::FortiOS::SystemSdwan HealthCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addrmode" title="AddrMode">AddrMode</a>" : <i>String</i>,
    "<a href="#diffservcode" title="Diffservcode">Diffservcode</a>" : <i>String</i>,
    "<a href="#dnsmatchip" title="DnsMatchIp">DnsMatchIp</a>" : <i>String</i>,
    "<a href="#dnsrequestdomain" title="DnsRequestDomain">DnsRequestDomain</a>" : <i>String</i>,
    "<a href="#failtime" title="Failtime">Failtime</a>" : <i>Double</i>,
    "<a href="#ftpfile" title="FtpFile">FtpFile</a>" : <i>String</i>,
    "<a href="#ftpmode" title="FtpMode">FtpMode</a>" : <i>String</i>,
    "<a href="#hapriority" title="HaPriority">HaPriority</a>" : <i>Double</i>,
    "<a href="#httpagent" title="HttpAgent">HttpAgent</a>" : <i>String</i>,
    "<a href="#httpget" title="HttpGet">HttpGet</a>" : <i>String</i>,
    "<a href="#httpmatch" title="HttpMatch">HttpMatch</a>" : <i>String</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#packetsize" title="PacketSize">PacketSize</a>" : <i>Double</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#probecount" title="ProbeCount">ProbeCount</a>" : <i>Double</i>,
    "<a href="#probepackets" title="ProbePackets">ProbePackets</a>" : <i>String</i>,
    "<a href="#probetimeout" title="ProbeTimeout">ProbeTimeout</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#qualitymeasuredmethod" title="QualityMeasuredMethod">QualityMeasuredMethod</a>" : <i>String</i>,
    "<a href="#recoverytime" title="Recoverytime">Recoverytime</a>" : <i>Double</i>,
    "<a href="#securitymode" title="SecurityMode">SecurityMode</a>" : <i>String</i>,
    "<a href="#server" title="Server">Server</a>" : <i>String</i>,
    "<a href="#slafaillogperiod" title="SlaFailLogPeriod">SlaFailLogPeriod</a>" : <i>Double</i>,
    "<a href="#slapasslogperiod" title="SlaPassLogPeriod">SlaPassLogPeriod</a>" : <i>Double</i>,
    "<a href="#systemdns" title="SystemDns">SystemDns</a>" : <i>String</i>,
    "<a href="#thresholdalertjitter" title="ThresholdAlertJitter">ThresholdAlertJitter</a>" : <i>Double</i>,
    "<a href="#thresholdalertlatency" title="ThresholdAlertLatency">ThresholdAlertLatency</a>" : <i>Double</i>,
    "<a href="#thresholdalertpacketloss" title="ThresholdAlertPacketloss">ThresholdAlertPacketloss</a>" : <i>Double</i>,
    "<a href="#thresholdwarningjitter" title="ThresholdWarningJitter">ThresholdWarningJitter</a>" : <i>Double</i>,
    "<a href="#thresholdwarninglatency" title="ThresholdWarningLatency">ThresholdWarningLatency</a>" : <i>Double</i>,
    "<a href="#thresholdwarningpacketloss" title="ThresholdWarningPacketloss">ThresholdWarningPacketloss</a>" : <i>Double</i>,
    "<a href="#updatecascadeinterface" title="UpdateCascadeInterface">UpdateCascadeInterface</a>" : <i>String</i>,
    "<a href="#updatestaticroute" title="UpdateStaticRoute">UpdateStaticRoute</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ <a href="membersdefinition.md">MembersDefinition</a>, ... ]</i>,
    "<a href="#sla" title="Sla">Sla</a>" : <i>[ <a href="sladefinition.md">SlaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addrmode" title="AddrMode">AddrMode</a>: <i>String</i>
<a href="#diffservcode" title="Diffservcode">Diffservcode</a>: <i>String</i>
<a href="#dnsmatchip" title="DnsMatchIp">DnsMatchIp</a>: <i>String</i>
<a href="#dnsrequestdomain" title="DnsRequestDomain">DnsRequestDomain</a>: <i>String</i>
<a href="#failtime" title="Failtime">Failtime</a>: <i>Double</i>
<a href="#ftpfile" title="FtpFile">FtpFile</a>: <i>String</i>
<a href="#ftpmode" title="FtpMode">FtpMode</a>: <i>String</i>
<a href="#hapriority" title="HaPriority">HaPriority</a>: <i>Double</i>
<a href="#httpagent" title="HttpAgent">HttpAgent</a>: <i>String</i>
<a href="#httpget" title="HttpGet">HttpGet</a>: <i>String</i>
<a href="#httpmatch" title="HttpMatch">HttpMatch</a>: <i>String</i>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#packetsize" title="PacketSize">PacketSize</a>: <i>Double</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#probecount" title="ProbeCount">ProbeCount</a>: <i>Double</i>
<a href="#probepackets" title="ProbePackets">ProbePackets</a>: <i>String</i>
<a href="#probetimeout" title="ProbeTimeout">ProbeTimeout</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#qualitymeasuredmethod" title="QualityMeasuredMethod">QualityMeasuredMethod</a>: <i>String</i>
<a href="#recoverytime" title="Recoverytime">Recoverytime</a>: <i>Double</i>
<a href="#securitymode" title="SecurityMode">SecurityMode</a>: <i>String</i>
<a href="#server" title="Server">Server</a>: <i>String</i>
<a href="#slafaillogperiod" title="SlaFailLogPeriod">SlaFailLogPeriod</a>: <i>Double</i>
<a href="#slapasslogperiod" title="SlaPassLogPeriod">SlaPassLogPeriod</a>: <i>Double</i>
<a href="#systemdns" title="SystemDns">SystemDns</a>: <i>String</i>
<a href="#thresholdalertjitter" title="ThresholdAlertJitter">ThresholdAlertJitter</a>: <i>Double</i>
<a href="#thresholdalertlatency" title="ThresholdAlertLatency">ThresholdAlertLatency</a>: <i>Double</i>
<a href="#thresholdalertpacketloss" title="ThresholdAlertPacketloss">ThresholdAlertPacketloss</a>: <i>Double</i>
<a href="#thresholdwarningjitter" title="ThresholdWarningJitter">ThresholdWarningJitter</a>: <i>Double</i>
<a href="#thresholdwarninglatency" title="ThresholdWarningLatency">ThresholdWarningLatency</a>: <i>Double</i>
<a href="#thresholdwarningpacketloss" title="ThresholdWarningPacketloss">ThresholdWarningPacketloss</a>: <i>Double</i>
<a href="#updatecascadeinterface" title="UpdateCascadeInterface">UpdateCascadeInterface</a>: <i>String</i>
<a href="#updatestaticroute" title="UpdateStaticRoute">UpdateStaticRoute</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#members" title="Members">Members</a>: <i>
      - <a href="membersdefinition.md">MembersDefinition</a></i>
<a href="#sla" title="Sla">Sla</a>: <i>
      - <a href="sladefinition.md">SlaDefinition</a></i>
</pre>

## Properties

#### AddrMode

Address mode (IPv4 or IPv6). Valid values: `ipv4`, `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Diffservcode

Differentiated services code point (DSCP) in the IP header of the probe packet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsMatchIp

Response IP expected from DNS server if the protocol is DNS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRequestDomain

Fully qualified domain name to resolve for the DNS probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Failtime

Number of failures before server is considered lost (1 - 3600, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpFile

Full path and file name on the FTP server to download for FTP health-check to probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpMode

FTP mode. Valid values: `passive`, `port`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaPriority

HA election priority (1 - 50).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAgent

String in the http-agent field in the HTTP header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpGet

URL used to communicate with the server if the protocol if the protocol is HTTP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMatch

Response string expected from the server if the protocol is HTTP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Status check interval in milliseconds, or the time between attempting to connect to the server (500 - 3600*1000 msec, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Health check name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketSize

Packet size of a twamp test session,.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Twamp controller password in authentication mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number used to communicate with the server over the selected protocol (0-65535, default = 0, auto select. http, twamp: 80, udp-echo, tcp-echo: 7, dns: 53, ftp: 21).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeCount

Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbePackets

Enable/disable transmission of probe packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeTimeout

Time to wait before a probe packet is considered lost (500 - 3600*1000 msec, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol used to determine if the FortiGate can communicate with the server. Valid values: `ping`, `tcp-echo`, `udp-echo`, `http`, `twamp`, `dns`, `tcp-connect`, `ftp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QualityMeasuredMethod

Method to measure the quality of tcp-connect. Valid values: `half-open`, `half-close`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recoverytime

Number of successful responses received before server is considered recovered (1 - 3600, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityMode

Twamp controller security mode. Valid values: `none`, `authentication`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

IP address or FQDN name of the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaFailLogPeriod

Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaPassLogPeriod

Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDns

Enable/disable system DNS as the probe server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdAlertJitter

Alert threshold for jitter (ms, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdAlertLatency

Alert threshold for latency (ms, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdAlertPacketloss

Alert threshold for packet loss (percentage, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdWarningJitter

Warning threshold for jitter (ms, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdWarningLatency

Warning threshold for latency (ms, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdWarningPacketloss

Warning threshold for packet loss (percentage, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateCascadeInterface

Enable/disable update cascade interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateStaticRoute

Enable/disable updating the static route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The user name to access probe server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of <a href="membersdefinition.md">MembersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sla

_Required_: No

_Type_: List of <a href="sladefinition.md">SlaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

