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
        "<a href="#requiredpullrequestreviews" title="RequiredPullRequestReviews">RequiredPullRequestReviews</a>" : <i>[ <a href="requiredpullrequestreviews.md">RequiredPullRequestReviews</a>, ... ]</i>,
        "<a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>" : <i>[ <a href="requiredstatuschecks.md">RequiredStatusChecks</a>, ... ]</i>,
        "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="restrictions.md">Restrictions</a>, ... ]</i>
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
      - <a href="requiredpullrequestreviews.md">RequiredPullRequestReviews</a></i>
    <a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>: <i>
      - <a href="requiredstatuschecks.md">RequiredStatusChecks</a></i>
    <a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="restrictions.md">Restrictions</a></i>
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

_Type_: List of <a href="requiredpullrequestreviews.md">RequiredPullRequestReviews</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredStatusChecks

_Required_: No

_Type_: List of <a href="requiredstatuschecks.md">RequiredStatusChecks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="restrictions.md">Restrictions</a>

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

Returns the <code>Etag</code> value.

