# TF::OCI::OptimizerRecommendation

This resource provides the Recommendation resource in Oracle Cloud Infrastructure Optimizer service.

Updates the recommendation that corresponds to the specified OCID.
Use this operation to implement the following actions:

  * Postpone recommendation
  * Dismiss recommendation
  * Reactivate recommendation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OptimizerRecommendation",
    "Properties" : {
        "<a href="#recommendationid" title="RecommendationId">RecommendationId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#timestatusend" title="TimeStatusEnd">TimeStatusEnd</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OptimizerRecommendation
Properties:
    <a href="#recommendationid" title="RecommendationId">RecommendationId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#timestatusend" title="TimeStatusEnd">TimeStatusEnd</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### RecommendationId

The unique OCID associated with the recommendation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

(Updatable) The status of the recommendation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeStatusEnd

(Updatable) The date and time the current status will change. The format is defined by RFC3339.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CategoryId

Returns the <code>CategoryId</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### Description

Returns the <code>Description</code> value.

#### EstimatedCostSaving

Returns the <code>EstimatedCostSaving</code> value.

#### Id

Returns the <code>Id</code> value.

#### Importance

Returns the <code>Importance</code> value.

#### Name

Returns the <code>Name</code> value.

#### ResourceCounts

Returns the <code>ResourceCounts</code> value.

#### State

Returns the <code>State</code> value.

#### SupportedLevels

Returns the <code>SupportedLevels</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeStatusBegin

Returns the <code>TimeStatusBegin</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

