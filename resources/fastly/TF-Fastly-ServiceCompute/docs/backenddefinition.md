# TF::Fastly::ServiceCompute BackendDefinition

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoLoadbalance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BetweenBytesTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstByteTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConn

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTlsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTlsVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideHost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shield

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCheckCert

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCiphers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSniHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

