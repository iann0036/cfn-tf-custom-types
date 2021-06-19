# TF::Kubernetes::HorizontalPodAutoscaler SpecDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#targetcpuutilizationpercentage" title="TargetCpuUtilizationPercentage">TargetCpuUtilizationPercentage</a>" : <i>Double</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>,
    "<a href="#scaletargetref" title="ScaleTargetRef">ScaleTargetRef</a>" : <i>[ <a href="scaletargetrefdefinition.md">ScaleTargetRefDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#targetcpuutilizationpercentage" title="TargetCpuUtilizationPercentage">TargetCpuUtilizationPercentage</a>: <i>Double</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
<a href="#scaletargetref" title="ScaleTargetRef">ScaleTargetRef</a>: <i>
      - <a href="scaletargetrefdefinition.md">ScaleTargetRefDefinition</a></i>
</pre>

## Properties

#### MaxReplicas

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinReplicas

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCpuUtilizationPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleTargetRef

_Required_: No

_Type_: List of <a href="scaletargetrefdefinition.md">ScaleTargetRefDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

