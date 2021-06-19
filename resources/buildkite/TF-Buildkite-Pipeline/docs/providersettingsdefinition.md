# TF::Buildkite::Pipeline ProviderSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buildbranches" title="BuildBranches">BuildBranches</a>" : <i>Boolean</i>,
    "<a href="#buildpullrequestforks" title="BuildPullRequestForks">BuildPullRequestForks</a>" : <i>Boolean</i>,
    "<a href="#buildpullrequestreadyforreview" title="BuildPullRequestReadyForReview">BuildPullRequestReadyForReview</a>" : <i>Boolean</i>,
    "<a href="#buildpullrequests" title="BuildPullRequests">BuildPullRequests</a>" : <i>Boolean</i>,
    "<a href="#buildtags" title="BuildTags">BuildTags</a>" : <i>Boolean</i>,
    "<a href="#canceldeletedbranchbuilds" title="CancelDeletedBranchBuilds">CancelDeletedBranchBuilds</a>" : <i>Boolean</i>,
    "<a href="#prefixpullrequestforkbranchnames" title="PrefixPullRequestForkBranchNames">PrefixPullRequestForkBranchNames</a>" : <i>Boolean</i>,
    "<a href="#publishblockedaspending" title="PublishBlockedAsPending">PublishBlockedAsPending</a>" : <i>Boolean</i>,
    "<a href="#publishcommitstatus" title="PublishCommitStatus">PublishCommitStatus</a>" : <i>Boolean</i>,
    "<a href="#publishcommitstatusperstep" title="PublishCommitStatusPerStep">PublishCommitStatusPerStep</a>" : <i>Boolean</i>,
    "<a href="#pullrequestbranchfilterconfiguration" title="PullRequestBranchFilterConfiguration">PullRequestBranchFilterConfiguration</a>" : <i>String</i>,
    "<a href="#pullrequestbranchfilterenabled" title="PullRequestBranchFilterEnabled">PullRequestBranchFilterEnabled</a>" : <i>Boolean</i>,
    "<a href="#separatepullrequeststatuses" title="SeparatePullRequestStatuses">SeparatePullRequestStatuses</a>" : <i>Boolean</i>,
    "<a href="#skippullrequestbuildsforexistingcommits" title="SkipPullRequestBuildsForExistingCommits">SkipPullRequestBuildsForExistingCommits</a>" : <i>Boolean</i>,
    "<a href="#triggermode" title="TriggerMode">TriggerMode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#buildbranches" title="BuildBranches">BuildBranches</a>: <i>Boolean</i>
<a href="#buildpullrequestforks" title="BuildPullRequestForks">BuildPullRequestForks</a>: <i>Boolean</i>
<a href="#buildpullrequestreadyforreview" title="BuildPullRequestReadyForReview">BuildPullRequestReadyForReview</a>: <i>Boolean</i>
<a href="#buildpullrequests" title="BuildPullRequests">BuildPullRequests</a>: <i>Boolean</i>
<a href="#buildtags" title="BuildTags">BuildTags</a>: <i>Boolean</i>
<a href="#canceldeletedbranchbuilds" title="CancelDeletedBranchBuilds">CancelDeletedBranchBuilds</a>: <i>Boolean</i>
<a href="#prefixpullrequestforkbranchnames" title="PrefixPullRequestForkBranchNames">PrefixPullRequestForkBranchNames</a>: <i>Boolean</i>
<a href="#publishblockedaspending" title="PublishBlockedAsPending">PublishBlockedAsPending</a>: <i>Boolean</i>
<a href="#publishcommitstatus" title="PublishCommitStatus">PublishCommitStatus</a>: <i>Boolean</i>
<a href="#publishcommitstatusperstep" title="PublishCommitStatusPerStep">PublishCommitStatusPerStep</a>: <i>Boolean</i>
<a href="#pullrequestbranchfilterconfiguration" title="PullRequestBranchFilterConfiguration">PullRequestBranchFilterConfiguration</a>: <i>String</i>
<a href="#pullrequestbranchfilterenabled" title="PullRequestBranchFilterEnabled">PullRequestBranchFilterEnabled</a>: <i>Boolean</i>
<a href="#separatepullrequeststatuses" title="SeparatePullRequestStatuses">SeparatePullRequestStatuses</a>: <i>Boolean</i>
<a href="#skippullrequestbuildsforexistingcommits" title="SkipPullRequestBuildsForExistingCommits">SkipPullRequestBuildsForExistingCommits</a>: <i>Boolean</i>
<a href="#triggermode" title="TriggerMode">TriggerMode</a>: <i>String</i>
</pre>

## Properties

#### BuildBranches

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildPullRequestForks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildPullRequestReadyForReview

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildPullRequests

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CancelDeletedBranchBuilds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixPullRequestForkBranchNames

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishBlockedAsPending

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishCommitStatus

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishCommitStatusPerStep

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullRequestBranchFilterConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullRequestBranchFilterEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeparatePullRequestStatuses

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipPullRequestBuildsForExistingCommits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

