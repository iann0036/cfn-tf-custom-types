# TF::GoogleBeta::GoogleContainerCluster AddonsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudrunconfig" title="CloudrunConfig">CloudrunConfig</a>" : <i>[ <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a>, ... ]</i>,
    "<a href="#configconnectorconfig" title="ConfigConnectorConfig">ConfigConnectorConfig</a>" : <i>[ <a href="configconnectorconfigdefinition.md">ConfigConnectorConfigDefinition</a>, ... ]</i>,
    "<a href="#dnscacheconfig" title="DnsCacheConfig">DnsCacheConfig</a>" : <i>[ <a href="dnscacheconfigdefinition.md">DnsCacheConfigDefinition</a>, ... ]</i>,
    "<a href="#gcepersistentdiskcsidriverconfig" title="GcePersistentDiskCsiDriverConfig">GcePersistentDiskCsiDriverConfig</a>" : <i>[ <a href="gcepersistentdiskcsidriverconfigdefinition.md">GcePersistentDiskCsiDriverConfigDefinition</a>, ... ]</i>,
    "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a>, ... ]</i>,
    "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a>, ... ]</i>,
    "<a href="#istioconfig" title="IstioConfig">IstioConfig</a>" : <i>[ <a href="istioconfigdefinition.md">IstioConfigDefinition</a>, ... ]</i>,
    "<a href="#kalmconfig" title="KalmConfig">KalmConfig</a>" : <i>[ <a href="kalmconfigdefinition.md">KalmConfigDefinition</a>, ... ]</i>,
    "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudrunconfig" title="CloudrunConfig">CloudrunConfig</a>: <i>
      - <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a></i>
<a href="#configconnectorconfig" title="ConfigConnectorConfig">ConfigConnectorConfig</a>: <i>
      - <a href="configconnectorconfigdefinition.md">ConfigConnectorConfigDefinition</a></i>
<a href="#dnscacheconfig" title="DnsCacheConfig">DnsCacheConfig</a>: <i>
      - <a href="dnscacheconfigdefinition.md">DnsCacheConfigDefinition</a></i>
<a href="#gcepersistentdiskcsidriverconfig" title="GcePersistentDiskCsiDriverConfig">GcePersistentDiskCsiDriverConfig</a>: <i>
      - <a href="gcepersistentdiskcsidriverconfigdefinition.md">GcePersistentDiskCsiDriverConfigDefinition</a></i>
<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a></i>
<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a></i>
<a href="#istioconfig" title="IstioConfig">IstioConfig</a>: <i>
      - <a href="istioconfigdefinition.md">IstioConfigDefinition</a></i>
<a href="#kalmconfig" title="KalmConfig">KalmConfig</a>: <i>
      - <a href="kalmconfigdefinition.md">KalmConfigDefinition</a></i>
<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a></i>
</pre>

## Properties

#### CloudrunConfig

_Required_: No

_Type_: List of <a href="cloudrunconfigdefinition.md">CloudrunConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigConnectorConfig

_Required_: No

_Type_: List of <a href="configconnectorconfigdefinition.md">ConfigConnectorConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsCacheConfig

_Required_: No

_Type_: List of <a href="dnscacheconfigdefinition.md">DnsCacheConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcePersistentDiskCsiDriverConfig

_Required_: No

_Type_: List of <a href="gcepersistentdiskcsidriverconfigdefinition.md">GcePersistentDiskCsiDriverConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HorizontalPodAutoscaling

_Required_: No

_Type_: List of <a href="horizontalpodautoscalingdefinition.md">HorizontalPodAutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No

_Type_: List of <a href="httploadbalancingdefinition.md">HttpLoadBalancingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IstioConfig

_Required_: No

_Type_: List of <a href="istioconfigdefinition.md">IstioConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KalmConfig

_Required_: No

_Type_: List of <a href="kalmconfigdefinition.md">KalmConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No

_Type_: List of <a href="networkpolicyconfigdefinition.md">NetworkPolicyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

