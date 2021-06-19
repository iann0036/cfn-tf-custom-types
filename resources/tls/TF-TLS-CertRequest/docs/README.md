# TF::TLS::CertRequest

Generates a *Certificate Signing Request* (CSR) in PEM format, which is the
typical format used to request a certificate from a certificate authority.

This resource is intended to be used in conjunction with a Terraform provider
for a particular certificate authority in order to provision a new certificate.
This is a *logical resource*, so it contributes only to the current Terraform
state and does not create any external managed resources.

~> **Compatibility Note** From Terraform 0.7.0 to 0.7.4 this resource was
converted to a data source, and the resource form of it was deprecated. This
turned out to be a design error since a cert request includes a random number
in the form of the signature nonce, and so the data source form of this
resource caused non-convergent configuration. The data source form is no longer
supported as of Terraform 0.7.5 and any users should return to using the
resource form.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TLS::CertRequest",
    "Properties" : {
        "<a href="#dnsnames" title="DnsNames">DnsNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#ipaddresses" title="IpAddresses">IpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
        "<a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>" : <i>String</i>,
        "<a href="#uris" title="Uris">Uris</a>" : <i>[ String, ... ]</i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="subjectdefinition.md">SubjectDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TLS::CertRequest
Properties:
    <a href="#dnsnames" title="DnsNames">DnsNames</a>: <i>
      - String</i>
    <a href="#ipaddresses" title="IpAddresses">IpAddresses</a>: <i>
      - String</i>
    <a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
    <a href="#privatekeypem" title="PrivateKeyPem">PrivateKeyPem</a>: <i>String</i>
    <a href="#uris" title="Uris">Uris</a>: <i>
      - String</i>
    <a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="subjectdefinition.md">SubjectDefinition</a></i>
</pre>

## Properties

#### DnsNames

List of DNS names for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddresses

List of IP addresses for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlgorithm

The name of the algorithm for the key provided
in `private_key_pem`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyPem

PEM-encoded private key data. This can be
read from a separate file using the ``file`` interpolation function. Only
an irreversable secure hash of the private key will be stored in the Terraform
state.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uris

List of URIs for which a certificate is being requested.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="subjectdefinition.md">SubjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertRequestPem

Returns the <code>CertRequestPem</code> value.

#### Id

Returns the <code>Id</code> value.

