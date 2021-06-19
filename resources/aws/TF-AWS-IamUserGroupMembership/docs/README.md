# TF::AWS::IamUserGroupMembership

Provides a resource for adding an [IAM User][2] to [IAM Groups][1]. This
resource can be used multiple times with the same user for non-overlapping
groups.

To exclusively manage the users in a group, see the
[`aws_iam_group_membership` resource][3].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::IamUserGroupMembership",
    "Properties" : {
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::IamUserGroupMembership
Properties:
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### Groups

A list of [IAM Groups][1] to add the user to.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The name of the [IAM User][2] to add to groups.

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

