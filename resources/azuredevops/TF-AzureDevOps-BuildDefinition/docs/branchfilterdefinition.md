# TF::AzureDevOps::BuildDefinition BranchFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exclude" title="Exclude">Exclude</a>" : <i>[ String, ... ]</i>,
    "<a href="#include" title="Include">Include</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exclude" title="Exclude">Exclude</a>: <i>
      - String</i>
<a href="#include" title="Include">Include</a>: <i>
      - String</i>
</pre>

## Properties

#### Exclude

List of branch patterns to exclude.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Include

List of branch patterns to include.
- `exclude` - (Optional) List of branch patterns to exclude.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

