# TF::Okta::SamlIdpSigningKey

CloudFormation equivalent of okta_saml_idp_signing_key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::SamlIdpSigningKey",
    "Properties" : {
        "<a href="#x5c" title="X5c">X5c</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::SamlIdpSigningKey
Properties:
    <a href="#x5c" title="X5c">X5c</a>: <i>
      - String</i>
</pre>

## Properties

#### X5c

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Created

Returns the <code>Created</code> value.

#### ExpiresAt

Returns the <code>ExpiresAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### Kid

Returns the <code>Kid</code> value.

#### Kty

Returns the <code>Kty</code> value.

#### Use

Returns the <code>Use</code> value.

#### X5tS256

Returns the <code>X5tS256</code> value.

