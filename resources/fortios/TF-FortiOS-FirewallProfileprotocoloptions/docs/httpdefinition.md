# TF::FortiOS::FirewallProfileprotocoloptions HttpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blockpagestatuscode" title="BlockPageStatusCode">BlockPageStatusCode</a>" : <i>Double</i>,
    "<a href="#comfortamount" title="ComfortAmount">ComfortAmount</a>" : <i>Double</i>,
    "<a href="#comfortinterval" title="ComfortInterval">ComfortInterval</a>" : <i>Double</i>,
    "<a href="#fortinetbar" title="FortinetBar">FortinetBar</a>" : <i>String</i>,
    "<a href="#fortinetbarport" title="FortinetBarPort">FortinetBarPort</a>" : <i>Double</i>,
    "<a href="#httppolicy" title="HttpPolicy">HttpPolicy</a>" : <i>String</i>,
    "<a href="#inspectall" title="InspectAll">InspectAll</a>" : <i>String</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>Double</i>,
    "<a href="#postlang" title="PostLang">PostLang</a>" : <i>String</i>,
    "<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>" : <i>String</i>,
    "<a href="#rangeblock" title="RangeBlock">RangeBlock</a>" : <i>String</i>,
    "<a href="#retrycount" title="RetryCount">RetryCount</a>" : <i>Double</i>,
    "<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>" : <i>String</i>,
    "<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#streambaseduncompressedlimit" title="StreamBasedUncompressedLimit">StreamBasedUncompressedLimit</a>" : <i>Double</i>,
    "<a href="#streamingcontentbypass" title="StreamingContentBypass">StreamingContentBypass</a>" : <i>String</i>,
    "<a href="#stripxforwardedfor" title="StripXForwardedFor">StripXForwardedFor</a>" : <i>String</i>,
    "<a href="#switchingprotocols" title="SwitchingProtocols">SwitchingProtocols</a>" : <i>String</i>,
    "<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>" : <i>Double</i>,
    "<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>" : <i>Double</i>,
    "<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>" : <i>Double</i>,
    "<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>" : <i>String</i>,
    "<a href="#tunnelnonhttp" title="TunnelNonHttp">TunnelNonHttp</a>" : <i>String</i>,
    "<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>" : <i>Double</i>,
    "<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>" : <i>Double</i>,
    "<a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#blockpagestatuscode" title="BlockPageStatusCode">BlockPageStatusCode</a>: <i>Double</i>
<a href="#comfortamount" title="ComfortAmount">ComfortAmount</a>: <i>Double</i>
<a href="#comfortinterval" title="ComfortInterval">ComfortInterval</a>: <i>Double</i>
<a href="#fortinetbar" title="FortinetBar">FortinetBar</a>: <i>String</i>
<a href="#fortinetbarport" title="FortinetBarPort">FortinetBarPort</a>: <i>Double</i>
<a href="#httppolicy" title="HttpPolicy">HttpPolicy</a>: <i>String</i>
<a href="#inspectall" title="InspectAll">InspectAll</a>: <i>String</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#oversizelimit" title="OversizeLimit">OversizeLimit</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>Double</i>
<a href="#postlang" title="PostLang">PostLang</a>: <i>String</i>
<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>: <i>String</i>
<a href="#rangeblock" title="RangeBlock">RangeBlock</a>: <i>String</i>
<a href="#retrycount" title="RetryCount">RetryCount</a>: <i>Double</i>
<a href="#scanbzip2" title="ScanBzip2">ScanBzip2</a>: <i>String</i>
<a href="#ssloffloaded" title="SslOffloaded">SslOffloaded</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#streambaseduncompressedlimit" title="StreamBasedUncompressedLimit">StreamBasedUncompressedLimit</a>: <i>Double</i>
<a href="#streamingcontentbypass" title="StreamingContentBypass">StreamingContentBypass</a>: <i>String</i>
<a href="#stripxforwardedfor" title="StripXForwardedFor">StripXForwardedFor</a>: <i>String</i>
<a href="#switchingprotocols" title="SwitchingProtocols">SwitchingProtocols</a>: <i>String</i>
<a href="#tcpwindowmaximum" title="TcpWindowMaximum">TcpWindowMaximum</a>: <i>Double</i>
<a href="#tcpwindowminimum" title="TcpWindowMinimum">TcpWindowMinimum</a>: <i>Double</i>
<a href="#tcpwindowsize" title="TcpWindowSize">TcpWindowSize</a>: <i>Double</i>
<a href="#tcpwindowtype" title="TcpWindowType">TcpWindowType</a>: <i>String</i>
<a href="#tunnelnonhttp" title="TunnelNonHttp">TunnelNonHttp</a>: <i>String</i>
<a href="#uncompressednestlimit" title="UncompressedNestLimit">UncompressedNestLimit</a>: <i>Double</i>
<a href="#uncompressedoversizelimit" title="UncompressedOversizeLimit">UncompressedOversizeLimit</a>: <i>Double</i>
<a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>: <i>String</i>
</pre>

## Properties

#### BlockPageStatusCode

Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComfortAmount

Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComfortInterval

Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortinetBar

Enable/disable Fortinet bar on HTML content. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortinetBarPort

Port for use by Fortinet Bar (1 - 65535, default = 8011).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpPolicy

Enable/disable HTTP policy check. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectAll

Enable/disable the inspection of all ports for the protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

One or more options that can be applied to the session. Valid values: `clientcomfort`, `servercomfort`, `oversize`, `chunkedbypass`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OversizeLimit

Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to scan for content (1 - 65535, default = 80).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostLang

ID codes for character sets to be used to convert to UTF-8 for banned words and DLP on HTTP posts (maximum of 5 character sets). Valid values: `jisx0201`, `jisx0208`, `jisx0212`, `gb2312`, `ksc5601-ex`, `euc-jp`, `sjis`, `iso2022-jp`, `iso2022-jp-1`, `iso2022-jp-2`, `euc-cn`, `ces-gbk`, `hz`, `ces-big5`, `euc-kr`, `iso2022-jp-3`, `iso8859-1`, `tis620`, `cp874`, `cp1252`, `cp1251`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAfterTcpHandshake

Proxy traffic after the TCP 3-way handshake has been established (not before). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeBlock

Enable/disable blocking of partial downloads. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryCount

Number of attempts to retry HTTP connection (0 - 100, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanBzip2

Enable/disable scanning of BZip2 compressed files. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslOffloaded

SSL decryption and encryption performed by an external device. Valid values: `no`, `yes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the active status of scanning for this protocol. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamBasedUncompressedLimit

Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default).  Stream-based uncompression used only under certain conditions.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingContentBypass

Enable/disable bypassing of streaming content from buffering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StripXForwardedFor

Enable/disable stripping of HTTP X-Forwarded-For header. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingProtocols

Bypass from scanning, or block a connection that attempts to switch protocol. Valid values: `bypass`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMaximum

Maximum dynamic TCP window size (default = 8MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowMinimum

Minimum dynamic TCP window size (default = 128KB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowSize

Set TCP static window size (default = 256KB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpWindowType

Specify type of TCP window to use for this protocol. Valid values: `system`, `static`, `dynamic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelNonHttp

Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncompressedNestLimit

Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncompressedOversizeLimit

Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownHttpVersion

How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1. Valid values: `reject`, `tunnel`, `best-effort`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

