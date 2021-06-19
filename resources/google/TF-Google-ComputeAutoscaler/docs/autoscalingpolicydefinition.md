# TF::Google::ComputeAutoscaler AutoscalingPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>" : <i>Double</i>,
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>" : <i>[ <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a>, ... ]</i>,
    "<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>" : <i>[ <a href="loadbalancingutilizationdefinition.md">LoadBalancingUtilizationDefinition</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>,
    "<a href="#scaleincontrol" title="ScaleInControl">ScaleInControl</a>" : <i>[ <a href="scaleincontroldefinition.md">ScaleInControlDefinition</a>, ... ]</i>,
    "<a href="#scalingschedules" title="ScalingSchedules">ScalingSchedules</a>" : <i>[ <a href="scalingschedulesdefinition.md">ScalingSchedulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>: <i>Double</i>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>: <i>
      - <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a></i>
<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>: <i>
      - <a href="loadbalancingutilizationdefinition.md">LoadBalancingUtilizationDefinition</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
<a href="#scaleincontrol" title="ScaleInControl">ScaleInControl</a>: <i>
      - <a href="scaleincontroldefinition.md">ScaleInControlDefinition</a></i>
<a href="#scalingschedules" title="ScalingSchedules">ScalingSchedules</a>: <i>
      - <a href="scalingschedulesdefinition.md">ScalingSchedulesDefinition</a></i>
</pre>

## Properties

#### CooldownPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxReplicas

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinReplicas

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuUtilization

_Required_: No

_Type_: List of <a href="cpuutilizationdefinition.md">CpuUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingUtilization

_Required_: No

_Type_: List of <a href="loadbalancingutilizationdefinition.md">LoadBalancingUtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScaleInControl

_Required_: No

_Type_: List of <a href="scaleincontroldefinition.md">ScaleInControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingSchedules

_Required_: No

_Type_: List of <a href="scalingschedulesdefinition.md">ScalingSchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

