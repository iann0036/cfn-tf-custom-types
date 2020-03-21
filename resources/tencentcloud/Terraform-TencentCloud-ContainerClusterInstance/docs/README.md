# Terraform::TencentCloud::ContainerClusterInstance

Provides a TencentCloud Container Cluster Instance resource.

~> **NOTE:** It has been deprecated and replaced by  tencentcloud_kubernetes_scale_worker.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::ContainerClusterInstance",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#bandwidthtype" title="BandwidthType">BandwidthType</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#cpu" title="Cpu">Cpu</a>" : <i>Double</i>,
        "<a href="#cvmtype" title="CvmType">CvmType</a>" : <i>String</i>,
        "<a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isvpcgateway" title="IsVpcGateway">IsVpcGateway</a>" : <i>Double</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#mem" title="Mem">Mem</a>" : <i>Double</i>,
        "<a href="#mounttarget" title="MountTarget">MountTarget</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#requirewanip" title="RequireWanIp">RequireWanIp</a>" : <i>Double</i>,
        "<a href="#rootsize" title="RootSize">RootSize</a>" : <i>Double</i>,
        "<a href="#roottype" title="RootType">RootType</a>" : <i>String</i>,
        "<a href="#sgid" title="SgId">SgId</a>" : <i>String</i>,
        "<a href="#storagesize" title="StorageSize">StorageSize</a>" : <i>Double</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#unschedulable" title="Unschedulable">Unschedulable</a>" : <i>Double</i>,
        "<a href="#userscript" title="UserScript">UserScript</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::ContainerClusterInstance
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#bandwidthtype" title="BandwidthType">BandwidthType</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#cpu" title="Cpu">Cpu</a>: <i>Double</i>
    <a href="#cvmtype" title="CvmType">CvmType</a>: <i>String</i>
    <a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isvpcgateway" title="IsVpcGateway">IsVpcGateway</a>: <i>Double</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#mem" title="Mem">Mem</a>: <i>Double</i>
    <a href="#mounttarget" title="MountTarget">MountTarget</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#requirewanip" title="RequireWanIp">RequireWanIp</a>: <i>Double</i>
    <a href="#rootsize" title="RootSize">RootSize</a>: <i>Double</i>
    <a href="#roottype" title="RootType">RootType</a>: <i>String</i>
    <a href="#sgid" title="SgId">SgId</a>: <i>String</i>
    <a href="#storagesize" title="StorageSize">StorageSize</a>: <i>Double</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#unschedulable" title="Unschedulable">Unschedulable</a>: <i>Double</i>
    <a href="#userscript" title="UserScript">UserScript</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

The network bandwidth of the node.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthType

The network type of the node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

The id of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cpu

It has been deprecated from version 1.16.0. Set 'instance_type' instead. The cpu of the node.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CvmType

The type of node needed by cvm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerGraphPath

The docker graph path is going to mounted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The name ot node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The instance type of the node needed by cvm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsVpcGateway

Describe whether the node enable the gateway capability.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

The key_id of each node(if using key pair to access).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mem

It has been deprecated from version 1.16.0. Set 'instance_type' instead. The memory of the node.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTarget

The path which volume is going to be mounted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of each node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The puchase duration of the node needed by cvm.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireWanIp

Indicate whether wan ip is needed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootSize

The size of the root volume.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootType

The type of the root volume. see more from CVM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgId

The security group id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSize

The size of the data volume.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

The type of the data volume. see more from CVM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The subnet id which the node stays in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unschedulable

Determine whether the node will be schedulable. 0 is the default meaning node will be schedulable. 1 for unschedulable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserScript

User defined script in a base64-format. The script runs after the kubernetes component is ready on node. see more from CCS api documents.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone which the node stays in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AbnormalReason

Returns the <code>AbnormalReason</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

#### IsNormal

Returns the <code>IsNormal</code> value.

#### LanIp

Returns the <code>LanIp</code> value.

#### WanIp

Returns the <code>WanIp</code> value.

