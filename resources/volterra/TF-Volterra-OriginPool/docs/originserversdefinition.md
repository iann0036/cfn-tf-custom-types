# TF::Volterra::OriginPool OriginServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#consulservice" title="ConsulService">ConsulService</a>" : <i>[ <a href="consulservicedefinition.md">ConsulServiceDefinition</a>, ... ]</i>,
    "<a href="#customendpointobject" title="CustomEndpointObject">CustomEndpointObject</a>" : <i>[ <a href="customendpointobjectdefinition.md">CustomEndpointObjectDefinition</a>, ... ]</i>,
    "<a href="#k8sservice" title="K8sService">K8sService</a>" : <i>[ <a href="k8sservicedefinition.md">K8sServiceDefinition</a>, ... ]</i>,
    "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>[ <a href="privateipdefinition.md">PrivateIpDefinition</a>, ... ]</i>,
    "<a href="#privatename" title="PrivateName">PrivateName</a>" : <i>[ <a href="privatenamedefinition.md">PrivateNameDefinition</a>, ... ]</i>,
    "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ <a href="publicipdefinition.md">PublicIpDefinition</a>, ... ]</i>,
    "<a href="#publicname" title="PublicName">PublicName</a>" : <i>[ <a href="publicnamedefinition.md">PublicNameDefinition</a>, ... ]</i>,
    "<a href="#vnprivateip" title="VnPrivateIp">VnPrivateIp</a>" : <i>[ <a href="vnprivateipdefinition.md">VnPrivateIpDefinition</a>, ... ]</i>,
    "<a href="#vnprivatename" title="VnPrivateName">VnPrivateName</a>" : <i>[ <a href="vnprivatenamedefinition.md">VnPrivateNameDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#consulservice" title="ConsulService">ConsulService</a>: <i>
      - <a href="consulservicedefinition.md">ConsulServiceDefinition</a></i>
<a href="#customendpointobject" title="CustomEndpointObject">CustomEndpointObject</a>: <i>
      - <a href="customendpointobjectdefinition.md">CustomEndpointObjectDefinition</a></i>
<a href="#k8sservice" title="K8sService">K8sService</a>: <i>
      - <a href="k8sservicedefinition.md">K8sServiceDefinition</a></i>
<a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>
      - <a href="privateipdefinition.md">PrivateIpDefinition</a></i>
<a href="#privatename" title="PrivateName">PrivateName</a>: <i>
      - <a href="privatenamedefinition.md">PrivateNameDefinition</a></i>
<a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - <a href="publicipdefinition.md">PublicIpDefinition</a></i>
<a href="#publicname" title="PublicName">PublicName</a>: <i>
      - <a href="publicnamedefinition.md">PublicNameDefinition</a></i>
<a href="#vnprivateip" title="VnPrivateIp">VnPrivateIp</a>: <i>
      - <a href="vnprivateipdefinition.md">VnPrivateIpDefinition</a></i>
<a href="#vnprivatename" title="VnPrivateName">VnPrivateName</a>: <i>
      - <a href="vnprivatenamedefinition.md">VnPrivateNameDefinition</a></i>
</pre>

## Properties

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsulService

_Required_: No

_Type_: List of <a href="consulservicedefinition.md">ConsulServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomEndpointObject

_Required_: No

_Type_: List of <a href="customendpointobjectdefinition.md">CustomEndpointObjectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### K8sService

_Required_: No

_Type_: List of <a href="k8sservicedefinition.md">K8sServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: No

_Type_: List of <a href="privateipdefinition.md">PrivateIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateName

_Required_: No

_Type_: List of <a href="privatenamedefinition.md">PrivateNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: List of <a href="publicipdefinition.md">PublicIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicName

_Required_: No

_Type_: List of <a href="publicnamedefinition.md">PublicNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnPrivateIp

_Required_: No

_Type_: List of <a href="vnprivateipdefinition.md">VnPrivateIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnPrivateName

_Required_: No

_Type_: List of <a href="vnprivatenamedefinition.md">VnPrivateNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

