# TF::Fastly::TlsActivation

Enables TLS on a domain using a specified custom TLS certificate.

~> **Note:** The Fastly service must be provisioned _prior_ to enabling TLS on it. This can be achieved in Terraform using [`depends_on`](https://www.terraform.io/docs/configuration/meta-arguments/depends_on.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::TlsActivation",
    "Properties" : {
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#configurationid" title="ConfigurationId">ConfigurationId</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::TlsActivation
Properties:
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#configurationid" title="ConfigurationId">ConfigurationId</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
</pre>

## Properties

#### CertificateId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

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

#### Id

Returns the <code>Id</code> value.

