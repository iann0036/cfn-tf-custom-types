# TF::FortiOS::SystemFortiguard

Configure FortiGuard services.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemFortiguard",
    "Properties" : {
        "<a href="#antispamcache" title="AntispamCache">AntispamCache</a>" : <i>String</i>,
        "<a href="#antispamcachempercent" title="AntispamCacheMpercent">AntispamCacheMpercent</a>" : <i>Double</i>,
        "<a href="#antispamcachettl" title="AntispamCacheTtl">AntispamCacheTtl</a>" : <i>Double</i>,
        "<a href="#antispamexpiration" title="AntispamExpiration">AntispamExpiration</a>" : <i>Double</i>,
        "<a href="#antispamforceoff" title="AntispamForceOff">AntispamForceOff</a>" : <i>String</i>,
        "<a href="#antispamlicense" title="AntispamLicense">AntispamLicense</a>" : <i>Double</i>,
        "<a href="#antispamtimeout" title="AntispamTimeout">AntispamTimeout</a>" : <i>Double</i>,
        "<a href="#anycastsdnsserverip" title="AnycastSdnsServerIp">AnycastSdnsServerIp</a>" : <i>String</i>,
        "<a href="#anycastsdnsserverport" title="AnycastSdnsServerPort">AnycastSdnsServerPort</a>" : <i>Double</i>,
        "<a href="#autojoinforticloud" title="AutoJoinForticloud">AutoJoinForticloud</a>" : <i>String</i>,
        "<a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>" : <i>String</i>,
        "<a href="#ddnsserverport" title="DdnsServerPort">DdnsServerPort</a>" : <i>Double</i>,
        "<a href="#fortiguardanycast" title="FortiguardAnycast">FortiguardAnycast</a>" : <i>String</i>,
        "<a href="#fortiguardanycastsource" title="FortiguardAnycastSource">FortiguardAnycastSource</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#loadbalanceservers" title="LoadBalanceServers">LoadBalanceServers</a>" : <i>Double</i>,
        "<a href="#outbreakpreventioncache" title="OutbreakPreventionCache">OutbreakPreventionCache</a>" : <i>String</i>,
        "<a href="#outbreakpreventioncachempercent" title="OutbreakPreventionCacheMpercent">OutbreakPreventionCacheMpercent</a>" : <i>Double</i>,
        "<a href="#outbreakpreventioncachettl" title="OutbreakPreventionCacheTtl">OutbreakPreventionCacheTtl</a>" : <i>Double</i>,
        "<a href="#outbreakpreventionexpiration" title="OutbreakPreventionExpiration">OutbreakPreventionExpiration</a>" : <i>Double</i>,
        "<a href="#outbreakpreventionforceoff" title="OutbreakPreventionForceOff">OutbreakPreventionForceOff</a>" : <i>String</i>,
        "<a href="#outbreakpreventionlicense" title="OutbreakPreventionLicense">OutbreakPreventionLicense</a>" : <i>Double</i>,
        "<a href="#outbreakpreventiontimeout" title="OutbreakPreventionTimeout">OutbreakPreventionTimeout</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>" : <i>String</i>,
        "<a href="#proxyserverip" title="ProxyServerIp">ProxyServerIp</a>" : <i>String</i>,
        "<a href="#proxyserverport" title="ProxyServerPort">ProxyServerPort</a>" : <i>Double</i>,
        "<a href="#proxyusername" title="ProxyUsername">ProxyUsername</a>" : <i>String</i>,
        "<a href="#sandboxregion" title="SandboxRegion">SandboxRegion</a>" : <i>String</i>,
        "<a href="#sdnsoptions" title="SdnsOptions">SdnsOptions</a>" : <i>String</i>,
        "<a href="#sdnsserverip" title="SdnsServerIp">SdnsServerIp</a>" : <i>String</i>,
        "<a href="#sdnsserverport" title="SdnsServerPort">SdnsServerPort</a>" : <i>Double</i>,
        "<a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#sourceip6" title="SourceIp6">SourceIp6</a>" : <i>String</i>,
        "<a href="#updateserverlocation" title="UpdateServerLocation">UpdateServerLocation</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#webfiltercache" title="WebfilterCache">WebfilterCache</a>" : <i>String</i>,
        "<a href="#webfiltercachettl" title="WebfilterCacheTtl">WebfilterCacheTtl</a>" : <i>Double</i>,
        "<a href="#webfilterexpiration" title="WebfilterExpiration">WebfilterExpiration</a>" : <i>Double</i>,
        "<a href="#webfilterforceoff" title="WebfilterForceOff">WebfilterForceOff</a>" : <i>String</i>,
        "<a href="#webfilterlicense" title="WebfilterLicense">WebfilterLicense</a>" : <i>Double</i>,
        "<a href="#webfiltertimeout" title="WebfilterTimeout">WebfilterTimeout</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemFortiguard
Properties:
    <a href="#antispamcache" title="AntispamCache">AntispamCache</a>: <i>String</i>
    <a href="#antispamcachempercent" title="AntispamCacheMpercent">AntispamCacheMpercent</a>: <i>Double</i>
    <a href="#antispamcachettl" title="AntispamCacheTtl">AntispamCacheTtl</a>: <i>Double</i>
    <a href="#antispamexpiration" title="AntispamExpiration">AntispamExpiration</a>: <i>Double</i>
    <a href="#antispamforceoff" title="AntispamForceOff">AntispamForceOff</a>: <i>String</i>
    <a href="#antispamlicense" title="AntispamLicense">AntispamLicense</a>: <i>Double</i>
    <a href="#antispamtimeout" title="AntispamTimeout">AntispamTimeout</a>: <i>Double</i>
    <a href="#anycastsdnsserverip" title="AnycastSdnsServerIp">AnycastSdnsServerIp</a>: <i>String</i>
    <a href="#anycastsdnsserverport" title="AnycastSdnsServerPort">AnycastSdnsServerPort</a>: <i>Double</i>
    <a href="#autojoinforticloud" title="AutoJoinForticloud">AutoJoinForticloud</a>: <i>String</i>
    <a href="#ddnsserverip" title="DdnsServerIp">DdnsServerIp</a>: <i>String</i>
    <a href="#ddnsserverport" title="DdnsServerPort">DdnsServerPort</a>: <i>Double</i>
    <a href="#fortiguardanycast" title="FortiguardAnycast">FortiguardAnycast</a>: <i>String</i>
    <a href="#fortiguardanycastsource" title="FortiguardAnycastSource">FortiguardAnycastSource</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#loadbalanceservers" title="LoadBalanceServers">LoadBalanceServers</a>: <i>Double</i>
    <a href="#outbreakpreventioncache" title="OutbreakPreventionCache">OutbreakPreventionCache</a>: <i>String</i>
    <a href="#outbreakpreventioncachempercent" title="OutbreakPreventionCacheMpercent">OutbreakPreventionCacheMpercent</a>: <i>Double</i>
    <a href="#outbreakpreventioncachettl" title="OutbreakPreventionCacheTtl">OutbreakPreventionCacheTtl</a>: <i>Double</i>
    <a href="#outbreakpreventionexpiration" title="OutbreakPreventionExpiration">OutbreakPreventionExpiration</a>: <i>Double</i>
    <a href="#outbreakpreventionforceoff" title="OutbreakPreventionForceOff">OutbreakPreventionForceOff</a>: <i>String</i>
    <a href="#outbreakpreventionlicense" title="OutbreakPreventionLicense">OutbreakPreventionLicense</a>: <i>Double</i>
    <a href="#outbreakpreventiontimeout" title="OutbreakPreventionTimeout">OutbreakPreventionTimeout</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>: <i>String</i>
    <a href="#proxyserverip" title="ProxyServerIp">ProxyServerIp</a>: <i>String</i>
    <a href="#proxyserverport" title="ProxyServerPort">ProxyServerPort</a>: <i>Double</i>
    <a href="#proxyusername" title="ProxyUsername">ProxyUsername</a>: <i>String</i>
    <a href="#sandboxregion" title="SandboxRegion">SandboxRegion</a>: <i>String</i>
    <a href="#sdnsoptions" title="SdnsOptions">SdnsOptions</a>: <i>String</i>
    <a href="#sdnsserverip" title="SdnsServerIp">SdnsServerIp</a>: <i>String</i>
    <a href="#sdnsserverport" title="SdnsServerPort">SdnsServerPort</a>: <i>Double</i>
    <a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#sourceip6" title="SourceIp6">SourceIp6</a>: <i>String</i>
    <a href="#updateserverlocation" title="UpdateServerLocation">UpdateServerLocation</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#webfiltercache" title="WebfilterCache">WebfilterCache</a>: <i>String</i>
    <a href="#webfiltercachettl" title="WebfilterCacheTtl">WebfilterCacheTtl</a>: <i>Double</i>
    <a href="#webfilterexpiration" title="WebfilterExpiration">WebfilterExpiration</a>: <i>Double</i>
    <a href="#webfilterforceoff" title="WebfilterForceOff">WebfilterForceOff</a>: <i>String</i>
    <a href="#webfilterlicense" title="WebfilterLicense">WebfilterLicense</a>: <i>Double</i>
    <a href="#webfiltertimeout" title="WebfilterTimeout">WebfilterTimeout</a>: <i>Double</i>
</pre>

## Properties

#### AntispamCache

Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamCacheMpercent

Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamCacheTtl

Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamExpiration

Expiration date of the FortiGuard antispam contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamForceOff

Enable/disable turning off the FortiGuard antispam service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamLicense

Interval of time between license checks for the FortiGuard antispam contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntispamTimeout

Antispam query time out (1 - 30 sec, default = 7).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnycastSdnsServerIp

IP address of the FortiGuard anycast DNS rating server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnycastSdnsServerPort

Port to connect to on the FortiGuard anycast DNS rating server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoJoinForticloud

Automatically connect to and login to FortiCloud. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsServerIp

IP address of the FortiDDNS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DdnsServerPort

Port used to communicate with FortiDDNS servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardAnycast

Enable/disable use of FortiGuard's anycast network. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardAnycastSource

Configure which of Fortinet's servers to provide FortiGuard services in FortiGuard's anycast network. Default is Fortinet. Valid values: `fortinet`, `aws`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalanceServers

Number of servers to alternate between as first FortiGuard option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionCache

Enable/disable FortiGuard Virus Outbreak Prevention cache. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionCacheMpercent

Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionCacheTtl

Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionExpiration

Expiration date of FortiGuard Virus Outbreak Prevention contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionForceOff

Turn off FortiGuard Virus Outbreak Prevention service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionLicense

Interval of time between license checks for FortiGuard Virus Outbreak Prevention contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPreventionTimeout

FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port used to communicate with the FortiGuard servers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol used to communicate with the FortiGuard servers. Valid values: `udp`, `http`, `https`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPassword

Proxy user password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyServerIp

IP address of the proxy server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyServerPort

Port used to communicate with the proxy server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUsername

Proxy user name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxRegion

Cloud sandbox region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnsOptions

Customization options for the FortiGuard DNS service. Valid values: `include-question-section`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnsServerIp

IP address of the FortiDNS server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnsServerPort

Port used to communicate with FortiDNS servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountId

Service account ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IPv4 address used to communicate with FortiGuard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp6

Source IPv6 address used to communicate with FortiGuard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateServerLocation

Signature update server location. Valid values: `usa`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterCache

Enable/disable FortiGuard web filter caching. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterCacheTtl

Time-to-live for web filter cache entries in seconds (300 - 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterExpiration

Expiration date of the FortiGuard web filter contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterForceOff

Enable/disable turning off the FortiGuard web filtering service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterLicense

Interval of time between license checks for the FortiGuard web filter contract.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterTimeout

Web filter query time out (1 - 30 sec, default = 7).

_Required_: Yes

_Type_: Double

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

