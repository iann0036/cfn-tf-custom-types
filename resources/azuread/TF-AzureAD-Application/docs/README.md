# TF::AzureAD::Application

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureAD::Application",
    "Properties" : {
        "<a href="#approle" title="AppRole">AppRole</a>" : <i>[ <a href="approledefinition.md">AppRoleDefinition</a>, ... ]</i>,
        "<a href="#availabletoothertenants" title="AvailableToOtherTenants">AvailableToOtherTenants</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#fallbackpublicclientenabled" title="FallbackPublicClientEnabled">FallbackPublicClientEnabled</a>" : <i>Boolean</i>,
        "<a href="#groupmembershipclaims" title="GroupMembershipClaims">GroupMembershipClaims</a>" : <i>String</i>,
        "<a href="#homepage" title="Homepage">Homepage</a>" : <i>String</i>,
        "<a href="#identifieruris" title="IdentifierUris">IdentifierUris</a>" : <i>[ String, ... ]</i>,
        "<a href="#logouturl" title="LogoutUrl">LogoutUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oauth2allowimplicitflow" title="Oauth2AllowImplicitFlow">Oauth2AllowImplicitFlow</a>" : <i>Boolean</i>,
        "<a href="#oauth2permissions" title="Oauth2Permissions">Oauth2Permissions</a>" : <i>[ <a href="oauth2permissionsdefinition.md">Oauth2PermissionsDefinition</a>, ... ]</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#preventduplicatenames" title="PreventDuplicateNames">PreventDuplicateNames</a>" : <i>Boolean</i>,
        "<a href="#publicclient" title="PublicClient">PublicClient</a>" : <i>Boolean</i>,
        "<a href="#replyurls" title="ReplyUrls">ReplyUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#signinaudience" title="SignInAudience">SignInAudience</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#api" title="Api">Api</a>" : <i>[ <a href="apidefinition.md">ApiDefinition</a>, ... ]</i>,
        "<a href="#optionalclaims" title="OptionalClaims">OptionalClaims</a>" : <i>[ <a href="optionalclaimsdefinition.md">OptionalClaimsDefinition</a>, ... ]</i>,
        "<a href="#requiredresourceaccess" title="RequiredResourceAccess">RequiredResourceAccess</a>" : <i>[ <a href="requiredresourceaccessdefinition.md">RequiredResourceAccessDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#web" title="Web">Web</a>" : <i>[ <a href="webdefinition.md">WebDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureAD::Application
Properties:
    <a href="#approle" title="AppRole">AppRole</a>: <i>
      - <a href="approledefinition.md">AppRoleDefinition</a></i>
    <a href="#availabletoothertenants" title="AvailableToOtherTenants">AvailableToOtherTenants</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#fallbackpublicclientenabled" title="FallbackPublicClientEnabled">FallbackPublicClientEnabled</a>: <i>Boolean</i>
    <a href="#groupmembershipclaims" title="GroupMembershipClaims">GroupMembershipClaims</a>: <i>String</i>
    <a href="#homepage" title="Homepage">Homepage</a>: <i>String</i>
    <a href="#identifieruris" title="IdentifierUris">IdentifierUris</a>: <i>
      - String</i>
    <a href="#logouturl" title="LogoutUrl">LogoutUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oauth2allowimplicitflow" title="Oauth2AllowImplicitFlow">Oauth2AllowImplicitFlow</a>: <i>Boolean</i>
    <a href="#oauth2permissions" title="Oauth2Permissions">Oauth2Permissions</a>: <i>
      - <a href="oauth2permissionsdefinition.md">Oauth2PermissionsDefinition</a></i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#preventduplicatenames" title="PreventDuplicateNames">PreventDuplicateNames</a>: <i>Boolean</i>
    <a href="#publicclient" title="PublicClient">PublicClient</a>: <i>Boolean</i>
    <a href="#replyurls" title="ReplyUrls">ReplyUrls</a>: <i>
      - String</i>
    <a href="#signinaudience" title="SignInAudience">SignInAudience</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#api" title="Api">Api</a>: <i>
      - <a href="apidefinition.md">ApiDefinition</a></i>
    <a href="#optionalclaims" title="OptionalClaims">OptionalClaims</a>: <i>
      - <a href="optionalclaimsdefinition.md">OptionalClaimsDefinition</a></i>
    <a href="#requiredresourceaccess" title="RequiredResourceAccess">RequiredResourceAccess</a>: <i>
      - <a href="requiredresourceaccessdefinition.md">RequiredResourceAccessDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#web" title="Web">Web</a>: <i>
      - <a href="webdefinition.md">WebDefinition</a></i>
</pre>

## Properties

#### AppRole

A collection of `app_role` blocks as documented below. For more information see [official documentation on Application Roles](https://docs.microsoft.com/en-us/azure/architecture/multitenant-identity/app-roles).

_Required_: No

_Type_: List of <a href="approledefinition.md">AppRoleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableToOtherTenants

Is this Azure AD Application available to other tenants? Defaults to `false`. This property is deprecated and has been replaced by the `sign_in_audience` property.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name for the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackPublicClientEnabled

The fallback application type as public client, such as an installed application running on a mobile device. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMembershipClaims

Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup`, `DirectoryRole`, `ApplicationGroup` or `All`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Homepage

The URL to the application's home page. This property is deprecated and has been replaced by the `homepage_url` property in the `web` block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentifierUris

The user-defined URI(s) that uniquely identify an application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrl

The URL of the logout page. This property is deprecated and has been replaced by the `logout_url` property in the `web` block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the optional claim.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oauth2AllowImplicitFlow

Does this Azure AD Application allow OAuth 2.0 implicit flow tokens? Defaults to `false`. This property is deprecated and has been replaced by the `access_token_issuance_enabled` property in the `implicit_grant` block.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oauth2Permissions

A collection of OAuth 2.0 permission scopes that the web API (resource) app exposes to client apps. Each permission is covered by `oauth2_permissions` blocks as documented below. This block is deprecated and has been replaced by the `oauth2_permission_scope` block in the `api` block.

_Required_: No

_Type_: List of <a href="oauth2permissionsdefinition.md">Oauth2PermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

A list of object IDs of principals that will be granted ownership of the application. It's recommended to specify the object ID of the authenticated principal running Terraform, to ensure sufficient permissions that the application can be subsequently updated.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreventDuplicateNames

If `true`, will return an error when an existing Application is found with the same name. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicClient

Is this Azure AD Application a public client? Defaults to `false`. This property is deprecated and has been replaced by the `fallback_public_client_enabled` property.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplyUrls

A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to. This property is deprecated and has been replaced by the `redirect_uris` property in the `web` block.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignInAudience

The Microsoft account types that are supported for the current application. Must be one of `AzureADMyOrg` or `AzureADMultipleOrgs`. Defaults to `AzureADMyOrg`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not be set. **This legacy property is deprecated and will be removed in version 2.0 of the provider**.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Api

_Required_: No

_Type_: List of <a href="apidefinition.md">ApiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalClaims

_Required_: No

_Type_: List of <a href="optionalclaimsdefinition.md">OptionalClaimsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredResourceAccess

_Required_: No

_Type_: List of <a href="requiredresourceaccessdefinition.md">RequiredResourceAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Web

_Required_: No

_Type_: List of <a href="webdefinition.md">WebDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApplicationId

Returns the <code>ApplicationId</code> value.

#### Id

Returns the <code>Id</code> value.

#### ObjectId

Returns the <code>ObjectId</code> value.

