# Terraform::AWS::CognitoIdentityPool

CloudFormation equivalent of aws_cognito_identity_pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoIdentityPool",
    "Properties" : {
        "<a href="#allowunauthenticatedidentities" title="AllowUnauthenticatedIdentities">AllowUnauthenticatedIdentities</a>" : <i>Boolean</i>,
        "<a href="#developerprovidername" title="DeveloperProviderName">DeveloperProviderName</a>" : <i>String</i>,
        "<a href="#identitypoolname" title="IdentityPoolName">IdentityPoolName</a>" : <i>String</i>,
        "<a href="#openidconnectproviderarns" title="OpenidConnectProviderArns">OpenidConnectProviderArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#samlproviderarns" title="SamlProviderArns">SamlProviderArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#supportedloginproviders" title="SupportedLoginProviders">SupportedLoginProviders</a>" : <i>[ <a href="supportedloginproviders.md">SupportedLoginProviders</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#cognitoidentityproviders" title="CognitoIdentityProviders">CognitoIdentityProviders</a>" : <i>[ <a href="cognitoidentityproviders.md">CognitoIdentityProviders</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoIdentityPool
Properties:
    <a href="#allowunauthenticatedidentities" title="AllowUnauthenticatedIdentities">AllowUnauthenticatedIdentities</a>: <i>Boolean</i>
    <a href="#developerprovidername" title="DeveloperProviderName">DeveloperProviderName</a>: <i>String</i>
    <a href="#identitypoolname" title="IdentityPoolName">IdentityPoolName</a>: <i>String</i>
    <a href="#openidconnectproviderarns" title="OpenidConnectProviderArns">OpenidConnectProviderArns</a>: <i>
      - String</i>
    <a href="#samlproviderarns" title="SamlProviderArns">SamlProviderArns</a>: <i>
      - String</i>
    <a href="#supportedloginproviders" title="SupportedLoginProviders">SupportedLoginProviders</a>: <i>
      - <a href="supportedloginproviders.md">SupportedLoginProviders</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#cognitoidentityproviders" title="CognitoIdentityProviders">CognitoIdentityProviders</a>: <i>
      - <a href="cognitoidentityproviders.md">CognitoIdentityProviders</a></i>
</pre>

## Properties

#### AllowUnauthenticatedIdentities

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeveloperProviderName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityPoolName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidConnectProviderArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamlProviderArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportedLoginProviders

_Required_: No

_Type_: List of <a href="supportedloginproviders.md">SupportedLoginProviders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CognitoIdentityProviders

_Required_: No

_Type_: List of <a href="cognitoidentityproviders.md">CognitoIdentityProviders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

