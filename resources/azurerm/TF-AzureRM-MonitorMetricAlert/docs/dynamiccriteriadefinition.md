# TF::AzureRM::MonitorMetricAlert DynamicCriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregation" title="Aggregation">Aggregation</a>" : <i>String</i>,
    "<a href="#alertsensitivity" title="AlertSensitivity">AlertSensitivity</a>" : <i>String</i>,
    "<a href="#evaluationfailurecount" title="EvaluationFailureCount">EvaluationFailureCount</a>" : <i>Double</i>,
    "<a href="#evaluationtotalcount" title="EvaluationTotalCount">EvaluationTotalCount</a>" : <i>Double</i>,
    "<a href="#ignoredatabefore" title="IgnoreDataBefore">IgnoreDataBefore</a>" : <i>String</i>,
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#metricnamespace" title="MetricNamespace">MetricNamespace</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#skipmetricvalidation" title="SkipMetricValidation">SkipMetricValidation</a>" : <i>Boolean</i>,
    "<a href="#dimension" title="Dimension">Dimension</a>" : <i>[ <a href="dimensiondefinition.md">DimensionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregation" title="Aggregation">Aggregation</a>: <i>String</i>
<a href="#alertsensitivity" title="AlertSensitivity">AlertSensitivity</a>: <i>String</i>
<a href="#evaluationfailurecount" title="EvaluationFailureCount">EvaluationFailureCount</a>: <i>Double</i>
<a href="#evaluationtotalcount" title="EvaluationTotalCount">EvaluationTotalCount</a>: <i>Double</i>
<a href="#ignoredatabefore" title="IgnoreDataBefore">IgnoreDataBefore</a>: <i>String</i>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#metricnamespace" title="MetricNamespace">MetricNamespace</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#skipmetricvalidation" title="SkipMetricValidation">SkipMetricValidation</a>: <i>Boolean</i>
<a href="#dimension" title="Dimension">Dimension</a>: <i>
      - <a href="dimensiondefinition.md">DimensionDefinition</a></i>
</pre>

## Properties

#### Aggregation

The statistic that runs over the metric values. Possible values are `Average`, `Count`, `Minimum`, `Maximum` and `Total`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertSensitivity

The extent of deviation required to trigger an alert. Possible values are `Low`, `Medium` and `High`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationFailureCount

The number of violations to trigger an alert. Should be smaller or equal to `evaluation_total_count`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationTotalCount

The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (`window_size`) and the selected number of aggregated points.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDataBefore

The [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date from which to start learning the metric historical data and calculate the dynamic thresholds.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

One of the metric names to be monitored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricNamespace

One of the metric namespaces to be monitored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

The criteria operator. Possible values are `LessThan`, `GreaterThan` and `GreaterOrLessThan`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipMetricValidation

Skip the metric validation to allow creating an alert rule on a custom metric that isn't yet emitted? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimension

_Required_: No

_Type_: List of <a href="dimensiondefinition.md">DimensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

