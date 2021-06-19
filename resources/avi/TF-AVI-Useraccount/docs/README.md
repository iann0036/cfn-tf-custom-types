# TF::AVI::Useraccount

The Useraccount resource allows the password update of a user and setting up admin password in the bootstrap.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Useraccount",
    "Properties" : {
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
        "<a href="#local" title="Local">Local</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oldpassword" title="OldPassword">OldPassword</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Useraccount
Properties:
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#fullname" title="FullName">FullName</a>: <i>String</i>
    <a href="#local" title="Local">Local</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oldpassword" title="OldPassword">OldPassword</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Email

To set email for the useraccount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

Is local user.
* `name` - (Optional) To set name for the user account.
* `full_name` - (Optional) To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

To set name for the user account.
* `full_name` - (Optional) To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OldPassword

Old/currant password of the user.
* `password` - (Required) New paswword for the given user.
* `local` - (Optional) Is local user.
* `name` - (Optional) To set name for the user account.
* `full_name` - (Optional) To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

New paswword for the given user.
* `local` - (Optional) Is local user.
* `name` - (Optional) To set name for the user account.
* `full_name` - (Optional) To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

User name of a user who's password needs to be updated.
* `old_password` - (Required) Old/currant password of the user.
* `password` - (Required) New paswword for the given user.
* `local` - (Optional) Is local user.
* `name` - (Optional) To set name for the user account.
* `full_name` - (Optional) To set full name for the user account.
* `email` - (Optional) To set email for the useraccount.

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

