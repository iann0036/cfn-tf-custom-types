# TF::FortiOS::WebproxyExplicit

Configure explicit Web proxy settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WebproxyExplicit",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#ftpincomingport" title="FtpIncomingPort">FtpIncomingPort</a>" : <i>String</i>,
        "<a href="#ftpoverhttp" title="FtpOverHttp">FtpOverHttp</a>" : <i>String</i>,
        "<a href="#httpincomingport" title="HttpIncomingPort">HttpIncomingPort</a>" : <i>String</i>,
        "<a href="#httpsincomingport" title="HttpsIncomingPort">HttpsIncomingPort</a>" : <i>String</i>,
        "<a href="#httpsreplacementmessage" title="HttpsReplacementMessage">HttpsReplacementMessage</a>" : <i>String</i>,
        "<a href="#incomingip" title="IncomingIp">IncomingIp</a>" : <i>String</i>,
        "<a href="#incomingip6" title="IncomingIp6">IncomingIp6</a>" : <i>String</i>,
        "<a href="#ipv6status" title="Ipv6Status">Ipv6Status</a>" : <i>String</i>,
        "<a href="#messageuponservererror" title="MessageUponServerError">MessageUponServerError</a>" : <i>String</i>,
        "<a href="#outgoingip" title="OutgoingIp">OutgoingIp</a>" : <i>String</i>,
        "<a href="#outgoingip6" title="OutgoingIp6">OutgoingIp6</a>" : <i>String</i>,
        "<a href="#pacfiledata" title="PacFileData">PacFileData</a>" : <i>String</i>,
        "<a href="#pacfilename" title="PacFileName">PacFileName</a>" : <i>String</i>,
        "<a href="#pacfileserverport" title="PacFileServerPort">PacFileServerPort</a>" : <i>String</i>,
        "<a href="#pacfileserverstatus" title="PacFileServerStatus">PacFileServerStatus</a>" : <i>String</i>,
        "<a href="#pacfileurl" title="PacFileUrl">PacFileUrl</a>" : <i>String</i>,
        "<a href="#prefdnsresult" title="PrefDnsResult">PrefDnsResult</a>" : <i>String</i>,
        "<a href="#realm" title="Realm">Realm</a>" : <i>String</i>,
        "<a href="#secdefaultaction" title="SecDefaultAction">SecDefaultAction</a>" : <i>String</i>,
        "<a href="#socks" title="Socks">Socks</a>" : <i>String</i>,
        "<a href="#socksincomingport" title="SocksIncomingPort">SocksIncomingPort</a>" : <i>String</i>,
        "<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#strictguest" title="StrictGuest">StrictGuest</a>" : <i>String</i>,
        "<a href="#traceauthnorsp" title="TraceAuthNoRsp">TraceAuthNoRsp</a>" : <i>String</i>,
        "<a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#pacpolicy" title="PacPolicy">PacPolicy</a>" : <i>[ <a href="pacpolicydefinition.md">PacPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WebproxyExplicit
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#ftpincomingport" title="FtpIncomingPort">FtpIncomingPort</a>: <i>String</i>
    <a href="#ftpoverhttp" title="FtpOverHttp">FtpOverHttp</a>: <i>String</i>
    <a href="#httpincomingport" title="HttpIncomingPort">HttpIncomingPort</a>: <i>String</i>
    <a href="#httpsincomingport" title="HttpsIncomingPort">HttpsIncomingPort</a>: <i>String</i>
    <a href="#httpsreplacementmessage" title="HttpsReplacementMessage">HttpsReplacementMessage</a>: <i>String</i>
    <a href="#incomingip" title="IncomingIp">IncomingIp</a>: <i>String</i>
    <a href="#incomingip6" title="IncomingIp6">IncomingIp6</a>: <i>String</i>
    <a href="#ipv6status" title="Ipv6Status">Ipv6Status</a>: <i>String</i>
    <a href="#messageuponservererror" title="MessageUponServerError">MessageUponServerError</a>: <i>String</i>
    <a href="#outgoingip" title="OutgoingIp">OutgoingIp</a>: <i>String</i>
    <a href="#outgoingip6" title="OutgoingIp6">OutgoingIp6</a>: <i>String</i>
    <a href="#pacfiledata" title="PacFileData">PacFileData</a>: <i>String</i>
    <a href="#pacfilename" title="PacFileName">PacFileName</a>: <i>String</i>
    <a href="#pacfileserverport" title="PacFileServerPort">PacFileServerPort</a>: <i>String</i>
    <a href="#pacfileserverstatus" title="PacFileServerStatus">PacFileServerStatus</a>: <i>String</i>
    <a href="#pacfileurl" title="PacFileUrl">PacFileUrl</a>: <i>String</i>
    <a href="#prefdnsresult" title="PrefDnsResult">PrefDnsResult</a>: <i>String</i>
    <a href="#realm" title="Realm">Realm</a>: <i>String</i>
    <a href="#secdefaultaction" title="SecDefaultAction">SecDefaultAction</a>: <i>String</i>
    <a href="#socks" title="Socks">Socks</a>: <i>String</i>
    <a href="#socksincomingport" title="SocksIncomingPort">SocksIncomingPort</a>: <i>String</i>
    <a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#strictguest" title="StrictGuest">StrictGuest</a>: <i>String</i>
    <a href="#traceauthnorsp" title="TraceAuthNoRsp">TraceAuthNoRsp</a>: <i>String</i>
    <a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#pacpolicy" title="PacPolicy">PacPolicy</a>: <i>
      - <a href="pacpolicydefinition.md">PacPolicyDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpIncomingPort

