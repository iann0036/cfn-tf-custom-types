# TF::FortiOS::FirewallSslsshprofile SslServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ftpsclientcertrequest" title="FtpsClientCertRequest">FtpsClientCertRequest</a>" : <i>String</i>,
    "<a href="#ftpsclientcertificate" title="FtpsClientCertificate">FtpsClientCertificate</a>" : <i>String</i>,
    "<a href="#httpsclientcertrequest" title="HttpsClientCertRequest">HttpsClientCertRequest</a>" : <i>String</i>,
    "<a href="#httpsclientcertificate" title="HttpsClientCertificate">HttpsClientCertificate</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#imapsclientcertrequest" title="ImapsClientCertRequest">ImapsClientCertRequest</a>" : <i>String</i>,
    "<a href="#imapsclientcertificate" title="ImapsClientCertificate">ImapsClientCertificate</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#pop3sclientcertrequest" title="Pop3sClientCertRequest">Pop3sClientCertRequest</a>" : <i>String</i>,
    "<a href="#pop3sclientcertificate" title="Pop3sClientCertificate">Pop3sClientCertificate</a>" : <i>String</i>,
    "<a href="#smtpsclientcertrequest" title="SmtpsClientCertRequest">SmtpsClientCertRequest</a>" : <i>String</i>,
    "<a href="#smtpsclientcertificate" title="SmtpsClientCertificate">SmtpsClientCertificate</a>" : <i>String</i>,
    "<a href="#sslotherclientcertrequest" title="SslOtherClientCertRequest">SslOtherClientCertRequest</a>" : <i>String</i>,
    "<a href="#sslotherclientcertificate" title="SslOtherClientCertificate">SslOtherClientCertificate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ftpsclientcertrequest" title="FtpsClientCertRequest">FtpsClientCertRequest</a>: <i>String</i>
<a href="#ftpsclientcertificate" title="FtpsClientCertificate">FtpsClientCertificate</a>: <i>String</i>
<a href="#httpsclientcertrequest" title="HttpsClientCertRequest">HttpsClientCertRequest</a>: <i>String</i>
<a href="#httpsclientcertificate" title="HttpsClientCertificate">HttpsClientCertificate</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#imapsclientcertrequest" title="ImapsClientCertRequest">ImapsClientCertRequest</a>: <i>String</i>
<a href="#imapsclientcertificate" title="ImapsClientCertificate">ImapsClientCertificate</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#pop3sclientcertrequest" title="Pop3sClientCertRequest">Pop3sClientCertRequest</a>: <i>String</i>
<a href="#pop3sclientcertificate" title="Pop3sClientCertificate">Pop3sClientCertificate</a>: <i>String</i>
<a href="#smtpsclientcertrequest" title="SmtpsClientCertRequest">SmtpsClientCertRequest</a>: <i>String</i>
<a href="#smtpsclientcertificate" title="SmtpsClientCertificate">SmtpsClientCertificate</a>: <i>String</i>
<a href="#sslotherclientcertrequest" title="SslOtherClientCertRequest">SslOtherClientCertRequest</a>: <i>String</i>
<a href="#sslotherclientcertificate" title="SslOtherClientCertificate">SslOtherClientCertificate</a>: <i>String</i>
</pre>

## Properties

#### FtpsClientCertRequest

Action based on client certificate request during the FTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtpsClientCertificate

Action based on received client certificate during the FTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsClientCertRequest

Action based on client certificate request during the HTTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsClientCertificate

Action based on received client certificate during the HTTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

SSL server ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImapsClientCertRequest

Action based on client certificate request during the IMAPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImapsClientCertificate

Action based on received client certificate during the IMAPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IPv4 address of the SSL server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3sClientCertRequest

Action based on client certificate request during the POP3S handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3sClientCertificate

Action based on received client certificate during the POP3S handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpsClientCertRequest

Action based on client certificate request during the SMTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpsClientCertificate

Action based on received client certificate during the SMTPS handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslOtherClientCertRequest

Action based on client certificate request during an SSL protocol handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslOtherClientCertificate

Action based on received client certificate during an SSL protocol handshake. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

