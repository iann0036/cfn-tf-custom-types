# TF::AWS::CloudwatchMetricAlarm

Provides a CloudWatch Metric Alarm resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchMetricAlarm",
    "Properties" : {
        "<a href="#actionsenabled" title="ActionsEnabled">ActionsEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmactions" title="AlarmActions">AlarmActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>" : <i>String</i>,
        "<a href="#alarmname" title="AlarmName">AlarmName</a>" : <i>String</i>,
        "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
        "<a href="#datapointstoalarm" title="DatapointsToAlarm">DatapointsToAlarm</a>" : <i>Double</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensionsdefinition.md">DimensionsDefinition</a>, ... ]</i>,
        "<a href="#evaluatelowsamplecountpercentiles" title="EvaluateLowSampleCountPercentiles">EvaluateLowSampleCountPercentiles</a>" : <i>String</i>,
        "<a href="#evaluationperiods" title="EvaluationPeriods">EvaluationPeriods</a>" : <i>Double</i>,
        "<a href="#extendedstatistic" title="ExtendedStatistic">ExtendedStatistic</a>" : <i>String</i>,
        "<a href="#insufficientdataactions" title="InsufficientDataActions">InsufficientDataActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#okactions" title="OkActions">OkActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
        "<a href="#thresholdmetricid" title="ThresholdMetricId">ThresholdMetricId</a>" : <i>String</i>,
        "<a href="#treatmissingdata" title="TreatMissingData">TreatMissingData</a>" : <i>String</i>,
        "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
        "<a href="#metricquery" title="MetricQuery">MetricQuery</a>" : <i>[ <a href="metricquerydefinition.md">MetricQueryDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchMetricAlarm
Properties:
    <a href="#actionsenabled" title="ActionsEnabled">ActionsEnabled</a>: <i>Boolean</i>
    <a href="#alarmactions" title="AlarmActions">AlarmActions</a>: <i>
      - String</i>
    <a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>: <i>String</i>
    <a href="#alarmname" title="AlarmName">AlarmName</a>: <i>String</i>
    <a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
    <a href="#datapointstoalarm" title="DatapointsToAlarm">DatapointsToAlarm</a>: <i>Double</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensionsdefinition.md">DimensionsDefinition</a></i>
    <a href="#evaluatelowsamplecountpercentiles" title="EvaluateLowSampleCountPercentiles">EvaluateLowSampleCountPercentiles</a>: <i>String</i>
    <a href="#evaluationperiods" title="EvaluationPeriods">EvaluationPeriods</a>: <i>Double</i>
    <a href="#extendedstatistic" title="ExtendedStatistic">ExtendedStatistic</a>: <i>String</i>
    <a href="#insufficientdataactions" title="InsufficientDataActions">InsufficientDataActions</a>: <i>
      - String</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#okactions" title="OkActions">OkActions</a>: <i>
      - String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#statistic" title="Statistic">Statistic</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
    <a href="#thresholdmetricid" title="ThresholdMetricId">ThresholdMetricId</a>: <i>String</i>
    <a href="#treatmissingdata" title="TreatMissingData">TreatMissingData</a>: <i>String</i>
    <a href="#unit" title="Unit">Unit</a>: <i>String</i>
    <a href="#metricquery" title="MetricQuery">MetricQuery</a>: <i>
      - <a href="metricquerydefinition.md">MetricQueryDefinition</a></i>
</pre>

## Properties

#### ActionsEnabled

Indicates whether or not actions should be executed during any changes to the alarm's state. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmActions

The list of actions to execute when this alarm transitions into an ALARM state from any other state. Each action is specified as an Amazon Resource Name (ARN).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmDescription

The description for the alarm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmName

The descriptive name for the alarm. This name must be unique within the user's AWS account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComparisonOperator

The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Either of the following is supported: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`. Additionally, the values  `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, and `GreaterThanUpperThreshold` are used only for alarms based on anomaly detection models.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatapointsToAlarm

The number of datapoints that must be breaching to trigger the alarm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

The dimensions for the alarm's associated metric.  For the list of available dimensions see the AWS documentation [here](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

_Required_: No

_Type_: List of <a href="dimensionsdefinition.md">DimensionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluateLowSampleCountPercentiles

Used only for alarms
based on percentiles. If you specify `ignore`, the alarm state will not
change during periods with too few data points to be statistically significant.
If you specify `evaluate` or omit this parameter, the alarm will always be
evaluated and possibly change state no matter how many data points are available.
The following values are supported: `ignore`, and `evaluate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationPeriods

The number of periods over which data is compared to the specified threshold.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStatistic

The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientDataActions

The list of actions to execute when this alarm transitions into an INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

The name for the alarm's associated metric.
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The namespace for the alarm's associated metric. See docs for the [list of namespaces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/aws-namespaces.html).
See docs for [supported metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OkActions

The list of actions to execute when this alarm transitions into an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The period in seconds over which the specified `statistic` is applied.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

The statistic to apply to the alarm's associated metric.
Either of the following is supported: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

The value against which the specified statistic is compared. This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdMetricId

If this is an alarm based on an anomaly detection model, make this value match the ID of the ANOMALY_DETECTION_BAND function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TreatMissingData

Sets how this alarm is to handle missing data points. The following values are supported: `missing`, `ignore`, `breaching` and `notBreaching`. Defaults to `missing`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

The unit for the alarm's associated metric.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricQuery

_Required_: No

_Type_: List of <a href="metricquerydefinition.md">MetricQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

