# TF::TencentCloud::KubernetesCluster ClusterExtraArgsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#kubeapiserver" title="KubeApiserver">KubeApiserver</a>" : <i>[ String, ... ]</i>,
    "<a href="#kubecontrollermanager" title="KubeControllerManager">KubeControllerManager</a>" : <i>[ String, ... ]</i>,
    "<a href="#kubescheduler" title="KubeScheduler">KubeScheduler</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#kubeapiserver" title="KubeApiserver">KubeApiserver</a>: <i>
      - String</i>
<a href="#kubecontrollermanager" title="KubeControllerManager">KubeControllerManager</a>: <i>
      - String</i>
<a href="#kubescheduler" title="KubeScheduler">KubeScheduler</a>: <i>
      - String</i>
</pre>

## Properties

#### KubeApiserver

The customized parameters for kube-apiserver.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeControllerManager

The customized parameters for kube-controller-manager.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeScheduler

The customized parameters for kube-scheduler.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

