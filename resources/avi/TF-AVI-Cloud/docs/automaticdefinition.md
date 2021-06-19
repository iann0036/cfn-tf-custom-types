# TF::AVI::Cloud AutomaticDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#numsepersegment" title="NumSePerSegment">NumSePerSegment</a>" : <i>Double</i>,
    "<a href="#tier1lrids" title="Tier1LrIds">Tier1LrIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#nsxtsegmentsubnet" title="NsxtSegmentSubnet">NsxtSegmentSubnet</a>" : <i>[ <a href="nsxtsegmentsubnetdefinition.md">NsxtSegmentSubnetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#numsepersegment" title="NumSePerSegment">NumSePerSegment</a>: <i>Double</i>
<a href="#tier1lrids" title="Tier1LrIds">Tier1LrIds</a>: <i>
      - String</i>
<a href="#nsxtsegmentsubnet" title="NsxtSegmentSubnet">NsxtSegmentSubnet</a>: <i>
      - <a href="nsxtsegmentsubnetdefinition.md">NsxtSegmentSubnetDefinition</a></i>
</pre>

## Properties

#### NumSePerSegment

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier1LrIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtSegmentSubnet

_Required_: No

_Type_: List of <a href="nsxtsegmentsubnetdefinition.md">NsxtSegmentSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

