# TF::AWS::CognitoIdentityPool

Provides an AWS Cognito Identity Pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CognitoIdentityPool",
    "Properties" : {
        "<a href="#allowclassicflow" title="AllowClassicFlow">AllowClassicFlow</a>" : <i>Boolean</i>,
        "<a href="#allowunauthenticatedidentities" title="AllowUnauthenticatedIdentities">AllowUnauthenticatedIdentities</a>" : <i>Boolean</i>,
        "<a href="#developerprovidername" title="DeveloperProviderName">DeveloperProviderName</a>" : <i>String</i>,
        "<a href="#identitypoolname" title="IdentityPoolName">IdentityPoolName</a>" : <i>String</i>,
        "<a href="#openidconnectproviderarns" title="OpenidConnectProviderArns">OpenidConnectProviderArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#samlproviderarns" title="SamlProviderArns">SamlProviderArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#supportedloginproviders" title="SupportedLoginProviders">SupportedLoginProviders</a>" : <i>[ <a href="supportedloginprovidersdefinition.md">SupportedLoginProvidersDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#cognitoidentityproviders" title="CognitoIdentityProviders">CognitoIdentityProviders</a>" : <i>[ <a href="cognitoidentityprovidersdefinition.md">CognitoIdentityProvidersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CognitoIdentityPool
Properties:
    <a href="#allowclassicflow" title="AllowClassicFlow">AllowClassicFlow</a>: <i>Boolean</i>
    <a href="#allowunauthenticatedidentities" title="AllowUnauthenticatedIdentities">AllowUnauthenticatedIdentities</a>: <i>Boolean</i>
    <a href="#developerprovidername" title="DeveloperProviderName">DeveloperProviderName</a>: <i>String</i>
    <a href="#identitypoolname" title="IdentityPoolName">IdentityPoolName</a>: <i>String</i>
    <a href="#openidconnectproviderarns" title="OpenidConnectProviderArns">OpenidConnectProviderArns</a>: <i>
      - String</i>
    <a href="#samlproviderarns" title="SamlProviderArns">SamlProviderArns</a>: <i>
      - String</i>
    <a href="#supportedloginproviders" title="SupportedLoginProviders">SupportedLoginProviders</a>: <i>
      - <a href="supportedloginprovidersdefinition.md">SupportedLoginProvidersDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#cognitoidentityproviders" title="CognitoIdentityProviders">CognitoIdentityProviders</a>: <i>
      - <a href="cognitoidentityprovidersdefinition.md">CognitoIdentityProvidersDefinition</a></i>
</pre>

## Properties

#### AllowClassicFlow

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of <a href="supportedloginprovidersdefinition.md">SupportedLoginProvidersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the Identity Pool. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CognitoIdentityProviders

_Required_: No

_Type_: List of <a href="cognitoidentityprovidersdefinition.md">CognitoIdentityProvidersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

