# TF::AWS::AcmpcaCertificate

Provides a resource to issue a certificate using AWS Certificate Manager Private Certificate Authority (ACM PCA).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AcmpcaCertificate",
    "Properties" : {
        "<a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>" : <i>String</i>,
        "<a href="#certificatesigningrequest" title="CertificateSigningRequest">CertificateSigningRequest</a>" : <i>String</i>,
        "<a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>" : <i>String</i>,
        "<a href="#templatearn" title="TemplateArn">TemplateArn</a>" : <i>String</i>,
        "<a href="#validity" title="Validity">Validity</a>" : <i>[ <a href="validitydefinition.md">ValidityDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AcmpcaCertificate
Properties:
    <a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>: <i>String</i>
    <a href="#certificatesigningrequest" title="CertificateSigningRequest">CertificateSigningRequest</a>: <i>String</i>
    <a href="#signingalgorithm" title="SigningAlgorithm">SigningAlgorithm</a>: <i>String</i>
    <a href="#templatearn" title="TemplateArn">TemplateArn</a>: <i>String</i>
    <a href="#validity" title="Validity">Validity</a>: <i>
      - <a href="validitydefinition.md">ValidityDefinition</a></i>
</pre>

## Properties

#### CertificateAuthorityArn

Amazon Resource Name (ARN) of the certificate authority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSigningRequest

Certificate Signing Request in PEM format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SigningAlgorithm

Algorithm to use to sign certificate requests. Valid values: `SHA256WITHRSA`, `SHA256WITHECDSA`, `SHA384WITHRSA`, `SHA384WITHECDSA`, `SHA512WITHRSA`, `SHA512WITHECDSA`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateArn

The template to use when issuing a certificate. See [ACM PCA Documentation](https://docs.aws.amazon.com/acm-pca/latest/userguide/UsingTemplates.html) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Validity

_Required_: No

_Type_: List of <a href="validitydefinition.md">ValidityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Certificate

Returns the <code>Certificate</code> value.

#### CertificateChain

Returns the <code>CertificateChain</code> value.

#### Id

Returns the <code>Id</code> value.

