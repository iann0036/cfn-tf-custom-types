# Terraform::OCI::ContainerengineNodePool

CloudFormation equivalent of oci_containerengine_node_pool

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeImageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeMetadata

_Required_: No

_Type_: List of <a href="nodemetadata.md">NodeMetadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeShape

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuantityPerSubnet

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshPublicKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

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

#### NodeSource

Returns the <code>NodeSource</code> value.

#### Nodes

Returns the <code>Nodes</code> value.

