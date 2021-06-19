# TF::FortiOS::VpnsslSettings

Configure SSL VPN.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnsslSettings",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#authsessionchecksourceip" title="AuthSessionCheckSourceIp">AuthSessionCheckSourceIp</a>" : <i>String</i>,
        "<a href="#authtimeout" title="AuthTimeout">AuthTimeout</a>" : <i>Double</i>,
        "<a href="#autotunnelstaticroute" title="AutoTunnelStaticRoute">AutoTunnelStaticRoute</a>" : <i>String</i>,
        "<a href="#bannedcipher" title="BannedCipher">BannedCipher</a>" : <i>String</i>,
        "<a href="#checkreferer" title="CheckReferer">CheckReferer</a>" : <i>String</i>,
        "<a href="#defaultportal" title="DefaultPortal">DefaultPortal</a>" : <i>String</i>,
        "<a href="#deflatecompressionlevel" title="DeflateCompressionLevel">DeflateCompressionLevel</a>" : <i>Double</i>,
        "<a href="#deflatemindatasize" title="DeflateMinDataSize">DeflateMinDataSize</a>" : <i>Double</i>,
        "<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>" : <i>String</i>,
        "<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>" : <i>String</i>,
        "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
        "<a href="#dtlshellotimeout" title="DtlsHelloTimeout">DtlsHelloTimeout</a>" : <i>Double</i>,
        "<a href="#dtlsmaxprotover" title="DtlsMaxProtoVer">DtlsMaxProtoVer</a>" : <i>String</i>,
        "<a href="#dtlsminprotover" title="DtlsMinProtoVer">DtlsMinProtoVer</a>" : <i>String</i>,
        "<a href="#dtlstunnel" title="DtlsTunnel">DtlsTunnel</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#encode2fsequence" title="Encode2fSequence">Encode2fSequence</a>" : <i>String</i>,
        "<a href="#encryptandstorepassword" title="EncryptAndStorePassword">EncryptAndStorePassword</a>" : <i>String</i>,
        "<a href="#forcetwofactorauth" title="ForceTwoFactorAuth">ForceTwoFactorAuth</a>" : <i>String</i>,
        "<a href="#headerxforwardedfor" title="HeaderXForwardedFor">HeaderXForwardedFor</a>" : <i>String</i>,
        "<a href="#hstsincludesubdomains" title="HstsIncludeSubdomains">HstsIncludeSubdomains</a>" : <i>String</i>,
        "<a href="#httpcompression" title="HttpCompression">HttpCompression</a>" : <i>String</i>,
        "<a href="#httponlycookie" title="HttpOnlyCookie">HttpOnlyCookie</a>" : <i>String</i>,
        "<a href="#httprequestbodytimeout" title="HttpRequestBodyTimeout">HttpRequestBodyTimeout</a>" : <i>Double</i>,
        "<a href="#httprequestheadertimeout" title="HttpRequestHeaderTimeout">HttpRequestHeaderTimeout</a>" : <i>Double</i>,
        "<a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>" : <i>String</i>,
        "<a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>" : <i>String</i>,
        "<a href="#ipv6winsserver1" title="Ipv6WinsServer1">Ipv6WinsServer1</a>" : <i>String</i>,
        "<a href="#ipv6winsserver2" title="Ipv6WinsServer2">Ipv6WinsServer2</a>" : <i>String</i>,
        "<a href="#loginattemptlimit" title="LoginAttemptLimit">LoginAttemptLimit</a>" : <i>Double</i>,
        "<a href="#loginblocktime" title="LoginBlockTime">LoginBlockTime</a>" : <i>Double</i>,
        "<a href="#logintimeout" title="LoginTimeout">LoginTimeout</a>" : <i>Double</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#portprecedence" title="PortPrecedence">PortPrecedence</a>" : <i>String</i>,
        "<a href="#reqclientcert" title="Reqclientcert">Reqclientcert</a>" : <i>String</i>,
        "<a href="#routesourceinterface" title="RouteSourceInterface">RouteSourceInterface</a>" : <i>String</i>,
        "<a href="#servercert" title="Servercert">Servercert</a>" : <i>String</i>,
        "<a href="#sourceaddress6negate" title="SourceAddress6Negate">SourceAddress6Negate</a>" : <i>String</i>,
        "<a href="#sourceaddressnegate" title="SourceAddressNegate">SourceAddressNegate</a>" : <i>String</i>,
        "<a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>" : <i>String</i>,
        "<a href="#sslinsertemptyfragment" title="SslInsertEmptyFragment">SslInsertEmptyFragment</a>" : <i>String</i>,
        "<a href="#sslmaxprotover" title="SslMaxProtoVer">SslMaxProtoVer</a>" : <i>String</i>,
        "<a href="#sslminprotover" title="SslMinProtoVer">SslMinProtoVer</a>" : <i>String</i>,
        "<a href="#tlsv10" title="Tlsv10">Tlsv10</a>" : <i>String</i>,
        "<a href="#tlsv11" title="Tlsv11">Tlsv11</a>" : <i>String</i>,
        "<a href="#tlsv12" title="Tlsv12">Tlsv12</a>" : <i>String</i>,
        "<a href="#tlsv13" title="Tlsv13">Tlsv13</a>" : <i>String</i>,
        "<a href="#transformbackwardslashes" title="TransformBackwardSlashes">TransformBackwardSlashes</a>" : <i>String</i>,
        "<a href="#tunnelconnectwithoutreauth" title="TunnelConnectWithoutReauth">TunnelConnectWithoutReauth</a>" : <i>String</i>,
        "<a href="#tunnelusersessiontimeout" title="TunnelUserSessionTimeout">TunnelUserSessionTimeout</a>" : <i>Double</i>,
        "<a href="#unsafelegacyrenegotiation" title="UnsafeLegacyRenegotiation">UnsafeLegacyRenegotiation</a>" : <i>String</i>,
        "<a href="#urlobscuration" title="UrlObscuration">UrlObscuration</a>" : <i>String</i>,
        "<a href="#userpeer" title="UserPeer">UserPeer</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#winsserver1" title="WinsServer1">WinsServer1</a>" : <i>String</i>,
        "<a href="#winsserver2" title="WinsServer2">WinsServer2</a>" : <i>String</i>,
        "<a href="#xcontenttypeoptions" title="XContentTypeOptions">XContentTypeOptions</a>" : <i>String</i>,
        "<a href="#authenticationrule" title="AuthenticationRule">AuthenticationRule</a>" : <i>[ <a href="authenticationruledefinition.md">AuthenticationRuleDefinition</a>, ... ]</i>,
        "<a href="#sourceaddress" title="SourceAddress">SourceAddress</a>" : <i>[ <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>, ... ]</i>,
        "<a href="#sourceaddress6" title="SourceAddress6">SourceAddress6</a>" : <i>[ <a href="sourceaddress6definition.md">SourceAddress6Definition</a>, ... ]</i>,
        "<a href="#sourceinterface" title="SourceInterface">SourceInterface</a>" : <i>[ <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a>, ... ]</i>,
        "<a href="#tunnelippools" title="TunnelIpPools">TunnelIpPools</a>" : <i>[ <a href="tunnelippoolsdefinition.md">TunnelIpPoolsDefinition</a>, ... ]</i>,
        "<a href="#tunnelipv6pools" title="TunnelIpv6Pools">TunnelIpv6Pools</a>" : <i>[ <a href="tunnelipv6poolsdefinition.md">TunnelIpv6PoolsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnsslSettings
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#authsessionchecksourceip" title="AuthSessionCheckSourceIp">AuthSessionCheckSourceIp</a>: <i>String</i>
    <a href="#authtimeout" title="AuthTimeout">AuthTimeout</a>: <i>Double</i>
    <a href="#autotunnelstaticroute" title="AutoTunnelStaticRoute">AutoTunnelStaticRoute</a>: <i>String</i>
    <a href="#bannedcipher" title="BannedCipher">BannedCipher</a>: <i>String</i>
    <a href="#checkreferer" title="CheckReferer">CheckReferer</a>: <i>String</i>
    <a href="#defaultportal" title="DefaultPortal">DefaultPortal</a>: <i>String</i>
    <a href="#deflatecompressionlevel" title="DeflateCompressionLevel">DeflateCompressionLevel</a>: <i>Double</i>
    <a href="#deflatemindatasize" title="DeflateMinDataSize">DeflateMinDataSize</a>: <i>Double</i>
    <a href="#dnsserver1" title="DnsServer1">DnsServer1</a>: <i>String</i>
    <a href="#dnsserver2" title="DnsServer2">DnsServer2</a>: <i>String</i>
    <a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
    <a href="#dtlshellotimeout" title="DtlsHelloTimeout">DtlsHelloTimeout</a>: <i>Double</i>
    <a href="#dtlsmaxprotover" title="DtlsMaxProtoVer">DtlsMaxProtoVer</a>: <i>String</i>
    <a href="#dtlsminprotover" title="DtlsMinProtoVer">DtlsMinProtoVer</a>: <i>String</i>
    <a href="#dtlstunnel" title="DtlsTunnel">DtlsTunnel</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#encode2fsequence" title="Encode2fSequence">Encode2fSequence</a>: <i>String</i>
    <a href="#encryptandstorepassword" title="EncryptAndStorePassword">EncryptAndStorePassword</a>: <i>String</i>
    <a href="#forcetwofactorauth" title="ForceTwoFactorAuth">ForceTwoFactorAuth</a>: <i>String</i>
    <a href="#headerxforwardedfor" title="HeaderXForwardedFor">HeaderXForwardedFor</a>: <i>String</i>
    <a href="#hstsincludesubdomains" title="HstsIncludeSubdomains">HstsIncludeSubdomains</a>: <i>String</i>
    <a href="#httpcompression" title="HttpCompression">HttpCompression</a>: <i>String</i>
    <a href="#httponlycookie" title="HttpOnlyCookie">HttpOnlyCookie</a>: <i>String</i>
    <a href="#httprequestbodytimeout" title="HttpRequestBodyTimeout">HttpRequestBodyTimeout</a>: <i>Double</i>
    <a href="#httprequestheadertimeout" title="HttpRequestHeaderTimeout">HttpRequestHeaderTimeout</a>: <i>Double</i>
    <a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#ipv6dnsserver1" title="Ipv6DnsServer1">Ipv6DnsServer1</a>: <i>String</i>
    <a href="#ipv6dnsserver2" title="Ipv6DnsServer2">Ipv6DnsServer2</a>: <i>String</i>
    <a href="#ipv6winsserver1" title="Ipv6WinsServer1">Ipv6WinsServer1</a>: <i>String</i>
    <a href="#ipv6winsserver2" title="Ipv6WinsServer2">Ipv6WinsServer2</a>: <i>String</i>
    <a href="#loginattemptlimit" title="LoginAttemptLimit">LoginAttemptLimit</a>: <i>Double</i>
    <a href="#loginblocktime" title="LoginBlockTime">LoginBlockTime</a>: <i>Double</i>
    <a href="#logintimeout" title="LoginTimeout">LoginTimeout</a>: <i>Double</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#portprecedence" title="PortPrecedence">PortPrecedence</a>: <i>String</i>
    <a href="#reqclientcert" title="Reqclientcert">Reqclientcert</a>: <i>String</i>
    <a href="#routesourceinterface" title="RouteSourceInterface">RouteSourceInterface</a>: <i>String</i>
    <a href="#servercert" title="Servercert">Servercert</a>: <i>String</i>
    <a href="#sourceaddress6negate" title="SourceAddress6Negate">SourceAddress6Negate</a>: <i>String</i>
    <a href="#sourceaddressnegate" title="SourceAddressNegate">SourceAddressNegate</a>: <i>String</i>
    <a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>: <i>String</i>
    <a href="#sslinsertemptyfragment" title="SslInsertEmptyFragment">SslInsertEmptyFragment</a>: <i>String</i>
    <a href="#sslmaxprotover" title="SslMaxProtoVer">SslMaxProtoVer</a>: <i>String</i>
    <a href="#sslminprotover" title="SslMinProtoVer">SslMinProtoVer</a>: <i>String</i>
    <a href="#tlsv10" title="Tlsv10">Tlsv10</a>: <i>String</i>
    <a href="#tlsv11" title="Tlsv11">Tlsv11</a>: <i>String</i>
    <a href="#tlsv12" title="Tlsv12">Tlsv12</a>: <i>String</i>
    <a href="#tlsv13" title="Tlsv13">Tlsv13</a>: <i>String</i>
    <a href="#transformbackwardslashes" title="TransformBackwardSlashes">TransformBackwardSlashes</a>: <i>String</i>
    <a href="#tunnelconnectwithoutreauth" title="TunnelConnectWithoutReauth">TunnelConnectWithoutReauth</a>: <i>String</i>
    <a href="#tunnelusersessiontimeout" title="TunnelUserSessionTimeout">TunnelUserSessionTimeout</a>: <i>Double</i>
    <a href="#unsafelegacyrenegotiation" title="UnsafeLegacyRenegotiation">UnsafeLegacyRenegotiation</a>: <i>String</i>
    <a href="#urlobscuration" title="UrlObscuration">UrlObscuration</a>: <i>String</i>
    <a href="#userpeer" title="UserPeer">UserPeer</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#winsserver1" title="WinsServer1">WinsServer1</a>: <i>String</i>
    <a href="#winsserver2" title="WinsServer2">WinsServer2</a>: <i>String</i>
    <a href="#xcontenttypeoptions" title="XContentTypeOptions">XContentTypeOptions</a>: <i>String</i>
    <a href="#authenticationrule" title="AuthenticationRule">AuthenticationRule</a>: <i>
      - <a href="authenticationruledefinition.md">AuthenticationRuleDefinition</a></i>
    <a href="#sourceaddress" title="SourceAddress">SourceAddress</a>: <i>
      - <a href="sourceaddressdefinition.md">SourceAddressDefinition</a></i>
    <a href="#sourceaddress6" title="SourceAddress6">SourceAddress6</a>: <i>
      - <a href="sourceaddress6definition.md">SourceAddress6Definition</a></i>
    <a href="#sourceinterface" title="SourceInterface">SourceInterface</a>: <i>
      - <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a></i>
    <a href="#tunnelippools" title="TunnelIpPools">TunnelIpPools</a>: <i>
      - <a href="tunnelippoolsdefinition.md">TunnelIpPoolsDefinition</a></i>
    <a href="#tunnelipv6pools" title="TunnelIpv6Pools">TunnelIpv6Pools</a>: <i>
      - <a href="tunnelipv6poolsdefinition.md">TunnelIpv6PoolsDefinition</a></i>
