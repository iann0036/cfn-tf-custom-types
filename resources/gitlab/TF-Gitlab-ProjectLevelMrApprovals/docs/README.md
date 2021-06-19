# TF::Gitlab::ProjectLevelMrApprovals

This resource allows you to configure project-level MR approvals. for your GitLab projects.
For further information on merge request approvals, consult the [GitLab API
documentation](https://docs.gitlab.com/ee/api/merge_request_approvals.html#project-level-mr-approvals).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ProjectLevelMrApprovals",
    "Properties" : {
        "<a href="#disableoverridingapproverspermergerequest" title="DisableOverridingApproversPerMergeRequest">DisableOverridingApproversPerMergeRequest</a>" : <i>Boolean</i>,
        "<a href="#mergerequestsauthorapproval" title="MergeRequestsAuthorApproval">MergeRequestsAuthorApproval</a>" : <i>Boolean</i>,
        "<a href="#mergerequestsdisablecommittersapproval" title="MergeRequestsDisableCommittersApproval">MergeRequestsDisableCommittersApproval</a>" : <i>Boolean</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#resetapprovalsonpush" title="ResetApprovalsOnPush">ResetApprovalsOnPush</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ProjectLevelMrApprovals
Properties:
    <a href="#disableoverridingapproverspermergerequest" title="DisableOverridingApproversPerMergeRequest">DisableOverridingApproversPerMergeRequest</a>: <i>Boolean</i>
    <a href="#mergerequestsauthorapproval" title="MergeRequestsAuthorApproval">MergeRequestsAuthorApproval</a>: <i>Boolean</i>
    <a href="#mergerequestsdisablecommittersapproval" title="MergeRequestsDisableCommittersApproval">MergeRequestsDisableCommittersApproval</a>: <i>Boolean</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#resetapprovalsonpush" title="ResetApprovalsOnPush">ResetApprovalsOnPush</a>: <i>Boolean</i>
</pre>

## Properties

#### DisableOverridingApproversPerMergeRequest

By default, users are able to edit the approval rules in merge requests. If set to true,
the approval rules for all new merge requests will be determined by the default approval rules. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsAuthorApproval

Set to `true` if you want to allow merge request authors to self-approve merge requests. Authors
also need to be included in the approvers list in order to be able to approve their merge request. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsDisableCommittersApproval

Set to `true` if you want to prevent approval of merge requests by merge request committers. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the project to change MR approval configuration.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetApprovalsOnPush

Set to `true` if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is `true`.

_Required_: No

_Type_: Boolean

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

