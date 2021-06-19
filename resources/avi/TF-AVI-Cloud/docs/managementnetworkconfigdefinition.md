# TF::AVI::Cloud ManagementNetworkConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#transportzone" title="TransportZone">TransportZone</a>" : <i>String</i>,
    "<a href="#tztype" title="TzType">TzType</a>" : <i>String</i>,
    "<a href="#vlansegment" title="VlanSegment">VlanSegment</a>" : <i>String</i>,
    "<a href="#overlaysegment" title="OverlaySegment">OverlaySegment</a>" : <i>[ <a href="overlaysegmentdefinition.md">OverlaySegmentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#transportzone" title="TransportZone">TransportZone</a>: <i>String</i>
<a href="#tztype" title="TzType">TzType</a>: <i>String</i>
<a href="#vlansegment" title="VlanSegment">VlanSegment</a>: <i>String</i>
<a href="#overlaysegment" title="OverlaySegment">OverlaySegment</a>: <i>
      - <a href="overlaysegmentdefinition.md">OverlaySegmentDefinition</a></i>
</pre>

## Properties

#### TransportZone

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TzType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanSegment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverlaySegment

_Required_: No

_Type_: List of <a href="overlaysegmentdefinition.md">OverlaySegmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

