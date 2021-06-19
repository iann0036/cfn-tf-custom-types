# TF::Brightbox::LoadBalancer

Provides a Brightbox Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Brightbox::LoadBalancer",
    "Properties" : {
        "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
        "<a href="#certificatepem" title="CertificatePem">CertificatePem</a>" : <i>String</i>,
        "<a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>" : <i>String</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ String, ... ]</i>,
        "<a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>" : <i>Boolean</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#sslminimumversion" title="SslMinimumVersion">SslMinimumVersion</a>" : <i>String</i>,
        "<a href="#sslv3" title="Sslv3">Sslv3</a>" : <i>Boolean</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheckdefinition.md">HealthcheckDefinition</a>, ... ]</i>,
        "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="listenerdefinition.md">ListenerDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Brightbox::LoadBalancer
Properties:
    <a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
    <a href="#certificatepem" title="CertificatePem">CertificatePem</a>: <i>String</i>
    <a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>: <i>String</i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - String</i>
    <a href="#httpsredirect" title="HttpsRedirect">HttpsRedirect</a>: <i>Boolean</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#sslminimumversion" title="SslMinimumVersion">SslMinimumVersion</a>: <i>String</i>
    <a href="#sslv3" title="Sslv3">Sslv3</a>: <i>Boolean</i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheckdefinition.md">HealthcheckDefinition</a></i>
    <a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="listenerdefinition.md">ListenerDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BufferSize

Buffer size in bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePem

A X509 SSL certificate in PEM format. Must be included along with `certificate_key`. If intermediate certificates are required they should be concatenated after the main certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePrivateKey

The RSA private key used to sign the certificate in PEM format. Must be included along with `certificate_pem`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

An array of domain names to attempt to register with ACME. Conflicts with `certificate_pem` and `certificate_private_key`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsRedirect

Redirect any requests on port 80 automatically to port 443.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

Set to true to stop the load balancer from being deleted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A label assigned to the Load Balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

An array of Server IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

Method of load balancing to use, either `least-connections` or `round-robin`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinimumVersion

The minimum TLS/SSL version for the load balancer to accept. Supports `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3` and `SSLv3`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslv3

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheckdefinition.md">HealthcheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of <a href="listenerdefinition.md">ListenerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

