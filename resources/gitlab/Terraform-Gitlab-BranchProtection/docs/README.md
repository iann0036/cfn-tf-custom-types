# Terraform::Gitlab::BranchProtection

This resource allows you to protect a specific branch by an access level so that the user with less access level cannot Merge/Push to the branch. GitLab EE features to protect by group or user are not supported.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::BranchProtection",
    "Properties" : {
        "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
        "<a href="#mergeaccesslevel" title="MergeAccessLevel">MergeAccessLevel</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#pushaccesslevel" title="PushAccessLevel">PushAccessLevel</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::BranchProtection
Properties:
    <a href="#branch" title="Branch">Branch</a>: <i>String</i>
    <a href="#mergeaccesslevel" title="MergeAccessLevel">MergeAccessLevel</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#pushaccesslevel" title="PushAccessLevel">PushAccessLevel</a>: <i>String</i>
</pre>

## Properties

#### Branch

Name of the branch.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeAccessLevel

One of five levels of access to the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The id of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushAccessLevel

One of five levels of access to the project.

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

