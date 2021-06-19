# TF::AWS::AcmpcaCertificateAuthorityCertificate

Associates a certificate with an AWS Certificate Manager Private Certificate Authority (ACM PCA Certificate Authority). An ACM PCA Certificate Authority is unable to issue certificates until it has a certificate associated with it. A root level ACM PCA Certificate Authority is able to self-sign its own root certificate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AcmpcaCertificateAuthorityCertificate",
    "Properties" : {
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>" : <i>String</i>,
        "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AcmpcaCertificateAuthorityCertificate
Properties:
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>: <i>String</i>
    <a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
</pre>

## Properties

#### Certificate

The PEM-encoded certificate for the Certificate Authority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateAuthorityArn

Amazon Resource Name (ARN) of the Certificate Authority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateChain

The PEM-encoded certificate chain that includes any intermediate certificates and chains up to root CA. Required for subordinate Certificate Authorities. Not allowed for root Certificate Authorities.

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

#### Id

Returns the <code>Id</code> value.

