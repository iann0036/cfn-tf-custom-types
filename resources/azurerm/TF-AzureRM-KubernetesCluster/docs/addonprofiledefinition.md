# TF::AzureRM::KubernetesCluster AddonProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>" : <i>[ <a href="aciconnectorlinuxdefinition.md">AciConnectorLinuxDefinition</a>, ... ]</i>,
    "<a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>" : <i>[ <a href="azurepolicydefinition.md">AzurePolicyDefinition</a>, ... ]</i>,
    "<a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>" : <i>[ <a href="httpapplicationroutingdefinition.md">HttpApplicationRoutingDefinition</a>, ... ]</i>,
    "<a href="#ingressapplicationgateway" title="IngressApplicationGateway">IngressApplicationGateway</a>" : <i>[ <a href="ingressapplicationgatewaydefinition.md">IngressApplicationGatewayDefinition</a>, ... ]</i>,
    "<a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>" : <i>[ <a href="kubedashboarddefinition.md">KubeDashboardDefinition</a>, ... ]</i>,
    "<a href="#omsagent" title="OmsAgent">OmsAgent</a>" : <i>[ <a href="omsagentdefinition.md">OmsAgentDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aciconnectorlinux" title="AciConnectorLinux">AciConnectorLinux</a>: <i>
      - <a href="aciconnectorlinuxdefinition.md">AciConnectorLinuxDefinition</a></i>
<a href="#azurepolicy" title="AzurePolicy">AzurePolicy</a>: <i>
      - <a href="azurepolicydefinition.md">AzurePolicyDefinition</a></i>
<a href="#httpapplicationrouting" title="HttpApplicationRouting">HttpApplicationRouting</a>: <i>
      - <a href="httpapplicationroutingdefinition.md">HttpApplicationRoutingDefinition</a></i>
<a href="#ingressapplicationgateway" title="IngressApplicationGateway">IngressApplicationGateway</a>: <i>
      - <a href="ingressapplicationgatewaydefinition.md">IngressApplicationGatewayDefinition</a></i>
<a href="#kubedashboard" title="KubeDashboard">KubeDashboard</a>: <i>
      - <a href="kubedashboarddefinition.md">KubeDashboardDefinition</a></i>
<a href="#omsagent" title="OmsAgent">OmsAgent</a>: <i>
      - <a href="omsagentdefinition.md">OmsAgentDefinition</a></i>
</pre>

## Properties

#### AciConnectorLinux

_Required_: No

_Type_: List of <a href="aciconnectorlinuxdefinition.md">AciConnectorLinuxDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurePolicy

_Required_: No

_Type_: List of <a href="azurepolicydefinition.md">AzurePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpApplicationRouting

_Required_: No

_Type_: List of <a href="httpapplicationroutingdefinition.md">HttpApplicationRoutingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressApplicationGateway

_Required_: No

_Type_: List of <a href="ingressapplicationgatewaydefinition.md">IngressApplicationGatewayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDashboard

_Required_: No

_Type_: List of <a href="kubedashboarddefinition.md">KubeDashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OmsAgent

_Required_: No

_Type_: List of <a href="omsagentdefinition.md">OmsAgentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

