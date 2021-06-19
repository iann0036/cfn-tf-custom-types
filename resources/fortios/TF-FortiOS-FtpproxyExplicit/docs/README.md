# TF::FortiOS::FtpproxyExplicit

Configure explicit FTP proxy settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FtpproxyExplicit",
    "Properties" : {
        "<a href="#incomingip" title="IncomingIp">IncomingIp</a>" : <i>String</i>,
        "<a href="#incomingport" title="IncomingPort">IncomingPort</a>" : <i>String</i>,
        "<a href="#outgoingip" title="OutgoingIp">OutgoingIp</a>" : <i>String</i>,
        "<a href="#secdefaultaction" title="SecDefaultAction">SecDefaultAction</a>" : <i>String</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>String</i>,
        "<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>" : <i>String</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#ssldhbits" title="SslDhBits">SslDhBits</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FtpproxyExplicit
Properties:
    <a href="#incomingip" title="IncomingIp">IncomingIp</a>: <i>String</i>
    <a href="#incomingport" title="IncomingPort">IncomingPort</a>: <i>String</i>
    <a href="#outgoingip" title="OutgoingIp">OutgoingIp</a>: <i>String</i>
    <a href="#secdefaultaction" title="SecDefaultAction">SecDefaultAction</a>: <i>String</i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>String</i>
    <a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>: <i>String</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#ssldhbits" title="SslDhBits">SslDhBits</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### IncomingIp

Accept incoming FTP requests from this IP address. An interface must have this IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingPort

Accept incoming FTP requests on one or more ports.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingIp

Outgoing FTP requests will leave from this IP address. An interface must have this IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecDefaultAction

Accept or deny explicit FTP proxy sessions when no FTP proxy firewall policy exists. Valid values: `accept`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

Enable/disable the explicit FTPS proxy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAlgorithm

Relative strength of encryption algorithms accepted in negotiation. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

Name of certificate for SSL connections to this server (default = "Fortinet_CA_SSL").

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslDhBits

Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation (default = 2048). Valid values: `768`, `1024`, `1536`, `2048`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable the explicit FTP proxy. Valid values: `enable`, `disable`.

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

