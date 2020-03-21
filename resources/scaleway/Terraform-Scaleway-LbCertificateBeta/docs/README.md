# Terraform::Scaleway::LbCertificateBeta

CloudFormation equivalent of scaleway_lb_certificate_beta

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::LbCertificateBeta",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#lbid" title="LbId">LbId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>" : <i>[ <a href="customcertificate.md">CustomCertificate</a>, ... ]</i>,
        "<a href="#letsencrypt" title="Letsencrypt">Letsencrypt</a>" : <i>[ <a href="letsencrypt.md">Letsencrypt</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::LbCertificateBeta
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#lbid" title="LbId">LbId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>: <i>
      - <a href="customcertificate.md">CustomCertificate</a></i>
    <a href="#letsencrypt" title="Letsencrypt">Letsencrypt</a>: <i>
      - <a href="letsencrypt.md">Letsencrypt</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCertificate

_Required_: No

_Type_: List of <a href="customcertificate.md">CustomCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Letsencrypt

_Required_: No

_Type_: List of <a href="letsencrypt.md">Letsencrypt</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CommonName

Returns the <code>CommonName</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### NotValidAfter

Returns the <code>NotValidAfter</code> value.

#### NotValidBefore

Returns the <code>NotValidBefore</code> value.

#### Status

Returns the <code>Status</code> value.

#### SubjectAlternativeName

Returns the <code>SubjectAlternativeName</code> value.

