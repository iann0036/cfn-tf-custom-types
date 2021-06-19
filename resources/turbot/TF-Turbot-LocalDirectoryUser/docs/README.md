# TF::Turbot::LocalDirectoryUser

The `Turbot Local Directory User` resource adds support for local directory users. It is used to create, manage and delete user settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::LocalDirectoryUser",
    "Properties" : {
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#familyname" title="FamilyName">FamilyName</a>" : <i>String</i>,
        "<a href="#givenname" title="GivenName">GivenName</a>" : <i>String</i>,
        "<a href="#middlename" title="MiddleName">MiddleName</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#picture" title="Picture">Picture</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::LocalDirectoryUser
Properties:
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#familyname" title="FamilyName">FamilyName</a>: <i>String</i>
    <a href="#givenname" title="GivenName">GivenName</a>: <i>String</i>
    <a href="#middlename" title="MiddleName">MiddleName</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#picture" title="Picture">Picture</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### DisplayName

Full display name for the new user. Usually a combination of the given name and family name.
- `email` - (Required) Email address of the new user.
- `parent` - (Required) ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the local directory user.
- `family_name` - (Optional) Surname of the user.
- `given_name` - (Optional) First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Email address of the new user.
- `parent` - (Required) ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the local directory user.
- `family_name` - (Optional) Surname of the user.
- `given_name` - (Optional) First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyName

Surname of the user.
- `given_name` - (Optional) First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GivenName

First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddleName

Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the local directory user.
- `family_name` - (Optional) Surname of the user.
- `given_name` - (Optional) First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Picture

Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Labels that can be used to manage, group, categorize, search, and save metadata for this user.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short descriptive name for the local directory user.
- `family_name` - (Optional) Surname of the user.
- `given_name` - (Optional) First name of the user.
- `middle_name` - (Optional) Middle name of the user.
- `picture` - (Optional) Picture of the user.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this user.

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

#### ParentAkas

Returns the <code>ParentAkas</code> value.

#### PasswordTimestamp

Returns the <code>PasswordTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

