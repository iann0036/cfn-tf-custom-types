# Terraform::Gitlab::ProjectHook

This resource allows you to create and manage hooks for your GitLab projects.
For further information on hooks, consult the [gitlab
documentation](https://docs.gitlab.com/ce/user/project/integrations/webhooks.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::ProjectHook",
    "Properties" : {
        "<a href="#enablesslverification" title="EnableSslVerification">EnableSslVerification</a>" : <i>Boolean</i>,
        "<a href="#issuesevents" title="IssuesEvents">IssuesEvents</a>" : <i>Boolean</i>,
        "<a href="#jobevents" title="JobEvents">JobEvents</a>" : <i>Boolean</i>,
        "<a href="#mergerequestsevents" title="MergeRequestsEvents">MergeRequestsEvents</a>" : <i>Boolean</i>,
        "<a href="#noteevents" title="NoteEvents">NoteEvents</a>" : <i>Boolean</i>,
        "<a href="#pipelineevents" title="PipelineEvents">PipelineEvents</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#pushevents" title="PushEvents">PushEvents</a>" : <i>Boolean</i>,
        "<a href="#tagpushevents" title="TagPushEvents">TagPushEvents</a>" : <i>Boolean</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#wikipageevents" title="WikiPageEvents">WikiPageEvents</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::ProjectHook
Properties:
    <a href="#enablesslverification" title="EnableSslVerification">EnableSslVerification</a>: <i>Boolean</i>
    <a href="#issuesevents" title="IssuesEvents">IssuesEvents</a>: <i>Boolean</i>
    <a href="#jobevents" title="JobEvents">JobEvents</a>: <i>Boolean</i>
    <a href="#mergerequestsevents" title="MergeRequestsEvents">MergeRequestsEvents</a>: <i>Boolean</i>
    <a href="#noteevents" title="NoteEvents">NoteEvents</a>: <i>Boolean</i>
    <a href="#pipelineevents" title="PipelineEvents">PipelineEvents</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#pushevents" title="PushEvents">PushEvents</a>: <i>Boolean</i>
    <a href="#tagpushevents" title="TagPushEvents">TagPushEvents</a>: <i>Boolean</i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#wikipageevents" title="WikiPageEvents">WikiPageEvents</a>: <i>Boolean</i>
</pre>

## Properties

#### EnableSslVerification

Enable ssl verification when invoking
the hook.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuesEvents

Invoke the hook for issues events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobEvents

Invoke the hook for job events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsEvents

Invoke the hook for merge requests.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoteEvents

Invoke the hook for notes events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelineEvents

Invoke the hook for pipeline events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or id of the project to add the hook to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushEvents

Invoke the hook for push events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagPushEvents

Invoke the hook for tag push events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

A token to present when invoking the hook.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The url of the hook to invoke.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiPageEvents

Invoke the hook for wiki page events.

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

