# TF::GitHub::BranchProtection RequiredPullRequestReviewsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dismissstalereviews" title="DismissStaleReviews">DismissStaleReviews</a>" : <i>Boolean</i>,
    "<a href="#dismissalrestrictions" title="DismissalRestrictions">DismissalRestrictions</a>" : <i>[ String, ... ]</i>,
    "<a href="#requirecodeownerreviews" title="RequireCodeOwnerReviews">RequireCodeOwnerReviews</a>" : <i>Boolean</i>,
    "<a href="#requiredapprovingreviewcount" title="RequiredApprovingReviewCount">RequiredApprovingReviewCount</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dismissstalereviews" title="DismissStaleReviews">DismissStaleReviews</a>: <i>Boolean</i>
<a href="#dismissalrestrictions" title="DismissalRestrictions">DismissalRestrictions</a>: <i>
      - String</i>
<a href="#requirecodeownerreviews" title="RequireCodeOwnerReviews">RequireCodeOwnerReviews</a>: <i>Boolean</i>
<a href="#requiredapprovingreviewcount" title="RequiredApprovingReviewCount">RequiredApprovingReviewCount</a>: <i>Double</i>
</pre>

## Properties

#### DismissStaleReviews

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DismissalRestrictions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireCodeOwnerReviews

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredApprovingReviewCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

