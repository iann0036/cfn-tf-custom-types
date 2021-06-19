# TF::AzureDevOps::BranchPolicyMinReviewers SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowcompletionwithrejectsorwaits" title="AllowCompletionWithRejectsOrWaits">AllowCompletionWithRejectsOrWaits</a>" : <i>Boolean</i>,
    "<a href="#lastpushercannotapprove" title="LastPusherCannotApprove">LastPusherCannotApprove</a>" : <i>Boolean</i>,
    "<a href="#onlastiterationrequirevote" title="OnLastIterationRequireVote">OnLastIterationRequireVote</a>" : <i>Boolean</i>,
    "<a href="#onpushresetallvotes" title="OnPushResetAllVotes">OnPushResetAllVotes</a>" : <i>Boolean</i>,
    "<a href="#onpushresetapprovedvotes" title="OnPushResetApprovedVotes">OnPushResetApprovedVotes</a>" : <i>Boolean</i>,
    "<a href="#reviewercount" title="ReviewerCount">ReviewerCount</a>" : <i>Double</i>,
    "<a href="#submittercanvote" title="SubmitterCanVote">SubmitterCanVote</a>" : <i>Boolean</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowcompletionwithrejectsorwaits" title="AllowCompletionWithRejectsOrWaits">AllowCompletionWithRejectsOrWaits</a>: <i>Boolean</i>
<a href="#lastpushercannotapprove" title="LastPusherCannotApprove">LastPusherCannotApprove</a>: <i>Boolean</i>
<a href="#onlastiterationrequirevote" title="OnLastIterationRequireVote">OnLastIterationRequireVote</a>: <i>Boolean</i>
<a href="#onpushresetallvotes" title="OnPushResetAllVotes">OnPushResetAllVotes</a>: <i>Boolean</i>
<a href="#onpushresetapprovedvotes" title="OnPushResetApprovedVotes">OnPushResetApprovedVotes</a>: <i>Boolean</i>
<a href="#reviewercount" title="ReviewerCount">ReviewerCount</a>: <i>Double</i>
<a href="#submittercanvote" title="SubmitterCanVote">SubmitterCanVote</a>: <i>Boolean</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### AllowCompletionWithRejectsOrWaits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastPusherCannotApprove

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnLastIterationRequireVote

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPushResetAllVotes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPushResetApprovedVotes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReviewerCount

The number of reviewers needed to approve.
- `submitter_can_vote` - (Optional) Allow requesters to approve their own changes. Defaults to `false`.
- `last_pusher_cannot_approve`(Optional) Prohibit the most recent pusher from approving their own changes. Defaults to `false`.
- `allow_completion_with_rejects_or_waits` (Optional) Allow completion even if some reviewers vote to wait or reject. Defaults to `false`.
- `on_push_reset_approved_votes` (Optional) When new changes are pushed reset all approval votes (does not reset votes to reject or wait). Defaults to `false`.
- `on_push_reset_all_votes` (Optional) When new changes are pushed reset all code reviewer votes. Defaults to `false`.
- `on_last_iteration_require_vote` (Optional) On last iteration require vote. Defaults to `false`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubmitterCanVote

Allow requesters to approve their own changes. Defaults to `false`.
- `last_pusher_cannot_approve`(Optional) Prohibit the most recent pusher from approving their own changes. Defaults to `false`.
- `allow_completion_with_rejects_or_waits` (Optional) Allow completion even if some reviewers vote to wait or reject. Defaults to `false`.
- `on_push_reset_approved_votes` (Optional) When new changes are pushed reset all approval votes (does not reset votes to reject or wait). Defaults to `false`.
- `on_push_reset_all_votes` (Optional) When new changes are pushed reset all code reviewer votes. Defaults to `false`.
- `on_last_iteration_require_vote` (Optional) On last iteration require vote. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

