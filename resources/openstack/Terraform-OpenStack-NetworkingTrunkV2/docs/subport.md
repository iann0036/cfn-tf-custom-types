# Terraform::OpenStack::NetworkingTrunkV2 SubPort

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>,
    "<a href="#segmentationid" title="SegmentationId">SegmentationId</a>" : <i>Double</i>,
    "<a href="#segmentationtype" title="SegmentationType">SegmentationType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#portid" title="PortId">PortId</a>: <i>String</i>
<a href="#segmentationid" title="SegmentationId">SegmentationId</a>: <i>Double</i>
<a href="#segmentationtype" title="SegmentationType">SegmentationType</a>: <i>String</i>
</pre>

## Properties

#### PortId

The ID of the port to be made a subport of the trunk.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationId

The numeric id of the subport segment.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentationType

The segmentation technology to use, e.g., "vlan".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

