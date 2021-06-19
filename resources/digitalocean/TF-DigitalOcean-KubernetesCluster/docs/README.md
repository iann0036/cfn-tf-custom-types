# TF::DigitalOcean::KubernetesCluster

Provides a DigitalOcean Kubernetes cluster resource. This can be used to create, delete, and modify clusters. For more information see the [official documentation](https://www.digitalocean.com/docs/kubernetes/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::KubernetesCluster",
    "Properties" : {
        "<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#surgeupgrade" title="SurgeUpgrade">SurgeUpgrade</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vpcuuid" title="VpcUuid">VpcUuid</a>" : <i>String</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ <a href="nodepooldefinition.md">NodePoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::KubernetesCluster
Properties:
    <a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#surgeupgrade" title="SurgeUpgrade">SurgeUpgrade</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vpcuuid" title="VpcUuid">VpcUuid</a>: <i>String</i>
    <a href="#nodepool" title="NodePool">NodePool</a>: <i>
      - <a href="nodepooldefinition.md">NodePoolDefinition</a></i>
</pre>

## Properties

#### AutoUpgrade

A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the node pool.
- `size` - (Required) The slug identifier for the type of Droplet to be used as workers in the node pool.
- `node_count` - (Optional) The number of Droplet instances in the node pool. If auto-scaling is enabled, this should only be set if the desired result is to explicitly reset the number of nodes to this value. If auto-scaling is enabled, and the node count is outside of the given min/max range, it will use the min nodes value.
- `auto_scale` - (Optional) Enable auto-scaling of the number of nodes in the node pool within the given min/max range.
- `min_nodes` - (Optional) If auto-scaling is enabled, this represents the minimum number of nodes that the node pool can be scaled down to.
- `max_nodes` - (Optional) If auto-scaling is enabled, this represents the maximum number of nodes that the node pool can be scaled up to.
- `tags` - (Optional) A list of tag names to be applied to the Kubernetes cluster.
- `labels` - (Optional) A map of key/value pairs to apply to nodes in the pool. The labels are exposed in the Kubernetes API as labels in the metadata of the corresponding [Node resources](https://kubernetes.io/docs/concepts/architecture/nodes/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The slug identifier for the region where the Kubernetes cluster will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SurgeUpgrade

Enable/disable surge upgrades for a cluster. Default: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tag names to be applied to the Kubernetes cluster.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The slug identifier for the version of Kubernetes used for the cluster. Use [doctl](https://github.com/digitalocean/doctl) to find the available versions `doctl kubernetes options versions`. (**Note:** A cluster may only be upgraded to newer versions in-place. If the version is decreased, a new resource will be created.).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcUuid

The ID of the VPC where the Kubernetes cluster will be located.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: No

_Type_: List of <a href="nodepooldefinition.md">NodePoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterSubnet

Returns the <code>ClusterSubnet</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ipv4Address

Returns the <code>Ipv4Address</code> value.

#### KubeConfig

Returns the <code>KubeConfig</code> value.

#### ServiceSubnet

Returns the <code>ServiceSubnet</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### Urn

Returns the <code>Urn</code> value.

