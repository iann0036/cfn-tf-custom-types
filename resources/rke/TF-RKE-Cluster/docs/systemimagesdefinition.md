# TF::RKE::Cluster SystemImagesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acicnideploycontainer" title="AciCniDeployContainer">AciCniDeployContainer</a>" : <i>String</i>,
    "<a href="#acicontrollercontainer" title="AciControllerContainer">AciControllerContainer</a>" : <i>String</i>,
    "<a href="#acihostcontainer" title="AciHostContainer">AciHostContainer</a>" : <i>String</i>,
    "<a href="#acimcastcontainer" title="AciMcastContainer">AciMcastContainer</a>" : <i>String</i>,
    "<a href="#aciopflexcontainer" title="AciOpflexContainer">AciOpflexContainer</a>" : <i>String</i>,
    "<a href="#aciovscontainer" title="AciOvsContainer">AciOvsContainer</a>" : <i>String</i>,
    "<a href="#alpine" title="Alpine">Alpine</a>" : <i>String</i>,
    "<a href="#calicocni" title="CalicoCni">CalicoCni</a>" : <i>String</i>,
    "<a href="#calicocontrollers" title="CalicoControllers">CalicoControllers</a>" : <i>String</i>,
    "<a href="#calicoctl" title="CalicoCtl">CalicoCtl</a>" : <i>String</i>,
    "<a href="#calicoflexvol" title="CalicoFlexVol">CalicoFlexVol</a>" : <i>String</i>,
    "<a href="#caliconode" title="CalicoNode">CalicoNode</a>" : <i>String</i>,
    "<a href="#canalcni" title="CanalCni">CanalCni</a>" : <i>String</i>,
    "<a href="#canalflannel" title="CanalFlannel">CanalFlannel</a>" : <i>String</i>,
    "<a href="#canalflexvol" title="CanalFlexVol">CanalFlexVol</a>" : <i>String</i>,
    "<a href="#canalnode" title="CanalNode">CanalNode</a>" : <i>String</i>,
    "<a href="#certdownloader" title="CertDownloader">CertDownloader</a>" : <i>String</i>,
    "<a href="#coredns" title="Coredns">Coredns</a>" : <i>String</i>,
    "<a href="#corednsautoscaler" title="CorednsAutoscaler">CorednsAutoscaler</a>" : <i>String</i>,
    "<a href="#dnsmasq" title="Dnsmasq">Dnsmasq</a>" : <i>String</i>,
    "<a href="#etcd" title="Etcd">Etcd</a>" : <i>[ <a href="etcddefinition.md">EtcdDefinition</a>, ... ]</i>,
    "<a href="#flannel" title="Flannel">Flannel</a>" : <i>String</i>,
    "<a href="#flannelcni" title="FlannelCni">FlannelCni</a>" : <i>String</i>,
    "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingressdefinition.md">IngressDefinition</a>, ... ]</i>,
    "<a href="#ingressbackend" title="IngressBackend">IngressBackend</a>" : <i>String</i>,
    "<a href="#kubedns" title="KubeDns">KubeDns</a>" : <i>String</i>,
    "<a href="#kubednsautoscaler" title="KubeDnsAutoscaler">KubeDnsAutoscaler</a>" : <i>String</i>,
    "<a href="#kubednssidecar" title="KubeDnsSidecar">KubeDnsSidecar</a>" : <i>String</i>,
    "<a href="#kubernetes" title="Kubernetes">Kubernetes</a>" : <i>String</i>,
    "<a href="#kubernetesservicessidecar" title="KubernetesServicesSidecar">KubernetesServicesSidecar</a>" : <i>String</i>,
    "<a href="#metricsserver" title="MetricsServer">MetricsServer</a>" : <i>String</i>,
    "<a href="#nginxproxy" title="NginxProxy">NginxProxy</a>" : <i>String</i>,
    "<a href="#nodelocal" title="Nodelocal">Nodelocal</a>" : <i>[ <a href="nodelocaldefinition.md">NodelocalDefinition</a>, ... ]</i>,
    "<a href="#podinfracontainer" title="PodInfraContainer">PodInfraContainer</a>" : <i>String</i>,
    "<a href="#weavecni" title="WeaveCni">WeaveCni</a>" : <i>String</i>,
    "<a href="#weavenode" title="WeaveNode">WeaveNode</a>" : <i>String</i>,
    "<a href="#windowspodinfracontainer" title="WindowsPodInfraContainer">WindowsPodInfraContainer</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acicnideploycontainer" title="AciCniDeployContainer">AciCniDeployContainer</a>: <i>String</i>
