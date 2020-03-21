# Terraform::Gitlab::Project

CloudFormation equivalent of gitlab_project

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
        "<a href="#sharedwithgroups" title="SharedWithGroups">SharedWithGroups</a>" : <i>[ &lt;a href=&#34;sharedwithgroups.md&#34;&gt;SharedWithGroups&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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
      - &lt;a href=&#34;sharedwithgroups.md&#34;&gt;SharedWithGroups&lt;/a&gt;</i>
</pre>

## Properties

#### ApprovalsBeforeMerge

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Archived

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRegistryEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBranch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeWithReadme

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssuesEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LfsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MergeRequestsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyAllowMergeIfAllDiscussionsAreResolved

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnlyAllowMergeIfPipelineSucceeds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelinesEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAccessEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedRunnersEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnippetsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilityLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WikiEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedWithGroups

_Required_: No

_Type_: List of &lt;a href=&#34;sharedwithgroups.md&#34;&gt;SharedWithGroups&lt;/a&gt;

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

Returns the &lt;code&gt;HttpUrlToRepo&lt;/code&gt; value.

#### RunnersToken

Returns the &lt;code&gt;RunnersToken&lt;/code&gt; value.

#### SshUrlToRepo

Returns the &lt;code&gt;SshUrlToRepo&lt;/code&gt; value.

#### WebUrl

Returns the &lt;code&gt;WebUrl&lt;/code&gt; value.

