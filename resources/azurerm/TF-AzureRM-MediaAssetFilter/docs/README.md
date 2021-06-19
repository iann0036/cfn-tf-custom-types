# TF::AzureRM::MediaAssetFilter

Manages an Azure Media Asset Filter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::MediaAssetFilter",
    "Properties" : {
        "<a href="#assetid" title="AssetId">AssetId</a>" : <i>String</i>,
        "<a href="#firstqualitybitrate" title="FirstQualityBitrate">FirstQualityBitrate</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#presentationtimerange" title="PresentationTimeRange">PresentationTimeRange</a>" : <i>[ <a href="presentationtimerangedefinition.md">PresentationTimeRangeDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#trackselection" title="TrackSelection">TrackSelection</a>" : <i>[ <a href="trackselectiondefinition.md">TrackSelectionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::MediaAssetFilter
Properties:
    <a href="#assetid" title="AssetId">AssetId</a>: <i>String</i>
    <a href="#firstqualitybitrate" title="FirstQualityBitrate">FirstQualityBitrate</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#presentationtimerange" title="PresentationTimeRange">PresentationTimeRange</a>: <i>
      - <a href="presentationtimerangedefinition.md">PresentationTimeRangeDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#trackselection" title="TrackSelection">TrackSelection</a>: <i>
      - <a href="trackselectiondefinition.md">TrackSelectionDefinition</a></i>
</pre>

## Properties

#### AssetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstQualityBitrate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresentationTimeRange

_Required_: No

_Type_: List of <a href="presentationtimerangedefinition.md">PresentationTimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackSelection

_Required_: No

_Type_: List of <a href="trackselectiondefinition.md">TrackSelectionDefinition</a>

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

