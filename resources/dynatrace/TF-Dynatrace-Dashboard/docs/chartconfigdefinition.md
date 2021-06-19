# TF::Dynatrace::Dashboard ChartConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#axislimits" title="AxisLimits">AxisLimits</a>" : <i>[ <a href="axislimitsdefinition.md">AxisLimitsDefinition</a>, ... ]</i>,
    "<a href="#leftaxiscustomunit" title="LeftAxisCustomUnit">LeftAxisCustomUnit</a>" : <i>String</i>,
    "<a href="#legend" title="Legend">Legend</a>" : <i>Boolean</i>,
    "<a href="#rightaxiscustomunit" title="RightAxisCustomUnit">RightAxisCustomUnit</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#resultmetadata" title="ResultMetadata">ResultMetadata</a>" : <i>[ <a href="resultmetadatadefinition.md">ResultMetadataDefinition</a>, ... ]</i>,
    "<a href="#series" title="Series">Series</a>" : <i>[ <a href="seriesdefinition.md">SeriesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#axislimits" title="AxisLimits">AxisLimits</a>: <i>
      - <a href="axislimitsdefinition.md">AxisLimitsDefinition</a></i>
<a href="#leftaxiscustomunit" title="LeftAxisCustomUnit">LeftAxisCustomUnit</a>: <i>String</i>
<a href="#legend" title="Legend">Legend</a>: <i>Boolean</i>
<a href="#rightaxiscustomunit" title="RightAxisCustomUnit">RightAxisCustomUnit</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#resultmetadata" title="ResultMetadata">ResultMetadata</a>: <i>
      - <a href="resultmetadatadefinition.md">ResultMetadataDefinition</a></i>
<a href="#series" title="Series">Series</a>: <i>
      - <a href="seriesdefinition.md">SeriesDefinition</a></i>
</pre>

## Properties

#### AxisLimits

_Required_: No

_Type_: List of <a href="axislimitsdefinition.md">AxisLimitsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeftAxisCustomUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Legend

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RightAxisCustomUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResultMetadata

_Required_: No

_Type_: List of <a href="resultmetadatadefinition.md">ResultMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Series

_Required_: No

_Type_: List of <a href="seriesdefinition.md">SeriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

