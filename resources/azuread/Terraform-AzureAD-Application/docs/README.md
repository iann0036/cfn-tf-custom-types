# Terraform::AzureAD::Application

Manages an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write owned by applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureAD::Application",
    "Properties" : {
        "<a href="#availabletoothertenants" title="AvailableToOtherTenants">AvailableToOtherTenants</a>" : <i>Boolean</i>,
        "<a href="#groupmembershipclaims" title="GroupMembershipClaims">GroupMembershipClaims</a>" : <i>String</i>,
        "<a href="#homepage" title="Homepage">Homepage</a>" : <i>String</i>,
        "<a href="#identifieruris" title="IdentifierUris">IdentifierUris</a>" : <i>[ String, ... ]</i>,
        "<a href="#logouturl" title="LogoutUrl">LogoutUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oauth2allowimplicitflow" title="Oauth2AllowImplicitFlow">Oauth2AllowImplicitFlow</a>" : <i>Boolean</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#publicclient" title="PublicClient">PublicClient</a>" : <i>Boolean</i>,
        "<a href="#replyurls" title="ReplyUrls">ReplyUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#approle" title="AppRole">AppRole</a>" : <i>[ <a href="approle.md">AppRole</a>, ... ]</i>,
        "<a href="#requiredresourceaccess" title="RequiredResourceAccess">RequiredResourceAccess</a>" : <i>[ <a href="requiredresourceaccess.md">RequiredResourceAccess</a>, ... ]</i>,
        "<a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>" : <i>[ <a href="resourceaccess.md">ResourceAccess</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureAD::Application
Properties:
    <a href="#availabletoothertenants" title="AvailableToOtherTenants">AvailableToOtherTenants</a>: <i>Boolean</i>
    <a href="#groupmembershipclaims" title="GroupMembershipClaims">GroupMembershipClaims</a>: <i>String</i>
    <a href="#homepage" title="Homepage">Homepage</a>: <i>String</i>
    <a href="#identifieruris" title="IdentifierUris">IdentifierUris</a>: <i>
      - String</i>
    <a href="#logouturl" title="LogoutUrl">LogoutUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oauth2allowimplicitflow" title="Oauth2AllowImplicitFlow">Oauth2AllowImplicitFlow</a>: <i>Boolean</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#publicclient" title="PublicClient">PublicClient</a>: <i>Boolean</i>
    <a href="#replyurls" title="ReplyUrls">ReplyUrls</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#approle" title="AppRole">AppRole</a>: <i>
      - <a href="approle.md">AppRole</a></i>
    <a href="#requiredresourceaccess" title="RequiredResourceAccess">RequiredResourceAccess</a>: <i>
      - <a href="requiredresourceaccess.md">RequiredResourceAccess</a></i>
    <a href="#resourceaccess" title="ResourceAccess">ResourceAccess</a>: <i>
      - <a href="resourceaccess.md">ResourceAccess</a></i>
</pre>

## Properties

#### AvailableToOtherTenants

Is this Azure AD Application available to other tenants? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMembershipClaims

Configures the `groups` claim issued in a user or OAuth 2.0 access token that the app expects. Defaults to `SecurityGroup`. Possible values are `None`, `SecurityGroup` or `All`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Homepage

The URL to the application's home page. If no homepage is specified this defaults to `https://{name}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentifierUris

A list of user-defined URI(s) that uniquely identify a Web application within it's Azure AD tenant, or within a verified custom domain if the application is multi-tenant.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrl

The URL of the logout page.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The display name for the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oauth2AllowImplicitFlow

Does this Azure AD Application allow OAuth2.0 implicit flow tokens? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

A list of Azure AD Object IDs that will be granted ownership of the application. Defaults to the Object ID of the caller creating the application. If a list is specified the caller Object ID will no longer be included unless explicitly added to the list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicClient

Is this Azure AD Application a public client? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplyUrls

A list of URLs that user tokens are sent to for sign in, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of an application: `webapp/api` or `native`. Defaults to `webapp/api`. For `native` apps type `identifier_uris` property can not not be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppRole

_Required_: No

_Type_: List of <a href="approle.md">AppRole</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredResourceAccess

_Required_: No

_Type_: List of <a href="requiredresourceaccess.md">RequiredResourceAccess</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAccess

_Required_: No

_Type_: List of <a href="resourceaccess.md">ResourceAccess</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

