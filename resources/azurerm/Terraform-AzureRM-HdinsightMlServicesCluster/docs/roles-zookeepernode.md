# Terraform::AzureRM::HdinsightMlServicesCluster Roles ZookeeperNode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#sshkeys" title="SshKeys">SshKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>" : <i>String</i>,
    "<a href="#vmsize" title="VmSize">VmSize</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#sshkeys" title="SshKeys">SshKeys</a>: <i>
      - String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>: <i>String</i>
<a href="#vmsize" title="VmSize">VmSize</a>: <i>String</i>
</pre>

## Properties

#### Password

The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeys

A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkId

The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmSize

The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

