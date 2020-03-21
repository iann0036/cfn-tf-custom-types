# Terraform::Fastly::ServiceV1 Backend

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#autoloadbalance" title="AutoLoadbalance">AutoLoadbalance</a>" : <i>Boolean</i>,
    "<a href="#betweenbytestimeout" title="BetweenBytesTimeout">BetweenBytesTimeout</a>" : <i>Double</i>,
    "<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>" : <i>Double</i>,
    "<a href="#errorthreshold" title="ErrorThreshold">ErrorThreshold</a>" : <i>Double</i>,
    "<a href="#firstbytetimeout" title="FirstByteTimeout">FirstByteTimeout</a>" : <i>Double</i>,
    "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>String</i>,
    "<a href="#maxconn" title="MaxConn">MaxConn</a>" : <i>Double</i>,
    "<a href="#maxtlsversion" title="MaxTlsVersion">MaxTlsVersion</a>" : <i>String</i>,
    "<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#overridehost" title="OverrideHost">OverrideHost</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#requestcondition" title="RequestCondition">RequestCondition</a>" : <i>String</i>,
    "<a href="#shield" title="Shield">Shield</a>" : <i>String</i>,
    "<a href="#sslcacert" title="SslCaCert">SslCaCert</a>" : <i>String</i>,
    "<a href="#sslcerthostname" title="SslCertHostname">SslCertHostname</a>" : <i>String</i>,
    "<a href="#sslcheckcert" title="SslCheckCert">SslCheckCert</a>" : <i>Boolean</i>,
    "<a href="#sslciphers" title="SslCiphers">SslCiphers</a>" : <i>String</i>,
    "<a href="#sslclientcert" title="SslClientCert">SslClientCert</a>" : <i>String</i>,
    "<a href="#sslclientkey" title="SslClientKey">SslClientKey</a>" : <i>String</i>,
    "<a href="#sslhostname" title="SslHostname">SslHostname</a>" : <i>String</i>,
    "<a href="#sslsnihostname" title="SslSniHostname">SslSniHostname</a>" : <i>String</i>,
    "<a href="#usessl" title="UseSsl">UseSsl</a>" : <i>Boolean</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#autoloadbalance" title="AutoLoadbalance">AutoLoadbalance</a>: <i>Boolean</i>
<a href="#betweenbytestimeout" title="BetweenBytesTimeout">BetweenBytesTimeout</a>: <i>Double</i>
<a href="#connecttimeout" title="ConnectTimeout">ConnectTimeout</a>: <i>Double</i>
<a href="#errorthreshold" title="ErrorThreshold">ErrorThreshold</a>: <i>Double</i>
<a href="#firstbytetimeout" title="FirstByteTimeout">FirstByteTimeout</a>: <i>Double</i>
<a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>String</i>
<a href="#maxconn" title="MaxConn">MaxConn</a>: <i>Double</i>
<a href="#maxtlsversion" title="MaxTlsVersion">MaxTlsVersion</a>: <i>String</i>
<a href="#mintlsversion" title="MinTlsVersion">MinTlsVersion</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#overridehost" title="OverrideHost">OverrideHost</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#requestcondition" title="RequestCondition">RequestCondition</a>: <i>String</i>
<a href="#shield" title="Shield">Shield</a>: <i>String</i>
<a href="#sslcacert" title="SslCaCert">SslCaCert</a>: <i>String</i>
<a href="#sslcerthostname" title="SslCertHostname">SslCertHostname</a>: <i>String</i>
<a href="#sslcheckcert" title="SslCheckCert">SslCheckCert</a>: <i>Boolean</i>
<a href="#sslciphers" title="SslCiphers">SslCiphers</a>: <i>String</i>
<a href="#sslclientcert" title="SslClientCert">SslClientCert</a>: <i>String</i>
<a href="#sslclientkey" title="SslClientKey">SslClientKey</a>: <i>String</i>
<a href="#sslhostname" title="SslHostname">SslHostname</a>: <i>String</i>
<a href="#sslsnihostname" title="SslSniHostname">SslSniHostname</a>: <i>String</i>
<a href="#usessl" title="UseSsl">UseSsl</a>: <i>Boolean</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Address

An IPv4, hostname, or IPv6 address for the Backend.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoLoadbalance

Denotes if this Backend should be
included in the pool of backends that requests are load balanced against.
Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BetweenBytesTimeout

How long to wait between bytes in milliseconds. Default `10000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeout

How long to wait for a timeout in milliseconds.
Default `1000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorThreshold

Number of errors to allow before the Backend is marked as down. Default `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstByteTimeout

How long to wait for the first bytes in milliseconds. Default `15000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

Name of a defined `healthcheck` to assign to this backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConn

Maximum number of connections for this Backend.
Default `200`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTlsVersion

Maximum allowed TLS version on SSL connections to this backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

Minimum allowed TLS version on SSL connections to this backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The unique name for the condition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideHost

The hostname to override the Host header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port number on which the Backend responds. Default `80`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestCondition

Name of already defined `condition`, which if met, will select this backend during a request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shield

The POP of the shield designated to reduce inbound load.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCaCert

CA certificate attached to origin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertHostname

Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCheckCert

Be strict about checking SSL certs. Default `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCiphers

Comma separated list of OpenSSL Ciphers to try when negotiating to the backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCert

Client certificate attached to origin. Used when connecting to the backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientKey

Client key attached to origin. Used when connecting to the backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHostname

Used for both SNI during the TLS handshake and to validate the cert.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSniHostname

Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSsl

Whether or not to use SSL to reach the backend. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The [portion of traffic](https://docs.fastly.com/guides/performance-tuning/load-balancing-configuration.html#how-weight-affects-load-balancing) to send to this Backend. Each Backend receives `weight / total` of the traffic. Default `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

