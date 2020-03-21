# Terraform::AzureRM::HdinsightKafkaCluster WorkerNode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>" : <i>Double</i>,
    "<a href="#numberofdiskspernode" title="NumberOfDisksPerNode">NumberOfDisksPerNode</a>" : <i>Double</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>" : <i>Double</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>" : <i>String</i>,
    "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>: <i>Double</i>
<a href="#numberofdiskspernode" title="NumberOfDisksPerNode">NumberOfDisksPerNode</a>: <i>Double</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#targetinstancecount" title="TargetInstanceCount">TargetInstanceCount</a>: <i>Double</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>: <i>String</i>
<a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
</pre>

## Properties

#### MinInstanceCount

The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDisksPerNode

The number of Data Disks which should be assigned to each Worker Node, which can be between 1 and 8. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetInstanceCount

The number of instances which should be run for the Worker Nodes.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkId

The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

