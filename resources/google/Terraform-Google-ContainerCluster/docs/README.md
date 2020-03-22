# Terraform::Google::ContainerCluster

Manages a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and [the API reference](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters).

~> **Note:** All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ContainerCluster",
    "Properties" : {
        "<a href="#additionalzones" title="AdditionalZones">AdditionalZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>" : <i>String</i>,
        "<a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>" : <i>Boolean</i>,
        "<a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>" : <i>Boolean</i>,
        "<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>" : <i>Boolean</i>,
        "<a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>" : <i>Boolean</i>,
        "<a href="#enabletpu" title="EnableTpu">EnableTpu</a>" : <i>Boolean</i>,
        "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#loggingservice" title="LoggingService">LoggingService</a>" : <i>String</i>,
        "<a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>" : <i>String</i>,
        "<a href="#monitoringservice" title="MonitoringService">MonitoringService</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#nodeversion" title="NodeVersion">NodeVersion</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>" : <i>Boolean</i>,
        "<a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>" : <i>[ <a href="resourcelabels.md">ResourceLabels</a>, ... ]</i>,
        "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>" : <i>[ <a href="addonsconfig.md">AddonsConfig</a>, ... ]</i>,
        "<a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>" : <i>[ <a href="authenticatorgroupsconfig.md">AuthenticatorGroupsConfig</a>, ... ]</i>,
        "<a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>" : <i>[ <a href="clusterautoscaling.md">ClusterAutoscaling</a>, ... ]</i>,
        "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>[ <a href="ipallocationpolicy.md">IpAllocationPolicy</a>, ... ]</i>,
        "<a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>" : <i>[ <a href="maintenancepolicy.md">MaintenancePolicy</a>, ... ]</i>,
        "<a href="#masterauth" title="MasterAuth">MasterAuth</a>" : <i>[ <a href="masterauth.md">MasterAuth</a>, ... ]</i>,
        "<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>" : <i>[ <a href="masterauthorizednetworksconfig.md">MasterAuthorizedNetworksConfig</a>, ... ]</i>,
        "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>[ <a href="networkpolicy.md">NetworkPolicy</a>, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfig.md">NodeConfig</a>, ... ]</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ <a href="nodepool.md">NodePool</a>, ... ]</i>,
        "<a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>" : <i>[ <a href="podsecuritypolicyconfig.md">PodSecurityPolicyConfig</a>, ... ]</i>,
        "<a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>" : <i>[ <a href="privateclusterconfig.md">PrivateClusterConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>" : <i>[ <a href="verticalpodautoscaling.md">VerticalPodAutoscaling</a>, ... ]</i>,
        "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ <a href="horizontalpodautoscaling.md">HorizontalPodAutoscaling</a>, ... ]</i>,
        "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ <a href="httploadbalancing.md">HttpLoadBalancing</a>, ... ]</i>,
        "<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>" : <i>[ <a href="kubernetesdashboard.md">KubernetesDashboard</a>, ... ]</i>,
        "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ <a href="networkpolicyconfig.md">NetworkPolicyConfig</a>, ... ]</i>,
        "<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>" : <i>[ <a href="autoprovisioningdefaults.md">AutoProvisioningDefaults</a>, ... ]</i>,
        "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ <a href="resourcelimits.md">ResourceLimits</a>, ... ]</i>,
        "<a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>" : <i>[ <a href="dailymaintenancewindow.md">DailyMaintenanceWindow</a>, ... ]</i>,
        "<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>" : <i>[ <a href="clientcertificateconfig.md">ClientCertificateConfig</a>, ... ]</i>,
        "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ <a href="cidrblocks.md">CidrBlocks</a>, ... ]</i>,
        "<a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>" : <i>[ <a href="sandboxconfig.md">SandboxConfig</a>, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>, ... ]</i>,
        "<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>" : <i>[ <a href="workloadmetadataconfig.md">WorkloadMetadataConfig</a>, ... ]</i>,
        "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ <a href="autoscaling.md">Autoscaling</a>, ... ]</i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ <a href="management.md">Management</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ContainerCluster
Properties:
    <a href="#additionalzones" title="AdditionalZones">AdditionalZones</a>: <i>
      - String</i>
    <a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>: <i>String</i>
    <a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>: <i>Boolean</i>
    <a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>: <i>Boolean</i>
    <a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>: <i>Boolean</i>
    <a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>: <i>Boolean</i>
    <a href="#enabletpu" title="EnableTpu">EnableTpu</a>: <i>Boolean</i>
    <a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#loggingservice" title="LoggingService">LoggingService</a>: <i>String</i>
    <a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>: <i>String</i>
    <a href="#monitoringservice" title="MonitoringService">MonitoringService</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
    <a href="#nodeversion" title="NodeVersion">NodeVersion</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>: <i>Boolean</i>
    <a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>: <i>
      - <a href="resourcelabels.md">ResourceLabels</a></i>
    <a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>: <i>
      - <a href="addonsconfig.md">AddonsConfig</a></i>
    <a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>: <i>
      - <a href="authenticatorgroupsconfig.md">AuthenticatorGroupsConfig</a></i>
    <a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>: <i>
      - <a href="clusterautoscaling.md">ClusterAutoscaling</a></i>
    <a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>: <i>
      - <a href="ipallocationpolicy.md">IpAllocationPolicy</a></i>
    <a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>: <i>
      - <a href="maintenancepolicy.md">MaintenancePolicy</a></i>
    <a href="#masterauth" title="MasterAuth">MasterAuth</a>: <i>
      - <a href="masterauth.md">MasterAuth</a></i>
    <a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>: <i>
      - <a href="masterauthorizednetworksconfig.md">MasterAuthorizedNetworksConfig</a></i>
    <a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>
      - <a href="networkpolicy.md">NetworkPolicy</a></i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfig.md">NodeConfig</a></i>
    <a href="#nodepool" title="NodePool">NodePool</a>: <i>
      - <a href="nodepool.md">NodePool</a></i>
    <a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>: <i>
      - <a href="podsecuritypolicyconfig.md">PodSecurityPolicyConfig</a></i>
    <a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>: <i>
      - <a href="privateclusterconfig.md">PrivateClusterConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>: <i>
      - <a href="verticalpodautoscaling.md">VerticalPodAutoscaling</a></i>
    <a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - <a href="horizontalpodautoscaling.md">HorizontalPodAutoscaling</a></i>
    <a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - <a href="httploadbalancing.md">HttpLoadBalancing</a></i>
    <a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>: <i>
      - <a href="kubernetesdashboard.md">KubernetesDashboard</a></i>
    <a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - <a href="networkpolicyconfig.md">NetworkPolicyConfig</a></i>
    <a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>: <i>
      - <a href="autoprovisioningdefaults.md">AutoProvisioningDefaults</a></i>
    <a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - <a href="resourcelimits.md">ResourceLimits</a></i>
    <a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>: <i>
      - <a href="dailymaintenancewindow.md">DailyMaintenanceWindow</a></i>
    <a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>: <i>
      - <a href="clientcertificateconfig.md">ClientCertificateConfig</a></i>
    <a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - <a href="cidrblocks.md">CidrBlocks</a></i>
    <a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>: <i>
      - <a href="sandboxconfig.md">SandboxConfig</a></i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a></i>
    <a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>: <i>
      - <a href="workloadmetadataconfig.md">WorkloadMetadataConfig</a></i>
    <a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - <a href="autoscaling.md">Autoscaling</a></i>
    <a href="#management" title="Management">Management</a>: <i>
      - <a href="management.md">Management</a></i>
</pre>

## Properties

#### AdditionalZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpv4Cidr

The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMaxPodsPerNode

The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBinaryAuthorization

Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIntranodeVisibility

)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKubernetesAlpha

Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLegacyAbac

Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTpu

) Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialNodeCount

