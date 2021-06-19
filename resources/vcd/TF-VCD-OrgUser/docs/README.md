# TF::VCD::OrgUser

Provides a vCloud Director Org User. This can be used to create, update, and delete organization users, including org administrators.

Supported in provider *v2.4+*

~> **Note:** Only `System Administrator` or `Org Administrator` users can create users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::OrgUser",
    "Properties" : {
        "<a href="#deployedvmquota" title="DeployedVmQuota">DeployedVmQuota</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
        "<a href="#instantmessaging" title="InstantMessaging">InstantMessaging</a>" : <i>String</i>,
        "<a href="#isgrouprole" title="IsGroupRole">IsGroupRole</a>" : <i>Boolean</i>,
        "<a href="#islocked" title="IsLocked">IsLocked</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#passwordfile" title="PasswordFile">PasswordFile</a>" : <i>String</i>,
        "<a href="#providertype" title="ProviderType">ProviderType</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#storedvmquota" title="StoredVmQuota">StoredVmQuota</a>" : <i>Double</i>,
        "<a href="#takeownership" title="TakeOwnership">TakeOwnership</a>" : <i>Boolean</i>,
        "<a href="#telephone" title="Telephone">Telephone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::OrgUser
Properties:
    <a href="#deployedvmquota" title="DeployedVmQuota">DeployedVmQuota</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#fullname" title="FullName">FullName</a>: <i>String</i>
    <a href="#instantmessaging" title="InstantMessaging">InstantMessaging</a>: <i>String</i>
    <a href="#isgrouprole" title="IsGroupRole">IsGroupRole</a>: <i>Boolean</i>
    <a href="#islocked" title="IsLocked">IsLocked</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#passwordfile" title="PasswordFile">PasswordFile</a>: <i>String</i>
    <a href="#providertype" title="ProviderType">ProviderType</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#storedvmquota" title="StoredVmQuota">StoredVmQuota</a>: <i>Double</i>
    <a href="#takeownership" title="TakeOwnership">TakeOwnership</a>: <i>Boolean</i>
    <a href="#telephone" title="Telephone">Telephone</a>: <i>String</i>
</pre>

## Properties

#### DeployedVmQuota

Quota of vApps that this user can deploy. A value of 0 specifies an unlimited quota.
The default is 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

An optional description of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddress

The Org User email address. Needs to be a properly formatted email address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

True if the user is enabled and can log in. The default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

The full name of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstantMessaging

The Org User instant messaging.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsGroupRole

True if this user has a group role. The default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsLocked

aIf the user account has been locked due to too many invalid login attempts, the value will
change to true (only the system can lock the user). To unlock the user re-set this flag to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to which the user belongs. Optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The user password. This value is never returned
on read. It is inspected on create and modify. To modify, fill with a different value. Note that if you remove the
password *on update*, Terraform will indicate that a change was occurring, but the empty password will be ignored by vCD.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderType

Identity provider type for this user. One of: `INTEGRATED`, `SAML`, `OAUTH`. The default
is `INTEGRATED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The role of the user. Role names can be retrieved from the organization. Both built-in roles and
custom built can be used. The roles normally available are:
* `Organization Administrator`
* `Catalog Author`
* `vApp Author`
* `vApp User`
* `Console Access Only`
* `Defer to Identity Provider`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoredVmQuota

Quota of vApps that this user can store. A value of 0 specifies an unlimited quota.
The default is 10.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TakeOwnership

Take ownership of user's objects on deletion.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Telephone

The Org User telephone number.

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

