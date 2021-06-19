# TF::Rancher2::Cluster ServicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#etcd" title="Etcd">Etcd</a>" : <i>[ <a href="etcddefinition.md">EtcdDefinition</a>, ... ]</i>,
    "<a href="#kubeapi" title="KubeApi">KubeApi</a>" : <i>[ <a href="kubeapidefinition.md">KubeApiDefinition</a>, ... ]</i>,
    "<a href="#kubecontroller" title="KubeController">KubeController</a>" : <i>[ <a href="kubecontrollerdefinition.md">KubeControllerDefinition</a>, ... ]</i>,
    "<a href="#kubelet" title="Kubelet">Kubelet</a>" : <i>[ <a href="kubeletdefinition.md">KubeletDefinition</a>, ... ]</i>,
    "<a href="#kubeproxy" title="Kubeproxy">Kubeproxy</a>" : <i>[ <a href="kubeproxydefinition.md">KubeproxyDefinition</a>, ... ]</i>,
    "<a href="#scheduler" title="Scheduler">Scheduler</a>" : <i>[ <a href="schedulerdefinition.md">SchedulerDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#etcd" title="Etcd">Etcd</a>: <i>
      - <a href="etcddefinition.md">EtcdDefinition</a></i>
<a href="#kubeapi" title="KubeApi">KubeApi</a>: <i>
      - <a href="kubeapidefinition.md">KubeApiDefinition</a></i>
<a href="#kubecontroller" title="KubeController">KubeController</a>: <i>
      - <a href="kubecontrollerdefinition.md">KubeControllerDefinition</a></i>
<a href="#kubelet" title="Kubelet">Kubelet</a>: <i>
      - <a href="kubeletdefinition.md">KubeletDefinition</a></i>
<a href="#kubeproxy" title="Kubeproxy">Kubeproxy</a>: <i>
      - <a href="kubeproxydefinition.md">KubeproxyDefinition</a></i>
<a href="#scheduler" title="Scheduler">Scheduler</a>: <i>
      - <a href="schedulerdefinition.md">SchedulerDefinition</a></i>
</pre>

## Properties

#### Etcd

_Required_: No

_Type_: List of <a href="etcddefinition.md">EtcdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeApi

_Required_: No

_Type_: List of <a href="kubeapidefinition.md">KubeApiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeController

_Required_: No

_Type_: List of <a href="kubecontrollerdefinition.md">KubeControllerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kubelet

_Required_: No

_Type_: List of <a href="kubeletdefinition.md">KubeletDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kubeproxy

_Required_: No

_Type_: List of <a href="kubeproxydefinition.md">KubeproxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scheduler

_Required_: No

_Type_: List of <a href="schedulerdefinition.md">SchedulerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

