# TF::AWS::AcmCertificate

The ACM certificate resource allows requesting and management of certificates
from the Amazon Certificate Manager.

It deals with requesting certificates and managing their attributes and life-cycle.
This resource does not deal with validation of a certificate but can provide inputs
for other resources implementing the validation. It does not wait for a certificate to be issued.
Use a [`aws_acm_certificate_validation`](acm_certificate_validation.html) resource for this.

Most commonly, this resource is used together with [`aws_route53_record`](route53_record.html) and
[`aws_acm_certificate_validation`](acm_certificate_validation.html) to request a DNS validated certificate,
deploy the required validation records and wait for validation to complete.

Domain validation through email is also supported but should be avoided as it requires a manual step outside
of Terraform.

It's recommended to specify `create_before_destroy = true` in a [lifecycle][1] block to replace a certificate
which is currently in use ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AcmCertificate",
    "Properties" : {
        "<a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>" : <i>String</i>,
        "<a href="#certificatebody" title="CertificateBody">CertificateBody</a>" : <i>String</i>,
        "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="optionsdefinition.md">OptionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AcmCertificate
Properties:
    <a href="#certificateauthorityarn" title="CertificateAuthorityArn">CertificateAuthorityArn</a>: <i>String</i>
    <a href="#certificatebody" title="CertificateBody">CertificateBody</a>: <i>String</i>
    <a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#subjectalternativenames" title="SubjectAlternativeNames">SubjectAlternativeNames</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#validationmethod" title="ValidationMethod">ValidationMethod</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="optionsdefinition.md">OptionsDefinition</a></i>
</pre>

## Properties

#### CertificateAuthorityArn

ARN of an ACM PCA
* `subject_alternative_names` - (Optional) Set of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) or use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html) to trigger recreation.

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
* `certificate_authority_arn` - (Required) ARN of an ACM PCA
* `subject_alternative_names` - (Optional) Set of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) or use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html) to trigger recreation.

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

Set of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) or use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html) to trigger recreation.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationMethod

Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into Terraform.
* `options` - (Optional) Configuration block used to set certificate options. Detailed below.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="optionsdefinition.md">OptionsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

#### ValidationEmails

Returns the <code>ValidationEmails</code> value.

