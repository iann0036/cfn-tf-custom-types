# TF::GoogleBeta::GoogleMonitoringSlo WindowsBasedSliDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#goodbadmetricfilter" title="GoodBadMetricFilter">GoodBadMetricFilter</a>" : <i>String</i>,
    "<a href="#windowperiod" title="WindowPeriod">WindowPeriod</a>" : <i>String</i>,
    "<a href="#goodtotalratiothreshold" title="GoodTotalRatioThreshold">GoodTotalRatioThreshold</a>" : <i>[ <a href="goodtotalratiothresholddefinition.md">GoodTotalRatioThresholdDefinition</a>, ... ]</i>,
    "<a href="#metricmeaninrange" title="MetricMeanInRange">MetricMeanInRange</a>" : <i>[ <a href="metricmeaninrangedefinition.md">MetricMeanInRangeDefinition</a>, ... ]</i>,
    "<a href="#metricsuminrange" title="MetricSumInRange">MetricSumInRange</a>" : <i>[ <a href="metricsuminrangedefinition.md">MetricSumInRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#goodbadmetricfilter" title="GoodBadMetricFilter">GoodBadMetricFilter</a>: <i>String</i>
<a href="#windowperiod" title="WindowPeriod">WindowPeriod</a>: <i>String</i>
<a href="#goodtotalratiothreshold" title="GoodTotalRatioThreshold">GoodTotalRatioThreshold</a>: <i>
      - <a href="goodtotalratiothresholddefinition.md">GoodTotalRatioThresholdDefinition</a></i>
<a href="#metricmeaninrange" title="MetricMeanInRange">MetricMeanInRange</a>: <i>
      - <a href="metricmeaninrangedefinition.md">MetricMeanInRangeDefinition</a></i>
<a href="#metricsuminrange" title="MetricSumInRange">MetricSumInRange</a>: <i>
      - <a href="metricsuminrangedefinition.md">MetricSumInRangeDefinition</a></i>
</pre>

## Properties

#### GoodBadMetricFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowPeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoodTotalRatioThreshold

_Required_: No

_Type_: List of <a href="goodtotalratiothresholddefinition.md">GoodTotalRatioThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricMeanInRange

_Required_: No

_Type_: List of <a href="metricmeaninrangedefinition.md">MetricMeanInRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricSumInRange

_Required_: No

_Type_: List of <a href="metricsuminrangedefinition.md">MetricSumInRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

