# Terraform::Google::ComputeAutoscaler AutoscalingPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>" : <i>Double</i>,
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>" : <i>[ <a href="autoscalingpolicy-cpuutilization.md">CpuUtilization</a>, ... ]</i>,
    "<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>" : <i>[ <a href="autoscalingpolicy-loadbalancingutilization.md">LoadBalancingUtilization</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="autoscalingpolicy-metric.md">Metric</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>: <i>Double</i>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>: <i>
      - <a href="autoscalingpolicy-cpuutilization.md">CpuUtilization</a></i>
<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>: <i>
      - <a href="autoscalingpolicy-loadbalancingutilization.md">LoadBalancingUtilization</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="autoscalingpolicy-metric.md">Metric</a></i>
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

#### CpuUtilization

_Required_: No

_Type_: List of <a href="autoscalingpolicy-cpuutilization.md">CpuUtilization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingUtilization

_Required_: No

_Type_: List of <a href="autoscalingpolicy-loadbalancingutilization.md">LoadBalancingUtilization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="autoscalingpolicy-metric.md">Metric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

