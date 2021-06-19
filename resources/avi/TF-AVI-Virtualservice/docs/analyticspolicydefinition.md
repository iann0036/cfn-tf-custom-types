# TF::AVI::Virtualservice AnalyticsPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allheaders" title="AllHeaders">AllHeaders</a>" : <i>Boolean</i>,
    "<a href="#clientinsights" title="ClientInsights">ClientInsights</a>" : <i>String</i>,
    "<a href="#significantlogthrottle" title="SignificantLogThrottle">SignificantLogThrottle</a>" : <i>Double</i>,
    "<a href="#udflogthrottle" title="UdfLogThrottle">UdfLogThrottle</a>" : <i>Double</i>,
    "<a href="#clientinsightssampling" title="ClientInsightsSampling">ClientInsightsSampling</a>" : <i>[ <a href="clientinsightssamplingdefinition.md">ClientInsightsSamplingDefinition</a>, ... ]</i>,
    "<a href="#clientlogfilters" title="ClientLogFilters">ClientLogFilters</a>" : <i>[ <a href="clientlogfiltersdefinition.md">ClientLogFiltersDefinition</a>, ... ]</i>,
    "<a href="#fullclientlogs" title="FullClientLogs">FullClientLogs</a>" : <i>[ <a href="fullclientlogsdefinition.md">FullClientLogsDefinition</a>, ... ]</i>,
    "<a href="#learninglogpolicy" title="LearningLogPolicy">LearningLogPolicy</a>" : <i>[ <a href="learninglogpolicydefinition.md">LearningLogPolicyDefinition</a>, ... ]</i>,
    "<a href="#metricsrealtimeupdate" title="MetricsRealtimeUpdate">MetricsRealtimeUpdate</a>" : <i>[ <a href="metricsrealtimeupdatedefinition.md">MetricsRealtimeUpdateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allheaders" title="AllHeaders">AllHeaders</a>: <i>Boolean</i>
<a href="#clientinsights" title="ClientInsights">ClientInsights</a>: <i>String</i>
<a href="#significantlogthrottle" title="SignificantLogThrottle">SignificantLogThrottle</a>: <i>Double</i>
<a href="#udflogthrottle" title="UdfLogThrottle">UdfLogThrottle</a>: <i>Double</i>
<a href="#clientinsightssampling" title="ClientInsightsSampling">ClientInsightsSampling</a>: <i>
      - <a href="clientinsightssamplingdefinition.md">ClientInsightsSamplingDefinition</a></i>
<a href="#clientlogfilters" title="ClientLogFilters">ClientLogFilters</a>: <i>
      - <a href="clientlogfiltersdefinition.md">ClientLogFiltersDefinition</a></i>
<a href="#fullclientlogs" title="FullClientLogs">FullClientLogs</a>: <i>
      - <a href="fullclientlogsdefinition.md">FullClientLogsDefinition</a></i>
<a href="#learninglogpolicy" title="LearningLogPolicy">LearningLogPolicy</a>: <i>
      - <a href="learninglogpolicydefinition.md">LearningLogPolicyDefinition</a></i>
<a href="#metricsrealtimeupdate" title="MetricsRealtimeUpdate">MetricsRealtimeUpdate</a>: <i>
      - <a href="metricsrealtimeupdatedefinition.md">MetricsRealtimeUpdateDefinition</a></i>
</pre>

## Properties

#### AllHeaders

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientInsights

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignificantLogThrottle

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdfLogThrottle

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientInsightsSampling

_Required_: No

_Type_: List of <a href="clientinsightssamplingdefinition.md">ClientInsightsSamplingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientLogFilters

_Required_: No

_Type_: List of <a href="clientlogfiltersdefinition.md">ClientLogFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullClientLogs

_Required_: No

_Type_: List of <a href="fullclientlogsdefinition.md">FullClientLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LearningLogPolicy

_Required_: No

_Type_: List of <a href="learninglogpolicydefinition.md">LearningLogPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsRealtimeUpdate

_Required_: No

_Type_: List of <a href="metricsrealtimeupdatedefinition.md">MetricsRealtimeUpdateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

