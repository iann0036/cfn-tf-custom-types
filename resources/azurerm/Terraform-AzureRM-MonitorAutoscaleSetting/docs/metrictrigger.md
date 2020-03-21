# Terraform::AzureRM::MonitorAutoscaleSetting MetricTrigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#metricresourceid" title="MetricResourceId">MetricResourceId</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#timeaggregation" title="TimeAggregation">TimeAggregation</a>" : <i>String</i>,
    "<a href="#timegrain" title="TimeGrain">TimeGrain</a>" : <i>String</i>,
    "<a href="#timewindow" title="TimeWindow">TimeWindow</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#metricresourceid" title="MetricResourceId">MetricResourceId</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#statistic" title="Statistic">Statistic</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#timeaggregation" title="TimeAggregation">TimeAggregation</a>: <i>String</i>
<a href="#timegrain" title="TimeGrain">TimeGrain</a>: <i>String</i>
<a href="#timewindow" title="TimeWindow">TimeWindow</a>: <i>String</i>
</pre>

## Properties

#### MetricName

The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricResourceId

The ID of the Resource which the Rule monitors.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Specifies the threshold of the metric that triggers the scale action.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeAggregation

Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeGrain

Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeWindow

Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

