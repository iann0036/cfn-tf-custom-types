# TF::Google::ContainerNodePool

-> See the [Using GKE with Terraform](/docs/providers/google/guides/using_gke_with_terraform.html)
guide for more information about using GKE with Terraform.

Manages a node pool in a Google Kubernetes Engine (GKE) cluster separately from
the cluster control plane. For more information see [the official documentation](https://cloud.google.com/container-engine/docs/node-pools)
and [the API reference](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ContainerNodePool",
    "Properties" : {
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
        "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ <a href="autoscalingdefinition.md">AutoscalingDefinition</a>, ... ]</i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ <a href="managementdefinition.md">ManagementDefinition</a>, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>" : <i>[ <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ContainerNodePool
Properties:
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maxpodspernode" title="MaxPodsPerNode">MaxPodsPerNode</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
    <a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - <a href="autoscalingdefinition.md">AutoscalingDefinition</a></i>
    <a href="#management" title="Management">Management</a>: <i>
      - <a href="managementdefinition.md">ManagementDefinition</a></i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#upgradesettings" title="UpgradeSettings">UpgradeSettings</a>: <i>
      - <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a></i>
</pre>

## Properties

#### Cluster

The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters. May be specified in the format `projects/{{project}}/locations/{{location}}/clusters/{{cluster}}` or as just the name of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialNodeCount

The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource. WARNING: Resizing your node pool manually
may change this value in your existing cluster, which will trigger destruction
and recreation on the next Terraform run (to rectify the discrepancy).  If you don't
need this value, don't set it.  If you do need it, you can [use a lifecycle block to
ignore subsqeuent changes to this field](https://github.com/hashicorp/terraform-provider-google/issues/6901#issuecomment-667369691).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location (region or zone) of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPodsPerNode

The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the node pool. If left blank, Terraform will
auto-generate a unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as Terraform will see spurious diffs
when fuzzy versions are used. See the `google_container_engine_versions` data source's
`version_prefix` field to approximate fuzzy versions in a Terraform-compatible way.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No

_Type_: List of <a href="autoscalingdefinition.md">AutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="managementdefinition.md">ManagementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeSettings

_Required_: No

_Type_: List of <a href="upgradesettingsdefinition.md">UpgradeSettingsDefinition</a>

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

#### InstanceGroupUrls

Returns the <code>InstanceGroupUrls</code> value.

#### Operation

Returns the <code>Operation</code> value.

