# TF::Dynatrace::Dashboard SeriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregation" title="Aggregation">Aggregation</a>" : <i>String</i>,
    "<a href="#aggregationrate" title="AggregationRate">AggregationRate</a>" : <i>String</i>,
    "<a href="#entitytype" title="EntityType">EntityType</a>" : <i>String</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#percentile" title="Percentile">Percentile</a>" : <i>Double</i>,
    "<a href="#sortascending" title="SortAscending">SortAscending</a>" : <i>Boolean</i>,
    "<a href="#sortcolumn" title="SortColumn">SortColumn</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ <a href="dimensiondefinition.md">DimensionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregation" title="Aggregation">Aggregation</a>: <i>String</i>
<a href="#aggregationrate" title="AggregationRate">AggregationRate</a>: <i>String</i>
<a href="#entitytype" title="EntityType">EntityType</a>: <i>String</i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#percentile" title="Percentile">Percentile</a>: <i>Double</i>
<a href="#sortascending" title="SortAscending">SortAscending</a>: <i>Boolean</i>
<a href="#sortcolumn" title="SortColumn">SortColumn</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - <a href="dimensiondefinition.md">DimensionDefinition</a></i>
</pre>

## Properties

#### Aggregation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregationRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Percentile

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortAscending

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortColumn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimension

_Required_: No

_Type_: List of <a href="dimensiondefinition.md">DimensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

