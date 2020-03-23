# Terraform::AWS::IamGroupMembership

~> **WARNING:** Multiple aws_iam_group_membership resources with the same group name will produce inconsistent behavior!

Provides a top level resource to manage IAM Group membership for IAM Users. For
more information on managing IAM Groups or IAM Users, see [IAM Groups][1] or
[IAM Users][2]

~> **Note:** `aws_iam_group_membership` will conflict with itself if used more than once with the same group. To non-exclusively manage the users in a group, see the
[`aws_iam_user_group_membership` resource][3].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IamGroupMembership",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IamGroupMembership
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - String</i>
</pre>

## Properties

#### Group

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name to identify the Group Membership.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

A list of IAM User names to associate with the Group.

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

#### Id

Returns the <code>Id</code> value.

