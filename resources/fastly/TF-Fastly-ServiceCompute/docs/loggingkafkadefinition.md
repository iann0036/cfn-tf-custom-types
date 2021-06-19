# TF::Fastly::ServiceCompute LoggingKafkaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authmethod" title="AuthMethod">AuthMethod</a>" : <i>String</i>,
    "<a href="#brokers" title="Brokers">Brokers</a>" : <i>String</i>,
    "<a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#parselogkeyvals" title="ParseLogKeyvals">ParseLogKeyvals</a>" : <i>Boolean</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#requestmaxbytes" title="RequestMaxBytes">RequestMaxBytes</a>" : <i>Double</i>,
    "<a href="#requiredacks" title="RequiredAcks">RequiredAcks</a>" : <i>String</i>,
    "<a href="#tlscacert" title="TlsCaCert">TlsCaCert</a>" : <i>String</i>,
    "<a href="#tlsclientcert" title="TlsClientCert">TlsClientCert</a>" : <i>String</i>,
    "<a href="#tlsclientkey" title="TlsClientKey">TlsClientKey</a>" : <i>String</i>,
    "<a href="#tlshostname" title="TlsHostname">TlsHostname</a>" : <i>String</i>,
    "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>,
    "<a href="#usetls" title="UseTls">UseTls</a>" : <i>Boolean</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authmethod" title="AuthMethod">AuthMethod</a>: <i>String</i>
<a href="#brokers" title="Brokers">Brokers</a>: <i>String</i>
<a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#parselogkeyvals" title="ParseLogKeyvals">ParseLogKeyvals</a>: <i>Boolean</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#requestmaxbytes" title="RequestMaxBytes">RequestMaxBytes</a>: <i>Double</i>
<a href="#requiredacks" title="RequiredAcks">RequiredAcks</a>: <i>String</i>
<a href="#tlscacert" title="TlsCaCert">TlsCaCert</a>: <i>String</i>
<a href="#tlsclientcert" title="TlsClientCert">TlsClientCert</a>: <i>String</i>
<a href="#tlsclientkey" title="TlsClientKey">TlsClientKey</a>: <i>String</i>
<a href="#tlshostname" title="TlsHostname">TlsHostname</a>: <i>String</i>
<a href="#topic" title="Topic">Topic</a>: <i>String</i>
<a href="#usetls" title="UseTls">UseTls</a>: <i>Boolean</i>
<a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### AuthMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Brokers

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionCodec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParseLogKeyvals

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMaxBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredAcks

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsClientCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsClientKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

