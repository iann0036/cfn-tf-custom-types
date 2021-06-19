# TF::FortiOS::FirewallSslsshprofile

Configure SSL/SSH protocol options.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallSslsshprofile",
    "Properties" : {
        "<a href="#allowlist" title="Allowlist">Allowlist</a>" : <i>String</i>,
        "<a href="#blockblacklistedcertificates" title="BlockBlacklistedCertificates">BlockBlacklistedCertificates</a>" : <i>String</i>,
        "<a href="#blockblocklistedcertificates" title="BlockBlocklistedCertificates">BlockBlocklistedCertificates</a>" : <i>String</i>,
        "<a href="#caname" title="Caname">Caname</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#mapioverhttps" title="MapiOverHttps">MapiOverHttps</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rpcoverhttps" title="RpcOverHttps">RpcOverHttps</a>" : <i>String</i>,
        "<a href="#servercert" title="ServerCert">ServerCert</a>" : <i>String</i>,
        "<a href="#servercertmode" title="ServerCertMode">ServerCertMode</a>" : <i>String</i>,
        "<a href="#sslanomalieslog" title="SslAnomaliesLog">SslAnomaliesLog</a>" : <i>String</i>,
        "<a href="#sslexemptionslog" title="SslExemptionsLog">SslExemptionsLog</a>" : <i>String</i>,
        "<a href="#sslnegotiationlog" title="SslNegotiationLog">SslNegotiationLog</a>" : <i>String</i>,
        "<a href="#supportedalpn" title="SupportedAlpn">SupportedAlpn</a>" : <i>String</i>,
        "<a href="#untrustedcaname" title="UntrustedCaname">UntrustedCaname</a>" : <i>String</i>,
        "<a href="#usesslserver" title="UseSslServer">UseSslServer</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>String</i>,
        "<a href="#ftps" title="Ftps">Ftps</a>" : <i>[ <a href="ftpsdefinition.md">FtpsDefinition</a>, ... ]</i>,
        "<a href="#https" title="Https">Https</a>" : <i>[ <a href="httpsdefinition.md">HttpsDefinition</a>, ... ]</i>,
        "<a href="#imaps" title="Imaps">Imaps</a>" : <i>[ <a href="imapsdefinition.md">ImapsDefinition</a>, ... ]</i>,
        "<a href="#pop3s" title="Pop3s">Pop3s</a>" : <i>[ <a href="pop3sdefinition.md">Pop3sDefinition</a>, ... ]</i>,
        "<a href="#smtps" title="Smtps">Smtps</a>" : <i>[ <a href="smtpsdefinition.md">SmtpsDefinition</a>, ... ]</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>[ <a href="sshdefinition.md">SshDefinition</a>, ... ]</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>[ <a href="ssldefinition.md">SslDefinition</a>, ... ]</i>,
        "<a href="#sslexempt" title="SslExempt">SslExempt</a>" : <i>[ <a href="sslexemptdefinition.md">SslExemptDefinition</a>, ... ]</i>,
        "<a href="#sslserver" title="SslServer">SslServer</a>" : <i>[ <a href="sslserverdefinition.md">SslServerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallSslsshprofile
Properties:
    <a href="#allowlist" title="Allowlist">Allowlist</a>: <i>String</i>
    <a href="#blockblacklistedcertificates" title="BlockBlacklistedCertificates">BlockBlacklistedCertificates</a>: <i>String</i>
    <a href="#blockblocklistedcertificates" title="BlockBlocklistedCertificates">BlockBlocklistedCertificates</a>: <i>String</i>
    <a href="#caname" title="Caname">Caname</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#mapioverhttps" title="MapiOverHttps">MapiOverHttps</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rpcoverhttps" title="RpcOverHttps">RpcOverHttps</a>: <i>String</i>
    <a href="#servercert" title="ServerCert">ServerCert</a>: <i>String</i>
    <a href="#servercertmode" title="ServerCertMode">ServerCertMode</a>: <i>String</i>
    <a href="#sslanomalieslog" title="SslAnomaliesLog">SslAnomaliesLog</a>: <i>String</i>
    <a href="#sslexemptionslog" title="SslExemptionsLog">SslExemptionsLog</a>: <i>String</i>
    <a href="#sslnegotiationlog" title="SslNegotiationLog">SslNegotiationLog</a>: <i>String</i>
    <a href="#supportedalpn" title="SupportedAlpn">SupportedAlpn</a>: <i>String</i>
    <a href="#untrustedcaname" title="UntrustedCaname">UntrustedCaname</a>: <i>String</i>
    <a href="#usesslserver" title="UseSslServer">UseSslServer</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#whitelist" title="Whitelist">Whitelist</a>: <i>String</i>
    <a href="#ftps" title="Ftps">Ftps</a>: <i>
      - <a href="ftpsdefinition.md">FtpsDefinition</a></i>
    <a href="#https" title="Https">Https</a>: <i>
      - <a href="httpsdefinition.md">HttpsDefinition</a></i>
    <a href="#imaps" title="Imaps">Imaps</a>: <i>
      - <a href="imapsdefinition.md">ImapsDefinition</a></i>
    <a href="#pop3s" title="Pop3s">Pop3s</a>: <i>
      - <a href="pop3sdefinition.md">Pop3sDefinition</a></i>
    <a href="#smtps" title="Smtps">Smtps</a>: <i>
      - <a href="smtpsdefinition.md">SmtpsDefinition</a></i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>
      - <a href="sshdefinition.md">SshDefinition</a></i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>
      - <a href="ssldefinition.md">SslDefinition</a></i>
    <a href="#sslexempt" title="SslExempt">SslExempt</a>: <i>
      - <a href="sslexemptdefinition.md">SslExemptDefinition</a></i>
    <a href="#sslserver" title="SslServer">SslServer</a>: <i>
      - <a href="sslserverdefinition.md">SslServerDefinition</a></i>
</pre>

## Properties

#### Allowlist

Enable/disable exempting servers by FortiGuard allowlist. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockBlacklistedCertificates

Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blacklist. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockBlocklistedCertificates

Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Caname

CA certificate used by SSL Inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapiOverHttps

Enable/disable inspection of MAPI over HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpcOverHttps

Enable/disable inspection of RPC over HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCert

Certificate used by SSL Inspection to replace server certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertMode

Re-sign or replace the server's certificate. Valid values: `re-sign`, `replace`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAnomaliesLog

Enable/disable logging SSL anomalies. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslExemptionsLog

Enable/disable logging SSL exemptions. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslNegotiationLog

Enable/disable logging SSL negotiation. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportedAlpn

Configure ALPN option. Valid values: `http1-1`, `http2`, `all`, `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntrustedCaname

Untrusted CA certificate used by SSL Inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSslServer

Enable/disable the use of SSL server table for SSL offloading. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

Enable/disable exempting servers by FortiGuard whitelist. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftps

_Required_: No

_Type_: List of <a href="ftpsdefinition.md">FtpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Https

_Required_: No

_Type_: List of <a href="httpsdefinition.md">HttpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imaps

_Required_: No

_Type_: List of <a href="imapsdefinition.md">ImapsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3s

_Required_: No

_Type_: List of <a href="pop3sdefinition.md">Pop3sDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smtps

_Required_: No

_Type_: List of <a href="smtpsdefinition.md">SmtpsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssh

_Required_: No

_Type_: List of <a href="sshdefinition.md">SshDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

_Required_: No

_Type_: List of <a href="ssldefinition.md">SslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslExempt

_Required_: No

_Type_: List of <a href="sslexemptdefinition.md">SslExemptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServer

_Required_: No

_Type_: List of <a href="sslserverdefinition.md">SslServerDefinition</a>

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

