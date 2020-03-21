# Terraform::Google::MonitoringAlertPolicy ConditionThreshold

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comparison" title="Comparison">Comparison</a>" : <i>String</i>,
    "<a href="#denominatorfilter" title="DenominatorFilter">DenominatorFilter</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#thresholdvalue" title="ThresholdValue">ThresholdValue</a>" : <i>Double</i>,
    "<a href="#aggregations" title="Aggregations">Aggregations</a>" : <i>[ &lt;a href=&#34;conditionthreshold-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;, ... ]</i>,
    "<a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>" : <i>[ &lt;a href=&#34;conditionthreshold-denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;, ... ]</i>,
    "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ &lt;a href=&#34;conditionthreshold-trigger.md&#34;&gt;Trigger&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comparison" title="Comparison">Comparison</a>: <i>String</i>
<a href="#denominatorfilter" title="DenominatorFilter">DenominatorFilter</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#thresholdvalue" title="ThresholdValue">ThresholdValue</a>: <i>Double</i>
<a href="#aggregations" title="Aggregations">Aggregations</a>: <i>
      - &lt;a href=&#34;conditionthreshold-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;</i>
<a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>: <i>
      - &lt;a href=&#34;conditionthreshold-denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;</i>
<a href="#trigger" title="Trigger">Trigger</a>: <i>
      - &lt;a href=&#34;conditionthreshold-trigger.md&#34;&gt;Trigger&lt;/a&gt;</i>
</pre>

## Properties

#### Comparison

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenominatorFilter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdValue

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregations

_Required_: No
_Type_: List of &lt;a href=&#34;conditionthreshold-aggregations.md&#34;&gt;Aggregations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenominatorAggregations

_Required_: No
_Type_: List of &lt;a href=&#34;conditionthreshold-denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No
_Type_: List of &lt;a href=&#34;conditionthreshold-trigger.md&#34;&gt;Trigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

