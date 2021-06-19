# TF::AWS::AutoscalingplansScalingPlan CustomizedLoadMetricSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensionsdefinition.md">DimensionsDefinition</a>, ... ]</i>,
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#statistic" title="Statistic">Statistic</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensionsdefinition.md">DimensionsDefinition</a></i>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#statistic" title="Statistic">Statistic</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
</pre>

## Properties

#### Dimensions

The dimensions of the metric.

_Required_: No

_Type_: List of <a href="dimensionsdefinition.md">DimensionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

The name of the metric.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The namespace of the metric.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistic

The statistic of the metric. Currently, the value must always be `Sum`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

The unit of the metric.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

