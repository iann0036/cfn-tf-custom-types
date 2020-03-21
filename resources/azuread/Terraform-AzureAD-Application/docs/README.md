# Terraform::AzureAD::Application

CloudFormation equivalent of azuread_application

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMembershipClaims

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Homepage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentifierUris

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oauth2AllowImplicitFlow

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicClient

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplyUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApplicationId

Returns the <code>ApplicationId</code> value.

#### ObjectId

Returns the <code>ObjectId</code> value.

