# TF::AVI::Cloud DataNetworkConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#transportzone" title="TransportZone">TransportZone</a>" : <i>String</i>,
    "<a href="#tztype" title="TzType">TzType</a>" : <i>String</i>,
    "<a href="#vlansegments" title="VlanSegments">VlanSegments</a>" : <i>[ String, ... ]</i>,
    "<a href="#tier1segmentconfig" title="Tier1SegmentConfig">Tier1SegmentConfig</a>" : <i>[ <a href="tier1segmentconfigdefinition.md">Tier1SegmentConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#transportzone" title="TransportZone">TransportZone</a>: <i>String</i>
<a href="#tztype" title="TzType">TzType</a>: <i>String</i>
<a href="#vlansegments" title="VlanSegments">VlanSegments</a>: <i>
      - String</i>
<a href="#tier1segmentconfig" title="Tier1SegmentConfig">Tier1SegmentConfig</a>: <i>
      - <a href="tier1segmentconfigdefinition.md">Tier1SegmentConfigDefinition</a></i>
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

#### VlanSegments

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier1SegmentConfig

_Required_: No

_Type_: List of <a href="tier1segmentconfigdefinition.md">Tier1SegmentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

