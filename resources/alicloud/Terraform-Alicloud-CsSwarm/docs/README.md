# Terraform::Alicloud::CsSwarm

-> **DEPRECATED:** This resource manages swarm cluster, which is being deprecated and will be replaced by Kubernetes cluster.

This resource will help you to manager a Swarm Cluster.

-> **NOTE:** Swarm cluster only supports VPC network and you can specify a VPC network by filed `vswitch_id`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CsSwarm",
    "Properties" : {
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#diskcategory" title="DiskCategory">DiskCategory</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isoutdated" title="IsOutdated">IsOutdated</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#needslb" title="NeedSlb">NeedSlb</a>" : <i>Boolean</i>,
        "<a href="#nodenumber" title="NodeNumber">NodeNumber</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#releaseeip" title="ReleaseEip">ReleaseEip</a>" : <i>Boolean</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CsSwarm
Properties:
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#diskcategory" title="DiskCategory">DiskCategory</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isoutdated" title="IsOutdated">IsOutdated</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#needslb" title="NeedSlb">NeedSlb</a>: <i>Boolean</i>
    <a href="#nodenumber" title="NodeNumber">NodeNumber</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#releaseeip" title="ReleaseEip">ReleaseEip</a>: <i>Boolean</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### CidrBlock

The CIDR block for the Container. It can not be same as the CIDR used by the VPC.
Valid value:
- 192.168.0.0/16
- 172.19-30.0.0/16
- 10.0.0.0/16.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskCategory

The data disk category of ECS instance node. Its valid value are `cloud`, `cloud_ssd`, `cloud_essd`, `ephemeral_essd` and `cloud_efficiency`. Default to `cloud_efficiency`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

The data disk size of ECS instance node. Its valid value is 20~32768 GB. Default to 20.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The image ID of ECS instance node used. Default to System automate allocated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of ECS instance node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOutdated

Whether to use outdated instance type. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The container cluster's name. It is the only in one Alicloud account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

The container cluster name's prefix. It is conflict with `name`. If it is specified, terraform will using it to build the only cluster name. Default to 'Terraform-Creation'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeedSlb

Whether to create the default simple routing Server Load Balancer instance for the cluster. The default value is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNumber

The ECS node number of the container cluster. Its value choices are 1~50, and default to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of ECS instance node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseEip

Whether to release EIP after creating swarm cluster successfully. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The password of ECS instance node. If it is not specified, the container cluster's network mode will be `Classic`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AgentVersion

Returns the <code>AgentVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### Nodes

Returns the <code>Nodes</code> value.

#### SecurityGroupId

Returns the <code>SecurityGroupId</code> value.

#### SlbId

Returns the <code>SlbId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

