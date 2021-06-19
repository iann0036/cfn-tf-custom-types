# TF::Gitlab::User

This resource allows you to create and manage GitLab users.
Note your provider will need to be configured with admin-level access for this resource to work.

-> **Note:** You must specify either `password` or `reset_password`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::User",
    "Properties" : {
        "<a href="#cancreategroup" title="CanCreateGroup">CanCreateGroup</a>" : <i>Boolean</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#isadmin" title="IsAdmin">IsAdmin</a>" : <i>Boolean</i>,
        "<a href="#isexternal" title="IsExternal">IsExternal</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#projectslimit" title="ProjectsLimit">ProjectsLimit</a>" : <i>Double</i>,
        "<a href="#resetpassword" title="ResetPassword">ResetPassword</a>" : <i>Boolean</i>,
        "<a href="#skipconfirmation" title="SkipConfirmation">SkipConfirmation</a>" : <i>Boolean</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::User
Properties:
    <a href="#cancreategroup" title="CanCreateGroup">CanCreateGroup</a>: <i>Boolean</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#isadmin" title="IsAdmin">IsAdmin</a>: <i>Boolean</i>
    <a href="#isexternal" title="IsExternal">IsExternal</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#projectslimit" title="ProjectsLimit">ProjectsLimit</a>: <i>Double</i>
    <a href="#resetpassword" title="ResetPassword">ResetPassword</a>: <i>Boolean</i>
    <a href="#skipconfirmation" title="SkipConfirmation">SkipConfirmation</a>: <i>Boolean</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CanCreateGroup

Boolean, defaults to false. Whether to allow the user to create groups.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

The e-mail address of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAdmin

Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsExternal

Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

The note associated to the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectsLimit

Integer, defaults to 0.  Number of projects user can create.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetPassword

Boolean, defaults to false. Send user password reset link.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipConfirmation

Boolean, defaults to true. Whether to skip confirmation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username of the user.

_Required_: Yes

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

