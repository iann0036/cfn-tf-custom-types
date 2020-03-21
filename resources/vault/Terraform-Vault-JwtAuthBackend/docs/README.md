# Terraform::Vault::JwtAuthBackend

CloudFormation equivalent of vault_jwt_auth_backend

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::JwtAuthBackend",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#accessor" title="Accessor">Accessor</a>" : <i>String</i>,
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
        "<a href="#tune" title="Tune">Tune</a>" : <i>[ &lt;a href=&#34;tune.md&#34;&gt;Tune&lt;/a&gt;, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::JwtAuthBackend
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#accessor" title="Accessor">Accessor</a>: <i>String</i>
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
      - &lt;a href=&#34;tune.md&#34;&gt;Tune&lt;/a&gt;</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Accessor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIssuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwksCaPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwksUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtSupportedAlgs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JwtValidationPubkeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcClientSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcDiscoveryCaPem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OidcDiscoveryUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tune

_Required_: No

_Type_: List of &lt;a href=&#34;tune.md&#34;&gt;Tune&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

Returns the &lt;code&gt;Accessor&lt;/code&gt; value.