The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`google_container_node_pool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingService

The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinMasterVersion

The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `google_container_engine_versions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
Terraform-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringService

The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the cluster, unique within the project and
location.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeVersion

The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as Terraform will see spurious diffs
when fuzzy versions are used. See the `google_container_engine_versions` data source's
`version_prefix` field to approximate fuzzy versions in a Terraform-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDefaultNodePool

If `true`, deletes the default node
pool upon cluster creation. If you're using `google_container_node_pool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLabels

The GCE resource labels (a map of key/value pairs) to be applied to the cluster.

_Required_: No

_Type_: List of <a href="resourcelabels.md">ResourceLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonsConfig

_Required_: No

_Type_: List of <a href="addonsconfig.md">AddonsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticatorGroupsConfig

_Required_: No

_Type_: List of <a href="authenticatorgroupsconfig.md">AuthenticatorGroupsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAutoscaling

_Required_: No

_Type_: List of <a href="clusterautoscaling.md">ClusterAutoscaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationPolicy

_Required_: No

_Type_: List of <a href="ipallocationpolicy.md">IpAllocationPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenancePolicy

_Required_: No

_Type_: List of <a href="maintenancepolicy.md">MaintenancePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuth

_Required_: No

_Type_: List of <a href="masterauth.md">MasterAuth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuthorizedNetworksConfig

