# TF::AzureDevOps::BranchPolicyBuildValidation SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#builddefinitionid" title="BuildDefinitionId">BuildDefinitionId</a>" : <i>Double</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#filenamepatterns" title="FilenamePatterns">FilenamePatterns</a>" : <i>[ String, ... ]</i>,
    "<a href="#manualqueueonly" title="ManualQueueOnly">ManualQueueOnly</a>" : <i>Boolean</i>,
    "<a href="#queueonsourceupdateonly" title="QueueOnSourceUpdateOnly">QueueOnSourceUpdateOnly</a>" : <i>Boolean</i>,
    "<a href="#validduration" title="ValidDuration">ValidDuration</a>" : <i>Double</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#builddefinitionid" title="BuildDefinitionId">BuildDefinitionId</a>: <i>Double</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#filenamepatterns" title="FilenamePatterns">FilenamePatterns</a>: <i>
      - String</i>
<a href="#manualqueueonly" title="ManualQueueOnly">ManualQueueOnly</a>: <i>Boolean</i>
<a href="#queueonsourceupdateonly" title="QueueOnSourceUpdateOnly">QueueOnSourceUpdateOnly</a>: <i>Boolean</i>
<a href="#validduration" title="ValidDuration">ValidDuration</a>: <i>Double</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### BuildDefinitionId

The ID of the build to monitor for the policy.
- `display_name` - (Required) The display name for the policy.
- `manual_queue_only` - (Optional) If set to true, the build will need to be manually queued. Defaults to `false`
- `queue_on_source_update_only` - (Optional) True if the build should queue on source updates only. Defaults to `true`.
- `valid_duration` - (Optional) The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name for the policy.
- `manual_queue_only` - (Optional) If set to true, the build will need to be manually queued. Defaults to `false`
- `queue_on_source_update_only` - (Optional) True if the build should queue on source updates only. Defaults to `true`.
- `valid_duration` - (Optional) The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilenamePatterns

If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManualQueueOnly

If set to true, the build will need to be manually queued. Defaults to `false`
- `queue_on_source_update_only` - (Optional) True if the build should queue on source updates only. Defaults to `true`.
- `valid_duration` - (Optional) The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueueOnSourceUpdateOnly

True if the build should queue on source updates only. Defaults to `true`.
- `valid_duration` - (Optional) The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidDuration

The number of minutes for which the build is valid. If `0`, the build will not expire. Defaults to `720` (12 hours).
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

