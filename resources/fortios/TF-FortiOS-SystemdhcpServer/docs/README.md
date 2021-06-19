# TF::FortiOS::SystemdhcpServer

Configure DHCP servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemdhcpServer",
    "Properties" : {
        "<a href="#autoconfiguration" title="AutoConfiguration">AutoConfiguration</a>" : <i>String</i>,
        "<a href="#automanagedstatus" title="AutoManagedStatus">AutoManagedStatus</a>" : <i>String</i>,
        "<a href="#conflictediptimeout" title="ConflictedIpTimeout">ConflictedIpTimeout</a>" : <i>Double</i>,
        "<a href="#ddnsauth" title="DdnsAuth">DdnsAuth</a>" : <i>String</i>,
        "<a href="#ddnskey" title="DdnsKey">DdnsKey</a>" : <i>String</i>,
        "<a href="#ddnskeyname" title="DdnsKeyname">DdnsKeyname</a>" : <i>String</i>,
        "<a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>" : <i>String</i>,
        "<a href="#ddnsttl" title="DdnsTtl">DdnsTtl</a>" : <i>Double</i>,
        "<a href="#ddnsupdate" title="DdnsUpdate">DdnsUpdate</a>" : <i>String</i>,
        "<a href="#ddnsupdateoverride" title="DdnsUpdateOverride">DdnsUpdateOverride</a>" : <i>String</i>,
        "<a href="#ddnszone" title="DdnsZone">DdnsZone</a>" : <i>String</i>,
        "<a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>" : <i>String</i>,
        "<a href="#dhcpsettingsfromfortiipam" title="DhcpSettingsFromFortiipam">DhcpSettingsFromFortiipam</a>" : <i>String</i>,
        "<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>" : <i>String</i>,
        "<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>" : <i>String</i>,
        "<a href="#dnsserver3" title="DnsServer3">DnsServer3</a>" : <i>String</i>,
        "<a href="#dnsserver4" title="DnsServer4">DnsServer4</a>" : <i>String</i>,
        "<a href="#dnsservice" title="DnsService">DnsService</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
        "<a href="#forticlientonnetstatus" title="ForticlientOnNetStatus">ForticlientOnNetStatus</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipmode" title="IpMode">IpMode</a>" : <i>String</i>,
        "<a href="#ipsecleasehold" title="IpsecLeaseHold">IpsecLeaseHold</a>" : <i>Double</i>,
        "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
        "<a href="#macacldefaultaction" title="MacAclDefaultAction">MacAclDefaultAction</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>String</i>,
        "<a href="#nextserver" title="NextServer">NextServer</a>" : <i>String</i>,
        "<a href="#ntpserver1" title="NtpServer1">NtpServer1</a>" : <i>String</i>,
        "<a href="#ntpserver2" title="NtpServer2">NtpServer2</a>" : <i>String</i>,
        "<a href="#ntpserver3" title="NtpServer3">NtpServer3</a>" : <i>String</i>,
        "<a href="#ntpservice" title="NtpService">NtpService</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#timezoneoption" title="TimezoneOption">TimezoneOption</a>" : <i>String</i>,
        "<a href="#vcimatch" title="VciMatch">VciMatch</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wifiac1" title="WifiAc1">WifiAc1</a>" : <i>String</i>,
        "<a href="#wifiac2" title="WifiAc2">WifiAc2</a>" : <i>String</i>,
        "<a href="#wifiac3" title="WifiAc3">WifiAc3</a>" : <i>String</i>,
        "<a href="#wifiacservice" title="WifiAcService">WifiAcService</a>" : <i>String</i>,
        "<a href="#winsserver1" title="WinsServer1">WinsServer1</a>" : <i>String</i>,
        "<a href="#winsserver2" title="WinsServer2">WinsServer2</a>" : <i>String</i>,
        "<a href="#excluderange" title="ExcludeRange">ExcludeRange</a>" : <i>[ <a href="excluderangedefinition.md">ExcludeRangeDefinition</a>, ... ]</i>,
        "<a href="#iprange" title="IpRange">IpRange</a>" : <i>[ <a href="iprangedefinition.md">IpRangeDefinition</a>, ... ]</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>,
        "<a href="#reservedaddress" title="ReservedAddress">ReservedAddress</a>" : <i>[ <a href="reservedaddressdefinition.md">ReservedAddressDefinition</a>, ... ]</i>,
        "<a href="#tftpserver" title="TftpServer">TftpServer</a>" : <i>[ <a href="tftpserverdefinition.md">TftpServerDefinition</a>, ... ]</i>,
        "<a href="#vcistring" title="VciString">VciString</a>" : <i>[ <a href="vcistringdefinition.md">VciStringDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemdhcpServer
Properties:
    <a href="#autoconfiguration" title="AutoConfiguration">AutoConfiguration</a>: <i>String</i>
    <a href="#automanagedstatus" title="AutoManagedStatus">AutoManagedStatus</a>: <i>String</i>
    <a href="#conflictediptimeout" title="ConflictedIpTimeout">ConflictedIpTimeout</a>: <i>Double</i>
    <a href="#ddnsauth" title="DdnsAuth">DdnsAuth</a>: <i>String</i>
    <a href="#ddnskey" title="DdnsKey">DdnsKey</a>: <i>String</i>
    <a href="#ddnskeyname" title="DdnsKeyname">DdnsKeyname</a>: <i>String</i>
    <a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>: <i>String</i>
    <a href="#ddnsttl" title="DdnsTtl">DdnsTtl</a>: <i>Double</i>
    <a href="#ddnsupdate" title="DdnsUpdate">DdnsUpdate</a>: <i>String</i>
    <a href="#ddnsupdateoverride" title="DdnsUpdateOverride">DdnsUpdateOverride</a>: <i>String</i>
    <a href="#ddnszone" title="DdnsZone">DdnsZone</a>: <i>String</i>
    <a href="#defaultgateway" title="DefaultGateway">DefaultGateway</a>: <i>String</i>
    <a href="#dhcpsettingsfromfortiipam" title="DhcpSettingsFromFortiipam">DhcpSettingsFromFortiipam</a>: <i>String</i>
    <a href="#dnsserver1" title="DnsServer1">DnsServer1</a>: <i>String</i>
    <a href="#dnsserver2" title="DnsServer2">DnsServer2</a>: <i>String</i>
    <a href="#dnsserver3" title="DnsServer3">DnsServer3</a>: <i>String</i>
    <a href="#dnsserver4" title="DnsServer4">DnsServer4</a>: <i>String</i>
    <a href="#dnsservice" title="DnsService">DnsService</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>String</i>
    <a href="#forticlientonnetstatus" title="ForticlientOnNetStatus">ForticlientOnNetStatus</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipmode" title="IpMode">IpMode</a>: <i>String</i>
    <a href="#ipsecleasehold" title="IpsecLeaseHold">IpsecLeaseHold</a>: <i>Double</i>
    <a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
    <a href="#macacldefaultaction" title="MacAclDefaultAction">MacAclDefaultAction</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>String</i>
    <a href="#nextserver" title="NextServer">NextServer</a>: <i>String</i>
    <a href="#ntpserver1" title="NtpServer1">NtpServer1</a>: <i>String</i>
    <a href="#ntpserver2" title="NtpServer2">NtpServer2</a>: <i>String</i>
    <a href="#ntpserver3" title="NtpServer3">NtpServer3</a>: <i>String</i>
    <a href="#ntpservice" title="NtpService">NtpService</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#timezoneoption" title="TimezoneOption">TimezoneOption</a>: <i>String</i>
    <a href="#vcimatch" title="VciMatch">VciMatch</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wifiac1" title="WifiAc1">WifiAc1</a>: <i>String</i>
    <a href="#wifiac2" title="WifiAc2">WifiAc2</a>: <i>String</i>
    <a href="#wifiac3" title="WifiAc3">WifiAc3</a>: <i>String</i>
    <a href="#wifiacservice" title="WifiAcService">WifiAcService</a>: <i>String</i>
    <a href="#winsserver1" title="WinsServer1">WinsServer1</a>: <i>String</i>
    <a href="#winsserver2" title="WinsServer2">WinsServer2</a>: <i>String</i>
    <a href="#excluderange" title="ExcludeRange">ExcludeRange</a>: <i>
      - <a href="excluderangedefinition.md">ExcludeRangeDefinition</a></i>
    <a href="#iprange" title="IpRange">IpRange</a>: <i>
      - <a href="iprangedefinition.md">IpRangeDefinition</a></i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
    <a href="#reservedaddress" title="ReservedAddress">ReservedAddress</a>: <i>
      - <a href="reservedaddressdefinition.md">ReservedAddressDefinition</a></i>
    <a href="#tftpserver" title="TftpServer">TftpServer</a>: <i>
      - <a href="tftpserverdefinition.md">TftpServerDefinition</a></i>
    <a href="#vcistring" title="VciString">VciString</a>: <i>
      - <a href="vcistringdefinition.md">VciStringDefinition</a></i>
</pre>

## Properties

#### AutoConfiguration

Enable/disable auto configuration. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoManagedStatus

Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConflictedIpTimeout

Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsAuth

DDNS authentication mode. Valid values: `disable`, `tsig`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsKey

DDNS update key (base 64 encoding).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsKeyname

DDNS update key name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsServerIp

DDNS server IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsTtl

TTL.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsUpdate

Enable/disable DDNS update for DHCP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsUpdateOverride

Enable/disable DDNS update override for DHCP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsZone

Zone of your domain name (ex. DDNS.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultGateway

Default gateway IP address assigned by the DHCP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpSettingsFromFortiipam

Enable/disable populating of DHCP server settings from FortiIPAM. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer1

DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer2

DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer3

DNS server 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer4

DNS server 4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsService

Options for assigning DNS servers to DHCP clients. Valid values: `local`, `default`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name suffix for the IP addresses that the DHCP server assigns to clients.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

Name of the boot file on the TFTP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientOnNetStatus

Enable/disable FortiClient-On-Net service for this DHCP server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

DHCP server can assign IP configurations to clients connected to this interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMode

Method used to assign client IP. Valid values: `range`, `usrgrp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecLeaseHold

DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

Lease time in seconds, 0 means unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAclDefaultAction

MAC access control default action (allow or block assigning IP settings). Valid values: `assign`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

Netmask assigned by the DHCP server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextServer

IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer1

NTP server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer2

NTP server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServer3

NTP server 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpService

Options for assigning Network Time Protocol (NTP) servers to DHCP clients. Valid values: `local`, `default`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

DHCP server can be a normal DHCP server or an IPsec DHCP server. Valid values: `regular`, `ipsec`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this DHCP configuration. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Select the time zone to be assigned to DHCP clients. Valid values: `01`, `02`, `03`, `04`, `05`, `81`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `74`, `14`, `77`, `15`, `87`, `16`, `17`, `18`, `19`, `20`, `75`, `21`, `22`, `23`, `24`, `80`, `79`, `25`, `26`, `27`, `28`, `78`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `83`, `84`, `40`, `85`, `41`, `42`, `43`, `39`, `44`, `46`, `47`, `51`, `48`, `45`, `49`, `50`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, `62`, `63`, `61`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `00`, `82`, `73`, `86`, `76`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimezoneOption

Options for the DHCP server to set the client's time zone. Valid values: `disable`, `default`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VciMatch

Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiAc1

WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiAc2

WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiAc3

WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WifiAcService

Options for assigning WiFi Access Controllers to DHCP clients Valid values: `specify`, `local`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WinsServer1

WINS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WinsServer2

WINS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeRange

_Required_: No

_Type_: List of <a href="excluderangedefinition.md">ExcludeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

_Required_: No

_Type_: List of <a href="iprangedefinition.md">IpRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedAddress

_Required_: No

_Type_: List of <a href="reservedaddressdefinition.md">ReservedAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TftpServer

_Required_: No

_Type_: List of <a href="tftpserverdefinition.md">TftpServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VciString

_Required_: No

_Type_: List of <a href="vcistringdefinition.md">VciStringDefinition</a>

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

