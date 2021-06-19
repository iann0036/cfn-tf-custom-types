# TF::AzureDevOps::BranchPolicyStatusCheck SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicability" title="Applicability">Applicability</a>" : <i>String</i>,
    "<a href="#authorid" title="AuthorId">AuthorId</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#filenamepatterns" title="FilenamePatterns">FilenamePatterns</a>" : <i>[ String, ... ]</i>,
    "<a href="#invalidateonupdate" title="InvalidateOnUpdate">InvalidateOnUpdate</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#applicability" title="Applicability">Applicability</a>: <i>String</i>
<a href="#authorid" title="AuthorId">AuthorId</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#filenamepatterns" title="FilenamePatterns">FilenamePatterns</a>: <i>
      - String</i>
<a href="#invalidateonupdate" title="InvalidateOnUpdate">InvalidateOnUpdate</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### Applicability

Policy applicability. If policy `applicability` is `default`, apply unless "Not Applicable"
status is posted to the pull request. If policy `applicability` is `conditional`, policy is applied only after a status
is posted to the pull request.
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `display_name` - (Optional) The display name.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorId

The authorized user can post the status.
- `invalidate_on_update` - (Optional) Reset status whenever there are new changes.
- `applicability` - (Optional) Policy applicability. If policy `applicability` is `default`, apply unless "Not Applicable"
status is posted to the pull request. If policy `applicability` is `conditional`, policy is applied only after a status
is posted to the pull request.
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `display_name` - (Optional) The display name.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilenamePatterns

If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `display_name` - (Optional) The display name.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvalidateOnUpdate

Reset status whenever there are new changes.
- `applicability` - (Optional) Policy applicability. If policy `applicability` is `default`, apply unless "Not Applicable"
status is posted to the pull request. If policy `applicability` is `conditional`, policy is applied only after a status
is posted to the pull request.
- `filename_patterns` - (Optional) If a path filter is set, the policy will only apply when files which match the filter are changes. Not setting this field means that the policy will always apply. You can specify absolute paths and wildcards. Example: `["/WebApp/Models/Data.cs", "/WebApp/*", "*.cs"]`. Paths prefixed with "!" are excluded. Example: `["/WebApp/*", "!/WebApp/Tests/*"]`. Order is significant.
- `display_name` - (Optional) The display name.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