_Required_: No

_Type_: List of <a href="masterauthorizednetworksconfig.md">MasterAuthorizedNetworksConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No

_Type_: List of <a href="networkpolicy.md">NetworkPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfig.md">NodeConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: No

_Type_: List of <a href="nodepool.md">NodePool</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSecurityPolicyConfig

_Required_: No

_Type_: List of <a href="podsecuritypolicyconfig.md">PodSecurityPolicyConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateClusterConfig

_Required_: No

_Type_: List of <a href="privateclusterconfig.md">PrivateClusterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerticalPodAutoscaling

_Required_: No

_Type_: List of <a href="verticalpodautoscaling.md">VerticalPodAutoscaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HorizontalPodAutoscaling

_Required_: No

_Type_: List of <a href="horizontalpodautoscaling.md">HorizontalPodAutoscaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No

_Type_: List of <a href="httploadbalancing.md">HttpLoadBalancing</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesDashboard

_Required_: No

_Type_: List of <a href="kubernetesdashboard.md">KubernetesDashboard</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No

_Type_: List of <a href="networkpolicyconfig.md">NetworkPolicyConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoProvisioningDefaults

_Required_: No

_Type_: List of <a href="autoprovisioningdefaults.md">AutoProvisioningDefaults</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of <a href="resourcelimits.md">ResourceLimits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyMaintenanceWindow

_Required_: No

_Type_: List of <a href="dailymaintenancewindow.md">DailyMaintenanceWindow</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateConfig

_Required_: No

_Type_: List of <a href="clientcertificateconfig.md">ClientCertificateConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlocks

_Required_: No

_Type_: List of <a href="cidrblocks.md">CidrBlocks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxConfig

_Required_: No

_Type_: List of <a href="sandboxconfig.md">SandboxConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of <a href="shieldedinstanceconfig.md">ShieldedInstanceConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadMetadataConfig

_Required_: No

_Type_: List of <a href="workloadmetadataconfig.md">WorkloadMetadataConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No

_Type_: List of <a href="autoscaling.md">Autoscaling</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of <a href="management.md">Management</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceGroupUrls

Returns the <code>InstanceGroupUrls</code> value.

#### LabelFingerprint

Returns the <code>LabelFingerprint</code> value.

#### MasterVersion

Returns the <code>MasterVersion</code> value.

#### Operation

Returns the <code>Operation</code> value.

#### ServicesIpv4Cidr

Returns the <code>ServicesIpv4Cidr</code> value.

