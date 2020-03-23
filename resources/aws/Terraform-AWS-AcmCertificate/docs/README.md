# Terraform::AWS::AcmCertificate

The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.

It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a [`aws_acm_certificate_validation`](acm_certificate_validation.html) resource for this.

Most commonly, this resource is used to together with [`aws_route53_record`](route53_record.html) and
[`aws_acm_certificate_validation`](acm_certificate_validation.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

Domain validation through email is also supported but should be avoided as it requires a manual step outside
of Terraform.

It's recommended to specify `create_before_destroy = true` in a [lifecycle][1] block to replace a certificate
which is currently in use (eg, by [`aws_lb_listener`](lb_listener.html)).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AcmCertificate",
    "Properties" : {
        "<a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>" : <i>String</i>,
        "<a href="#certificatebody" title="CertificateBody">CertificateBody</a>" : <i>String</i>,
        "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AcmCertificate
Properties:
    <a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>: <i>String</i>
    <a href="#certificatebody" title="CertificateBody">CertificateBody</a>: <i>String</i>
    <a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
</pre>

## Properties

#### CertificateAuthorityArn

ARN of an ACMPCA
* `subject_alternative_names` - (Optional) A list of domains that should be SANs in the issued certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateBody

The certificate's PEM-formatted public key
* `certificate_chain` - (Optional) The certificate's PEM-formatted chain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateChain

The certificate's PEM-formatted chain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

A domain name for which the certificate should be issued
* `certificate_authority_arn` - (Required) ARN of an ACMPCA
* `subject_alternative_names` - (Optional) A list of domains that should be SANs in the issued certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

The certificate's PEM-formatted private key
* `certificate_body` - (Required) The certificate's PEM-formatted public key
* `certificate_chain` - (Optional) The certificate's PEM-formatted chain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectAlternativeNames

A list of domains that should be SANs in the issued certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationMethod

Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.
* `options` - (Optional) Configuration block used to set certificate options. Detailed below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="options.md">Options</a>

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

#### DomainValidationOptions

Returns the <code>DomainValidationOptions</code> value.

#### Id

Returns the <code>Id</code> value.

#### ValidationEmails

Returns the <code>ValidationEmails</code> value.

