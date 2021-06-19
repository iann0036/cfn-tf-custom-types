# TF::Google::ContainerCluster AddonsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudrunconfig" title="CloudrunConfig">CloudrunConfig</a>" : <i>[ <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a>, ... ]</i>,
    "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a>, ... ]</i>,
    "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a>, ... ]</i>,
    "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudrunconfig" title="CloudrunConfig">CloudrunConfig</a>: <i>
      - <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a></i>
<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a></i>
<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a></i>
<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a></i>
</pre>

## Properties

#### CloudrunConfig

_Required_: No

_Type_: List of <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HorizontalPodAutoscaling

_Required_: No

_Type_: List of <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No

_Type_: List of <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No

_Type_: List of <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

