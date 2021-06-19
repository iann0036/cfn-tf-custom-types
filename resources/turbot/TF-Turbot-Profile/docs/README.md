# TF::Turbot::Profile

The `Turbot Profile` resource adds support for creating user profiles. It is used to create, manage and delete profile settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::Profile",
    "Properties" : {
        "<a href="#directorypoolid" title="DirectoryPoolId">DirectoryPoolId</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>String</i>,
        "<a href="#familyname" title="FamilyName">FamilyName</a>" : <i>String</i>,
        "<a href="#givenname" title="GivenName">GivenName</a>" : <i>String</i>,
        "<a href="#lastlogintimestamp" title="LastLoginTimestamp">LastLoginTimestamp</a>" : <i>String</i>,
        "<a href="#middlename" title="MiddleName">MiddleName</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#picture" title="Picture">Picture</a>" : <i>String</i>,
        "<a href="#profileid" title="ProfileId">ProfileId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::Profile
Properties:
    <a href="#directorypoolid" title="DirectoryPoolId">DirectoryPoolId</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>String</i>
    <a href="#familyname" title="FamilyName">FamilyName</a>: <i>String</i>
    <a href="#givenname" title="GivenName">GivenName</a>: <i>String</i>
    <a href="#lastlogintimestamp" title="LastLoginTimestamp">LastLoginTimestamp</a>: <i>String</i>
    <a href="#middlename" title="MiddleName">MiddleName</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#picture" title="Picture">Picture</a>: <i>String</i>
    <a href="#profileid" title="ProfileId">ProfileId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### DirectoryPoolId

Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of the profile.
- `email` - (Required) Email ID associated with the profile.
- `family_name` - (Required) Last name of the user associated with the profile.
- `given_name` - (Required) First name of the user associated with the profile.
- `parent` - (Required) The `aka` or `id` of the level at which the profile is created.
- `profile_id` - (Required) An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Email ID associated with the profile.
- `family_name` - (Required) Last name of the user associated with the profile.
- `given_name` - (Required) First name of the user associated with the profile.
- `parent` - (Required) The `aka` or `id` of the level at which the profile is created.
- `profile_id` - (Required) An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FamilyName

Last name of the user associated with the profile.
- `given_name` - (Required) First name of the user associated with the profile.
- `parent` - (Required) The `aka` or `id` of the level at which the profile is created.
- `profile_id` - (Required) An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GivenName

First name of the user associated with the profile.
- `parent` - (Required) The `aka` or `id` of the level at which the profile is created.
- `profile_id` - (Required) An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastLoginTimestamp

The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MiddleName

Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

The `aka` or `id` of the level at which the profile is created.
- `profile_id` - (Required) An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Picture

A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileId

An unique identifier of the profile.
- `title` - (Required) Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Name of the profile.
- `directory_pool_id` - (Optional) Pool ID for the directory in the current resource. Allows grouping of related directories e.g. SAML for authentication and LDAP for AD searching.
- `external_id` - (Optional) A link between the local directory and the profile.
- `last_login_timestamp` - (Optional) The most recent login through the profile.
- `middle_name` - (Optional) Middle name of the user associated with the profile.
- `picture` - (Optional) A valid URL which contains a picture which will be associated to the profile.
- `status` - (Optional) Status of the profile, which defaults to `Active`. Valid options are `Active` and `Inactive`.

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

