# TF::AzureDevOps::RepositoryPolicyAuthorEmailPattern SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authoremailpatterns" title="AuthorEmailPatterns">AuthorEmailPatterns</a>" : <i>[ String, ... ]</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authoremailpatterns" title="AuthorEmailPatterns">AuthorEmailPatterns</a>: <i>
      - String</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### AuthorEmailPatterns

Block pushes with a commit author email that does not match the patterns. You can specify exact emails or use wildcards.
Email patterns prefixed with "!" are excluded. Order is important.
- `scope` (Required) Controls which repositories and branches the policy will be enabled for. This block must be defined
at least once.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

