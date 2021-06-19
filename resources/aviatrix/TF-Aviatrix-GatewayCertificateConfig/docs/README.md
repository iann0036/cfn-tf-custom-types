# TF::Aviatrix::GatewayCertificateConfig

The **aviatrix_gateway_certificate_config** resource allows the management of Aviatrix [gateway certificate](https://docs.aviatrix.com/HowTos/controller_certificate.html#gateway-certificate-management) configuration. Available as of provider version R2.18.1+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::GatewayCertificateConfig",
    "Properties" : {
        "<a href="#cacertificate" title="CaCertificate">CaCertificate</a>" : <i>String</i>,
        "<a href="#caprivatekey" title="CaPrivateKey">CaPrivateKey</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::GatewayCertificateConfig
Properties:
    <a href="#cacertificate" title="CaCertificate">CaCertificate</a>: <i>String</i>
    <a href="#caprivatekey" title="CaPrivateKey">CaPrivateKey</a>: <i>String</i>
</pre>

## Properties

#### CaCertificate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaPrivateKey

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

#### Id

Returns the <code>Id</code> value.

