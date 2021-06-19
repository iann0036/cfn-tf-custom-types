# TF::Thunder::SlbTemplateServerSsl

`thunder_slb_template_server_ssl` provides details about slb template server_ssl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateServerSsl",
    "Properties" : {
        "<a href="#alerttype" title="AlertType">AlertType</a>" : <i>String</i>,
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#certsharedstr" title="CertSharedStr">CertSharedStr</a>" : <i>String</i>,
        "<a href="#ciphertemplate" title="CipherTemplate">CipherTemplate</a>" : <i>String</i>,
        "<a href="#closenotify" title="CloseNotify">CloseNotify</a>" : <i>Double</i>,
        "<a href="#dgversion" title="Dgversion">Dgversion</a>" : <i>Double</i>,
        "<a href="#dhtype" title="DhType">DhType</a>" : <i>String</i>,
        "<a href="#enabletlsalertlogging" title="EnableTlsAlertLogging">EnableTlsAlertLogging</a>" : <i>Double</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>" : <i>Double</i>,
        "<a href="#handshakeloggingenable" title="HandshakeLoggingEnable">HandshakeLoggingEnable</a>" : <i>Double</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keysharedencrypted" title="KeySharedEncrypted">KeySharedEncrypted</a>" : <i>String</i>,
        "<a href="#keysharedpassphrase" title="KeySharedPassphrase">KeySharedPassphrase</a>" : <i>String</i>,
        "<a href="#keysharedstr" title="KeySharedStr">KeySharedStr</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ocspstapling" title="OcspStapling">OcspStapling</a>" : <i>Double</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#renegotiationdisable" title="RenegotiationDisable">RenegotiationDisable</a>" : <i>Double</i>,
        "<a href="#sessioncachesize" title="SessionCacheSize">SessionCacheSize</a>" : <i>Double</i>,
        "<a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>" : <i>Double</i>,
        "<a href="#sessionticketenable" title="SessionTicketEnable">SessionTicketEnable</a>" : <i>Double</i>,
        "<a href="#sharedpartitionciphertemplate" title="SharedPartitionCipherTemplate">SharedPartitionCipherTemplate</a>" : <i>Double</i>,
        "<a href="#sslilogging" title="SsliLogging">SsliLogging</a>" : <i>Double</i>,
        "<a href="#sslilogging" title="Sslilogging">Sslilogging</a>" : <i>String</i>,
        "<a href="#templateciphershared" title="TemplateCipherShared">TemplateCipherShared</a>" : <i>String</i>,
        "<a href="#useclientsni" title="UseClientSni">UseClientSni</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#cacerts" title="CaCerts">CaCerts</a>" : <i>[ <a href="cacertsdefinition.md">CaCertsDefinition</a>, ... ]</i>,
        "<a href="#cipherwithoutpriolist" title="CipherWithoutPrioList">CipherWithoutPrioList</a>" : <i>[ <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a>, ... ]</i>,
        "<a href="#crlcerts" title="CrlCerts">CrlCerts</a>" : <i>[ <a href="crlcertsdefinition.md">CrlCertsDefinition</a>, ... ]</i>,
        "<a href="#eclist" title="EcList">EcList</a>" : <i>[ <a href="eclistdefinition.md">EcListDefinition</a>, ... ]</i>,
        "<a href="#servercertificateerror" title="ServerCertificateError">ServerCertificateError</a>" : <i>[ <a href="servercertificateerrordefinition.md">ServerCertificateErrorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateServerSsl
Properties:
    <a href="#alerttype" title="AlertType">AlertType</a>: <i>String</i>
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#certsharedstr" title="CertSharedStr">CertSharedStr</a>: <i>String</i>
    <a href="#ciphertemplate" title="CipherTemplate">CipherTemplate</a>: <i>String</i>
    <a href="#closenotify" title="CloseNotify">CloseNotify</a>: <i>Double</i>
    <a href="#dgversion" title="Dgversion">Dgversion</a>: <i>Double</i>
    <a href="#dhtype" title="DhType">DhType</a>: <i>String</i>
    <a href="#enabletlsalertlogging" title="EnableTlsAlertLogging">EnableTlsAlertLogging</a>: <i>Double</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>: <i>Double</i>
    <a href="#handshakeloggingenable" title="HandshakeLoggingEnable">HandshakeLoggingEnable</a>: <i>Double</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keysharedencrypted" title="KeySharedEncrypted">KeySharedEncrypted</a>: <i>String</i>
    <a href="#keysharedpassphrase" title="KeySharedPassphrase">KeySharedPassphrase</a>: <i>String</i>
    <a href="#keysharedstr" title="KeySharedStr">KeySharedStr</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ocspstapling" title="OcspStapling">OcspStapling</a>: <i>Double</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#renegotiationdisable" title="RenegotiationDisable">RenegotiationDisable</a>: <i>Double</i>
    <a href="#sessioncachesize" title="SessionCacheSize">SessionCacheSize</a>: <i>Double</i>
    <a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>: <i>Double</i>
    <a href="#sessionticketenable" title="SessionTicketEnable">SessionTicketEnable</a>: <i>Double</i>
    <a href="#sharedpartitionciphertemplate" title="SharedPartitionCipherTemplate">SharedPartitionCipherTemplate</a>: <i>Double</i>
    <a href="#sslilogging" title="SsliLogging">SsliLogging</a>: <i>Double</i>
    <a href="#sslilogging" title="Sslilogging">Sslilogging</a>: <i>String</i>
    <a href="#templateciphershared" title="TemplateCipherShared">TemplateCipherShared</a>: <i>String</i>
    <a href="#useclientsni" title="UseClientSni">UseClientSni</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#cacerts" title="CaCerts">CaCerts</a>: <i>
      - <a href="cacertsdefinition.md">CaCertsDefinition</a></i>
    <a href="#cipherwithoutpriolist" title="CipherWithoutPrioList">CipherWithoutPrioList</a>: <i>
      - <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a></i>
    <a href="#crlcerts" title="CrlCerts">CrlCerts</a>: <i>
      - <a href="crlcertsdefinition.md">CrlCertsDefinition</a></i>
    <a href="#eclist" title="EcList">EcList</a>: <i>
      - <a href="eclistdefinition.md">EcListDefinition</a></i>
    <a href="#servercertificateerror" title="ServerCertificateError">ServerCertificateError</a>: <i>
      - <a href="servercertificateerrordefinition.md">ServerCertificateErrorDefinition</a></i>
</pre>

## Properties

#### AlertType

‘fatal’: Log fatal alerts;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cert

Specify Client certificate (Certificate Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertSharedStr

Certificate Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherTemplate

Cipher Template (Cipher Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloseNotify

Send close notification when terminate connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dgversion

Lower TLS/SSL version can be downgraded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhType

‘1024’: 1024; ‘1024-dsa’: 1024-dsa; ‘2048’: 2048;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTlsAlertLogging

Enable TLS alert logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyEnable

Enable SSL forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandshakeLoggingEnable

Enable SSL handshake logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Client private-key (Key Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedStr

Key Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server SSL Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspStapling

Enable ocsp-stapling support.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenegotiationDisable

Disable SSL renegotiation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheSize

Session Cache Size (Specify 0 to disable Session ID reuse.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheTimeout

Session Cache Timeout (Timeout value, in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTicketEnable

Enable server side session ticket support.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionCipherTemplate

Reference a cipher template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsliLogging

SSLi logging level, default is error logging only.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslilogging

‘disable’: Disable all logging; ‘all’: enable all logging(error, info);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCipherShared

Cipher Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseClientSni

use client SNI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

TLS/SSL version, default is the highest number supported (TLS/SSL version: 30-SSLv3.0, 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCerts

_Required_: No

_Type_: List of <a href="cacertsdefinition.md">CaCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherWithoutPrioList

_Required_: No

_Type_: List of <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlCerts

_Required_: No

_Type_: List of <a href="crlcertsdefinition.md">CrlCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcList

_Required_: No

_Type_: List of <a href="eclistdefinition.md">EcListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateError

_Required_: No

_Type_: List of <a href="servercertificateerrordefinition.md">ServerCertificateErrorDefinition</a>

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

