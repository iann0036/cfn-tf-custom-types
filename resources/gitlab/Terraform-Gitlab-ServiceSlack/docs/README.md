# Terraform::Gitlab::ServiceSlack

CloudFormation equivalent of gitlab_service_slack

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ServiceSlack",
    "Properties" : {
        "<a href="#confidentialissuechannel" title="ConfidentialIssueChannel">ConfidentialIssueChannel</a>" : <i>String</i>,
        "<a href="#confidentialissuesevents" title="ConfidentialIssuesEvents">ConfidentialIssuesEvents</a>" : <i>Boolean</i>,
        "<a href="#confidentialnoteevents" title="ConfidentialNoteEvents">ConfidentialNoteEvents</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
Type: Terraform::Gitlab::ServiceSlack
Properties:
    <a href="#confidentialissuechannel" title="ConfidentialIssueChannel">ConfidentialIssueChannel</a>: <i>String</i>
    <a href="#confidentialissuesevents" title="ConfidentialIssuesEvents">ConfidentialIssuesEvents</a>: <i>Boolean</i>
    <a href="#confidentialnoteevents" title="ConfidentialNoteEvents">ConfidentialNoteEvents</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

#### ConfidentialIssueChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialIssuesEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialNoteEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuesEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnlyBrokenPipelines

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOnlyDefaultBranch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagPushChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagPushEvents

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiPageChannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiPageEvents

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

#### JobEvents

Returns the &lt;code&gt;JobEvents&lt;/code&gt; value.

