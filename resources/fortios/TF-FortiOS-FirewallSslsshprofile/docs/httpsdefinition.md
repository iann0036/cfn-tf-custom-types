# TF::FortiOS::FirewallSslsshprofile HttpsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certvalidationfailure" title="CertValidationFailure">CertValidationFailure</a>" : <i>String</i>,
    "<a href="#certvalidationtimeout" title="CertValidationTimeout">CertValidationTimeout</a>" : <i>String</i>,
    "<a href="#clientcertrequest" title="ClientCertRequest">ClientCertRequest</a>" : <i>String</i>,
    "<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>" : <i>String</i>,
    "<a href="#expiredservercert" title="ExpiredServerCert">ExpiredServerCert</a>" : <i>String</i>,
    "<a href="#invalidservercert" title="InvalidServerCert">InvalidServerCert</a>" : <i>String</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>String</i>,
    "<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>" : <i>String</i>,
    "<a href="#revokedservercert" title="RevokedServerCert">RevokedServerCert</a>" : <i>String</i>,
    "<a href="#sniservercertcheck" title="SniServerCertCheck">SniServerCertCheck</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#unsupportedssl" title="UnsupportedSsl">UnsupportedSsl</a>" : <i>String</i>,
    "<a href="#unsupportedsslcipher" title="UnsupportedSslCipher">UnsupportedSslCipher</a>" : <i>String</i>,
    "<a href="#unsupportedsslnegotiation" title="UnsupportedSslNegotiation">UnsupportedSslNegotiation</a>" : <i>String</i>,
    "<a href="#untrustedservercert" title="UntrustedServerCert">UntrustedServerCert</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certvalidationfailure" title="CertValidationFailure">CertValidationFailure</a>: <i>String</i>
<a href="#certvalidationtimeout" title="CertValidationTimeout">CertValidationTimeout</a>: <i>String</i>
<a href="#clientcertrequest" title="ClientCertRequest">ClientCertRequest</a>: <i>String</i>
<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>: <i>String</i>
<a href="#expiredservercert" title="ExpiredServerCert">ExpiredServerCert</a>: <i>String</i>
<a href="#invalidservercert" title="InvalidServerCert">InvalidServerCert</a>: <i>String</i>
<a href="#ports" title="Ports">Ports</a>: <i>String</i>
<a href="#proxyaftertcphandshake" title="ProxyAfterTcpHandshake">ProxyAfterTcpHandshake</a>: <i>String</i>
<a href="#revokedservercert" title="RevokedServerCert">RevokedServerCert</a>: <i>String</i>
<a href="#sniservercertcheck" title="SniServerCertCheck">SniServerCertCheck</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#unsupportedssl" title="UnsupportedSsl">UnsupportedSsl</a>: <i>String</i>
<a href="#unsupportedsslcipher" title="UnsupportedSslCipher">UnsupportedSslCipher</a>: <i>String</i>
<a href="#unsupportedsslnegotiation" title="UnsupportedSslNegotiation">UnsupportedSslNegotiation</a>: <i>String</i>
<a href="#untrustedservercert" title="UntrustedServerCert">UntrustedServerCert</a>: <i>String</i>
</pre>

## Properties

#### CertValidationFailure

Action based on certificate validation failure. Valid values: `allow`, `block`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertValidationTimeout

Action based on certificate validation timeout. Valid values: `allow`, `block`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertRequest

Action based on client certificate request. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificate

Action based on received client certificate. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiredServerCert

Action based on server certificate is expired. Valid values: `allow`, `block`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvalidServerCert

Allow or block the invalid SSL session server certificate. Valid values: `allow`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Ports to use for scanning (1 - 65535, default = 443).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyAfterTcpHandshake

Proxy traffic after the TCP 3-way handshake has been established (not before). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokedServerCert

Action based on server certificate is revoked. Valid values: `allow`, `block`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniServerCertCheck

Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. Valid values: `enable`, `strict`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Configure protocol inspection status. Valid values: `disable`, `certificate-inspection`, `deep-inspection`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsupportedSsl

Action based on the SSL encryption used being unsupported. Valid values: `bypass`, `inspect`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsupportedSslCipher

Action based on the SSL cipher used being unsupported. Valid values: `allow`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnsupportedSslNegotiation

Action based on the SSL negotiation used being unsupported. Valid values: `allow`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntrustedServerCert

Allow, ignore, or block the untrusted SSL session server certificate. Valid values: `allow`, `block`, `ignore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

