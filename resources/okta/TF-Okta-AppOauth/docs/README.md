# TF::Okta::AppOauth

Creates an OIDC Application.

This resource allows you to create and configure an OIDC Application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AppOauth",
    "Properties" : {
        "<a href="#autokeyrotation" title="AutoKeyRotation">AutoKeyRotation</a>" : <i>Boolean</i>,
        "<a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>" : <i>Boolean</i>,
        "<a href="#clientbasicsecret" title="ClientBasicSecret">ClientBasicSecret</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clienturi" title="ClientUri">ClientUri</a>" : <i>String</i>,
        "<a href="#consentmethod" title="ConsentMethod">ConsentMethod</a>" : <i>String</i>,
        "<a href="#customclientid" title="CustomClientId">CustomClientId</a>" : <i>String</i>,
        "<a href="#granttypes" title="GrantTypes">GrantTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#hideios" title="HideIos">HideIos</a>" : <i>Boolean</i>,
        "<a href="#hideweb" title="HideWeb">HideWeb</a>" : <i>Boolean</i>,
        "<a href="#implicitassignment" title="ImplicitAssignment">ImplicitAssignment</a>" : <i>Boolean</i>,
        "<a href="#issuermode" title="IssuerMode">IssuerMode</a>" : <i>String</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#loginmode" title="LoginMode">LoginMode</a>" : <i>String</i>,
        "<a href="#loginscopes" title="LoginScopes">LoginScopes</a>" : <i>[ String, ... ]</i>,
        "<a href="#loginuri" title="LoginUri">LoginUri</a>" : <i>String</i>,
        "<a href="#logouri" title="LogoUri">LogoUri</a>" : <i>String</i>,
        "<a href="#omitsecret" title="OmitSecret">OmitSecret</a>" : <i>Boolean</i>,
        "<a href="#policyuri" title="PolicyUri">PolicyUri</a>" : <i>String</i>,
        "<a href="#postlogoutredirecturis" title="PostLogoutRedirectUris">PostLogoutRedirectUris</a>" : <i>[ String, ... ]</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>String</i>,
        "<a href="#redirecturis" title="RedirectUris">RedirectUris</a>" : <i>[ String, ... ]</i>,
        "<a href="#responsetypes" title="ResponseTypes">ResponseTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tokenendpointauthmethod" title="TokenEndpointAuthMethod">TokenEndpointAuthMethod</a>" : <i>String</i>,
        "<a href="#tosuri" title="TosUri">TosUri</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#jwks" title="Jwks">Jwks</a>" : <i>[ <a href="jwksdefinition.md">JwksDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AppOauth
Properties:
    <a href="#autokeyrotation" title="AutoKeyRotation">AutoKeyRotation</a>: <i>Boolean</i>
    <a href="#autosubmittoolbar" title="AutoSubmitToolbar">AutoSubmitToolbar</a>: <i>Boolean</i>
    <a href="#clientbasicsecret" title="ClientBasicSecret">ClientBasicSecret</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clienturi" title="ClientUri">ClientUri</a>: <i>String</i>
    <a href="#consentmethod" title="ConsentMethod">ConsentMethod</a>: <i>String</i>
    <a href="#customclientid" title="CustomClientId">CustomClientId</a>: <i>String</i>
    <a href="#granttypes" title="GrantTypes">GrantTypes</a>: <i>
      - String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#hideios" title="HideIos">HideIos</a>: <i>Boolean</i>
    <a href="#hideweb" title="HideWeb">HideWeb</a>: <i>Boolean</i>
    <a href="#implicitassignment" title="ImplicitAssignment">ImplicitAssignment</a>: <i>Boolean</i>
    <a href="#issuermode" title="IssuerMode">IssuerMode</a>: <i>String</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#loginmode" title="LoginMode">LoginMode</a>: <i>String</i>
    <a href="#loginscopes" title="LoginScopes">LoginScopes</a>: <i>
      - String</i>
    <a href="#loginuri" title="LoginUri">LoginUri</a>: <i>String</i>
    <a href="#logouri" title="LogoUri">LogoUri</a>: <i>String</i>
    <a href="#omitsecret" title="OmitSecret">OmitSecret</a>: <i>Boolean</i>
    <a href="#policyuri" title="PolicyUri">PolicyUri</a>: <i>String</i>
    <a href="#postlogoutredirecturis" title="PostLogoutRedirectUris">PostLogoutRedirectUris</a>: <i>
      - String</i>
    <a href="#profile" title="Profile">Profile</a>: <i>String</i>
    <a href="#redirecturis" title="RedirectUris">RedirectUris</a>: <i>
      - String</i>
    <a href="#responsetypes" title="ResponseTypes">ResponseTypes</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tokenendpointauthmethod" title="TokenEndpointAuthMethod">TokenEndpointAuthMethod</a>: <i>String</i>
    <a href="#tosuri" title="TosUri">TosUri</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#jwks" title="Jwks">Jwks</a>: <i>
      - <a href="jwksdefinition.md">JwksDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### AutoKeyRotation

Requested key rotation mode.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSubmitToolbar

Display auto submit toolbar.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientBasicSecret

OAuth client secret key, this can be set when token_endpoint_auth_method is client_secret_basic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

OAuth client ID. If set during creation, app is created with this id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientUri

URI to a web page providing information about the client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsentMethod

Indicates whether user consent is required or implicit. Valid values: `"REQUIRED"`, `"TRUSTED"`. Default value is `"TRUSTED"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrantTypes

List of OAuth 2.0 grant types. Conditional validation params found [here](https://developer.okta.com/docs/api/resources/apps#credentials-settings-details).
Defaults to minimum requirements per app type. Valid values: `"authorization_code"`, `"implicit"`, `"password"`, `"refresh_token"`, `"client_credentials"`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

The groups assigned to the application. It is recommended not to use this and instead use `okta_app_group_assignment`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideIos

Do not display application icon on mobile app.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideWeb

Do not display application icon to users.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImplicitAssignment

*Early Access Property*. Enables [Federation Broker Mode]( https://help.okta.com/en/prod/Content/Topics/Apps/apps-fbm-enable.htm). When this mode is enabled, `users` and `groups` arguments are ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerMode

Indicates whether the Okta Authorization Server uses the original Okta org domain URL or a custom domain URL as the issuer of ID token for this client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The Application's display name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginMode

The type of Idp-Initiated login that the client supports, if any. Valid values: `"DISABLED"`, `"SPEC"`, `"OKTA"`. Default is `"DISABLED"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginScopes

List of scopes to use for the request. Valid values: `"openid"`, `"profile"`, `"email"`, `"address"`, `"phone"`. Required when `login_mode` is NOT `DISABLED`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginUri

URI that initiates login. Required when `login_mode` is NOT `DISABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoUri

URI that references a logo for the client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OmitSecret

This tells the provider not to persist the application's secret to state. Your app will be recreated if this ever changes from true => false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyUri

URI to web page providing client policy document.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostLogoutRedirectUris

List of URIs for redirection after logout.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

Custom JSON that represents an OAuth application's profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUris

List of URIs for use in the redirect-based flow. This is required for all application types except service.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTypes

List of OAuth 2.0 response type strings.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the application, by default, it is `"ACTIVE"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenEndpointAuthMethod

Requested authentication method for the token endpoint. It can be set to `"none"`, `"client_secret_post"`, `"client_secret_basic"`, `"client_secret_jwt"`, `"private_key_jwt"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosUri

URI to web page providing client tos (terms of service).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Groups claim type. Valid values: `"FILTER"`, `"EXPRESSION"`.
- `filter_type` - (Optional) Groups claim filter. Can only be set if type is `"FILTER"`. Valid values: `"EQUALS"`, `"STARTS_WITH"`, `"CONTAINS"`, `"REGEX"`.
- `name` - (Required) Name of the claim that will be used in the token.
- `value` - (Required) Value of the claim. Can be an Okta Expression Language statement that evaluates at the time the token is minted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Jwks

_Required_: No

_Type_: List of <a href="jwksdefinition.md">JwksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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

#### Name

Name of the claim that will be used in the token.
- `value` - (Required) Value of the claim. Can be an Okta Expression Language statement that evaluates at the time the token is minted.

#### SignOnMode

Returns the <code>SignOnMode</code> value.

