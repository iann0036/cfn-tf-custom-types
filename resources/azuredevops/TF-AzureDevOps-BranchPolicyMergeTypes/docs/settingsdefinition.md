# TF::AzureDevOps::BranchPolicyMergeTypes SettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowbasicnofastforward" title="AllowBasicNoFastForward">AllowBasicNoFastForward</a>" : <i>Boolean</i>,
    "<a href="#allowrebaseandfastforward" title="AllowRebaseAndFastForward">AllowRebaseAndFastForward</a>" : <i>Boolean</i>,
    "<a href="#allowrebasewithmerge" title="AllowRebaseWithMerge">AllowRebaseWithMerge</a>" : <i>Boolean</i>,
    "<a href="#allowsquash" title="AllowSquash">AllowSquash</a>" : <i>Boolean</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ <a href="scopedefinition.md">ScopeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowbasicnofastforward" title="AllowBasicNoFastForward">AllowBasicNoFastForward</a>: <i>Boolean</i>
<a href="#allowrebaseandfastforward" title="AllowRebaseAndFastForward">AllowRebaseAndFastForward</a>: <i>Boolean</i>
<a href="#allowrebasewithmerge" title="AllowRebaseWithMerge">AllowRebaseWithMerge</a>: <i>Boolean</i>
<a href="#allowsquash" title="AllowSquash">AllowSquash</a>: <i>Boolean</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - <a href="scopedefinition.md">ScopeDefinition</a></i>
</pre>

## Properties

#### AllowBasicNoFastForward

Allow basic merge with no fast forward. Defaults to `false`.
- `allow_rebase_with_merge` - (Optional) Allow rebase with merge commit. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRebaseAndFastForward

Allow rebase with fast forward. Defaults to `false`.
- `allow_basic_no_fast_forward` - (Optional) Allow basic merge with no fast forward. Defaults to `false`.
- `allow_rebase_with_merge` - (Optional) Allow rebase with merge commit. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRebaseWithMerge

Allow rebase with merge commit. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSquash

Allow squash merge. Defaults to `false`
- `allow_rebase_and_fast_forward` - (Optional) Allow rebase with fast forward. Defaults to `false`.
- `allow_basic_no_fast_forward` - (Optional) Allow basic merge with no fast forward. Defaults to `false`.
- `allow_rebase_with_merge` - (Optional) Allow rebase with merge commit. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No

_Type_: List of <a href="scopedefinition.md">ScopeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

