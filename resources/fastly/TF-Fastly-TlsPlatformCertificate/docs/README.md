# TF::Fastly::TlsPlatformCertificate

Uploads a TLS certificate to the Fastly Platform TLS service.

-> Each TLS certificate **must** have its corresponding private key uploaded _prior_ to uploading the certificate. This
can be achieved in Terraform using [`depends_on`](https://www.terraform.io/docs/configuration/meta-arguments/depends_on.html)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::TlsPlatformCertificate",
    "Properties" : {
        "<a href="#allowuntrustedroot" title="AllowUntrustedRoot">AllowUntrustedRoot</a>" : <i>Boolean</i>,
        "<a href="#certificatebody" title="CertificateBody">CertificateBody</a>" : <i>String</i>,
        "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
        "<a href="#intermediatesblob" title="IntermediatesBlob">IntermediatesBlob</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::TlsPlatformCertificate
Properties:
    <a href="#allowuntrustedroot" title="AllowUntrustedRoot">AllowUntrustedRoot</a>: <i>Boolean</i>
    <a href="#certificatebody" title="CertificateBody">CertificateBody</a>: <i>String</i>
    <a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
    <a href="#intermediatesblob" title="IntermediatesBlob">IntermediatesBlob</a>: <i>String</i>
</pre>

## Properties

#### AllowUntrustedRoot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateBody

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntermediatesBlob

_Required_: Yes

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

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Domains

Returns the <code>Domains</code> value.

#### Id

Returns the <code>Id</code> value.

#### NotAfter

Returns the <code>NotAfter</code> value.

#### NotBefore

Returns the <code>NotBefore</code> value.

#### Replace

Returns the <code>Replace</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