Accept incoming FTP-over-HTTP requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpOverHttp

Enable to proxy FTP-over-HTTP sessions sent from a web browser. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpIncomingPort

Accept incoming HTTP requests on one or more ports (0 - 65535, default = 8080).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsIncomingPort

Accept incoming HTTPS requests on one or more ports (0 - 65535, default = 0, use the same as HTTP).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsReplacementMessage

Enable/disable sending the client a replacement message for HTTPS requests. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingIp

Restrict the explicit HTTP proxy to only accept sessions from this IP address. An interface must have this IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingIp6

Restrict the explicit web proxy to only accept sessions from this IPv6 address. An interface must have this IPv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Status

Enable/disable allowing an IPv6 web proxy destination in policies and all IPv6 related entries in this command. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageUponServerError

Enable/disable displaying a replacement message when a server error is detected. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingIp

Outgoing HTTP requests will have this IP address as their source address. An interface must have this IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingIp6

Outgoing HTTP requests will leave this IPv6. Multiple interfaces can be specified. Interfaces must have these IPv6 addresses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileData

PAC file contents enclosed in quotes (maximum of 256K bytes).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileName

Pac file name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileServerPort

Port number that PAC traffic from client web browsers uses to connect to the explicit web proxy (0 - 65535, default = 0; use the same as HTTP).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileServerStatus

Enable/disable Proxy Auto-Configuration (PAC) for users of this explicit proxy profile. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacFileUrl

PAC file access URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefDnsResult

Prefer resolving addresses using the configured IPv4 or IPv6 DNS server (default = ipv4). Valid values: `ipv4`, `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Realm

Authentication realm used to identify the explicit web proxy (maximum of 63 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecDefaultAction

Accept or deny explicit web proxy sessions when no web proxy firewall policy exists. Valid values: `accept`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Socks

Enable/disable the SOCKS proxy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SocksIncomingPort

Accept incoming SOCKS proxy requests on one or more ports (0 - 65535, default = 0; use the same as HTTP).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAlgorithm

Relative strength of encryption algorithms accepted in HTTPS deep scan: high, medium, or low. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the explicit Web proxy for HTTP and HTTPS session. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictGuest

Enable/disable strict guest user checking by the explicit web proxy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TraceAuthNoRsp

Enable/disable logging timed-out authentication requests. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownHttpVersion

Either reject unknown HTTP traffic as malformed or handle unknown HTTP traffic as best as the proxy server can.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacPolicy

_Required_: No

_Type_: List of <a href="pacpolicydefinition.md">PacPolicyDefinition</a>

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

