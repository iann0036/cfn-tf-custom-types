# TF::AzureRM::MediaContentKeyPolicy TokenRestrictionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#audience" title="Audience">Audience</a>" : <i>String</i>,
    "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
    "<a href="#openidconnectdiscoverydocument" title="OpenIdConnectDiscoveryDocument">OpenIdConnectDiscoveryDocument</a>" : <i>String</i>,
    "<a href="#primaryrsatokenkeyexponent" title="PrimaryRsaTokenKeyExponent">PrimaryRsaTokenKeyExponent</a>" : <i>String</i>,
    "<a href="#primaryrsatokenkeymodulus" title="PrimaryRsaTokenKeyModulus">PrimaryRsaTokenKeyModulus</a>" : <i>String</i>,
    "<a href="#primarysymmetrictokenkey" title="PrimarySymmetricTokenKey">PrimarySymmetricTokenKey</a>" : <i>String</i>,
    "<a href="#primaryx509tokenkeyraw" title="PrimaryX509TokenKeyRaw">PrimaryX509TokenKeyRaw</a>" : <i>String</i>,
    "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
    "<a href="#requiredclaim" title="RequiredClaim">RequiredClaim</a>" : <i>[ <a href="requiredclaimdefinition.md">RequiredClaimDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#audience" title="Audience">Audience</a>: <i>String</i>
<a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
<a href="#openidconnectdiscoverydocument" title="OpenIdConnectDiscoveryDocument">OpenIdConnectDiscoveryDocument</a>: <i>String</i>
<a href="#primaryrsatokenkeyexponent" title="PrimaryRsaTokenKeyExponent">PrimaryRsaTokenKeyExponent</a>: <i>String</i>
<a href="#primaryrsatokenkeymodulus" title="PrimaryRsaTokenKeyModulus">PrimaryRsaTokenKeyModulus</a>: <i>String</i>
<a href="#primarysymmetrictokenkey" title="PrimarySymmetricTokenKey">PrimarySymmetricTokenKey</a>: <i>String</i>
<a href="#primaryx509tokenkeyraw" title="PrimaryX509TokenKeyRaw">PrimaryX509TokenKeyRaw</a>: <i>String</i>
<a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
<a href="#requiredclaim" title="RequiredClaim">RequiredClaim</a>: <i>
      - <a href="requiredclaimdefinition.md">RequiredClaimDefinition</a></i>
</pre>

## Properties

#### Audience

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenIdConnectDiscoveryDocument

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryRsaTokenKeyExponent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryRsaTokenKeyModulus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimarySymmetricTokenKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryX509TokenKeyRaw

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredClaim

_Required_: No

_Type_: List of <a href="requiredclaimdefinition.md">RequiredClaimDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

