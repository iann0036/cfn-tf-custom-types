# Terraform::GitHub::BranchProtection

CloudFormation equivalent of github_branch_protection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::GitHub::BranchProtection",
    "Properties" : {
        "<a href="#branch" title="Branch">Branch</a>" : <i>String</i>,
        "<a href="#enforceadmins" title="EnforceAdmins">EnforceAdmins</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#requiresignedcommits" title="RequireSignedCommits">RequireSignedCommits</a>" : <i>Boolean</i>,
        "<a href="#requiredpullrequestreviews" title="RequiredPullRequestReviews">RequiredPullRequestReviews</a>" : <i>[ &lt;a href=&#34;requiredpullrequestreviews.md&#34;&gt;RequiredPullRequestReviews&lt;/a&gt;, ... ]</i>,
        "<a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>" : <i>[ &lt;a href=&#34;requiredstatuschecks.md&#34;&gt;RequiredStatusChecks&lt;/a&gt;, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::GitHub::BranchProtection
Properties:
    <a href="#branch" title="Branch">Branch</a>: <i>String</i>
    <a href="#enforceadmins" title="EnforceAdmins">EnforceAdmins</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#requiresignedcommits" title="RequireSignedCommits">RequireSignedCommits</a>: <i>Boolean</i>
    <a href="#requiredpullrequestreviews" title="RequiredPullRequestReviews">RequiredPullRequestReviews</a>: <i>
      - &lt;a href=&#34;requiredpullrequestreviews.md&#34;&gt;RequiredPullRequestReviews&lt;/a&gt;</i>
    <a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>: <i>
      - &lt;a href=&#34;requiredstatuschecks.md&#34;&gt;RequiredStatusChecks&lt;/a&gt;</i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
</pre>

## Properties

#### Branch

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceAdmins

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSignedCommits

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredPullRequestReviews

_Required_: No

_Type_: List of &lt;a href=&#34;requiredpullrequestreviews.md&#34;&gt;RequiredPullRequestReviews&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredStatusChecks

_Required_: No

_Type_: List of &lt;a href=&#34;requiredstatuschecks.md&#34;&gt;RequiredStatusChecks&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of &lt;a href=&#34;restrictions.md&#34;&gt;Restrictions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the &lt;code&gt;Etag&lt;/code&gt; value.

