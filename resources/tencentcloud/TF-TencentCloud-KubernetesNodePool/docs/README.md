# TF::TencentCloud::KubernetesNodePool

Provide a resource to create an auto scaling group for kubernetes cluster.

~> **NOTE:**  We recommend the usage of one cluster with essential worker config + node pool to manage cluster and nodes. Its a more flexible way than manage worker config with tencentcloud_kubernetes_cluster, tencentcloud_kubernetes_scale_worker or exist node management of `tencentcloud_kubernetes_attachment`. Cause some unchangeable parameters of `worker_config` may cause the whole cluster resource `force new`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::KubernetesNodePool",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#deletekeepinstance" title="DeleteKeepInstance">DeleteKeepInstance</a>" : <i>Boolean</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#enableautoscale" title="EnableAutoScale">EnableAutoScale</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeos" title="NodeOs">NodeOs</a>" : <i>String</i>,
        "<a href="#nodeostype" title="NodeOsType">NodeOsType</a>" : <i>String</i>,
        "<a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>" : <i>String</i>,
        "<a href="#scalingmode" title="ScalingMode">ScalingMode</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#unschedulable" title="Unschedulable">Unschedulable</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>" : <i>[ <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a>, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
        "<a href="#taints" title="Taints">Taints</a>" : <i>[ <a href="taintsdefinition.md">TaintsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::KubernetesNodePool
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#deletekeepinstance" title="DeleteKeepInstance">DeleteKeepInstance</a>: <i>Boolean</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#enableautoscale" title="EnableAutoScale">EnableAutoScale</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeos" title="NodeOs">NodeOs</a>: <i>String</i>
    <a href="#nodeostype" title="NodeOsType">NodeOsType</a>: <i>String</i>
    <a href="#retrypolicy" title="RetryPolicy">RetryPolicy</a>: <i>String</i>
    <a href="#scalingmode" title="ScalingMode">ScalingMode</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#unschedulable" title="Unschedulable">Unschedulable</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#autoscalingconfig" title="AutoScalingConfig">AutoScalingConfig</a>: <i>
      - <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a></i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
    <a href="#taints" title="Taints">Taints</a>: <i>
      - <a href="taintsdefinition.md">TaintsDefinition</a></i>
</pre>

## Properties

#### ClusterId

ID of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteKeepInstance

Indicate to keep the CVM instance when delete the node pool. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

Desired capacity ot the node. If `enable_auto_scale` is set `true`, this will be a computed parameter.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoScale

Indicate whether to enable auto scaling or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels of kubernetes node pool created nodes. The label key name does not exceed 63 characters, only supports English, numbers,'/','-', and does not allow beginning with ('/').

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Maximum number of node.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

Minimum number of node.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the node pool. The name does not exceed 25 characters, and only supports Chinese, English, numbers, underscores, separators (`-`) and decimal points.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeOs

Operating system of the cluster, the available values include: `tlinux2.4x86_64`, `ubuntu18.04.1x86_64`, `ubuntu16.04.1 LTSx86_64`, `centos7.6.0_x64` and `centos7.2x86_64`. Default is 'tlinux2.4x86_64'. This parameter will only affect new nodes, not including the existing nodes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeOsType

The image version of the node. Valida values are `DOCKER_CUSTOMIZE` and `GENERAL`. Default is `GENERAL`. This parameter will only affect new nodes, not including the existing nodes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryPolicy

Available values for retry policies include `IMMEDIATE_RETRY` and `INCREMENTAL_INTERVALS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingMode

Auto scaling mode. Valid values are `CLASSIC_SCALING`(scaling by create/destroy instances), `WAKE_UP_STOPPED_SCALING`(Boot priority for expansion. When expanding the capacity, the shutdown operation is given priority to the shutdown of the instance. If the number of instances is still lower than the expected number of instances after the startup, the instance will be created, and the method of destroying the instance will still be used for shrinking).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

ID list of subnet, and for VPC it is required.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unschedulable

Sets whether the joining node participates in the schedule. Default is '0'. Participate in scheduling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of VPC network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoScalingConfig

_Required_: No

_Type_: List of <a href="autoscalingconfigdefinition.md">AutoScalingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taints

_Required_: No

_Type_: List of <a href="taintsdefinition.md">TaintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AutoScalingGroupId

Returns the <code>AutoScalingGroupId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LaunchConfigId

Returns the <code>LaunchConfigId</code> value.

#### NodeCount

Returns the <code>NodeCount</code> value.

#### Status

Returns the <code>Status</code> value.

