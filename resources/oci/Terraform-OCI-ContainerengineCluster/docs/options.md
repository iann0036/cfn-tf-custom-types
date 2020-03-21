# Terraform::OCI::ContainerengineCluster Options

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#addons" title="AddOns">AddOns</a>" : <i>[ <a href="options-addons.md">AddOns</a>, ... ]</i>,
    "<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>" : <i>[ <a href="options-kubernetesnetworkconfig.md">KubernetesNetworkConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>: <i>
      - String</i>
<a href="#addons" title="AddOns">AddOns</a>: <i>
      - <a href="options-addons.md">AddOns</a></i>
<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>: <i>
      - <a href="options-kubernetesnetworkconfig.md">KubernetesNetworkConfig</a></i>
</pre>

## Properties

#### ServiceLbSubnetIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddOns

_Required_: No
_Type_: List of <a href="options-addons.md">AddOns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNetworkConfig

_Required_: No
_Type_: List of <a href="options-kubernetesnetworkconfig.md">KubernetesNetworkConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

