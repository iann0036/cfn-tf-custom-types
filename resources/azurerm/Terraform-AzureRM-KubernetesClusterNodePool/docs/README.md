# Terraform::AzureRM::KubernetesClusterNodePool

Manages a Node Pool within a Kubernetes Cluster

~> **NOTE:** Multiple Node Pools are only supported when the Kubernetes Cluster is using Virtual Machine Scale Sets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::KubernetesClusterNodePool",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>" : <i>Boolean</i>,
        "<a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>" : <i>Boolean</i>,
        "<a href="#kubernetesclusterid" title="KubernetesClusterId">KubernetesClusterId</a>" : <i>String</i>,
        "<a href="#maxcount" title="MaxCount">MaxCount</a>" : <i>Double</i>,
        "<a href="#maxpods" title="MaxPods">MaxPods</a>" : <i>Double</i>,
        "<a href="#mincount" title="MinCount">MinCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#nodelabels" title="NodeLabels">NodeLabels</a>" : <i>[ <a href="nodelabels.md">NodeLabels</a>, ... ]</i>,
        "<a href="#nodetaints" title="NodeTaints">NodeTaints</a>" : <i>[ String, ... ]</i>,
        "<a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>" : <i>Double</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>,
        "<a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::KubernetesClusterNodePool
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#enableautoscaling" title="EnableAutoScaling">EnableAutoScaling</a>: <i>Boolean</i>
    <a href="#enablenodepublicip" title="EnableNodePublicIp">EnableNodePublicIp</a>: <i>Boolean</i>
    <a href="#kubernetesclusterid" title="KubernetesClusterId">KubernetesClusterId</a>: <i>String</i>
    <a href="#maxcount" title="MaxCount">MaxCount</a>: <i>Double</i>
    <a href="#maxpods" title="MaxPods">MaxPods</a>: <i>Double</i>
    <a href="#mincount" title="MinCount">MinCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#nodelabels" title="NodeLabels">NodeLabels</a>: <i>
      - <a href="nodelabels.md">NodeLabels</a></i>
    <a href="#nodetaints" title="NodeTaints">NodeTaints</a>: <i>
      - String</i>
    <a href="#osdisksizegb" title="OsDiskSizeGb">OsDiskSizeGb</a>: <i>Double</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
    <a href="#vnetsubnetid" title="VnetSubnetId">VnetSubnetId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityZones

A list of Availability Zones where the Nodes in this Node Pool should be created in.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoScaling

Whether to enable [auto-scaler](https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler). Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNodePublicIp

Should each node have a Public IP Address? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesClusterId

The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPods

The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLabels

A map of Kubernetes labels which should be applied to nodes in this Node Pool.

_Required_: No

_Type_: List of <a href="nodelabels.md">NodeLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeTaints

A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g `key=value:NoSchedule`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsDiskSizeGb

The Agent Operating System disk size in GB. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are `Linux` and `Windows`. Defaults to `Linux`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetSubnetId

The ID of the Subnet where this Node Pool should exist.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

