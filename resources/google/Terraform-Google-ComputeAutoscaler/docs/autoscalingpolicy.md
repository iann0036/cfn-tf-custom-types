# Terraform::Google::ComputeAutoscaler AutoscalingPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>" : <i>Double</i>,
    "<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>" : <i>Double</i>,
    "<a href="#minreplicas" title="MinReplicas">MinReplicas</a>" : <i>Double</i>,
    "<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>" : <i>[ &lt;a href=&#34;autoscalingpolicy-cpuutilization.md&#34;&gt;CpuUtilization&lt;/a&gt;, ... ]</i>,
    "<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>" : <i>[ &lt;a href=&#34;autoscalingpolicy-loadbalancingutilization.md&#34;&gt;LoadBalancingUtilization&lt;/a&gt;, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;autoscalingpolicy-metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cooldownperiod" title="CooldownPeriod">CooldownPeriod</a>: <i>Double</i>
<a href="#maxreplicas" title="MaxReplicas">MaxReplicas</a>: <i>Double</i>
<a href="#minreplicas" title="MinReplicas">MinReplicas</a>: <i>Double</i>
<a href="#cpuutilization" title="CpuUtilization">CpuUtilization</a>: <i>
      - &lt;a href=&#34;autoscalingpolicy-cpuutilization.md&#34;&gt;CpuUtilization&lt;/a&gt;</i>
<a href="#loadbalancingutilization" title="LoadBalancingUtilization">LoadBalancingUtilization</a>: <i>
      - &lt;a href=&#34;autoscalingpolicy-loadbalancingutilization.md&#34;&gt;LoadBalancingUtilization&lt;/a&gt;</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;autoscalingpolicy-metric.md&#34;&gt;Metric&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;autoscalingpolicy-cpuutilization.md&#34;&gt;CpuUtilization&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingUtilization

_Required_: No
_Type_: List of &lt;a href=&#34;autoscalingpolicy-loadbalancingutilization.md&#34;&gt;LoadBalancingUtilization&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No
_Type_: List of &lt;a href=&#34;autoscalingpolicy-metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

