# TF::FortiOS::WebproxyGlobal

Configure Web proxy global settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WebproxyGlobal",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fastpolicymatch" title="FastPolicyMatch">FastPolicyMatch</a>" : <i>String</i>,
        "<a href="#forwardproxyauth" title="ForwardProxyAuth">ForwardProxyAuth</a>" : <i>String</i>,
        "<a href="#forwardserveraffinitytimeout" title="ForwardServerAffinityTimeout">ForwardServerAffinityTimeout</a>" : <i>Double</i>,
        "<a href="#learnclientip" title="LearnClientIp">LearnClientIp</a>" : <i>String</i>,
        "<a href="#learnclientipfromheader" title="LearnClientIpFromHeader">LearnClientIpFromHeader</a>" : <i>String</i>,
        "<a href="#maxmessagelength" title="MaxMessageLength">MaxMessageLength</a>" : <i>Double</i>,
        "<a href="#maxrequestlength" title="MaxRequestLength">MaxRequestLength</a>" : <i>Double</i>,
        "<a href="#maxwafbodycachelength" title="MaxWafBodyCacheLength">MaxWafBodyCacheLength</a>" : <i>Double</i>,
        "<a href="#proxyfqdn" title="ProxyFqdn">ProxyFqdn</a>" : <i>String</i>,
        "<a href="#sslcacert" title="SslCaCert">SslCaCert</a>" : <i>String</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#strictwebcheck" title="StrictWebCheck">StrictWebCheck</a>" : <i>String</i>,
        "<a href="#tunnelnonhttp" title="TunnelNonHttp">TunnelNonHttp</a>" : <i>String</i>,
        "<a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#webproxyprofile" title="WebproxyProfile">WebproxyProfile</a>" : <i>String</i>,
        "<a href="#learnclientipsrcaddr" title="LearnClientIpSrcaddr">LearnClientIpSrcaddr</a>" : <i>[ <a href="learnclientipsrcaddrdefinition.md">LearnClientIpSrcaddrDefinition</a>, ... ]</i>,
        "<a href="#learnclientipsrcaddr6" title="LearnClientIpSrcaddr6">LearnClientIpSrcaddr6</a>" : <i>[ <a href="learnclientipsrcaddr6definition.md">LearnClientIpSrcaddr6Definition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WebproxyGlobal
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fastpolicymatch" title="FastPolicyMatch">FastPolicyMatch</a>: <i>String</i>
    <a href="#forwardproxyauth" title="ForwardProxyAuth">ForwardProxyAuth</a>: <i>String</i>
    <a href="#forwardserveraffinitytimeout" title="ForwardServerAffinityTimeout">ForwardServerAffinityTimeout</a>: <i>Double</i>
    <a href="#learnclientip" title="LearnClientIp">LearnClientIp</a>: <i>String</i>
    <a href="#learnclientipfromheader" title="LearnClientIpFromHeader">LearnClientIpFromHeader</a>: <i>String</i>
    <a href="#maxmessagelength" title="MaxMessageLength">MaxMessageLength</a>: <i>Double</i>
    <a href="#maxrequestlength" title="MaxRequestLength">MaxRequestLength</a>: <i>Double</i>
    <a href="#maxwafbodycachelength" title="MaxWafBodyCacheLength">MaxWafBodyCacheLength</a>: <i>Double</i>
    <a href="#proxyfqdn" title="ProxyFqdn">ProxyFqdn</a>: <i>String</i>
    <a href="#sslcacert" title="SslCaCert">SslCaCert</a>: <i>String</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#strictwebcheck" title="StrictWebCheck">StrictWebCheck</a>: <i>String</i>
    <a href="#tunnelnonhttp" title="TunnelNonHttp">TunnelNonHttp</a>: <i>String</i>
    <a href="#unknownhttpversion" title="UnknownHttpVersion">UnknownHttpVersion</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#webproxyprofile" title="WebproxyProfile">WebproxyProfile</a>: <i>String</i>
    <a href="#learnclientipsrcaddr" title="LearnClientIpSrcaddr">LearnClientIpSrcaddr</a>: <i>
      - <a href="learnclientipsrcaddrdefinition.md">LearnClientIpSrcaddrDefinition</a></i>
    <a href="#learnclientipsrcaddr6" title="LearnClientIpSrcaddr6">LearnClientIpSrcaddr6</a>: <i>
      - <a href="learnclientipsrcaddr6definition.md">LearnClientIpSrcaddr6Definition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastPolicyMatch

Enable/disable fast matching algorithm for explicit and transparent proxy policy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyAuth

Enable/disable forwarding proxy authentication headers. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardServerAffinityTimeout

Period of time before the source IP's traffic is no longer assigned to the forwarding server (6 - 60 min, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearnClientIp

Enable/disable learning the client's IP address from headers. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearnClientIpFromHeader

Learn client IP address from the specified headers. Valid values: `true-client-ip`, `x-real-ip`, `x-forwarded-for`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxMessageLength

Maximum length of HTTP message, not including body (16 - 256 Kbytes, default = 32).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestLength

Maximum length of HTTP request line (2 - 64 Kbytes, default = 4).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxWafBodyCacheLength

Maximum length of HTTP messages processed by Web Application Firewall (WAF) (10 - 1024 Kbytes, default = 32).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyFqdn

Fully Qualified Domain Name (FQDN) that clients connect to (default = default.fqdn) to connect to the explicit web proxy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCaCert

SSL CA certificate for SSL interception.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

SSL certificate for SSL interception.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictWebCheck

Enable/disable strict web checking to block web sites that send incorrect headers that don't conform to HTTP 1.1. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelNonHttp

Enable/disable allowing non-HTTP traffic. Allowed non-HTTP traffic is tunneled. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownHttpVersion

Action to take when an unknown version of HTTP is encountered: reject, allow (tunnel), or proceed with best-effort. Valid values: `reject`, `tunnel`, `best-effort`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebproxyProfile

Name of the web proxy profile to apply when explicit proxy traffic is allowed by default and traffic is accepted that does not match an explicit proxy policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearnClientIpSrcaddr

_Required_: No

_Type_: List of <a href="learnclientipsrcaddrdefinition.md">LearnClientIpSrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearnClientIpSrcaddr6

_Required_: No

_Type_: List of <a href="learnclientipsrcaddr6definition.md">LearnClientIpSrcaddr6Definition</a>

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