</pre>

## Properties

#### Algorithm

Force the SSL-VPN security level. High allows only high. Medium allows medium and high. Low allows any. Valid values: `high`, `medium`, `default`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSessionCheckSourceIp

Enable/disable checking of source IP for authentication session. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthTimeout

SSL-VPN authentication timeout (1 - 259200 sec (3 days), 0 for no timeout).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoTunnelStaticRoute

Enable to auto-create static routes for the SSL-VPN tunnel IP addresses. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BannedCipher

Select one or more cipher technologies that cannot be used in SSL-VPN negotiations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckReferer

Enable/disable verification of referer field in HTTP request header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPortal

Default SSL VPN portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeflateCompressionLevel

Compression level (0~9).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeflateMinDataSize

Minimum amount of data that triggers compression (200 - 65535 bytes).

_Required_: No

_Type_: Double

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

#### DnsSuffix

DNS suffix used for SSL-VPN clients.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsHelloTimeout

SSLVPN maximum DTLS hello timeout (10 - 60 sec, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsMaxProtoVer

DTLS maximum protocol version. Valid values: `dtls1-0`, `dtls1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsMinProtoVer

DTLS minimum protocol version. Valid values: `dtls1-0`, `dtls1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DtlsTunnel

Enable DTLS to prevent eavesdropping, tampering, or message forgery. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encode2fSequence

Encode \2F sequence to forward slash in URLs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptAndStorePassword

Encrypt and store user passwords for SSL-VPN web sessions. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceTwoFactorAuth

Enable to force two-factor authentication for all SSL-VPNs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderXForwardedFor

Forward the same, add, or remove HTTP header. Valid values: `pass`, `add`, `remove`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HstsIncludeSubdomains

Add HSTS includeSubDomains response header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCompression

Enable to allow HTTP compression over SSL-VPN tunnels. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpOnlyCookie

Enable/disable SSL-VPN support for HttpOnly cookies. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestBodyTimeout

SSL-VPN session is disconnected if an HTTP request body is not received within this time (1 - 60 sec, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestHeaderTimeout

SSL-VPN session is disconnected if an HTTP request header is not received within this time (1 - 60 sec, default = 20).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsRedirect

Enable/disable redirect of port 80 to SSL-VPN port. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

SSL VPN disconnects if idle for specified time in seconds.

_Required_: No

_Type_: Double

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

#### LoginAttemptLimit

SSL VPN maximum login attempt times before block (0 - 10, default = 2, 0 = no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginBlockTime

Time for which a user is blocked from logging in after too many failed login attempts (0 - 86400 sec, default = 60).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginTimeout

SSLVPN maximum login timeout (10 - 180 sec, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

SSL-VPN access port (1 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortPrecedence

Enable means that if SSL-VPN connections are allowed on an interface admin GUI connections are blocked on that interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reqclientcert

Enable to require client certificates for all SSL-VPN users. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteSourceInterface

Enable to allow SSL-VPN sessions to bypass routing and bind to the incoming interface. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servercert

Name of the server certificate to be used for SSL-VPNs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress6Negate

Enable/disable negated source IPv6 address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressNegate

Enable/disable negated source address match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientRenegotiation

Enable to allow client renegotiation by the server if the tunnel goes down. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslInsertEmptyFragment

Enable/disable insertion of empty fragment. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMaxProtoVer

SSL maximum protocol version. Valid values: `tls1-0`, `tls1-1`, `tls1-2`, `tls1-3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVer

SSL minimum protocol version. Valid values: `tls1-0`, `tls1-1`, `tls1-2`, `tls1-3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tlsv10

Enable/disable TLSv1.0. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tlsv11

Enable/disable TLSv1.1. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tlsv12

Enable/disable TLSv1.2. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tlsv13

Enable/disable TLSv1.3. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransformBackwardSlashes

Transform backward slashes to forward slashes in URLs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelConnectWithoutReauth

Enable/disable tunnel connection without re-authorization if previous connection dropped. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelUserSessionTimeout

Time out value to clean up user session after tunnel connection is dropped (1 - 255 sec, default=30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsafeLegacyRenegotiation

Enable/disable unsafe legacy re-negotiation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlObscuration

Enable to obscure the host name of the URL of the web browser display. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPeer

Name of user peer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

#### XContentTypeOptions

Add HTTP X-Content-Type-Options header. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticationRule

_Required_: No

_Type_: List of <a href="authenticationruledefinition.md">AuthenticationRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress

_Required_: No

_Type_: List of <a href="sourceaddressdefinition.md">SourceAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress6

_Required_: No

_Type_: List of <a href="sourceaddress6definition.md">SourceAddress6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceInterface

_Required_: No

_Type_: List of <a href="sourceinterfacedefinition.md">SourceInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelIpPools

_Required_: No

_Type_: List of <a href="tunnelippoolsdefinition.md">TunnelIpPoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelIpv6Pools

_Required_: No

_Type_: List of <a href="tunnelipv6poolsdefinition.md">TunnelIpv6PoolsDefinition</a>

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

