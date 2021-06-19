# TF::SumoLogic::Dashboard ColoringRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#multipleseriesaggregatefunction" title="MultipleSeriesAggregateFunction">MultipleSeriesAggregateFunction</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    "<a href="#singleseriesaggregatefunction" title="SingleSeriesAggregateFunction">SingleSeriesAggregateFunction</a>" : <i>String</i>,
    "<a href="#colorthreshold" title="ColorThreshold">ColorThreshold</a>" : <i>[ <a href="colorthresholddefinition.md">ColorThresholdDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#multipleseriesaggregatefunction" title="MultipleSeriesAggregateFunction">MultipleSeriesAggregateFunction</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
<a href="#singleseriesaggregatefunction" title="SingleSeriesAggregateFunction">SingleSeriesAggregateFunction</a>: <i>String</i>
<a href="#colorthreshold" title="ColorThreshold">ColorThreshold</a>: <i>
      - <a href="colorthresholddefinition.md">ColorThresholdDefinition</a></i>
</pre>

## Properties

#### MultipleSeriesAggregateFunction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSeriesAggregateFunction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColorThreshold

_Required_: No

_Type_: List of <a href="colorthresholddefinition.md">ColorThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

