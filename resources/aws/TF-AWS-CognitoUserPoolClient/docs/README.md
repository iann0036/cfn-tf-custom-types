# TF::AWS::CognitoUserPoolClient

Provides a Cognito User Pool Client resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CognitoUserPoolClient",
    "Properties" : {
        "<a href="#accesstokenvalidity" title="AccessTokenValidity">AccessTokenValidity</a>" : <i>Double</i>,
        "<a href="#allowedoauthflows" title="AllowedOauthFlows">AllowedOauthFlows</a>" : <i>[ String, ... ]</i>,
        "<a href="#allowedoauthflowsuserpoolclient" title="AllowedOauthFlowsUserPoolClient">AllowedOauthFlowsUserPoolClient</a>" : <i>Boolean</i>,
        "<a href="#allowedoauthscopes" title="AllowedOauthScopes">AllowedOauthScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#callbackurls" title="CallbackUrls">CallbackUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultredirecturi" title="DefaultRedirectUri">DefaultRedirectUri</a>" : <i>String</i>,
        "<a href="#explicitauthflows" title="ExplicitAuthFlows">ExplicitAuthFlows</a>" : <i>[ String, ... ]</i>,
        "<a href="#generatesecret" title="GenerateSecret">GenerateSecret</a>" : <i>Boolean</i>,
        "<a href="#idtokenvalidity" title="IdTokenValidity">IdTokenValidity</a>" : <i>Double</i>,
        "<a href="#logouturls" title="LogoutUrls">LogoutUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preventuserexistenceerrors" title="PreventUserExistenceErrors">PreventUserExistenceErrors</a>" : <i>String</i>,
        "<a href="#readattributes" title="ReadAttributes">ReadAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#refreshtokenvalidity" title="RefreshTokenValidity">RefreshTokenValidity</a>" : <i>Double</i>,
        "<a href="#supportedidentityproviders" title="SupportedIdentityProviders">SupportedIdentityProviders</a>" : <i>[ String, ... ]</i>,
        "<a href="#userpoolid" title="UserPoolId">UserPoolId</a>" : <i>String</i>,
        "<a href="#writeattributes" title="WriteAttributes">WriteAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#analyticsconfiguration" title="AnalyticsConfiguration">AnalyticsConfiguration</a>" : <i>[ <a href="analyticsconfigurationdefinition.md">AnalyticsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#tokenvalidityunits" title="TokenValidityUnits">TokenValidityUnits</a>" : <i>[ <a href="tokenvalidityunitsdefinition.md">TokenValidityUnitsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CognitoUserPoolClient
Properties:
    <a href="#accesstokenvalidity" title="AccessTokenValidity">AccessTokenValidity</a>: <i>Double</i>
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
    <a href="#idtokenvalidity" title="IdTokenValidity">IdTokenValidity</a>: <i>Double</i>
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
      - <a href="analyticsconfigurationdefinition.md">AnalyticsConfigurationDefinition</a></i>
    <a href="#tokenvalidityunits" title="TokenValidityUnits">TokenValidityUnits</a>: <i>
      - <a href="tokenvalidityunitsdefinition.md">TokenValidityUnitsDefinition</a></i>
</pre>

## Properties

#### AccessTokenValidity

Time limit, between 5 minutes and 1 day, after which the access token is no longer valid and cannot be used. This value will be overridden if you have entered a value in `token_validity_units`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOauthFlows

List of allowed OAuth flows (code, implicit, client_credentials).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOauthFlowsUserPoolClient

Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOauthScopes

List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallbackUrls

List of allowed callback URLs for the identity providers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRedirectUri

Default redirect URI. Must be in the list of callback URLs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitAuthFlows

List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY, USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateSecret

Should an application secret be generated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdTokenValidity

Time limit, between 5 minutes and 1 day, after which the ID token is no longer valid and cannot be used. This value will be overridden if you have entered a value in `token_validity_units`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrls

List of allowed logout URLs for the identity providers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the application client.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventUserExistenceErrors

Choose which errors and responses are returned by Cognito APIs during authentication, account confirmation, and password recovery when the user does not exist in the user pool. When set to `ENABLED` and the user does not exist, authentication returns an error indicating either the username or password was incorrect, and account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to `LEGACY`, those APIs will return a `UserNotFoundException` exception if the user does not exist in the user pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadAttributes

List of user pool attributes the application client can read from.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTokenValidity

Time limit in days refresh tokens are valid for.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportedIdentityProviders

List of provider names for the identity providers that are supported on this client.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPoolId

User pool the client belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAttributes

List of user pool attributes the application client can write to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsConfiguration

_Required_: No

_Type_: List of <a href="analyticsconfigurationdefinition.md">AnalyticsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenValidityUnits

_Required_: No

_Type_: List of <a href="tokenvalidityunitsdefinition.md">TokenValidityUnitsDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

