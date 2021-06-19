# TF::OneLogin::Users

Manage User resources.

This resource allows you to create and configure Users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::Users",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributesdefinition.md">CustomAttributesDefinition</a>, ... ]</i>,
        "<a href="#department" title="Department">Department</a>" : <i>String</i>,
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>Double</i>,
        "<a href="#distinguishedname" title="DistinguishedName">DistinguishedName</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>Double</i>,
        "<a href="#firstname" title="Firstname">Firstname</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
        "<a href="#lastname" title="Lastname">Lastname</a>" : <i>String</i>,
        "<a href="#manageradid" title="ManagerAdId">ManagerAdId</a>" : <i>Double</i>,
        "<a href="#manageruserid" title="ManagerUserId">ManagerUserId</a>" : <i>Double</i>,
        "<a href="#memberof" title="MemberOf">MemberOf</a>" : <i>String</i>,
        "<a href="#phone" title="Phone">Phone</a>" : <i>String</i>,
        "<a href="#samaccountname" title="Samaccountname">Samaccountname</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>Double</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#trustedidpid" title="TrustedIdpId">TrustedIdpId</a>" : <i>Double</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#userprincipalname" title="Userprincipalname">Userprincipalname</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::Users
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributesdefinition.md">CustomAttributesDefinition</a></i>
    <a href="#department" title="Department">Department</a>: <i>String</i>
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>Double</i>
    <a href="#distinguishedname" title="DistinguishedName">DistinguishedName</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>Double</i>
    <a href="#firstname" title="Firstname">Firstname</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
    <a href="#lastname" title="Lastname">Lastname</a>: <i>String</i>
    <a href="#manageradid" title="ManagerAdId">ManagerAdId</a>: <i>Double</i>
    <a href="#manageruserid" title="ManagerUserId">ManagerUserId</a>: <i>Double</i>
    <a href="#memberof" title="MemberOf">MemberOf</a>: <i>String</i>
    <a href="#phone" title="Phone">Phone</a>: <i>String</i>
    <a href="#samaccountname" title="Samaccountname">Samaccountname</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>Double</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#trustedidpid" title="TrustedIdpId">TrustedIdpId</a>: <i>Double</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#userprincipalname" title="Userprincipalname">Userprincipalname</a>: <i>String</i>
</pre>

## Properties

#### Comment

A comment about the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

The user's company.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributesdefinition.md">CustomAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Department

The user's department.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryId

The user's directory_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistinguishedName

The user's distinguished name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The user's email.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

The user's external_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Firstname

The user's first name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The user's group_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lastname

The user's last name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagerAdId

The user's manager_ad_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagerUserId

The user's manager_user_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberOf

The user's member_of.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phone

The user's phone number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Samaccountname

The user's samaccount name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

The user's state. Must be one of `0: Unapproved` `1: Approved` `2: Rejected` `3: Unlicensed`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The user's status. Must be one of `0: Unactivated` `1: Active` `2: Suspended` `3: Locked` `4: Password expired` `5: Awaiting password reset` `7: Password Pending` `8: Security questions required`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The user's title.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedIdpId

The user's trusted_idp_id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The user's username.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userprincipalname

The user's user principal name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

