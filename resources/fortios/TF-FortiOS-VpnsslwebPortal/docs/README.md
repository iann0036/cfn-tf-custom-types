# TF::FortiOS::VpnsslwebPortal

CloudFormation equivalent of fortios_vpnsslweb_portal

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnsslwebPortal",
    "Properties" : {
        "<a href="#allowuseraccess" title="AllowUserAccess">AllowUserAccess</a>" : <i>String</i>,
        "<a href="#autoconnect" title="AutoConnect">AutoConnect</a>" : <i>String</i>,
        "<a href="#customlang" title="CustomLang">CustomLang</a>" : <i>String</i>,
        "<a href="#customizeforticlientdownloadurl" title="CustomizeForticlientDownloadUrl">CustomizeForticlientDownloadUrl</a>" : <i>String</i>,
        "<a href="#displaybookmark" title="DisplayBookmark">DisplayBookmark</a>" : <i>String</i>,
        "<a href="#displayconnectiontools" title="DisplayConnectionTools">DisplayConnectionTools</a>" : <i>String</i>,
        "<a href="#displayhistory" title="DisplayHistory">DisplayHistory</a>" : <i>String</i>,
        "<a href="#displaystatus" title="DisplayStatus">DisplayStatus</a>" : <i>String</i>,
        "<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>" : <i>String</i>,
        "<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>" : <i>String</i>,
        "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#exclusiverouting" title="ExclusiveRouting">ExclusiveRouting</a>" : <i>String</i>,
        "<a href="#forticlientdownload" title="ForticlientDownload">ForticlientDownload</a>" : <i>String</i>,
        "<a href="#forticlientdownloadmethod" title="ForticlientDownloadMethod">ForticlientDownloadMethod</a>" : <i>String</i>,
        "<a href="#heading" title="Heading">Heading</a>" : <i>String</i>,
        "<a href="#hidessocredential" title="HideSsoCredential">HideSsoCredential</a>" : <i>String</i>,
        "<a href="#hostcheck" title="HostCheck">HostCheck</a>" : <i>String</i>,
        "<a href="#hostcheckinterval" title="HostCheckInterval">HostCheckInterval</a>" : <i>Double</i>,
        "<a href="#ipmode" title="IpMode">IpMode</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>" : <i>String</i>,
        "<a href="#ipv6exclusiverouting" title="Ipv6ExclusiveRouting">Ipv6ExclusiveRouting</a>" : <i>String</i>,
        "<a href="#ipv6servicerestriction" title="Ipv6ServiceRestriction">Ipv6ServiceRestriction</a>" : <i>String</i>,
        "<a href="#ipv6splittunneling" title="Ipv6SplitTunneling">Ipv6SplitTunneling</a>" : <i>String</i>,
        "<a href="#ipv6splittunnelingroutingnegate" title="Ipv6SplitTunnelingRoutingNegate">Ipv6SplitTunnelingRoutingNegate</a>" : <i>String</i>,
        "<a href="#ipv6tunnelmode" title="Ipv6TunnelMode">Ipv6TunnelMode</a>" : <i>String</i>,
        "<a href="#ipv6winsserver1" title="Ipv6WinsServer1">Ipv6WinsServer1</a>" : <i>String</i>,
        "<a href="#ipv6winsserver2" title="Ipv6WinsServer2">Ipv6WinsServer2</a>" : <i>String</i>,
        "<a href="#keepalive" title="KeepAlive">KeepAlive</a>" : <i>String</i>,
        "<a href="#limituserlogins" title="LimitUserLogins">LimitUserLogins</a>" : <i>String</i>,
        "<a href="#macaddraction" title="MacAddrAction">MacAddrAction</a>" : <i>String</i>,
        "<a href="#macaddrcheck" title="MacAddrCheck">MacAddrCheck</a>" : <i>String</i>,
        "<a href="#macosforticlientdownloadurl" title="MacosForticlientDownloadUrl">MacosForticlientDownloadUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oscheck" title="OsCheck">OsCheck</a>" : <i>String</i>,
        "<a href="#redirurl" title="RedirUrl">RedirUrl</a>" : <i>String</i>,
        "<a href="#savepassword" title="SavePassword">SavePassword</a>" : <i>String</i>,
        "<a href="#servicerestriction" title="ServiceRestriction">ServiceRestriction</a>" : <i>String</i>,
        "<a href="#skipcheckforbrowser" title="SkipCheckForBrowser">SkipCheckForBrowser</a>" : <i>String</i>,
        "<a href="#skipcheckforunsupportedos" title="SkipCheckForUnsupportedOs">SkipCheckForUnsupportedOs</a>" : <i>String</i>,
        "<a href="#smbmaxversion" title="SmbMaxVersion">SmbMaxVersion</a>" : <i>String</i>,
        "<a href="#smbminversion" title="SmbMinVersion">SmbMinVersion</a>" : <i>String</i>,
        "<a href="#smbntlmv1auth" title="SmbNtlmv1Auth">SmbNtlmv1Auth</a>" : <i>String</i>,
        "<a href="#smbv1" title="Smbv1">Smbv1</a>" : <i>String</i>,
        "<a href="#splittunneling" title="SplitTunneling">SplitTunneling</a>" : <i>String</i>,
        "<a href="#splittunnelingroutingnegate" title="SplitTunnelingRoutingNegate">SplitTunnelingRoutingNegate</a>" : <i>String</i>,
        "<a href="#theme" title="Theme">Theme</a>" : <i>String</i>,
        "<a href="#transformbackwardslashes" title="TransformBackwardSlashes">TransformBackwardSlashes</a>" : <i>String</i>,
        "<a href="#tunnelmode" title="TunnelMode">TunnelMode</a>" : <i>String</i>,
        "<a href="#usesdwan" title="UseSdwan">UseSdwan</a>" : <i>String</i>,
        "<a href="#userbookmark" title="UserBookmark">UserBookmark</a>" : <i>String</i>,
        "<a href="#usergroupbookmark" title="UserGroupBookmark">UserGroupBookmark</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#webmode" title="WebMode">WebMode</a>" : <i>String</i>,
        "<a href="#windowsforticlientdownloadurl" title="WindowsForticlientDownloadUrl">WindowsForticlientDownloadUrl</a>" : <i>String</i>,
        "<a href="#winsserver1" title="WinsServer1">WinsServer1</a>" : <i>String</i>,
        "<a href="#winsserver2" title="WinsServer2">WinsServer2</a>" : <i>String</i>,
        "<a href="#bookmarkgroup" title="BookmarkGroup">BookmarkGroup</a>" : <i>[ <a href="bookmarkgroupdefinition.md">BookmarkGroupDefinition</a>, ... ]</i>,
        "<a href="#hostcheckpolicy" title="HostCheckPolicy">HostCheckPolicy</a>" : <i>[ <a href="hostcheckpolicydefinition.md">HostCheckPolicyDefinition</a>, ... ]</i>,
        "<a href="#ippools" title="IpPools">IpPools</a>" : <i>[ <a href="ippoolsdefinition.md">IpPoolsDefinition</a>, ... ]</i>,
        "<a href="#ipv6pools" title="Ipv6Pools">Ipv6Pools</a>" : <i>[ <a href="ipv6poolsdefinition.md">Ipv6PoolsDefinition</a>, ... ]</i>,
        "<a href="#ipv6splittunnelingroutingaddress" title="Ipv6SplitTunnelingRoutingAddress">Ipv6SplitTunnelingRoutingAddress</a>" : <i>[ <a href="ipv6splittunnelingroutingaddressdefinition.md">Ipv6SplitTunnelingRoutingAddressDefinition</a>, ... ]</i>,
        "<a href="#macaddrcheckrule" title="MacAddrCheckRule">MacAddrCheckRule</a>" : <i>[ <a href="macaddrcheckruledefinition.md">MacAddrCheckRuleDefinition</a>, ... ]</i>,
        "<a href="#oschecklist" title="OsCheckList">OsCheckList</a>" : <i>[ <a href="oschecklistdefinition.md">OsCheckListDefinition</a>, ... ]</i>,
        "<a href="#splitdns" title="SplitDns">SplitDns</a>" : <i>[ <a href="splitdnsdefinition.md">SplitDnsDefinition</a>, ... ]</i>,
        "<a href="#splittunnelingroutingaddress" title="SplitTunnelingRoutingAddress">SplitTunnelingRoutingAddress</a>" : <i>[ <a href="splittunnelingroutingaddressdefinition.md">SplitTunnelingRoutingAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnsslwebPortal
Properties:
    <a href="#allowuseraccess" title="AllowUserAccess">AllowUserAccess</a>: <i>String</i>
    <a href="#autoconnect" title="AutoConnect">AutoConnect</a>: <i>String</i>
    <a href="#customlang" title="CustomLang">CustomLang</a>: <i>String</i>
    <a href="#customizeforticlientdownloadurl" title="CustomizeForticlientDownloadUrl">CustomizeForticlientDownloadUrl</a>: <i>String</i>
    <a href="#displaybookmark" title="DisplayBookmark">DisplayBookmark</a>: <i>String</i>
    <a href="#displayconnectiontools" title="DisplayConnectionTools">DisplayConnectionTools</a>: <i>String</i>
    <a href="#displayhistory" title="DisplayHistory">DisplayHistory</a>: <i>String</i>
    <a href="#displaystatus" title="DisplayStatus">DisplayStatus</a>: <i>String</i>
    <a href="#dnsserver1" title="DnsServer1">DnsServer1</a>: <i>String</i>
    <a href="#dnsserver2" title="DnsServer2">DnsServer2</a>: <i>String</i>
    <a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#exclusiverouting" title="ExclusiveRouting">ExclusiveRouting</a>: <i>String</i>
    <a href="#forticlientdownload" title="ForticlientDownload">ForticlientDownload</a>: <i>String</i>
    <a href="#forticlientdownloadmethod" title="ForticlientDownloadMethod">ForticlientDownloadMethod</a>: <i>String</i>
    <a href="#heading" title="Heading">Heading</a>: <i>String</i>
    <a href="#hidessocredential" title="HideSsoCredential">HideSsoCredential</a>: <i>String</i>
    <a href="#hostcheck" title="HostCheck">HostCheck</a>: <i>String</i>
    <a href="#hostcheckinterval" title="HostCheckInterval">HostCheckInterval</a>: <i>Double</i>
    <a href="#ipmode" title="IpMode">IpMode</a>: <i>String</i>
    <a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>: <i>String</i>
    <a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>: <i>String</i>
    <a href="#ipv6exclusiverouting" title="Ipv6ExclusiveRouting">Ipv6ExclusiveRouting</a>: <i>String</i>
    <a href="#ipv6servicerestriction" title="Ipv6ServiceRestriction">Ipv6ServiceRestriction</a>: <i>String</i>
    <a href="#ipv6splittunneling" title="Ipv6SplitTunneling">Ipv6SplitTunneling</a>: <i>String</i>
    <a href="#ipv6splittunnelingroutingnegate" title="Ipv6SplitTunnelingRoutingNegate">Ipv6SplitTunnelingRoutingNegate</a>: <i>String</i>
    <a href="#ipv6tunnelmode" title="Ipv6TunnelMode">Ipv6TunnelMode</a>: <i>String</i>
    <a href="#ipv6winsserver1" title="Ipv6WinsServer1">Ipv6WinsServer1</a>: <i>String</i>
    <a href="#ipv6winsserver2" title="Ipv6WinsServer2">Ipv6WinsServer2</a>: <i>String</i>
    <a href="#keepalive" title="KeepAlive">KeepAlive</a>: <i>String</i>
    <a href="#limituserlogins" title="LimitUserLogins">LimitUserLogins</a>: <i>String</i>
    <a href="#macaddraction" title="MacAddrAction">MacAddrAction</a>: <i>String</i>
    <a href="#macaddrcheck" title="MacAddrCheck">MacAddrCheck</a>: <i>String</i>
    <a href="#macosforticlientdownloadurl" title="MacosForticlientDownloadUrl">MacosForticlientDownloadUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oscheck" title="OsCheck">OsCheck</a>: <i>String</i>
    <a href="#redirurl" title="RedirUrl">RedirUrl</a>: <i>String</i>
    <a href="#savepassword" title="SavePassword">SavePassword</a>: <i>String</i>
    <a href="#servicerestriction" title="ServiceRestriction">ServiceRestriction</a>: <i>String</i>
    <a href="#skipcheckforbrowser" title="SkipCheckForBrowser">SkipCheckForBrowser</a>: <i>String</i>
    <a href="#skipcheckforunsupportedos" title="SkipCheckForUnsupportedOs">SkipCheckForUnsupportedOs</a>: <i>String</i>
    <a href="#smbmaxversion" title="SmbMaxVersion">SmbMaxVersion</a>: <i>String</i>
    <a href="#smbminversion" title="SmbMinVersion">SmbMinVersion</a>: <i>String</i>
    <a href="#smbntlmv1auth" title="SmbNtlmv1Auth">SmbNtlmv1Auth</a>: <i>String</i>
    <a href="#smbv1" title="Smbv1">Smbv1</a>: <i>String</i>
    <a href="#splittunneling" title="SplitTunneling">SplitTunneling</a>: <i>String</i>
    <a href="#splittunnelingroutingnegate" title="SplitTunnelingRoutingNegate">SplitTunnelingRoutingNegate</a>: <i>String</i>
    <a href="#theme" title="Theme">Theme</a>: <i>String</i>
    <a href="#transformbackwardslashes" title="TransformBackwardSlashes">TransformBackwardSlashes</a>: <i>String</i>
    <a href="#tunnelmode" title="TunnelMode">TunnelMode</a>: <i>String</i>
    <a href="#usesdwan" title="UseSdwan">UseSdwan</a>: <i>String</i>
    <a href="#userbookmark" title="UserBookmark">UserBookmark</a>: <i>String</i>
    <a href="#usergroupbookmark" title="UserGroupBookmark">UserGroupBookmark</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#webmode" title="WebMode">WebMode</a>: <i>String</i>
    <a href="#windowsforticlientdownloadurl" title="WindowsForticlientDownloadUrl">WindowsForticlientDownloadUrl</a>: <i>String</i>
    <a href="#winsserver1" title="WinsServer1">WinsServer1</a>: <i>String</i>
    <a href="#winsserver2" title="WinsServer2">WinsServer2</a>: <i>String</i>
    <a href="#bookmarkgroup" title="BookmarkGroup">BookmarkGroup</a>: <i>
      - <a href="bookmarkgroupdefinition.md">BookmarkGroupDefinition</a></i>
    <a href="#hostcheckpolicy" title="HostCheckPolicy">HostCheckPolicy</a>: <i>
      - <a href="hostcheckpolicydefinition.md">HostCheckPolicyDefinition</a></i>
    <a href="#ippools" title="IpPools">IpPools</a>: <i>
      - <a href="ippoolsdefinition.md">IpPoolsDefinition</a></i>
    <a href="#ipv6pools" title="Ipv6Pools">Ipv6Pools</a>: <i>
      - <a href="ipv6poolsdefinition.md">Ipv6PoolsDefinition</a></i>
    <a href="#ipv6splittunnelingroutingaddress" title="Ipv6SplitTunnelingRoutingAddress">Ipv6SplitTunnelingRoutingAddress</a>: <i>
      - <a href="ipv6splittunnelingroutingaddressdefinition.md">Ipv6SplitTunnelingRoutingAddressDefinition</a></i>
    <a href="#macaddrcheckrule" title="MacAddrCheckRule">MacAddrCheckRule</a>: <i>
      - <a href="macaddrcheckruledefinition.md">MacAddrCheckRuleDefinition</a></i>
    <a href="#oschecklist" title="OsCheckList">OsCheckList</a>: <i>
      - <a href="oschecklistdefinition.md">OsCheckListDefinition</a></i>
    <a href="#splitdns" title="SplitDns">SplitDns</a>: <i>
      - <a href="splitdnsdefinition.md">SplitDnsDefinition</a></i>
    <a href="#splittunnelingroutingaddress" title="SplitTunnelingRoutingAddress">SplitTunnelingRoutingAddress</a>: <i>
      - <a href="splittunnelingroutingaddressdefinition.md">SplitTunnelingRoutingAddressDefinition</a></i>
</pre>

## Properties

#### AllowUserAccess

Allow user access to SSL-VPN applications. Valid values: `web`, `ftp`, `smb`, `sftp`, `telnet`, `ssh`, `vnc`, `rdp`, `ping`, `citrix`, `portforward`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoConnect

Enable/disable automatic connect by client when system is up. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomLang

Change the web portal display language. Overrides config system global set language. You can use config system custom-language and execute system custom-language to add custom language files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizeForticlientDownloadUrl

Enable support of customized download URL for FortiClient. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayBookmark

Enable to display the web portal bookmark widget. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayConnectionTools

Enable to display the web portal connection tools widget. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayHistory

Enable to display the web portal user login history widget. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayStatus

Enable to display the web portal status widget. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer1

IPv4 DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer2

IPv4 DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffix

DNS suffix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExclusiveRouting

Enable/disable all traffic go through tunnel only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientDownload

Enable/disable download option for FortiClient. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientDownloadMethod

FortiClient download method. Valid values: `direct`, `ssl-vpn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Heading

Web portal heading message.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideSsoCredential

Enable to prevent SSO credential being sent to client. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostCheck

Type of host checking performed on endpoints. Valid values: `none`, `av`, `fw`, `av-fw`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostCheckInterval

Periodic host check interval. Value of 0 means disabled and host checking only happens when the endpoint connects.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMode

Method by which users of this SSL-VPN tunnel obtain IP addresses. Valid values: `range`, `user-group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer1

IPv6 DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DnsServer2

IPv6 DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6ExclusiveRouting

Enable/disable all IPv6 traffic go through tunnel only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6ServiceRestriction

Enable/disable IPv6 tunnel service restriction. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6SplitTunneling

Enable/disable IPv6 split tunneling. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6SplitTunnelingRoutingNegate

Enable to negate IPv6 split tunneling routing address. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6TunnelMode

Enable/disable IPv6 SSL-VPN tunnel mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6WinsServer1

IPv6 WINS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6WinsServer2

IPv6 WINS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAlive

Enable/disable automatic reconnect for FortiClient connections. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitUserLogins

Enable to limit each user to one SSL-VPN session at a time. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddrAction

Client MAC address action. Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddrCheck

Enable/disable MAC address host checking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacosForticlientDownloadUrl

Download URL for Mac FortiClient.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Portal name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsCheck

Enable to let the FortiGate decide action based on client OS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirUrl

Client login redirect URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SavePassword

Enable/disable FortiClient saving the user's password. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRestriction

Enable/disable tunnel service restriction. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipCheckForBrowser

Enable to skip host check for browser support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipCheckForUnsupportedOs

Enable to skip host check if client OS does not support it. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbMaxVersion

SMB maximum client protocol version. Valid values: `smbv1`, `smbv2`, `smbv3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbMinVersion

SMB minimum client protocol version. Valid values: `smbv1`, `smbv2`, `smbv3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbNtlmv1Auth

Enable support of NTLMv1 for Samba authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smbv1

Enable/disable support of SMBv1 for Samba. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunneling

Enable/disable IPv4 split tunneling. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnelingRoutingNegate

Enable to negate split tunneling routing address. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Theme

Web portal color scheme.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransformBackwardSlashes

Transform backward slashes to forward slashes in URLs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMode

Enable/disable IPv4 SSL-VPN tunnel mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSdwan

Use SD-WAN rules to get output interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserBookmark

Enable to allow web portal users to create their own bookmarks. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroupBookmark

Enable to allow web portal users to create bookmarks for all users in the same user group. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebMode

Enable/disable SSL VPN web mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsForticlientDownloadUrl

Download URL for Windows FortiClient.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WinsServer1

IPv4 WINS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WinsServer2

IPv4 WINS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BookmarkGroup

_Required_: No

_Type_: List of <a href="bookmarkgroupdefinition.md">BookmarkGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostCheckPolicy

_Required_: No

_Type_: List of <a href="hostcheckpolicydefinition.md">HostCheckPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPools

_Required_: No

_Type_: List of <a href="ippoolsdefinition.md">IpPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Pools

_Required_: No

_Type_: List of <a href="ipv6poolsdefinition.md">Ipv6PoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6SplitTunnelingRoutingAddress

_Required_: No

_Type_: List of <a href="ipv6splittunnelingroutingaddressdefinition.md">Ipv6SplitTunnelingRoutingAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddrCheckRule

_Required_: No

_Type_: List of <a href="macaddrcheckruledefinition.md">MacAddrCheckRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsCheckList

_Required_: No

_Type_: List of <a href="oschecklistdefinition.md">OsCheckListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitDns

_Required_: No

_Type_: List of <a href="splitdnsdefinition.md">SplitDnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnelingRoutingAddress

_Required_: No

_Type_: List of <a href="splittunnelingroutingaddressdefinition.md">SplitTunnelingRoutingAddressDefinition</a>

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

