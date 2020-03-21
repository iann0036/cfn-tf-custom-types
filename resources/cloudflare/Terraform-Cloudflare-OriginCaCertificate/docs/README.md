# Terraform::Cloudflare::OriginCaCertificate

CloudFormation equivalent of cloudflare_origin_ca_certificate

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::OriginCaCertificate",
    "Properties" : {
        "<a href="#csr" title="Csr">Csr</a>" : <i>String</i>,
        "<a href="#hostnames" title="Hostnames">Hostnames</a>" : <i>[ String, ... ]</i>,
        "<a href="#requesttype" title="RequestType">RequestType</a>" : <i>String</i>,
        "<a href="#requestedvalidity" title="RequestedValidity">RequestedValidity</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::OriginCaCertificate
Properties:
    <a href="#csr" title="Csr">Csr</a>: <i>String</i>
    <a href="#hostnames" title="Hostnames">Hostnames</a>: <i>
      - String</i>
    <a href="#requesttype" title="RequestType">RequestType</a>: <i>String</i>
    <a href="#requestedvalidity" title="RequestedValidity">RequestedValidity</a>: <i>Double</i>
</pre>

## Properties

#### Csr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostnames

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedValidity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Certificate

Returns the <code>Certificate</code> value.

#### ExpiresOn

Returns the <code>ExpiresOn</code> value.

