# Terraform::HuaweiCloud::IdentityUserV3

Manages a User resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::IdentityUserV3",
    "Properties" : {
        "<a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::IdentityUserV3
Properties:
    <a href="#defaultprojectid" title="DefaultProjectId">DefaultProjectId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### DefaultProjectId

The default project this user belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

The domain this user belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the user is enabled or disabled. Valid
values are `true` and `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user. The user name consists of 5 to 32
characters. It can contain only uppercase letters, lowercase letters,
digits, spaces, and special characters (-_) and cannot start with a digit.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password for the user. It must contain at least
two of the following character types: uppercase letters, lowercase letters,
digits, and special characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V3 Keystone client.
If omitted, the `region` argument of the provider is used. Changing this
creates a new User.

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

