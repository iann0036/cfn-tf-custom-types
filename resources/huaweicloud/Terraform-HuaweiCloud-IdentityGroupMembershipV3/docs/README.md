# Terraform::HuaweiCloud::IdentityGroupMembershipV3

Manages a User Group Membership resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::IdentityGroupMembershipV3",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::IdentityGroupMembershipV3
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
</pre>

## Properties

#### Group

The group ID of this membership.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

A List of user IDs to associate to the group.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

