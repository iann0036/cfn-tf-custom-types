# TF::AWS::AutoscalingPolicy MetricSpecificationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#targetvalue" title="TargetValue">TargetValue</a>" : <i>Double</i>,
    "<a href="#predefinedloadmetricspecification" title="PredefinedLoadMetricSpecification">PredefinedLoadMetricSpecification</a>" : <i>[ <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a>, ... ]</i>,
    "<a href="#predefinedmetricpairspecification" title="PredefinedMetricPairSpecification">PredefinedMetricPairSpecification</a>" : <i>[ <a href="predefinedmetricpairspecificationdefinition.md">PredefinedMetricPairSpecificationDefinition</a>, ... ]</i>,
    "<a href="#predefinedscalingmetricspecification" title="PredefinedScalingMetricSpecification">PredefinedScalingMetricSpecification</a>" : <i>[ <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#targetvalue" title="TargetValue">TargetValue</a>: <i>Double</i>
<a href="#predefinedloadmetricspecification" title="PredefinedLoadMetricSpecification">PredefinedLoadMetricSpecification</a>: <i>
      - <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a></i>
<a href="#predefinedmetricpairspecification" title="PredefinedMetricPairSpecification">PredefinedMetricPairSpecification</a>: <i>
      - <a href="predefinedmetricpairspecificationdefinition.md">PredefinedMetricPairSpecificationDefinition</a></i>
<a href="#predefinedscalingmetricspecification" title="PredefinedScalingMetricSpecification">PredefinedScalingMetricSpecification</a>: <i>
      - <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a></i>
</pre>

## Properties

#### TargetValue

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedLoadMetricSpecification

_Required_: No

_Type_: List of <a href="predefinedloadmetricspecificationdefinition.md">PredefinedLoadMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedMetricPairSpecification

_Required_: No

_Type_: List of <a href="predefinedmetricpairspecificationdefinition.md">PredefinedMetricPairSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedScalingMetricSpecification

_Required_: No

_Type_: List of <a href="predefinedscalingmetricspecificationdefinition.md">PredefinedScalingMetricSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

