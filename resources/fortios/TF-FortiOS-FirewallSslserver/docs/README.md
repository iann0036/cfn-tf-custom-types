# TF::FortiOS::FirewallSslserver

Configure SSL servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallSslserver",
    "Properties" : {
        "<a href="#addheaderxforwardedproto" title="AddHeaderXForwardedProto">AddHeaderXForwardedProto</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#mappedport" title="MappedPort">MappedPort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>" : <i>String</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>" : <i>String</i>,
        "<a href="#ssldhbits" title="SslDhBits">SslDhBits</a>" : <i>String</i>,
        "<a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>" : <i>String</i>,
        "<a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>" : <i>String</i>,
        "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
        "<a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>" : <i>String</i>,
        "<a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallSslserver
Properties:
    <a href="#addheaderxforwardedproto" title="AddHeaderXForwardedProto">AddHeaderXForwardedProto</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#mappedport" title="MappedPort">MappedPort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>: <i>String</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>: <i>String</i>
    <a href="#ssldhbits" title="SslDhBits">SslDhBits</a>: <i>String</i>
    <a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>: <i>String</i>
    <a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>: <i>String</i>
    <a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
    <a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>: <i>String</i>
    <a href="#urlrewrite" title="UrlRewrite">UrlRewrite</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AddHeaderXForwardedProto

Enable/disable adding an X-Forwarded-Proto header to forwarded requests. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IPv4 address of the SSL server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappedPort

Mapped server service port (1 - 65535, default = 80).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Server service port (1 - 65535, default = 443).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAlgorithm

Relative strength of encryption algorithms accepted in negotiation. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

Name of certificate for SSL connections to this server (default = "Fortinet_CA_SSL").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientRenegotiation

Allow or block client renegotiation by server. Valid values: `allow`, `deny`, `secure`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslDhBits

Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048). Valid values: `768`, `1024`, `1536`, `2048`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMaxVersion

Highest SSL/TLS version to negotiate. Valid values: `tls-1.0`, `tls-1.1`, `tls-1.2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinVersion

Lowest SSL/TLS version to negotiate. Valid values: `tls-1.0`, `tls-1.1`, `tls-1.2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

SSL/TLS mode for encryption and decryption of traffic. Valid values: `half`, `full`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSendEmptyFrags

Enable/disable sending empty fragments to avoid attack on CBC IV. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRewrite

Enable/disable rewriting the URL. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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

