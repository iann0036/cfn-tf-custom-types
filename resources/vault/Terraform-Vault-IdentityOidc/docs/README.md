# Terraform::Vault::IdentityOidc

Configure the [Identity Tokens Backend](https://www.vaultproject.io/docs/secrets/identity/index.html#identity-tokens).

The Identity secrets engine is the identity management solution for Vault. It internally maintains
the clients who are recognized by Vault.

~> **NOTE:** Each Vault server may only have one Identity Tokens Backend configuration. Multiple configurations of the resource against the same Vault server will cause a perpetual difference.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::IdentityOidc",
    "Properties" : {
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::IdentityOidc
Properties:
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
</pre>

## Properties

#### Issuer

Issuer URL to be used in the iss claim of the token. If not set, Vault's
`api_addr` will be used. The issuer is a case sensitive URL using the https scheme that contains
scheme, host, and optionally, port number and path components, but no query or fragment
components.

_Required_: No

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

