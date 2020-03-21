# Terraform::Gitlab::Project

This resource allows you to create and manage projects within your
GitLab group or within your user.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::Project",
    "Properties" : {
        "<a href="#approvalsbeforemerge" title="ApprovalsBeforeMerge">ApprovalsBeforeMerge</a>" : <i>Double</i>,
        "<a href="#archived" title="Archived">Archived</a>" : <i>Boolean</i>,
        "<a href="#containerregistryenabled" title="ContainerRegistryEnabled">ContainerRegistryEnabled</a>" : <i>Boolean</i>,
        "<a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#initializewithreadme" title="InitializeWithReadme">InitializeWithReadme</a>" : <i>Boolean</i>,
        "<a href="#issuesenabled" title="IssuesEnabled">IssuesEnabled</a>" : <i>Boolean</i>,
        "<a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>" : <i>Boolean</i>,
        "<a href="#mergemethod" title="MergeMethod">MergeMethod</a>" : <i>String</i>,
        "<a href="#mergerequestsenabled" title="MergeRequestsEnabled">MergeRequestsEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>Double</i>,
        "<a href="#onlyallowmergeifalldiscussionsareresolved" title="OnlyAllowMergeIfAllDiscussionsAreResolved">OnlyAllowMergeIfAllDiscussionsAreResolved</a>" : <i>Boolean</i>,
        "<a href="#onlyallowmergeifpipelinesucceeds" title="OnlyAllowMergeIfPipelineSucceeds">OnlyAllowMergeIfPipelineSucceeds</a>" : <i>Boolean</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#pipelinesenabled" title="PipelinesEnabled">PipelinesEnabled</a>" : <i>Boolean</i>,
        "<a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#sharedrunnersenabled" title="SharedRunnersEnabled">SharedRunnersEnabled</a>" : <i>Boolean</i>,
        "<a href="#snippetsenabled" title="SnippetsEnabled">SnippetsEnabled</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>" : <i>String</i>,
        "<a href="#wikienabled" title="WikiEnabled">WikiEnabled</a>" : <i>Boolean</i>,
        "<a href="#sharedwithgroups" title="SharedWithGroups">SharedWithGroups</a>" : <i>[ <a href="sharedwithgroups.md">SharedWithGroups</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::Project
Properties:
    <a href="#approvalsbeforemerge" title="ApprovalsBeforeMerge">ApprovalsBeforeMerge</a>: <i>Double</i>
    <a href="#archived" title="Archived">Archived</a>: <i>Boolean</i>
    <a href="#containerregistryenabled" title="ContainerRegistryEnabled">ContainerRegistryEnabled</a>: <i>Boolean</i>
    <a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#initializewithreadme" title="InitializeWithReadme">InitializeWithReadme</a>: <i>Boolean</i>
    <a href="#issuesenabled" title="IssuesEnabled">IssuesEnabled</a>: <i>Boolean</i>
    <a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>: <i>Boolean</i>
    <a href="#mergemethod" title="MergeMethod">MergeMethod</a>: <i>String</i>
    <a href="#mergerequestsenabled" title="MergeRequestsEnabled">MergeRequestsEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>Double</i>
    <a href="#onlyallowmergeifalldiscussionsareresolved" title="OnlyAllowMergeIfAllDiscussionsAreResolved">OnlyAllowMergeIfAllDiscussionsAreResolved</a>: <i>Boolean</i>
    <a href="#onlyallowmergeifpipelinesucceeds" title="OnlyAllowMergeIfPipelineSucceeds">OnlyAllowMergeIfPipelineSucceeds</a>: <i>Boolean</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#pipelinesenabled" title="PipelinesEnabled">PipelinesEnabled</a>: <i>Boolean</i>
    <a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>: <i>Boolean</i>
    <a href="#sharedrunnersenabled" title="SharedRunnersEnabled">SharedRunnersEnabled</a>: <i>Boolean</i>
    <a href="#snippetsenabled" title="SnippetsEnabled">SnippetsEnabled</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>: <i>String</i>
    <a href="#wikienabled" title="WikiEnabled">WikiEnabled</a>: <i>Boolean</i>
    <a href="#sharedwithgroups" title="SharedWithGroups">SharedWithGroups</a>: <i>
      - <a href="sharedwithgroups.md">SharedWithGroups</a></i>
</pre>

## Properties

#### ApprovalsBeforeMerge

Number of merge request approvals required for merging. Default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Archived

Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRegistryEnabled

Enable container registry for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBranch

The default branch for the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeWithReadme

Create master branch with first commit containing a README.md file.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuesEnabled

Enable issue tracking for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LfsEnabled

Enable LFS for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeMethod

Set to `ff` to create fast-forward merges
Valid values are `merge`, `rebase_merge`, `ff`
Repositories are created with `merge` by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsEnabled

Enable merge requests for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

The namespace (group or user) of the project. Defaults to your user.
See [`gitlab_group`](group.html) for an example.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyAllowMergeIfAllDiscussionsAreResolved

Set to true if you want allow merges only if all discussions are resolved.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyAllowMergeIfPipelineSucceeds

Set to true if you want allow merges only if a pipeline succeeds.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path of the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelinesEnabled

Enable pipelines for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAccessEnabled

Allow users to request member access.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedRunnersEnabled

Enable shared runners for this project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnippetsEnabled

Enable snippets for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags (topics) of the project.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilityLevel

Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiEnabled

Enable wiki for the project.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedWithGroups

_Required_: No

_Type_: List of <a href="sharedwithgroups.md">SharedWithGroups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### HttpUrlToRepo

Returns the <code>HttpUrlToRepo</code> value.

#### RunnersToken

Returns the <code>RunnersToken</code> value.

#### SshUrlToRepo

Returns the <code>SshUrlToRepo</code> value.

#### WebUrl

Returns the <code>WebUrl</code> value.

