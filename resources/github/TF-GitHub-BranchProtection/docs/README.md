# TF::GitHub::BranchProtection

Protects a GitHub branch.

This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users, teams, and apps, can also be configured.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GitHub::BranchProtection",
    "Properties" : {
        "<a href="#allowsdeletions" title="AllowsDeletions">AllowsDeletions</a>" : <i>Boolean</i>,
        "<a href="#allowsforcepushes" title="AllowsForcePushes">AllowsForcePushes</a>" : <i>Boolean</i>,
        "<a href="#enforceadmins" title="EnforceAdmins">EnforceAdmins</a>" : <i>Boolean</i>,
        "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
        "<a href="#pushrestrictions" title="PushRestrictions">PushRestrictions</a>" : <i>[ String, ... ]</i>,
        "<a href="#repositoryid" title="RepositoryId">RepositoryId</a>" : <i>String</i>,
        "<a href="#requiresignedcommits" title="RequireSignedCommits">RequireSignedCommits</a>" : <i>Boolean</i>,
        "<a href="#requiredpullrequestreviews" title="RequiredPullRequestReviews">RequiredPullRequestReviews</a>" : <i>[ <a href="requiredpullrequestreviewsdefinition.md">RequiredPullRequestReviewsDefinition</a>, ... ]</i>,
        "<a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>" : <i>[ <a href="requiredstatuschecksdefinition.md">RequiredStatusChecksDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GitHub::BranchProtection
Properties:
    <a href="#allowsdeletions" title="AllowsDeletions">AllowsDeletions</a>: <i>Boolean</i>
    <a href="#allowsforcepushes" title="AllowsForcePushes">AllowsForcePushes</a>: <i>Boolean</i>
    <a href="#enforceadmins" title="EnforceAdmins">EnforceAdmins</a>: <i>Boolean</i>
    <a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
    <a href="#pushrestrictions" title="PushRestrictions">PushRestrictions</a>: <i>
      - String</i>
    <a href="#repositoryid" title="RepositoryId">RepositoryId</a>: <i>String</i>
    <a href="#requiresignedcommits" title="RequireSignedCommits">RequireSignedCommits</a>: <i>Boolean</i>
    <a href="#requiredpullrequestreviews" title="RequiredPullRequestReviews">RequiredPullRequestReviews</a>: <i>
      - <a href="requiredpullrequestreviewsdefinition.md">RequiredPullRequestReviewsDefinition</a></i>
    <a href="#requiredstatuschecks" title="RequiredStatusChecks">RequiredStatusChecks</a>: <i>
      - <a href="requiredstatuschecksdefinition.md">RequiredStatusChecksDefinition</a></i>
</pre>

## Properties

#### AllowsDeletions

Boolean, setting this to `true` to allow the branch to be deleted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowsForcePushes

Boolean, setting this to `true` to allow force pushes on the branch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceAdmins

Boolean, setting this to `true` enforces status checks for repository administrators.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

Identifies the protection rule pattern.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PushRestrictions

The list of actor IDs that may push to the branch.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryId

The name or node ID of the repository associated with this branch protection rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireSignedCommits

Boolean, setting this to `true` requires all commits to be signed with GPG.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredPullRequestReviews

_Required_: No

_Type_: List of <a href="requiredpullrequestreviewsdefinition.md">RequiredPullRequestReviewsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredStatusChecks

_Required_: No

_Type_: List of <a href="requiredstatuschecksdefinition.md">RequiredStatusChecksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

