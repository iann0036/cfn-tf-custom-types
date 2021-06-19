# TF::OpsGenie::User

Manages a User within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::User",
    "Properties" : {
        "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
        "<a href="#locale" title="Locale">Locale</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#skypeusername" title="SkypeUsername">SkypeUsername</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#userdetails" title="UserDetails">UserDetails</a>" : <i>[ <a href="userdetailsdefinition.md">UserDetailsDefinition</a>, ... ]</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#useraddress" title="UserAddress">UserAddress</a>" : <i>[ <a href="useraddressdefinition.md">UserAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::User
Properties:
    <a href="#fullname" title="FullName">FullName</a>: <i>String</i>
    <a href="#locale" title="Locale">Locale</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#skypeusername" title="SkypeUsername">SkypeUsername</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#userdetails" title="UserDetails">UserDetails</a>: <i>
      - <a href="userdetailsdefinition.md">UserDetailsDefinition</a></i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#useraddress" title="UserAddress">UserAddress</a>: <i>
      - <a href="useraddressdefinition.md">UserAddressDefinition</a></i>
</pre>

## Properties

#### FullName

The Full Name of the User.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locale

Location information for the user. Please look at [Supported Locale Ids](https://docs.opsgenie.com/docs/supported-locales) for available locales.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The Role assigned to the User. Either a built-in such as 'Admin' or 'User' - or the name of a custom role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkypeUsername

Skype username of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to be associated with the user.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Timezone information of the user. Please look at [Supported Timezone Ids](https://docs.opsgenie.com/docs/supported-timezone-ids) for available timezones.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDetails

Details about the user in form of key and list. of values.

_Required_: No

_Type_: List of <a href="userdetailsdefinition.md">UserDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The email address associated with this user. Opsgenie defines that this must not be longer than 100 characters and must contain lowercase characters only.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAddress

_Required_: No

_Type_: List of <a href="useraddressdefinition.md">UserAddressDefinition</a>

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

