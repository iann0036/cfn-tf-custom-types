# Terraform::AWS::CognitoUserPoolClient

CloudFormation equivalent of aws_cognito_user_pool_client

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CognitoUserPoolClient",
    "Properties" : {
        "<a href="#allowedoauthflows" title="AllowedOauthFlows">AllowedOauthFlows</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedoauthflowsuserpoolclient" title="AllowedOauthFlowsUserPoolClient">AllowedOauthFlowsUserPoolClient</a>" : <i>Boolean</i>,
        "<a href="#allowedoauthscopes" title="AllowedOauthScopes">AllowedOauthScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#callbackurls" title="CallbackUrls">CallbackUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultredirecturi" title="DefaultRedirectUri">DefaultRedirectUri</a>" : <i>String</i>,
        "<a href="#explicitauthflows" title="ExplicitAuthFlows">ExplicitAuthFlows</a>" : <i>[ String, ... ]</i>,
        "<a href="#generatesecret" title="GenerateSecret">GenerateSecret</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#logouturls" title="LogoutUrls">LogoutUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preventuserexistenceerrors" title="PreventUserExistenceErrors">PreventUserExistenceErrors</a>" : <i>String</i>,
        "<a href="#readattributes" title="ReadAttributes">ReadAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#refreshtokenvalidity" title="RefreshTokenValidity">RefreshTokenValidity</a>" : <i>Double</i>,
        "<a href="#supportedidentityproviders" title="SupportedIdentityProviders">SupportedIdentityProviders</a>" : <i>[ String, ... ]</i>,
        "<a href="#userpoolid" title="UserPoolId">UserPoolId</a>" : <i>String</i>,
        "<a href="#writeattributes" title="WriteAttributes">WriteAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#analyticsconfiguration" title="AnalyticsConfiguration">AnalyticsConfiguration</a>" : <i>[ <a href="analyticsconfiguration.md">AnalyticsConfiguration</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CognitoUserPoolClient
Properties:
    <a href="#allowedoauthflows" title="AllowedOauthFlows">AllowedOauthFlows</a>: <i>
      - String</i>
    <a href="#allowedoauthflowsuserpoolclient" title="AllowedOauthFlowsUserPoolClient">AllowedOauthFlowsUserPoolClient</a>: <i>Boolean</i>
    <a href="#allowedoauthscopes" title="AllowedOauthScopes">AllowedOauthScopes</a>: <i>
      - String</i>
    <a href="#callbackurls" title="CallbackUrls">CallbackUrls</a>: <i>
      - String</i>
    <a href="#defaultredirecturi" title="DefaultRedirectUri">DefaultRedirectUri</a>: <i>String</i>
    <a href="#explicitauthflows" title="ExplicitAuthFlows">ExplicitAuthFlows</a>: <i>
      - String</i>
    <a href="#generatesecret" title="GenerateSecret">GenerateSecret</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#logouturls" title="LogoutUrls">LogoutUrls</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preventuserexistenceerrors" title="PreventUserExistenceErrors">PreventUserExistenceErrors</a>: <i>String</i>
    <a href="#readattributes" title="ReadAttributes">ReadAttributes</a>: <i>
      - String</i>
    <a href="#refreshtokenvalidity" title="RefreshTokenValidity">RefreshTokenValidity</a>: <i>Double</i>
    <a href="#supportedidentityproviders" title="SupportedIdentityProviders">SupportedIdentityProviders</a>: <i>
      - String</i>
    <a href="#userpoolid" title="UserPoolId">UserPoolId</a>: <i>String</i>
    <a href="#writeattributes" title="WriteAttributes">WriteAttributes</a>: <i>
      - String</i>
    <a href="#analyticsconfiguration" title="AnalyticsConfiguration">AnalyticsConfiguration</a>: <i>
      - <a href="analyticsconfiguration.md">AnalyticsConfiguration</a></i>
</pre>

## Properties

#### AllowedOauthFlows

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOauthFlowsUserPoolClient

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOauthScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallbackUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRedirectUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitAuthFlows

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateSecret

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventUserExistenceErrors

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTokenValidity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportedIdentityProviders

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAttributes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsConfiguration

_Required_: No

_Type_: List of <a href="analyticsconfiguration.md">AnalyticsConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClientSecret

Returns the <code>ClientSecret</code> value.

