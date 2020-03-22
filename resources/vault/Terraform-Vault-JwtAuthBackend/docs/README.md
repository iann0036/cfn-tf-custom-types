# Terraform::Vault::JwtAuthBackend

Provides a resource for managing an
[JWT auth backend within Vault](https://www.vaultproject.io/docs/auth/jwt.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::JwtAuthBackend",
    "Properties" : {
        "<a href="#boundissuer" title="BoundIssuer">BoundIssuer</a>" : <i>String</i>,
        "<a href="#defaultrole" title="DefaultRole">DefaultRole</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#jwkscapem" title="JwksCaPem">JwksCaPem</a>" : <i>String</i>,
        "<a href="#jwksurl" title="JwksUrl">JwksUrl</a>" : <i>String</i>,
        "<a href="#jwtsupportedalgs" title="JwtSupportedAlgs">JwtSupportedAlgs</a>" : <i>[ String, ... ]</i>,
        "<a href="#jwtvalidationpubkeys" title="JwtValidationPubkeys">JwtValidationPubkeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#oidcclientid" title="OidcClientId">OidcClientId</a>" : <i>String</i>,
        "<a href="#oidcclientsecret" title="OidcClientSecret">OidcClientSecret</a>" : <i>String</i>,
        "<a href="#oidcdiscoverycapem" title="OidcDiscoveryCaPem">OidcDiscoveryCaPem</a>" : <i>String</i>,
        "<a href="#oidcdiscoveryurl" title="OidcDiscoveryUrl">OidcDiscoveryUrl</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#tune" title="Tune">Tune</a>" : <i>[ <a href="tune.md">Tune</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::JwtAuthBackend
Properties:
    <a href="#boundissuer" title="BoundIssuer">BoundIssuer</a>: <i>String</i>
    <a href="#defaultrole" title="DefaultRole">DefaultRole</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#jwkscapem" title="JwksCaPem">JwksCaPem</a>: <i>String</i>
    <a href="#jwksurl" title="JwksUrl">JwksUrl</a>: <i>String</i>
    <a href="#jwtsupportedalgs" title="JwtSupportedAlgs">JwtSupportedAlgs</a>: <i>
      - String</i>
    <a href="#jwtvalidationpubkeys" title="JwtValidationPubkeys">JwtValidationPubkeys</a>: <i>
      - String</i>
    <a href="#oidcclientid" title="OidcClientId">OidcClientId</a>: <i>String</i>
    <a href="#oidcclientsecret" title="OidcClientSecret">OidcClientSecret</a>: <i>String</i>
    <a href="#oidcdiscoverycapem" title="OidcDiscoveryCaPem">OidcDiscoveryCaPem</a>: <i>String</i>
    <a href="#oidcdiscoveryurl" title="OidcDiscoveryUrl">OidcDiscoveryUrl</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#tune" title="Tune">Tune</a>: <i>
      - <a href="tune.md">Tune</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### BoundIssuer

The value against which to match the iss claim in a JWT.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRole

The default role to use if none is provided during login.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the auth backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwksCaPem

The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwksUrl

JWKS URL to use to authenticate signatures. Cannot be used with "oidc_discovery_url" or "jwt_validation_pubkeys".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtSupportedAlgs

A list of supported signing algorithms. Vault 1.1.0 defaults to [RS256] but future or past versions of Vault may differ.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtValidationPubkeys

A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used in combination with `oidc_discovery_url`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcClientId

Client ID used for OIDC backends.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcClientSecret

Client Secret used for OIDC backends.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcDiscoveryCaPem

The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcDiscoveryUrl

The OIDC Discovery URL, without any .well-known component (base path). Cannot be used in combination with `jwt_validation_pubkeys`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path to mount the JWT/OIDC auth backend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tune

_Required_: No

_Type_: List of <a href="tune.md">Tune</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of auth backend. Should be one of `jwt` or `oidc`. Default - `jwt`.

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

#### Accessor

Returns the <code>Accessor</code> value.

#### Id

Returns the <code>Id</code> value.

