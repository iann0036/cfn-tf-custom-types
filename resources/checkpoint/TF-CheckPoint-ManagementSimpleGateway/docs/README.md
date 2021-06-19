# TF::CheckPoint::ManagementSimpleGateway

This resource allows you to execute Check Point Simple Gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementSimpleGateway",
    "Properties" : {
        "<a href="#antibot" title="AntiBot">AntiBot</a>" : <i>Boolean</i>,
        "<a href="#antivirus" title="AntiVirus">AntiVirus</a>" : <i>Boolean</i>,
        "<a href="#applicationcontrol" title="ApplicationControl">ApplicationControl</a>" : <i>Boolean</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#contentawareness" title="ContentAwareness">ContentAwareness</a>" : <i>Boolean</i>,
        "<a href="#firewall" title="Firewall">Firewall</a>" : <i>Boolean</i>,
        "<a href="#firewallsettings" title="FirewallSettings">FirewallSettings</a>" : <i>[ <a href="firewallsettingsdefinition.md">FirewallSettingsDefinition</a>, ... ]</i>,
        "<a href="#icapserver" title="IcapServer">IcapServer</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ips" title="Ips">Ips</a>" : <i>Boolean</i>,
        "<a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>" : <i>String</i>,
        "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
        "<a href="#logssettings" title="LogsSettings">LogsSettings</a>" : <i>[ <a href="logssettingsdefinition.md">LogsSettingsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>" : <i>String</i>,
        "<a href="#osname" title="OsName">OsName</a>" : <i>String</i>,
        "<a href="#savelogslocally" title="SaveLogsLocally">SaveLogsLocally</a>" : <i>Boolean</i>,
        "<a href="#sendalertstoserver" title="SendAlertsToServer">SendAlertsToServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#sendlogstobackupserver" title="SendLogsToBackupServer">SendLogsToBackupServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#sendlogstoserver" title="SendLogsToServer">SendLogsToServer</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#threatemulation" title="ThreatEmulation">ThreatEmulation</a>" : <i>Boolean</i>,
        "<a href="#threatextraction" title="ThreatExtraction">ThreatExtraction</a>" : <i>Boolean</i>,
        "<a href="#urlfiltering" title="UrlFiltering">UrlFiltering</a>" : <i>Boolean</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vpn" title="Vpn">Vpn</a>" : <i>Boolean</i>,
        "<a href="#vpnsettings" title="VpnSettings">VpnSettings</a>" : <i>[ <a href="vpnsettingsdefinition.md">VpnSettingsDefinition</a>, ... ]</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ <a href="interfacesdefinition.md">InterfacesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementSimpleGateway
Properties:
    <a href="#antibot" title="AntiBot">AntiBot</a>: <i>Boolean</i>
    <a href="#antivirus" title="AntiVirus">AntiVirus</a>: <i>Boolean</i>
    <a href="#applicationcontrol" title="ApplicationControl">ApplicationControl</a>: <i>Boolean</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#contentawareness" title="ContentAwareness">ContentAwareness</a>: <i>Boolean</i>
    <a href="#firewall" title="Firewall">Firewall</a>: <i>Boolean</i>
    <a href="#firewallsettings" title="FirewallSettings">FirewallSettings</a>: <i>
      - <a href="firewallsettingsdefinition.md">FirewallSettingsDefinition</a></i>
    <a href="#icapserver" title="IcapServer">IcapServer</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ips" title="Ips">Ips</a>: <i>Boolean</i>
    <a href="#ipv4address" title="Ipv4Address">Ipv4Address</a>: <i>String</i>
    <a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
    <a href="#logssettings" title="LogsSettings">LogsSettings</a>: <i>
      - <a href="logssettingsdefinition.md">LogsSettingsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#onetimepassword" title="OneTimePassword">OneTimePassword</a>: <i>String</i>
    <a href="#osname" title="OsName">OsName</a>: <i>String</i>
    <a href="#savelogslocally" title="SaveLogsLocally">SaveLogsLocally</a>: <i>Boolean</i>
    <a href="#sendalertstoserver" title="SendAlertsToServer">SendAlertsToServer</a>: <i>
      - String</i>
    <a href="#sendlogstobackupserver" title="SendLogsToBackupServer">SendLogsToBackupServer</a>: <i>
      - String</i>
    <a href="#sendlogstoserver" title="SendLogsToServer">SendLogsToServer</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#threatemulation" title="ThreatEmulation">ThreatEmulation</a>: <i>Boolean</i>
    <a href="#threatextraction" title="ThreatExtraction">ThreatExtraction</a>: <i>Boolean</i>
    <a href="#urlfiltering" title="UrlFiltering">UrlFiltering</a>: <i>Boolean</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vpn" title="Vpn">Vpn</a>: <i>Boolean</i>
    <a href="#vpnsettings" title="VpnSettings">VpnSettings</a>: <i>
      - <a href="vpnsettingsdefinition.md">VpnSettingsDefinition</a></i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - <a href="interfacesdefinition.md">InterfacesDefinition</a></i>
</pre>

## Properties

#### AntiBot

Anti-Bot blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiVirus

Anti-Virus blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationControl

Application Control blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of the object. Should be one of existing colors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentAwareness

Content Awareness blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firewall

Firewall blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallSettings

Firewall settings. firewall_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="firewallsettingsdefinition.md">FirewallSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcapServer

ICAP Server enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ips

Intrusion Prevention System blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4Address

IPv4 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsSettings

Logs settings. logs_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="logssettingsdefinition.md">LogsSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneTimePassword

Secure internal connection one time password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsName

Operating system name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaveLogsLocally

Enable save logs locally.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendAlertsToServer

Collection of Server(s) to send alerts to identified by the name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendLogsToBackupServer

Collection of Backup server(s) to send logs to identified by the name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendLogsToServer

Collection of Server(s) to send logs to identified by the name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tags identified by name.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatEmulation

Threat Emulation blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatExtraction

Threat Extraction blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFiltering

URL Filtering blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Gateway platform version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpn

VPN blade enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnSettings

Gateway VPN settings. vpn_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="vpnsettingsdefinition.md">VpnSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

_Required_: No

_Type_: List of <a href="interfacesdefinition.md">InterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DynamicIp

Dynamic IP address.

#### Hardware

Gateway platform hardware name.

#### Id

Returns the <code>Id</code> value.

#### SicName

Secure Internal Communication name.

#### SicState

Secure Internal Communication state.

