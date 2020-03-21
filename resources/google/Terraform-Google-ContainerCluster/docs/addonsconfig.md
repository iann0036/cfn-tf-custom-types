# Terraform::Google::ContainerCluster AddonsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ &lt;a href=&#34;addonsconfig-horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;, ... ]</i>,
    "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ &lt;a href=&#34;addonsconfig-httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;, ... ]</i>,
    "<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>" : <i>[ &lt;a href=&#34;addonsconfig-kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;, ... ]</i>,
    "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ &lt;a href=&#34;addonsconfig-networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - &lt;a href=&#34;addonsconfig-horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;</i>
<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - &lt;a href=&#34;addonsconfig-httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;</i>
<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>: <i>
      - &lt;a href=&#34;addonsconfig-kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;</i>
<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - &lt;a href=&#34;addonsconfig-networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;</i>
</pre>

## Properties

#### HorizontalPodAutoscaling

_Required_: No
_Type_: List of &lt;a href=&#34;addonsconfig-horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No
_Type_: List of &lt;a href=&#34;addonsconfig-httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesDashboard

_Required_: No
_Type_: List of &lt;a href=&#34;addonsconfig-kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No
_Type_: List of &lt;a href=&#34;addonsconfig-networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

