# TF::Gitlab::ProjectApprovalRule

This resource allows you to create and manage multiple approval rules for your GitLab
projects. For further information on approval rules, consult the [gitlab
documentation](https://docs.gitlab.com/ee/api/merge_request_approvals.html#project-level-mr-approvals).

-> This feature requires a GitLab Starter account or above.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ProjectApprovalRule",
    "Properties" : {
        "<a href="#approvalsrequired" title="ApprovalsRequired">ApprovalsRequired</a>" : <i>Double</i>,
        "<a href="#groupids" title="GroupIds">GroupIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#userids" title="UserIds">UserIds</a>" : <i>[ Double, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ProjectApprovalRule
Properties:
    <a href="#approvalsrequired" title="ApprovalsRequired">ApprovalsRequired</a>: <i>Double</i>
    <a href="#groupids" title="GroupIds">GroupIds</a>: <i>
      - Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#userids" title="UserIds">UserIds</a>: <i>
      - Double</i>
</pre>

## Properties

#### ApprovalsRequired

The number of approvals required for this rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIds

A list of group IDs who's members can approve of the merge request.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the approval rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or id of the project to add the approval rules.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIds

A list of specific User IDs to add to the list of approvers.

_Required_: No

_Type_: List of Double

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

