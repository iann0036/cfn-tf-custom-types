# Terraform::AWS::AcmpcaCertificateAuthority

CloudFormation equivalent of aws_acmpca_certificate_authority

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AcmpcaCertificateAuthority",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#permanentdeletiontimeindays" title="PermanentDeletionTimeInDays">PermanentDeletionTimeInDays</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#certificateauthorityconfiguration" title="CertificateAuthorityConfiguration">CertificateAuthorityConfiguration</a>" : <i>[ <a href="certificateauthorityconfiguration.md">CertificateAuthorityConfiguration</a>, ... ]</i>,
        "<a href="#revocationconfiguration" title="RevocationConfiguration">RevocationConfiguration</a>" : <i>[ <a href="revocationconfiguration.md">RevocationConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#subject" title="Subject">Subject</a>" : <i>[ <a href="subject.md">Subject</a>, ... ]</i>,
        "<a href="#crlconfiguration" title="CrlConfiguration">CrlConfiguration</a>" : <i>[ <a href="crlconfiguration.md">CrlConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AcmpcaCertificateAuthority
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#permanentdeletiontimeindays" title="PermanentDeletionTimeInDays">PermanentDeletionTimeInDays</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#certificateauthorityconfiguration" title="CertificateAuthorityConfiguration">CertificateAuthorityConfiguration</a>: <i>
      - <a href="certificateauthorityconfiguration.md">CertificateAuthorityConfiguration</a></i>
    <a href="#revocationconfiguration" title="RevocationConfiguration">RevocationConfiguration</a>: <i>
      - <a href="revocationconfiguration.md">RevocationConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#subject" title="Subject">Subject</a>: <i>
      - <a href="subject.md">Subject</a></i>
    <a href="#crlconfiguration" title="CrlConfiguration">CrlConfiguration</a>: <i>
      - <a href="crlconfiguration.md">CrlConfiguration</a></i>
</pre>

## Properties

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermanentDeletionTimeInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateAuthorityConfiguration

_Required_: No

_Type_: List of <a href="certificateauthorityconfiguration.md">CertificateAuthorityConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevocationConfiguration

_Required_: No

_Type_: List of <a href="revocationconfiguration.md">RevocationConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subject

_Required_: No

_Type_: List of <a href="subject.md">Subject</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlConfiguration

_Required_: No

_Type_: List of <a href="crlconfiguration.md">CrlConfiguration</a>

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

#### CertificateSigningRequest

Returns the <code>CertificateSigningRequest</code> value.

#### NotAfter

Returns the <code>NotAfter</code> value.

#### NotBefore

Returns the <code>NotBefore</code> value.

#### Serial

Returns the <code>Serial</code> value.

#### Status

Returns the <code>Status</code> value.

