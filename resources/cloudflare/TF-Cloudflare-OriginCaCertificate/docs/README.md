# TF::Cloudflare::OriginCaCertificate

Provides a Cloudflare Origin CA certificate used to protect traffic to your origin without involving a third party Certificate Authority.

**This resource requires you use your Origin CA Key as the [`api_user_service_key`](../index.html#api_user_service_key), in conjunction with an `api_token` or `email` and `api_key`.**

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::OriginCaCertificate",
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
Type: TF::Cloudflare::OriginCaCertificate
Properties:
    <a href="#csr" title="Csr">Csr</a>: <i>String</i>
    <a href="#hostnames" title="Hostnames">Hostnames</a>: <i>
      - String</i>
    <a href="#requesttype" title="RequestType">RequestType</a>: <i>String</i>
    <a href="#requestedvalidity" title="RequestedValidity">RequestedValidity</a>: <i>Double</i>
</pre>

## Properties

#### Csr

The Certificate Signing Request. Must be newline-encoded.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostnames

An array of hostnames or wildcard names bound to the certificate.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestType

The signature type desired on the certificate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestedValidity

The number of days for which the certificate should be valid.

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

#### Id

Returns the <code>Id</code> value.

