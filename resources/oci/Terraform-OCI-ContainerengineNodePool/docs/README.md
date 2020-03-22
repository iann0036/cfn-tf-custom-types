# Terraform::OCI::ContainerengineNodePool

This resource provides the Node Pool resource in Oracle Cloud Infrastructure Container Engine service.

Create a new node pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ContainerengineNodePool",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeimageid" title="NodeImageId">NodeImageId</a>" : <i>String</i>,
        "<a href="#nodeimagename" title="NodeImageName">NodeImageName</a>" : <i>String</i>,
        "<a href="#nodemetadata" title="NodeMetadata">NodeMetadata</a>" : <i>[ <a href="nodemetadata.md">NodeMetadata</a>, ... ]</i>,
        "<a href="#nodeshape" title="NodeShape">NodeShape</a>" : <i>String</i>,
        "<a href="#quantitypersubnet" title="QuantityPerSubnet">QuantityPerSubnet</a>" : <i>Double</i>,
        "<a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#initialnodelabels" title="InitialNodeLabels">InitialNodeLabels</a>" : <i>[ <a href="initialnodelabels.md">InitialNodeLabels</a>, ... ]</i>,
        "<a href="#nodeconfigdetails" title="NodeConfigDetails">NodeConfigDetails</a>" : <i>[ <a href="nodeconfigdetails.md">NodeConfigDetails</a>, ... ]</i>,
        "<a href="#nodesourcedetails" title="NodeSourceDetails">NodeSourceDetails</a>" : <i>[ <a href="nodesourcedetails.md">NodeSourceDetails</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#placementconfigs" title="PlacementConfigs">PlacementConfigs</a>" : <i>[ <a href="placementconfigs.md">PlacementConfigs</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ContainerengineNodePool
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeimageid" title="NodeImageId">NodeImageId</a>: <i>String</i>
    <a href="#nodeimagename" title="NodeImageName">NodeImageName</a>: <i>String</i>
    <a href="#nodemetadata" title="NodeMetadata">NodeMetadata</a>: <i>
      - <a href="nodemetadata.md">NodeMetadata</a></i>
    <a href="#nodeshape" title="NodeShape">NodeShape</a>: <i>String</i>
    <a href="#quantitypersubnet" title="QuantityPerSubnet">QuantityPerSubnet</a>: <i>Double</i>
    <a href="#sshpublickey" title="SshPublicKey">SshPublicKey</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#initialnodelabels" title="InitialNodeLabels">InitialNodeLabels</a>: <i>
      - <a href="initialnodelabels.md">InitialNodeLabels</a></i>
    <a href="#nodeconfigdetails" title="NodeConfigDetails">NodeConfigDetails</a>: <i>
      - <a href="nodeconfigdetails.md">NodeConfigDetails</a></i>
    <a href="#nodesourcedetails" title="NodeSourceDetails">NodeSourceDetails</a>: <i>
      - <a href="nodesourcedetails.md">NodeSourceDetails</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#placementconfigs" title="PlacementConfigs">PlacementConfigs</a>: <i>
      - <a href="placementconfigs.md">PlacementConfigs</a></i>
</pre>

## Properties

#### ClusterId

The OCID of the cluster to which this node pool is attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

The OCID of the compartment in which the node pool exists.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

(Updatable) The version of Kubernetes to install on the nodes in the node pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

(Updatable) The name of the node pool. Avoid entering confidential information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImageId

Deprecated. Use `node_source_details` instead. The OCID of the image running on the nodes in the node pool. Cannot be used when `node_image_name` is specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImageName

Deprecated. Use `node_source_details` instead. If you specify values for both, this value is ignored. The name of the image running on the nodes in the node pool. Cannot be used when `node_image_id` is specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeMetadata

A list of key/value pairs to add to each underlying Oracle Cloud Infrastructure instance in the node pool.

_Required_: No

_Type_: List of <a href="nodemetadata.md">NodeMetadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeShape

The name of the node shape of the nodes in the node pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuantityPerSubnet

(Updatable) Optional, default to 1. The number of nodes to create in each subnet specified in subnetIds property.  When used, subnetIds is required. This property is deprecated, use nodeConfigDetails instead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

The SSH public key to add to each node in the node pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

(Updatable) The OCIDs of the subnets in which to place nodes for this node pool. When used, quantityPerSubnet can be provided. This property is deprecated, use nodeConfigDetails. Exactly one of the subnetIds or nodeConfigDetails properties must be specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialNodeLabels

_Required_: No

_Type_: List of <a href="initialnodelabels.md">InitialNodeLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfigDetails

_Required_: No

_Type_: List of <a href="nodeconfigdetails.md">NodeConfigDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeSourceDetails

_Required_: No

_Type_: List of <a href="nodesourcedetails.md">NodeSourceDetails</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConfigs

_Required_: No

_Type_: List of <a href="placementconfigs.md">PlacementConfigs</a>

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

#### NodeSource

Returns the <code>NodeSource</code> value.

#### Nodes

Returns the <code>Nodes</code> value.

