# TF::PrismaCloud::UserRole

Manage an user role.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::UserRole",
    "Properties" : {
        "<a href="#accountgroupids" title="AccountGroupIds">AccountGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#associatedusers" title="AssociatedUsers">AssociatedUsers</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#restrictdismissalaccess" title="RestrictDismissalAccess">RestrictDismissalAccess</a>" : <i>Boolean</i>,
        "<a href="#roletype" title="RoleType">RoleType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::UserRole
Properties:
    <a href="#accountgroupids" title="AccountGroupIds">AccountGroupIds</a>: <i>
      - String</i>
    <a href="#associatedusers" title="AssociatedUsers">AssociatedUsers</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#restrictdismissalaccess" title="RestrictDismissalAccess">RestrictDismissalAccess</a>: <i>Boolean</i>
    <a href="#roletype" title="RoleType">RoleType</a>: <i>String</i>
</pre>

## Properties

#### AccountGroupIds

List of accessible account group IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedUsers

List of associated application users which cannot exist in the system without the user role.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictDismissalAccess

Restrict dismissal access.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleType

User role type.  Valid valies are `System Admin`, `Account Group Admin`, `Account Group Read Only`, `Cloud Provisioning Admin`, or `Account and Cloud Provisioning Admin`.

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

#### AccountGroups

Returns the <code>AccountGroups</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### LastModifiedTs

Returns the <code>LastModifiedTs</code> value.

#### RoleId

Returns the <code>RoleId</code> value.

