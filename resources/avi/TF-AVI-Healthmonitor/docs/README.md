# TF::AVI::Healthmonitor

The HealthMonitor resource allows the creation and management of Avi HealthMonitor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Healthmonitor",
    "Properties" : {
        "<a href="#allowduplicatemonitors" title="AllowDuplicateMonitors">AllowDuplicateMonitors</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disablequickstart" title="DisableQuickstart">DisableQuickstart</a>" : <i>Boolean</i>,
        "<a href="#failedchecks" title="FailedChecks">FailedChecks</a>" : <i>Double</i>,
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#monitorport" title="MonitorPort">MonitorPort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#receivetimeout" title="ReceiveTimeout">ReceiveTimeout</a>" : <i>Double</i>,
        "<a href="#sendinterval" title="SendInterval">SendInterval</a>" : <i>Double</i>,
        "<a href="#successfulchecks" title="SuccessfulChecks">SuccessfulChecks</a>" : <i>Double</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authenticationdefinition.md">AuthenticationDefinition</a>, ... ]</i>,
        "<a href="#dnsmonitor" title="DnsMonitor">DnsMonitor</a>" : <i>[ <a href="dnsmonitordefinition.md">DnsMonitorDefinition</a>, ... ]</i>,
        "<a href="#externalmonitor" title="ExternalMonitor">ExternalMonitor</a>" : <i>[ <a href="externalmonitordefinition.md">ExternalMonitorDefinition</a>, ... ]</i>,
        "<a href="#httpmonitor" title="HttpMonitor">HttpMonitor</a>" : <i>[ <a href="httpmonitordefinition.md">HttpMonitorDefinition</a>, ... ]</i>,
        "<a href="#httpsmonitor" title="HttpsMonitor">HttpsMonitor</a>" : <i>[ <a href="httpsmonitordefinition.md">HttpsMonitorDefinition</a>, ... ]</i>,
        "<a href="#imapmonitor" title="ImapMonitor">ImapMonitor</a>" : <i>[ <a href="imapmonitordefinition.md">ImapMonitorDefinition</a>, ... ]</i>,
        "<a href="#imapsmonitor" title="ImapsMonitor">ImapsMonitor</a>" : <i>[ <a href="imapsmonitordefinition.md">ImapsMonitorDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#pop3monitor" title="Pop3Monitor">Pop3Monitor</a>" : <i>[ <a href="pop3monitordefinition.md">Pop3MonitorDefinition</a>, ... ]</i>,
        "<a href="#pop3smonitor" title="Pop3sMonitor">Pop3sMonitor</a>" : <i>[ <a href="pop3smonitordefinition.md">Pop3sMonitorDefinition</a>, ... ]</i>,
        "<a href="#radiusmonitor" title="RadiusMonitor">RadiusMonitor</a>" : <i>[ <a href="radiusmonitordefinition.md">RadiusMonitorDefinition</a>, ... ]</i>,
        "<a href="#sipmonitor" title="SipMonitor">SipMonitor</a>" : <i>[ <a href="sipmonitordefinition.md">SipMonitorDefinition</a>, ... ]</i>,
        "<a href="#smtpmonitor" title="SmtpMonitor">SmtpMonitor</a>" : <i>[ <a href="smtpmonitordefinition.md">SmtpMonitorDefinition</a>, ... ]</i>,
        "<a href="#smtpsmonitor" title="SmtpsMonitor">SmtpsMonitor</a>" : <i>[ <a href="smtpsmonitordefinition.md">SmtpsMonitorDefinition</a>, ... ]</i>,
        "<a href="#tcpmonitor" title="TcpMonitor">TcpMonitor</a>" : <i>[ <a href="tcpmonitordefinition.md">TcpMonitorDefinition</a>, ... ]</i>,
        "<a href="#udpmonitor" title="UdpMonitor">UdpMonitor</a>" : <i>[ <a href="udpmonitordefinition.md">UdpMonitorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Healthmonitor
Properties:
    <a href="#allowduplicatemonitors" title="AllowDuplicateMonitors">AllowDuplicateMonitors</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disablequickstart" title="DisableQuickstart">DisableQuickstart</a>: <i>Boolean</i>
    <a href="#failedchecks" title="FailedChecks">FailedChecks</a>: <i>Double</i>
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#monitorport" title="MonitorPort">MonitorPort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#receivetimeout" title="ReceiveTimeout">ReceiveTimeout</a>: <i>Double</i>
    <a href="#sendinterval" title="SendInterval">SendInterval</a>: <i>Double</i>
    <a href="#successfulchecks" title="SuccessfulChecks">SuccessfulChecks</a>: <i>Double</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authenticationdefinition.md">AuthenticationDefinition</a></i>
    <a href="#dnsmonitor" title="DnsMonitor">DnsMonitor</a>: <i>
      - <a href="dnsmonitordefinition.md">DnsMonitorDefinition</a></i>
    <a href="#externalmonitor" title="ExternalMonitor">ExternalMonitor</a>: <i>
      - <a href="externalmonitordefinition.md">ExternalMonitorDefinition</a></i>
    <a href="#httpmonitor" title="HttpMonitor">HttpMonitor</a>: <i>
      - <a href="httpmonitordefinition.md">HttpMonitorDefinition</a></i>
    <a href="#httpsmonitor" title="HttpsMonitor">HttpsMonitor</a>: <i>
      - <a href="httpsmonitordefinition.md">HttpsMonitorDefinition</a></i>
    <a href="#imapmonitor" title="ImapMonitor">ImapMonitor</a>: <i>
      - <a href="imapmonitordefinition.md">ImapMonitorDefinition</a></i>
    <a href="#imapsmonitor" title="ImapsMonitor">ImapsMonitor</a>: <i>
      - <a href="imapsmonitordefinition.md">ImapsMonitorDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#pop3monitor" title="Pop3Monitor">Pop3Monitor</a>: <i>
      - <a href="pop3monitordefinition.md">Pop3MonitorDefinition</a></i>
    <a href="#pop3smonitor" title="Pop3sMonitor">Pop3sMonitor</a>: <i>
      - <a href="pop3smonitordefinition.md">Pop3sMonitorDefinition</a></i>
    <a href="#radiusmonitor" title="RadiusMonitor">RadiusMonitor</a>: <i>
      - <a href="radiusmonitordefinition.md">RadiusMonitorDefinition</a></i>
    <a href="#sipmonitor" title="SipMonitor">SipMonitor</a>: <i>
      - <a href="sipmonitordefinition.md">SipMonitorDefinition</a></i>
    <a href="#smtpmonitor" title="SmtpMonitor">SmtpMonitor</a>: <i>
      - <a href="smtpmonitordefinition.md">SmtpMonitorDefinition</a></i>
    <a href="#smtpsmonitor" title="SmtpsMonitor">SmtpsMonitor</a>: <i>
      - <a href="smtpsmonitordefinition.md">SmtpsMonitorDefinition</a></i>
    <a href="#tcpmonitor" title="TcpMonitor">TcpMonitor</a>: <i>
      - <a href="tcpmonitordefinition.md">TcpMonitorDefinition</a></i>
    <a href="#udpmonitor" title="UdpMonitor">UdpMonitor</a>: <i>
      - <a href="udpmonitordefinition.md">UdpMonitorDefinition</a></i>
</pre>

## Properties

#### AllowDuplicateMonitors

By default, multiple instances of the same healthmonitor to the same server are suppressed intelligently. In rare cases, the monitor may have specific constructs that go beyond the server keys (ip, port, etc.) during which such suppression is not desired. Use this knob to allow duplicates. Field introduced in 18.2.8. Allowed in basic(allowed values- true) edition, essentials(allowed values- true) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableQuickstart

During addition of a server or healthmonitors or during bootup, avi performs sequential health checks rather than waiting for send-interval to kick in, to mark the server up as soon as possible. This knob may be used to turn this feature off. Field introduced in 18.2.7. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailedChecks

Number of continuous failed health checks before the server is marked down. Allowed values are 1-50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFederated

This field describes the object's replication scope. If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines. If the field is set to true, then the object is replicated across the federation. Field introduced in 17.1.3. Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorPort

Use this port instead of the port defined for the server in the pool. If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the pool. Allowed values are 1-65535. Special values are 0 - 'use server port'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A user friendly name for this health monitor.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveTimeout

A valid response from the server is expected within the receive timeout window. This timeout must be less than the send interval. If server status is regularly flapping up and down, consider increasing this value. Allowed values are 1-2400. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendInterval

Frequency, in seconds, that monitors are sent to a server. Allowed values are 1-3600. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessfulChecks

Number of continuous successful health checks before server is marked up. Allowed values are 1-50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the health monitor. Enum options - HEALTH_MONITOR_PING, HEALTH_MONITOR_TCP, HEALTH_MONITOR_HTTP, HEALTH_MONITOR_HTTPS, HEALTH_MONITOR_EXTERNAL, HEALTH_MONITOR_UDP, HEALTH_MONITOR_DNS, HEALTH_MONITOR_GSLB, HEALTH_MONITOR_SIP, HEALTH_MONITOR_RADIUS, HEALTH_MONITOR_SMTP, HEALTH_MONITOR_SMTPS, HEALTH_MONITOR_POP3, HEALTH_MONITOR_POP3S, HEALTH_MONITOR_IMAP, HEALTH_MONITOR_IMAPS. Allowed in basic(allowed values- health_monitor_ping,health_monitor_tcp,health_monitor_udp,health_monitor_http,health_monitor_https) edition, essentials(allowed values- health_monitor_ping,health_monitor_tcp,health_monitor_udp) edition, enterprise edition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authenticationdefinition.md">AuthenticationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsMonitor

_Required_: No

_Type_: List of <a href="dnsmonitordefinition.md">DnsMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalMonitor

_Required_: No

_Type_: List of <a href="externalmonitordefinition.md">ExternalMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMonitor

_Required_: No

_Type_: List of <a href="httpmonitordefinition.md">HttpMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsMonitor

_Required_: No

_Type_: List of <a href="httpsmonitordefinition.md">HttpsMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImapMonitor

_Required_: No

_Type_: List of <a href="imapmonitordefinition.md">ImapMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImapsMonitor

_Required_: No

_Type_: List of <a href="imapsmonitordefinition.md">ImapsMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3Monitor

_Required_: No

_Type_: List of <a href="pop3monitordefinition.md">Pop3MonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3sMonitor

_Required_: No

_Type_: List of <a href="pop3smonitordefinition.md">Pop3sMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusMonitor

_Required_: No

_Type_: List of <a href="radiusmonitordefinition.md">RadiusMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SipMonitor

_Required_: No

_Type_: List of <a href="sipmonitordefinition.md">SipMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpMonitor

_Required_: No

_Type_: List of <a href="smtpmonitordefinition.md">SmtpMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpsMonitor

_Required_: No

_Type_: List of <a href="smtpsmonitordefinition.md">SmtpsMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMonitor

_Required_: No

_Type_: List of <a href="tcpmonitordefinition.md">TcpMonitorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpMonitor

_Required_: No

_Type_: List of <a href="udpmonitordefinition.md">UdpMonitorDefinition</a>

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

