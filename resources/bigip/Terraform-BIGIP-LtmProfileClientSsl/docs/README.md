# Terraform::BIGIP::LtmProfileClientSsl

`bigip_ltm_profile_client_ssl` Manages client SSL profiles on a BIG-IP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileClientSsl",
    "Properties" : {
        "<a href="#alerttimeout" title="AlertTimeout">AlertTimeout</a>" : <i>String</i>,
        "<a href="#allownonssl" title="AllowNonSsl">AllowNonSsl</a>" : <i>String</i>,
        "<a href="#authenticate" title="Authenticate">Authenticate</a>" : <i>String</i>,
        "<a href="#authenticatedepth" title="AuthenticateDepth">AuthenticateDepth</a>" : <i>Double</i>,
        "<a href="#cafile" title="CaFile">CaFile</a>" : <i>String</i>,
        "<a href="#cachesize" title="CacheSize">CacheSize</a>" : <i>Double</i>,
        "<a href="#cachetimeout" title="CacheTimeout">CacheTimeout</a>" : <i>Double</i>,
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#certextensionincludes" title="CertExtensionIncludes">CertExtensionIncludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#certlifespan" title="CertLifeSpan">CertLifeSpan</a>" : <i>Double</i>,
        "<a href="#certlookupbyipaddrport" title="CertLookupByIpaddrPort">CertLookupByIpaddrPort</a>" : <i>String</i>,
        "<a href="#chain" title="Chain">Chain</a>" : <i>String</i>,
        "<a href="#ciphers" title="Ciphers">Ciphers</a>" : <i>String</i>,
        "<a href="#clientcertca" title="ClientCertCa">ClientCertCa</a>" : <i>String</i>,
        "<a href="#crlfile" title="CrlFile">CrlFile</a>" : <i>String</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#forwardproxybypassdefaultaction" title="ForwardProxyBypassDefaultAction">ForwardProxyBypassDefaultAction</a>" : <i>String</i>,
        "<a href="#fullpath" title="FullPath">FullPath</a>" : <i>String</i>,
        "<a href="#generation" title="Generation">Generation</a>" : <i>Double</i>,
        "<a href="#genericalert" title="GenericAlert">GenericAlert</a>" : <i>String</i>,
        "<a href="#handshaketimeout" title="HandshakeTimeout">HandshakeTimeout</a>" : <i>String</i>,
        "<a href="#inheritcertkeychain" title="InheritCertKeychain">InheritCertKeychain</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#modsslmethods" title="ModSslMethods">ModSslMethods</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#passphrase" title="Passphrase">Passphrase</a>" : <i>String</i>,
        "<a href="#peercertmode" title="PeerCertMode">PeerCertMode</a>" : <i>String</i>,
        "<a href="#proxycacert" title="ProxyCaCert">ProxyCaCert</a>" : <i>String</i>,
        "<a href="#proxycakey" title="ProxyCaKey">ProxyCaKey</a>" : <i>String</i>,
        "<a href="#proxycapassphrase" title="ProxyCaPassphrase">ProxyCaPassphrase</a>" : <i>String</i>,
        "<a href="#proxyssl" title="ProxySsl">ProxySsl</a>" : <i>String</i>,
        "<a href="#proxysslpassthrough" title="ProxySslPassthrough">ProxySslPassthrough</a>" : <i>String</i>,
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
        "<a href="#certkeychain" title="CertKeyChain">CertKeyChain</a>" : <i>[ <a href="certkeychain.md">CertKeyChain</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileClientSsl
Properties:
    <a href="#alerttimeout" title="AlertTimeout">AlertTimeout</a>: <i>String</i>
    <a href="#allownonssl" title="AllowNonSsl">AllowNonSsl</a>: <i>String</i>
    <a href="#authenticate" title="Authenticate">Authenticate</a>: <i>String</i>
    <a href="#authenticatedepth" title="AuthenticateDepth">AuthenticateDepth</a>: <i>Double</i>
    <a href="#cafile" title="CaFile">CaFile</a>: <i>String</i>
    <a href="#cachesize" title="CacheSize">CacheSize</a>: <i>Double</i>
    <a href="#cachetimeout" title="CacheTimeout">CacheTimeout</a>: <i>Double</i>
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#certextensionincludes" title="CertExtensionIncludes">CertExtensionIncludes</a>: <i>
      - String</i>
    <a href="#certlifespan" title="CertLifeSpan">CertLifeSpan</a>: <i>Double</i>
    <a href="#certlookupbyipaddrport" title="CertLookupByIpaddrPort">CertLookupByIpaddrPort</a>: <i>String</i>
    <a href="#chain" title="Chain">Chain</a>: <i>String</i>
    <a href="#ciphers" title="Ciphers">Ciphers</a>: <i>String</i>
    <a href="#clientcertca" title="ClientCertCa">ClientCertCa</a>: <i>String</i>
    <a href="#crlfile" title="CrlFile">CrlFile</a>: <i>String</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#forwardproxybypassdefaultaction" title="ForwardProxyBypassDefaultAction">ForwardProxyBypassDefaultAction</a>: <i>String</i>
    <a href="#fullpath" title="FullPath">FullPath</a>: <i>String</i>
    <a href="#generation" title="Generation">Generation</a>: <i>Double</i>
    <a href="#genericalert" title="GenericAlert">GenericAlert</a>: <i>String</i>
    <a href="#handshaketimeout" title="HandshakeTimeout">HandshakeTimeout</a>: <i>String</i>
    <a href="#inheritcertkeychain" title="InheritCertKeychain">InheritCertKeychain</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#modsslmethods" title="ModSslMethods">ModSslMethods</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#passphrase" title="Passphrase">Passphrase</a>: <i>String</i>
    <a href="#peercertmode" title="PeerCertMode">PeerCertMode</a>: <i>String</i>
    <a href="#proxycacert" title="ProxyCaCert">ProxyCaCert</a>: <i>String</i>
    <a href="#proxycakey" title="ProxyCaKey">ProxyCaKey</a>: <i>String</i>
    <a href="#proxycapassphrase" title="ProxyCaPassphrase">ProxyCaPassphrase</a>: <i>String</i>
    <a href="#proxyssl" title="ProxySsl">ProxySsl</a>: <i>String</i>
    <a href="#proxysslpassthrough" title="ProxySslPassthrough">ProxySslPassthrough</a>: <i>String</i>
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
    <a href="#certkeychain" title="CertKeyChain">CertKeyChain</a>: <i>
      - <a href="certkeychain.md">CertKeyChain</a></i>
</pre>

## Properties

#### AlertTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowNonSsl

Enables or disables acceptance of non-SSL connections, When creating a new profile, the setting is provided by the parent profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authenticate

Specifies the frequency of client authentication for an SSL session.When `once`,specifies that the system authenticates the client once for an SSL session.
When `always`, specifies that the system authenticates the client once for an SSL session and also upon reuse of that session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateDepth

Specifies the maximum number of certificates to be traversed in a client certificate chain.

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

Specifies a cert name for use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertExtensionIncludes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertLifeSpan

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertLookupByIpaddrPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Chain

Contains a certificate chain that is relevant to the certificate and key mentioned earlier.This key is optional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphers

Specifies the list of ciphers that the system supports. When creating a new profile, the default cipher list is provided by the parent profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertCa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

The parent template of this monitor template. Once this value has been set, it cannot be changed. By default, this value is the `clientssl` parent on the `Common` partition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyBypassDefaultAction

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

#### InheritCertKeychain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Contains a key name.

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

Device partition to manage resources on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCertMode

Specifies the way the system handles client certificates.When ignore, specifies that the system ignores certificates from client systems.When require, specifies that the system requires a client to present a valid certificate.When request, specifies that the system requests a valid certificate from a client but always authenticate the client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCaKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCaPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxySsl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxySslPassthrough

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

Enables or disables SSL renegotiation.When creating a new profile, the setting is provided by the parent profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainCertificate

When `true`, client certificate is retained in SSL session.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureRenegotiation

Specifies the method of secure renegotiations for SSL connections. When creating a new profile, the setting is provided by the parent profile.
When `request` is set the system request secure renegotation of SSL connections.
`require` is a default setting and when set the system permits initial SSL handshakes from clients but terminates renegotiations from unpatched clients.
The `require-strict` setting the system requires strict renegotiation of SSL connections. In this mode the system refuses connections to insecure servers, and terminates existing SSL connections to insecure servers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

Specifies the fully qualified DNS hostname of the server used in Server Name Indication communications. When creating a new profile, the setting is provided by the parent profile.The server name can also be a wildcard string containing the asterisk `*` character.

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

Indicates that the system uses this profile as the default SSL profile when there is no match to the server name, or when the client provides no SNI extension support.When creating a new profile, the setting is provided by the parent profile.
There can be only one SSL profile with this setting enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniRequire

Requires that the network peers also provide SNI support, this setting only takes effect when `sni_default` is set to `true`.When creating a new profile, the setting is provided by the parent profile.

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

Enables or disables the resumption of SSL sessions after an unclean shutdown.When creating a new profile, the setting is provided by the parent profile.

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

#### CertKeyChain

_Required_: No

_Type_: List of <a href="certkeychain.md">CertKeyChain</a>

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

