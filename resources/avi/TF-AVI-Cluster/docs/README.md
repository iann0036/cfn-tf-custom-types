# TF::AVI::Cluster

The Cluster resource allows the creation and management of Avi Cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Cluster",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rejoinnodesautomatically" title="RejoinNodesAutomatically">RejoinNodesAutomatically</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#clusterstate" title="ClusterState">ClusterState</a>" : <i>[ <a href="clusterstatedefinition.md">ClusterStateDefinition</a>, ... ]</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ <a href="nodesdefinition.md">NodesDefinition</a>, ... ]</i>,
        "<a href="#virtualip" title="VirtualIp">VirtualIp</a>" : <i>[ <a href="virtualipdefinition.md">VirtualIpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Cluster
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rejoinnodesautomatically" title="RejoinNodesAutomatically">RejoinNodesAutomatically</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#clusterstate" title="ClusterState">ClusterState</a>: <i>
      - <a href="clusterstatedefinition.md">ClusterStateDefinition</a></i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - <a href="nodesdefinition.md">NodesDefinition</a></i>
    <a href="#virtualip" title="VirtualIp">VirtualIp</a>: <i>
      - <a href="virtualipdefinition.md">VirtualIpDefinition</a></i>
</pre>

## Properties

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejoinNodesAutomatically

Re-join cluster nodes automatically in the event one of the node is reset to factory.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterState

_Required_: No

_Type_: List of <a href="clusterstatedefinition.md">ClusterStateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

_Required_: No

_Type_: List of <a href="nodesdefinition.md">NodesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualIp

_Required_: No

_Type_: List of <a href="virtualipdefinition.md">VirtualIpDefinition</a>

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

