# TF::OCI::ContainerengineCluster OptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#addons" title="AddOns">AddOns</a>" : <i>[ <a href="addonsdefinition.md">AddOnsDefinition</a>, ... ]</i>,
    "<a href="#admissioncontrolleroptions" title="AdmissionControllerOptions">AdmissionControllerOptions</a>" : <i>[ <a href="admissioncontrolleroptionsdefinition.md">AdmissionControllerOptionsDefinition</a>, ... ]</i>,
    "<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>" : <i>[ <a href="kubernetesnetworkconfigdefinition.md">KubernetesNetworkConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#servicelbsubnetids" title="ServiceLbSubnetIds">ServiceLbSubnetIds</a>: <i>
      - String</i>
<a href="#addons" title="AddOns">AddOns</a>: <i>
      - <a href="addonsdefinition.md">AddOnsDefinition</a></i>
<a href="#admissioncontrolleroptions" title="AdmissionControllerOptions">AdmissionControllerOptions</a>: <i>
      - <a href="admissioncontrolleroptionsdefinition.md">AdmissionControllerOptionsDefinition</a></i>
<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>: <i>
      - <a href="kubernetesnetworkconfigdefinition.md">KubernetesNetworkConfigDefinition</a></i>
</pre>

## Properties

#### ServiceLbSubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddOns

_Required_: No

_Type_: List of <a href="addonsdefinition.md">AddOnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdmissionControllerOptions

_Required_: No

_Type_: List of <a href="admissioncontrolleroptionsdefinition.md">AdmissionControllerOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNetworkConfig

_Required_: No

_Type_: List of <a href="kubernetesnetworkconfigdefinition.md">KubernetesNetworkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

