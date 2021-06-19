# TF::AzureDevOps::BranchPolicyAutoReviewers SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoreviewerids" title="AutoReviewerIds">AutoReviewerIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#message" title="Message">Message</a>" : <i>String</i>,
    "<a href="#pathfilters" title="PathFilters">PathFilters</a>" : <i>[ String, ... ]</i>,
    "<a href="#submittercanvote" title="SubmitterCanVote">SubmitterCanVote</a>" : <i>Boolean</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoreviewerids" title="AutoReviewerIds">AutoReviewerIds</a>: <i>
      - String</i>
<a href="#message" title="Message">Message</a>: <i>String</i>
<a href="#pathfilters" title="PathFilters">PathFilters</a>: <i>
      - String</i>
<a href="#submittercanvote" title="SubmitterCanVote">SubmitterCanVote</a>: <i>Boolean</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### AutoReviewerIds

Required reviewers ids. Supports multiples user Ids.
- `path_filters` - (Optional) Filter path(s) on which the policy is applied. Supports absolute paths, wildcards and multiple paths. Example: /WebApp/Models/Data.cs, /WebApp/* or *.cs,/WebApp/Models/Data.cs;ClientApp/Models/Data.cs.
- `submitter_can_vote` - (Optional) Controls whether or not the submitter's vote counts. Defaults to `false`.
- `message` - (Optional) Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathFilters

Filter path(s) on which the policy is applied. Supports absolute paths, wildcards and multiple paths. Example: /WebApp/Models/Data.cs, /WebApp/* or *.cs,/WebApp/Models/Data.cs;ClientApp/Models/Data.cs.
- `submitter_can_vote` - (Optional) Controls whether or not the submitter's vote counts. Defaults to `false`.
- `message` - (Optional) Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubmitterCanVote

Controls whether or not the submitter's vote counts. Defaults to `false`.
- `message` - (Optional) Activity feed message, Message will appear in the activity feed of pull requests with automatically added reviewers.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

