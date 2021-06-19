# TF::Okta::OauthApp

CloudFormation equivalent of okta_oauth_app

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::OauthApp",
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
Type: TF::Okta::OauthApp
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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoSubmitToolbar

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientBasicSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsentMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomClientId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrantTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideIos

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HideWeb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImplicitAssignment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuerMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OmitSecret

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostLogoutRedirectUris

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUris

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenEndpointAuthMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TosUri

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

Returns the <code>Name</code> value.

#### SignOnMode

Returns the <code>SignOnMode</code> value.

