# TF::OpenNebula::User

Provides an OpenNebula user resource.

This resource allows you to manage users on your OpenNebula clusters. When applied,
a new user is created. When destroyed, it is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::User",
    "Properties" : {
        "<a href="#authdriver" title="AuthDriver">AuthDriver</a>" : <i>String</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#primarygroup" title="PrimaryGroup">PrimaryGroup</a>" : <i>Double</i>,
        "<a href="#quotas" title="Quotas">Quotas</a>" : <i>[ <a href="quotasdefinition.md">QuotasDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::User
Properties:
    <a href="#authdriver" title="AuthDriver">AuthDriver</a>: <i>String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#primarygroup" title="PrimaryGroup">PrimaryGroup</a>: <i>Double</i>
    <a href="#quotas" title="Quotas">Quotas</a>: <i>
      - <a href="quotasdefinition.md">QuotasDefinition</a></i>
</pre>

## Properties

#### AuthDriver

Authentication Driver for User management. DEfaults to 'core'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

List of secondary groups ID of the user.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of the user. It is required for all `auth_driver` excepted 'ldap'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryGroup

Primary group ID of the User. Defaults to 0 (oneadmin).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quotas

_Required_: No

_Type_: List of <a href="quotasdefinition.md">QuotasDefinition</a>

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

