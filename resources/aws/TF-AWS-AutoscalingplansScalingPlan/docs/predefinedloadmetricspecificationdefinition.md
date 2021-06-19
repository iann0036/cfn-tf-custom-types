# TF::AWS::AutoscalingplansScalingPlan PredefinedLoadMetricSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#predefinedloadmetrictype" title="PredefinedLoadMetricType">PredefinedLoadMetricType</a>" : <i>String</i>,
    "<a href="#resourcelabel" title="ResourceLabel">ResourceLabel</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#predefinedloadmetrictype" title="PredefinedLoadMetricType">PredefinedLoadMetricType</a>: <i>String</i>
<a href="#resourcelabel" title="ResourceLabel">ResourceLabel</a>: <i>String</i>
</pre>

## Properties

#### PredefinedLoadMetricType

The metric type. Valid values: `ALBTargetGroupRequestCount`, `ASGTotalCPUUtilization`, `ASGTotalNetworkIn`, `ASGTotalNetworkOut`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLabel

Identifies the resource associated with the metric type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

