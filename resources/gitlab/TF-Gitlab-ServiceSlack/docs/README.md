# TF::Gitlab::ServiceSlack

This resource allows you to manage Slack notifications integration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::ServiceSlack",
    "Properties" : {
        "<a href="#branchestobenotified" title="BranchesToBeNotified">BranchesToBeNotified</a>" : <i>String</i>,
        "<a href="#confidentialissuechannel" title="ConfidentialIssueChannel">ConfidentialIssueChannel</a>" : <i>String</i>,
        "<a href="#confidentialissuesevents" title="ConfidentialIssuesEvents">ConfidentialIssuesEvents</a>" : <i>Boolean</i>,
        "<a href="#confidentialnoteevents" title="ConfidentialNoteEvents">ConfidentialNoteEvents</a>" : <i>Boolean</i>,
        "<a href="#issuechannel" title="IssueChannel">IssueChannel</a>" : <i>String</i>,
        "<a href="#issuesevents" title="IssuesEvents">IssuesEvents</a>" : <i>Boolean</i>,
        "<a href="#mergerequestchannel" title="MergeRequestChannel">MergeRequestChannel</a>" : <i>String</i>,
        "<a href="#mergerequestsevents" title="MergeRequestsEvents">MergeRequestsEvents</a>" : <i>Boolean</i>,
        "<a href="#notechannel" title="NoteChannel">NoteChannel</a>" : <i>String</i>,
        "<a href="#noteevents" title="NoteEvents">NoteEvents</a>" : <i>Boolean</i>,
        "<a href="#notifyonlybrokenpipelines" title="NotifyOnlyBrokenPipelines">NotifyOnlyBrokenPipelines</a>" : <i>Boolean</i>,
        "<a href="#notifyonlydefaultbranch" title="NotifyOnlyDefaultBranch">NotifyOnlyDefaultBranch</a>" : <i>Boolean</i>,
        "<a href="#pipelinechannel" title="PipelineChannel">PipelineChannel</a>" : <i>String</i>,
        "<a href="#pipelineevents" title="PipelineEvents">PipelineEvents</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#pushchannel" title="PushChannel">PushChannel</a>" : <i>String</i>,
        "<a href="#pushevents" title="PushEvents">PushEvents</a>" : <i>Boolean</i>,
        "<a href="#tagpushchannel" title="TagPushChannel">TagPushChannel</a>" : <i>String</i>,
        "<a href="#tagpushevents" title="TagPushEvents">TagPushEvents</a>" : <i>Boolean</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>String</i>,
        "<a href="#wikipagechannel" title="WikiPageChannel">WikiPageChannel</a>" : <i>String</i>,
        "<a href="#wikipageevents" title="WikiPageEvents">WikiPageEvents</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::ServiceSlack
Properties:
    <a href="#branchestobenotified" title="BranchesToBeNotified">BranchesToBeNotified</a>: <i>String</i>
    <a href="#confidentialissuechannel" title="ConfidentialIssueChannel">ConfidentialIssueChannel</a>: <i>String</i>
    <a href="#confidentialissuesevents" title="ConfidentialIssuesEvents">ConfidentialIssuesEvents</a>: <i>Boolean</i>
    <a href="#confidentialnoteevents" title="ConfidentialNoteEvents">ConfidentialNoteEvents</a>: <i>Boolean</i>
    <a href="#issuechannel" title="IssueChannel">IssueChannel</a>: <i>String</i>
    <a href="#issuesevents" title="IssuesEvents">IssuesEvents</a>: <i>Boolean</i>
    <a href="#mergerequestchannel" title="MergeRequestChannel">MergeRequestChannel</a>: <i>String</i>
    <a href="#mergerequestsevents" title="MergeRequestsEvents">MergeRequestsEvents</a>: <i>Boolean</i>
    <a href="#notechannel" title="NoteChannel">NoteChannel</a>: <i>String</i>
    <a href="#noteevents" title="NoteEvents">NoteEvents</a>: <i>Boolean</i>
    <a href="#notifyonlybrokenpipelines" title="NotifyOnlyBrokenPipelines">NotifyOnlyBrokenPipelines</a>: <i>Boolean</i>
    <a href="#notifyonlydefaultbranch" title="NotifyOnlyDefaultBranch">NotifyOnlyDefaultBranch</a>: <i>Boolean</i>
    <a href="#pipelinechannel" title="PipelineChannel">PipelineChannel</a>: <i>String</i>
    <a href="#pipelineevents" title="PipelineEvents">PipelineEvents</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#pushchannel" title="PushChannel">PushChannel</a>: <i>String</i>
    <a href="#pushevents" title="PushEvents">PushEvents</a>: <i>Boolean</i>
    <a href="#tagpushchannel" title="TagPushChannel">TagPushChannel</a>: <i>String</i>
    <a href="#tagpushevents" title="TagPushEvents">TagPushEvents</a>: <i>Boolean</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>String</i>
    <a href="#wikipagechannel" title="WikiPageChannel">WikiPageChannel</a>: <i>String</i>
    <a href="#wikipageevents" title="WikiPageEvents">WikiPageEvents</a>: <i>Boolean</i>
</pre>

## Properties

#### BranchesToBeNotified

Branches to send notifications for. Valid options are "all", "default", "protected", and "default_and_protected".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialIssueChannel

The name of the channel to receive confidential issue events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialIssuesEvents

Enable notifications for confidential issues events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialNoteEvents

Enable notifications for confidential note events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueChannel

The name of the channel to receive issue events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuesEvents

Enable notifications for issues events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestChannel

The name of the channel to receive merge request events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsEvents

Enable notifications for merge requests events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteChannel

The name of the channel to receive note events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteEvents

Enable notifications for note events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnlyBrokenPipelines

Send notifications for broken pipelines.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnlyDefaultBranch

DEPRECATED: This parameter has been replaced with `branches_to_be_notified`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineChannel

The name of the channel to receive pipeline events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineEvents

Enable notifications for pipeline events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

ID of the project you want to activate integration on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushChannel

The name of the channel to receive push events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushEvents

Enable notifications for push events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagPushChannel

The name of the channel to receive tag push events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagPushEvents

Enable notifications for tag push events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

Webhook URL (ex.: https://hooks.slack.com/services/...).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiPageChannel

The name of the channel to receive wiki page events notifications.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiPageEvents

Enable notifications for wiki page events.

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

#### JobEvents

Returns the <code>JobEvents</code> value.

