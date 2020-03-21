# Terraform::HuaweiCloud::NetworkingNetworkV2 Segments

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
    "<a href="#physicalnetwork" title="PhysicalNetwork">PhysicalNetwork</a>" : <i>String</i>,
    "<a href="#segmentationid" title="SegmentationId">SegmentationId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
<a href="#physicalnetwork" title="PhysicalNetwork">PhysicalNetwork</a>: <i>String</i>
<a href="#segmentationid" title="SegmentationId">SegmentationId</a>: <i>Double</i>
</pre>

## Properties

#### NetworkType

The type of physical network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalNetwork

The phisical network where this network is implemented.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationId

An isolated segment on the physical network.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

