# Terraform::AWS::CloudwatchMetricAlarm

CloudFormation equivalent of aws_cloudwatch_metric_alarm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudwatchMetricAlarm",
    "Properties" : {
        "<a href="#actionsenabled" title="ActionsEnabled">ActionsEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmactions" title="AlarmActions">AlarmActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>" : <i>String</i>,
        "<a href="#alarmname" title="AlarmName">AlarmName</a>" : <i>String</i>,
        "<a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>" : <i>String</i>,
        "<a href="#datapointstoalarm" title="DatapointsToAlarm">DatapointsToAlarm</a>" : <i>Double</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>,
        "<a href="#evaluatelowsamplecountpercentiles" title="EvaluateLowSampleCountPercentiles">EvaluateLowSampleCountPercentiles</a>" : <i>String</i>,
        "<a href="#evaluationperiods" title="EvaluationPeriods">EvaluationPeriods</a>" : <i>Double</i>,
        "<a href="#extendedstatistic" title="ExtendedStatistic">ExtendedStatistic</a>" : <i>String</i>,
        "<a href="#insufficientdataactions" title="InsufficientDataActions">InsufficientDataActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#okactions" title="OkActions">OkActions</a>" : <i>[ String, ... ]</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
        "<a href="#thresholdmetricid" title="ThresholdMetricId">ThresholdMetricId</a>" : <i>String</i>,
        "<a href="#treatmissingdata" title="TreatMissingData">TreatMissingData</a>" : <i>String</i>,
        "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
        "<a href="#metricquery" title="MetricQuery">MetricQuery</a>" : <i>[ <a href="metricquery.md">MetricQuery</a>, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metric.md">Metric</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudwatchMetricAlarm
Properties:
    <a href="#actionsenabled" title="ActionsEnabled">ActionsEnabled</a>: <i>Boolean</i>
    <a href="#alarmactions" title="AlarmActions">AlarmActions</a>: <i>
      - String</i>
    <a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>: <i>String</i>
    <a href="#alarmname" title="AlarmName">AlarmName</a>: <i>String</i>
    <a href="#comparisonoperator" title="ComparisonOperator">ComparisonOperator</a>: <i>String</i>
    <a href="#datapointstoalarm" title="DatapointsToAlarm">DatapointsToAlarm</a>: <i>Double</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
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
      - <a href="tags.md">Tags</a></i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
    <a href="#thresholdmetricid" title="ThresholdMetricId">ThresholdMetricId</a>: <i>String</i>
    <a href="#treatmissingdata" title="TreatMissingData">TreatMissingData</a>: <i>String</i>
    <a href="#unit" title="Unit">Unit</a>: <i>String</i>
    <a href="#metricquery" title="MetricQuery">MetricQuery</a>: <i>
      - <a href="metricquery.md">MetricQuery</a></i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metric.md">Metric</a></i>
</pre>

## Properties

#### ActionsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmActions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComparisonOperator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatapointsToAlarm

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluateLowSampleCountPercentiles

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationPeriods

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStatistic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientDataActions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OkActions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdMetricId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TreatMissingData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricQuery

_Required_: No

_Type_: List of <a href="metricquery.md">MetricQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metric.md">Metric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

