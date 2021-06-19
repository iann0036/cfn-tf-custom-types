# TF::AzureDevOps::BuildDefinition OverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autocancel" title="AutoCancel">AutoCancel</a>" : <i>Boolean</i>,
    "<a href="#branchfilter" title="BranchFilter">BranchFilter</a>" : <i>[ <a href="branchfilterdefinition.md">BranchFilterDefinition</a>, ... ]</i>,
    "<a href="#pathfilter" title="PathFilter">PathFilter</a>" : <i>[ <a href="pathfilterdefinition.md">PathFilterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autocancel" title="AutoCancel">AutoCancel</a>: <i>Boolean</i>
<a href="#branchfilter" title="BranchFilter">BranchFilter</a>: <i>
      - <a href="branchfilterdefinition.md">BranchFilterDefinition</a></i>
<a href="#pathfilter" title="PathFilter">PathFilter</a>: <i>
      - <a href="pathfilterdefinition.md">PathFilterDefinition</a></i>
</pre>

## Properties

#### AutoCancel

. Defaults to `true`.
- `branch_filter` - (Optional) The branches to include and exclude from the trigger.
- `path_filter` - (Optional) Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BranchFilter

_Required_: No

_Type_: List of <a href="branchfilterdefinition.md">BranchFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathFilter

_Required_: No

_Type_: List of <a href="pathfilterdefinition.md">PathFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

