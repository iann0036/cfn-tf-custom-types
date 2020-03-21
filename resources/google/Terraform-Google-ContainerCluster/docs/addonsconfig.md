# Terraform::Google::ContainerCluster AddonsConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ <a href="addonsconfig-horizontalpodautoscaling.md">HorizontalPodAutoscaling</a>, ... ]</i>,
    "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ <a href="addonsconfig-httploadbalancing.md">HttpLoadBalancing</a>, ... ]</i>,
    "<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>" : <i>[ <a href="addonsconfig-kubernetesdashboard.md">KubernetesDashboard</a>, ... ]</i>,
    "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ <a href="addonsconfig-networkpolicyconfig.md">NetworkPolicyConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - <a href="addonsconfig-horizontalpodautoscaling.md">HorizontalPodAutoscaling</a></i>
<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - <a href="addonsconfig-httploadbalancing.md">HttpLoadBalancing</a></i>
<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>: <i>
      - <a href="addonsconfig-kubernetesdashboard.md">KubernetesDashboard</a></i>
<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - <a href="addonsconfig-networkpolicyconfig.md">NetworkPolicyConfig</a></i>
</pre>

## Properties

#### HorizontalPodAutoscaling

_Required_: No

_Type_: List of <a href="addonsconfig-horizontalpodautoscaling.md">HorizontalPodAutoscaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No

_Type_: List of <a href="addonsconfig-httploadbalancing.md">HttpLoadBalancing</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesDashboard

_Required_: No

_Type_: List of <a href="addonsconfig-kubernetesdashboard.md">KubernetesDashboard</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No

_Type_: List of <a href="addonsconfig-networkpolicyconfig.md">NetworkPolicyConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

