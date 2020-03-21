# Terraform::BIGIP::LtmProfileServerSsl

CloudFormation equivalent of bigip_ltm_profile_server_ssl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileServerSsl",
    "Properties" : {
        "<a href="#alerttimeout" title="AlertTimeout">AlertTimeout</a>" : <i>String</i>,
        "<a href="#authenticate" title="Authenticate">Authenticate</a>" : <i>String</i>,
        "<a href="#authenticatedepth" title="AuthenticateDepth">AuthenticateDepth</a>" : <i>Double</i>,
        "<a href="#cafile" title="CaFile">CaFile</a>" : <i>String</i>,
        "<a href="#cachesize" title="CacheSize">CacheSize</a>" : <i>Double</i>,
        "<a href="#cachetimeout" title="CacheTimeout">CacheTimeout</a>" : <i>Double</i>,
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#chain" title="Chain">Chain</a>" : <i>String</i>,
        "<a href="#ciphers" title="Ciphers">Ciphers</a>" : <i>String</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#expirecertresponsecontrol" title="ExpireCertResponseControl">ExpireCertResponseControl</a>" : <i>String</i>,
        "<a href="#fullpath" title="FullPath">FullPath</a>" : <i>String</i>,
        "<a href="#generation" title="Generation">Generation</a>" : <i>Double</i>,
        "<a href="#genericalert" title="GenericAlert">GenericAlert</a>" : <i>String</i>,
        "<a href="#handshaketimeout" title="HandshakeTimeout">HandshakeTimeout</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#modsslmethods" title="ModSslMethods">ModSslMethods</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#peercertmode" title="PeerCertMode">PeerCertMode</a>" : <i>String</i>,
        "<a href="#proxyssl" title="ProxySsl">ProxySsl</a>" : <i>String</i>,
        "<a href="#renegotiateperiod" title="RenegotiatePeriod">RenegotiatePeriod</a>" : <i>String</i>,
        "<a href="#renegotiatesize" title="RenegotiateSize">RenegotiateSize</a>" : <i>String</i>,
        "<a href="#renegotiation" title="Renegotiation">Renegotiation</a>" : <i>String</i>,
        "<a href="#retaincertificate" title="RetainCertificate">RetainCertificate</a>" : <i>String</i>,
        "<a href="#securerenegotiation" title="SecureRenegotiation">SecureRenegotiation</a>" : <i>String</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#sessionmirroring" title="SessionMirroring">SessionMirroring</a>" : <i>String</i>,
        "<a href="#sessionticket" title="SessionTicket">SessionTicket</a>" : <i>String</i>,
        "<a href="#snidefault" title="SniDefault">SniDefault</a>" : <i>String</i>,
        "<a href="#snirequire" title="SniRequire">SniRequire</a>" : <i>String</i>,
        "<a href="#sslforwardproxy" title="SslForwardProxy">SslForwardProxy</a>" : <i>String</i>,
        "<a href="#sslforwardproxybypass" title="SslForwardProxyBypass">SslForwardProxyBypass</a>" : <i>String</i>,
        "<a href="#sslsignhash" title="SslSignHash">SslSignHash</a>" : <i>String</i>,
        "<a href="#strictresume" title="StrictResume">StrictResume</a>" : <i>String</i>,
        "<a href="#tmoptions" title="TmOptions">TmOptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#uncleanshutdown" title="UncleanShutdown">UncleanShutdown</a>" : <i>String</i>,
        "<a href="#untrustedcertresponsecontrol" title="UntrustedCertResponseControl">UntrustedCertResponseControl</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileServerSsl
Properties:
    <a href="#alerttimeout" title="AlertTimeout">AlertTimeout</a>: <i>String</i>
    <a href="#authenticate" title="Authenticate">Authenticate</a>: <i>String</i>
    <a href="#authenticatedepth" title="AuthenticateDepth">AuthenticateDepth</a>: <i>Double</i>
    <a href="#cafile" title="CaFile">CaFile</a>: <i>String</i>
    <a href="#cachesize" title="CacheSize">CacheSize</a>: <i>Double</i>
    <a href="#cachetimeout" title="CacheTimeout">CacheTimeout</a>: <i>Double</i>
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#chain" title="Chain">Chain</a>: <i>String</i>
    <a href="#ciphers" title="Ciphers">Ciphers</a>: <i>String</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#expirecertresponsecontrol" title="ExpireCertResponseControl">ExpireCertResponseControl</a>: <i>String</i>
    <a href="#fullpath" title="FullPath">FullPath</a>: <i>String</i>
    <a href="#generation" title="Generation">Generation</a>: <i>Double</i>
    <a href="#genericalert" title="GenericAlert">GenericAlert</a>: <i>String</i>
    <a href="#handshaketimeout" title="HandshakeTimeout">HandshakeTimeout</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#modsslmethods" title="ModSslMethods">ModSslMethods</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#peercertmode" title="PeerCertMode">PeerCertMode</a>: <i>String</i>
    <a href="#proxyssl" title="ProxySsl">ProxySsl</a>: <i>String</i>
    <a href="#renegotiateperiod" title="RenegotiatePeriod">RenegotiatePeriod</a>: <i>String</i>
    <a href="#renegotiatesize" title="RenegotiateSize">RenegotiateSize</a>: <i>String</i>
    <a href="#renegotiation" title="Renegotiation">Renegotiation</a>: <i>String</i>
    <a href="#retaincertificate" title="RetainCertificate">RetainCertificate</a>: <i>String</i>
    <a href="#securerenegotiation" title="SecureRenegotiation">SecureRenegotiation</a>: <i>String</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#sessionmirroring" title="SessionMirroring">SessionMirroring</a>: <i>String</i>
    <a href="#sessionticket" title="SessionTicket">SessionTicket</a>: <i>String</i>
    <a href="#snidefault" title="SniDefault">SniDefault</a>: <i>String</i>
    <a href="#snirequire" title="SniRequire">SniRequire</a>: <i>String</i>
    <a href="#sslforwardproxy" title="SslForwardProxy">SslForwardProxy</a>: <i>String</i>
    <a href="#sslforwardproxybypass" title="SslForwardProxyBypass">SslForwardProxyBypass</a>: <i>String</i>
    <a href="#sslsignhash" title="SslSignHash">SslSignHash</a>: <i>String</i>
    <a href="#strictresume" title="StrictResume">StrictResume</a>: <i>String</i>
    <a href="#tmoptions" title="TmOptions">TmOptions</a>: <i>
      - String</i>
    <a href="#uncleanshutdown" title="UncleanShutdown">UncleanShutdown</a>: <i>String</i>
    <a href="#untrustedcertresponsecontrol" title="UntrustedCertResponseControl">UntrustedCertResponseControl</a>: <i>String</i>
</pre>

## Properties

#### AlertTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authenticate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateDepth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireCertResponseControl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Generation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenericAlert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandshakeTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModSslMethods

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCertMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxySsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenegotiatePeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenegotiateSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Renegotiation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureRenegotiation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionMirroring

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTicket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniDefault

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniRequire

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslForwardProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslForwardProxyBypass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSignHash

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictResume

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TmOptions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UncleanShutdown

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UntrustedCertResponseControl

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

