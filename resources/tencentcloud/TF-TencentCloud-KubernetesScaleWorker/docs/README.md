# TF::TencentCloud::KubernetesScaleWorker

Provide a resource to increase instance to cluster

~> **NOTE:** To use the custom Kubernetes component startup parameter function (parameter `extra_args`), you need to submit a ticket for application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::KubernetesScaleWorker",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#desiredpodnum" title="DesiredPodNum">DesiredPodNum</a>" : <i>Double</i>,
        "<a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>" : <i>String</i>,
        "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ String, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#mounttarget" title="MountTarget">MountTarget</a>" : <i>String</i>,
        "<a href="#unschedulable" title="Unschedulable">Unschedulable</a>" : <i>Double</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadiskdefinition.md">DataDiskDefinition</a>, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::KubernetesScaleWorker
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#desiredpodnum" title="DesiredPodNum">DesiredPodNum</a>: <i>Double</i>
    <a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>: <i>String</i>
    <a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#mounttarget" title="MountTarget">MountTarget</a>: <i>String</i>
    <a href="#unschedulable" title="Unschedulable">Unschedulable</a>: <i>Double</i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadiskdefinition.md">DataDiskDefinition</a></i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfigdefinition.md">WorkerConfigDefinition</a></i>
</pre>

## Properties

#### ClusterId

ID of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredPodNum

Indicate to set desired pod number in current node. Valid when the cluster enable customized pod cidr.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerGraphPath

Docker graph path. Default is `/var/lib/docker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

Custom parameter information related to the node.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels of kubernetes scale worker created nodes.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTarget

Mount target. Default is not mounting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unschedulable

Sets whether the joining node participates in the schedule. Default is '0'. Participate in scheduling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadiskdefinition.md">DataDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### WorkerInstancesList

Returns the <code>WorkerInstancesList</code> value.

