# Terraform::Fastly::ServiceV1 Syslog

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#formatversion" title="FormatVersion">FormatVersion</a>" : <i>Double</i>,
    "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#tlscacert" title="TlsCaCert">TlsCaCert</a>" : <i>String</i>,
    "<a href="#tlsclientcert" title="TlsClientCert">TlsClientCert</a>" : <i>String</i>,
    "<a href="#tlsclientkey" title="TlsClientKey">TlsClientKey</a>" : <i>String</i>,
    "<a href="#tlshostname" title="TlsHostname">TlsHostname</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    "<a href="#usetls" title="UseTls">UseTls</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#formatversion" title="FormatVersion">FormatVersion</a>: <i>Double</i>
<a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#tlscacert" title="TlsCaCert">TlsCaCert</a>: <i>String</i>
<a href="#tlsclientcert" title="TlsClientCert">TlsClientCert</a>: <i>String</i>
<a href="#tlsclientkey" title="TlsClientKey">TlsClientKey</a>: <i>String</i>
<a href="#tlshostname" title="TlsHostname">TlsHostname</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
<a href="#usetls" title="UseTls">UseTls</a>: <i>Boolean</i>
</pre>

## Properties

#### Address

A hostname or IPv4 address of the Syslog endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (%h %l %u %t %r %>s).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatVersion

The version of the custom logging format used for the configured endpoint. Can be either 1 (the default, version 1 log format) or 2 (the version 2 log format).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

How the message should be formatted; one of: `classic`, `loggly`, `logplex` or `blank`.  Default `classic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this Syslog endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port associated with the address where the Syslog endpoint can be accessed. Default `514`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals,
see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsCaCert

A secure certificate to authenticate the server with. Must be in PEM format. You can provide this certificate via an environment variable, `FASTLY_SYSLOG_CA_CERT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsClientCert

The client certificate used to make authenticated requests. Must be in PEM format. You can provide this certificate via an environment variable, `FASTLY_SYSLOG_CLIENT_CERT`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsClientKey

The client private key used to make authenticated requests. Must be in PEM format. You can provide this key via an environment variable, `FASTLY_SYSLOG_CLIENT_KEY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsHostname

Used during the TLS handshake to validate the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

Whether to prepend each message with a specific token.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTls

Whether to use TLS for secure logging. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

