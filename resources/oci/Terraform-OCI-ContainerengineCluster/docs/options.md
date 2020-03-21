# Terraform::OCI::ContainerengineCluster Options

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#addons" title="AddOns">AddOns</a>" : <i>[ &lt;a href=&#34;options-addons.md&#34;&gt;AddOns&lt;/a&gt;, ... ]</i>,
    "<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>" : <i>[ &lt;a href=&#34;options-kubernetesnetworkconfig.md&#34;&gt;KubernetesNetworkConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>: <i>
      - String</i>
<a href="#addons" title="AddOns">AddOns</a>: <i>
      - &lt;a href=&#34;options-addons.md&#34;&gt;AddOns&lt;/a&gt;</i>
<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>: <i>
      - &lt;a href=&#34;options-kubernetesnetworkconfig.md&#34;&gt;KubernetesNetworkConfig&lt;/a&gt;</i>
</pre>

## Properties

#### ServiceLbSubnetIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddOns

_Required_: No
_Type_: List of &lt;a href=&#34;options-addons.md&#34;&gt;AddOns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNetworkConfig

_Required_: No
_Type_: List of &lt;a href=&#34;options-kubernetesnetworkconfig.md&#34;&gt;KubernetesNetworkConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