<a href="#acicontrollercontainer" title="AciControllerContainer">AciControllerContainer</a>: <i>String</i>
<a href="#acihostcontainer" title="AciHostContainer">AciHostContainer</a>: <i>String</i>
<a href="#acimcastcontainer" title="AciMcastContainer">AciMcastContainer</a>: <i>String</i>
<a href="#aciopflexcontainer" title="AciOpflexContainer">AciOpflexContainer</a>: <i>String</i>
<a href="#aciovscontainer" title="AciOvsContainer">AciOvsContainer</a>: <i>String</i>
<a href="#alpine" title="Alpine">Alpine</a>: <i>String</i>
<a href="#calicocni" title="CalicoCni">CalicoCni</a>: <i>String</i>
<a href="#calicocontrollers" title="CalicoControllers">CalicoControllers</a>: <i>String</i>
<a href="#calicoctl" title="CalicoCtl">CalicoCtl</a>: <i>String</i>
<a href="#calicoflexvol" title="CalicoFlexVol">CalicoFlexVol</a>: <i>String</i>
<a href="#caliconode" title="CalicoNode">CalicoNode</a>: <i>String</i>
<a href="#canalcni" title="CanalCni">CanalCni</a>: <i>String</i>
<a href="#canalflannel" title="CanalFlannel">CanalFlannel</a>: <i>String</i>
<a href="#canalflexvol" title="CanalFlexVol">CanalFlexVol</a>: <i>String</i>
<a href="#canalnode" title="CanalNode">CanalNode</a>: <i>String</i>
<a href="#certdownloader" title="CertDownloader">CertDownloader</a>: <i>String</i>
<a href="#coredns" title="Coredns">Coredns</a>: <i>String</i>
<a href="#corednsautoscaler" title="CorednsAutoscaler">CorednsAutoscaler</a>: <i>String</i>
<a href="#dnsmasq" title="Dnsmasq">Dnsmasq</a>: <i>String</i>
<a href="#etcd" title="Etcd">Etcd</a>: <i>
      - <a href="etcddefinition.md">EtcdDefinition</a></i>
<a href="#flannel" title="Flannel">Flannel</a>: <i>String</i>
<a href="#flannelcni" title="FlannelCni">FlannelCni</a>: <i>String</i>
<a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingressdefinition.md">IngressDefinition</a></i>
<a href="#ingressbackend" title="IngressBackend">IngressBackend</a>: <i>String</i>
<a href="#kubedns" title="KubeDns">KubeDns</a>: <i>String</i>
<a href="#kubednsautoscaler" title="KubeDnsAutoscaler">KubeDnsAutoscaler</a>: <i>String</i>
<a href="#kubednssidecar" title="KubeDnsSidecar">KubeDnsSidecar</a>: <i>String</i>
<a href="#kubernetes" title="Kubernetes">Kubernetes</a>: <i>String</i>
<a href="#kubernetesservicessidecar" title="KubernetesServicesSidecar">KubernetesServicesSidecar</a>: <i>String</i>
<a href="#metricsserver" title="MetricsServer">MetricsServer</a>: <i>String</i>
<a href="#nginxproxy" title="NginxProxy">NginxProxy</a>: <i>String</i>
<a href="#nodelocal" title="Nodelocal">Nodelocal</a>: <i>
      - <a href="nodelocaldefinition.md">NodelocalDefinition</a></i>
<a href="#podinfracontainer" title="PodInfraContainer">PodInfraContainer</a>: <i>String</i>
<a href="#weavecni" title="WeaveCni">WeaveCni</a>: <i>String</i>
<a href="#weavenode" title="WeaveNode">WeaveNode</a>: <i>String</i>
<a href="#windowspodinfracontainer" title="WindowsPodInfraContainer">WindowsPodInfraContainer</a>: <i>String</i>
</pre>

## Properties

#### AciCniDeployContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciControllerContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciHostContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciMcastContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciOpflexContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AciOvsContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alpine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalicoCni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalicoControllers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalicoCtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalicoFlexVol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalicoNode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanalCni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanalFlannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanalFlexVol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CanalNode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertDownloader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coredns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorednsAutoscaler

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dnsmasq

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etcd

_Required_: No

_Type_: List of <a href="etcddefinition.md">EtcdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flannel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlannelCni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingressdefinition.md">IngressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressBackend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDnsAutoscaler

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeDnsSidecar

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kubernetes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesServicesSidecar

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricsServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NginxProxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodelocal

_Required_: No

_Type_: List of <a href="nodelocaldefinition.md">NodelocalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodInfraContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeaveCni

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeaveNode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WindowsPodInfraContainer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

