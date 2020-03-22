# Terraform::Vault::IdentityOidcKey

Creates an Identity OIDC Named Key for Vault Identity secrets engine which is used by a role
to sign
[identity tokens](https://www.vaultproject.io/docs/secrets/identity/index.html#identity-tokens).

The Identity secrets engine is the identity management solution for Vault. It internally
maintains the clients who are recognized by Vault.

Use this with [`vault_identity_oidc_key`](identity_oidc_key.html)
and [`vault_identity_oidc_key_allowed_client_id`](identity_oidc_key_allowed_client_id.html)
to configure a Role to generate Identity Tokens.

~> **NOTE on `allowed_client_ids`:** Terraform currently
provides both a standalone [Allowed Client ID](identity_oidc_key_allowed_client_id.html) (a single
Client ID), and a [OIDC Named Key](identity_oidc_key.html) with a inline list of Allowed Client IDs.
At this time you cannot use an OIDC Named Key inline list of Allowed Client IDs
in conjunction with any Allowed Client ID resources. Doing so will cause
a conflict of the list of Allowed Client IDs for the named Key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::IdentityOidcKey",
    "Properties" : {
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#allowedclientids" title="AllowedClientIds">AllowedClientIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>" : <i>Double</i>,
        "<a href="#verificationttl" title="VerificationTtl">VerificationTtl</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::IdentityOidcKey
Properties:
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#allowedclientids" title="AllowedClientIds">AllowedClientIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rotationperiod" title="RotationPeriod">RotationPeriod</a>: <i>Double</i>
    <a href="#verificationttl" title="VerificationTtl">VerificationTtl</a>: <i>Double</i>
</pre>

## Properties

#### Algorithm

Signing algorithm to use. Signing algorithm to use.
Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedClientIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the OIDC Key to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationPeriod

How often to generate a new signing key in number of seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerificationTtl

"Controls how long the public portion of a signing key will be
available for verification after being rotated in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

