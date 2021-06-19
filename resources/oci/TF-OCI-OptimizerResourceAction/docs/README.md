# TF::OCI::OptimizerResourceAction

This resource provides the Resource Action resource in Oracle Cloud Infrastructure Optimizer service.

Updates the resource action that corresponds to the specified OCID. 
Use this operation to implement the following actions:

  * Postpone resource action
  * Ignore resource action
  * Reactivate resource action

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::OptimizerResourceAction",
    "Properties" : {
        "<a href="#resourceactionid" title="ResourceActionId">ResourceActionId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#timestatusend" title="TimeStatusEnd">TimeStatusEnd</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::OptimizerResourceAction
Properties:
    <a href="#resourceactionid" title="ResourceActionId">ResourceActionId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#timestatusend" title="TimeStatusEnd">TimeStatusEnd</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ResourceActionId

The unique OCID associated with the resource action.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

(Updatable) The status of the resource action.

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

#### Action

Returns the <code>Action</code> value.

#### CategoryId

Returns the <code>CategoryId</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### CompartmentName

Returns the <code>CompartmentName</code> value.

#### EstimatedCostSaving

Returns the <code>EstimatedCostSaving</code> value.

#### ExtendedMetadata

Returns the <code>ExtendedMetadata</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Name

Returns the <code>Name</code> value.

#### RecommendationId

Returns the <code>RecommendationId</code> value.

#### ResourceId

Returns the <code>ResourceId</code> value.

#### ResourceType

Returns the <code>ResourceType</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeStatusBegin

Returns the <code>TimeStatusBegin</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

