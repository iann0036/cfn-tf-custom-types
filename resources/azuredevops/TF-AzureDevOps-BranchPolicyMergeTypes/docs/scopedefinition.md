# TF::AzureDevOps::BranchPolicyMergeTypes ScopeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>String</i>,
    "<a href="#repositoryid" title="RepositoryId">RepositoryId</a>" : <i>String</i>,
    "<a href="#repositoryref" title="RepositoryRef">RepositoryRef</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#matchtype" title="MatchType">MatchType</a>: <i>String</i>
<a href="#repositoryid" title="RepositoryId">RepositoryId</a>: <i>String</i>
<a href="#repositoryref" title="RepositoryRef">RepositoryRef</a>: <i>String</i>
</pre>

## Properties

#### MatchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryId

The repository ID. Needed only if the scope of the policy will be limited to a single repository.
- `repository_ref` - (Optional) The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
- `match_type` (Optional) The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryRef

The ref pattern to use for the match. If `match_type` is `Exact`, this should be a qualified ref such as `refs/heads/master`. If `match_type` is `Prefix`, this should be a ref path such as `refs/heads/releases`.
- `match_type` (Optional) The match type to use when applying the policy. Supported values are `Exact` (default) or `Prefix`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

