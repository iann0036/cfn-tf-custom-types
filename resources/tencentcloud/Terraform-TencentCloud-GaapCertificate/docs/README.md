# Terraform::TencentCloud::GaapCertificate

Provides a resource to create a certificate of GAAP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::GaapCertificate",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::GaapCertificate
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Content

Content of the certificate, and URL encoding. When the certificate is basic authentication, use the `user:xxx password:xxx` format, where the password is encrypted with `htpasswd` or `openssl`; When the certificate is `CA` or `SSL`, the format is `pem`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Key of the `SSL` certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the certificate, the available values include `BASIC`, `CLIENT`, `SERVER`, `REALSERVER` and `PROXY`; `BASIC` means basic certificate; `CLIENT` means client CA certificate; `SERVER` means server SSL certificate; `REALSERVER` means realserver CA certificate; `PROXY` means proxy SSL certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BeginTime

Returns the <code>BeginTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### EndTime

Returns the <code>EndTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IssuerCn

Returns the <code>IssuerCn</code> value.

#### SubjectCn

Returns the <code>SubjectCn</code> value.

