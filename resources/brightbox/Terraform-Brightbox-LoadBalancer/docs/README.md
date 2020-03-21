# Terraform::Brightbox::LoadBalancer

Provides a Brightbox Load Balancer resource. This can be used to create,
modify, and delete Load Balancers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Brightbox::LoadBalancer",
    "Properties" : {
        "<a href="#buffersize" title="BufferSize">BufferSize</a>" : <i>Double</i>,
        "<a href="#certificatepem" title="CertificatePem">CertificatePem</a>" : <i>String</i>,
        "<a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#sslv3" title="Sslv3">Sslv3</a>" : <i>Boolean</i>,
        "<a href="#healthcheck" title="Healthcheck">Healthcheck</a>" : <i>[ <a href="healthcheck.md">Healthcheck</a>, ... ]</i>,
        "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="listener.md">Listener</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Brightbox::LoadBalancer
Properties:
    <a href="#buffersize" title="BufferSize">BufferSize</a>: <i>Double</i>
    <a href="#certificatepem" title="CertificatePem">CertificatePem</a>: <i>String</i>
    <a href="#certificateprivatekey" title="CertificatePrivateKey">CertificatePrivateKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#sslv3" title="Sslv3">Sslv3</a>: <i>Boolean</i>
    <a href="#healthcheck" title="Healthcheck">Healthcheck</a>: <i>
      - <a href="healthcheck.md">Healthcheck</a></i>
    <a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="listener.md">Listener</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
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

#### Sslv3

Allow SSL v3 to be used. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Healthcheck

_Required_: No

_Type_: List of <a href="healthcheck.md">Healthcheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of <a href="listener.md">Listener</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Locked

Returns the <code>Locked</code> value.

#### Status

Returns the <code>Status</code> value.

