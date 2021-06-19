# TF::Google::ContainerCluster

-> Visit the [Provision a GKE Cluster (Google Cloud)](https://learn.hashicorp.com/tutorials/terraform/gke?in=terraform/kubernetes&utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS) Learn tutorial to learn how to provision and interact
with a GKE cluster.

-> See the [Using GKE with Terraform](/docs/providers/google/guides/using_gke_with_terraform.html)
guide for more information about using GKE with Terraform.

Manages a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and [the API reference](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters).

~> **Note:** All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. [Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ContainerCluster",
    "Properties" : {
        "<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>" : <i>String</i>,
        "<a href="#datapathprovider" title="DatapathProvider">DatapathProvider</a>" : <i>String</i>,
        "<a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableautopilot" title="EnableAutopilot">EnableAutopilot</a>" : <i>Boolean</i>,
        "<a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>" : <i>Boolean</i>,
        "<a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>" : <i>Boolean</i>,
        "<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>" : <i>Boolean</i>,
        "<a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>" : <i>Boolean</i>,
        "<a href="#enableshieldednodes" title="EnableShieldedNodes">EnableShieldedNodes</a>" : <i>Boolean</i>,
        "<a href="#enabletpu" title="EnableTpu">EnableTpu</a>" : <i>Boolean</i>,
        "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#loggingservice" title="LoggingService">LoggingService</a>" : <i>String</i>,
        "<a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>" : <i>String</i>,
        "<a href="#monitoringservice" title="MonitoringService">MonitoringService</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#networkingmode" title="NetworkingMode">NetworkingMode</a>" : <i>String</i>,
        "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#nodeversion" title="NodeVersion">NodeVersion</a>" : <i>String</i>,
        "<a href="#privateipv6googleaccess" title="PrivateIpv6GoogleAccess">PrivateIpv6GoogleAccess</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>" : <i>Boolean</i>,
        "<a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>" : <i>[ <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a>, ... ]</i>,
        "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
        "<a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>" : <i>[ <a href="addonsconfigdefinition.md">AddonsConfigDefinition</a>, ... ]</i>,
        "<a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>" : <i>[ <a href="authenticatorgroupsconfigdefinition.md">AuthenticatorGroupsConfigDefinition</a>, ... ]</i>,
        "<a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>" : <i>[ <a href="clusterautoscalingdefinition.md">ClusterAutoscalingDefinition</a>, ... ]</i>,
        "<a href="#databaseencryption" title="DatabaseEncryption">DatabaseEncryption</a>" : <i>[ <a href="databaseencryptiondefinition.md">DatabaseEncryptionDefinition</a>, ... ]</i>,
        "<a href="#defaultsnatstatus" title="DefaultSnatStatus">DefaultSnatStatus</a>" : <i>[ <a href="defaultsnatstatusdefinition.md">DefaultSnatStatusDefinition</a>, ... ]</i>,
        "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>[ <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a>, ... ]</i>,
        "<a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>" : <i>[ <a href="maintenancepolicydefinition.md">MaintenancePolicyDefinition</a>, ... ]</i>,
        "<a href="#masterauth" title="MasterAuth">MasterAuth</a>" : <i>[ <a href="masterauthdefinition.md">MasterAuthDefinition</a>, ... ]</i>,
        "<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>" : <i>[ <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a>, ... ]</i>,
        "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>[ <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a>, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ <a href="nodepooldefinition.md">NodePoolDefinition</a>, ... ]</i>,
        "<a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>" : <i>[ <a href="podsecuritypolicyconfigdefinition.md">PodSecurityPolicyConfigDefinition</a>, ... ]</i>,
        "<a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>" : <i>[ <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a>, ... ]</i>,
        "<a href="#releasechannel" title="ReleaseChannel">ReleaseChannel</a>" : <i>[ <a href="releasechanneldefinition.md">ReleaseChannelDefinition</a>, ... ]</i>,
        "<a href="#resourceusageexportconfig" title="ResourceUsageExportConfig">ResourceUsageExportConfig</a>" : <i>[ <a href="resourceusageexportconfigdefinition.md">ResourceUsageExportConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>" : <i>[ <a href="verticalpodautoscalingdefinition.md">VerticalPodAutoscalingDefinition</a>, ... ]</i>,
        "<a href="#workloadidentityconfig" title="WorkloadIdentityConfig">WorkloadIdentityConfig</a>" : <i>[ <a href="workloadidentityconfigdefinition.md">WorkloadIdentityConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ContainerCluster
Properties:
    <a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>: <i>String</i>
    <a href="#datapathprovider" title="DatapathProvider">DatapathProvider</a>: <i>String</i>
    <a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableautopilot" title="EnableAutopilot">EnableAutopilot</a>: <i>Boolean</i>
    <a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>: <i>Boolean</i>
    <a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>: <i>Boolean</i>
    <a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>: <i>Boolean</i>
    <a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>: <i>Boolean</i>
    <a href="#enableshieldednodes" title="EnableShieldedNodes">EnableShieldedNodes</a>: <i>Boolean</i>
    <a href="#enabletpu" title="EnableTpu">EnableTpu</a>: <i>Boolean</i>
    <a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#loggingservice" title="LoggingService">LoggingService</a>: <i>String</i>
    <a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>: <i>String</i>
    <a href="#monitoringservice" title="MonitoringService">MonitoringService</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#networkingmode" title="NetworkingMode">NetworkingMode</a>: <i>String</i>
    <a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
    <a href="#nodeversion" title="NodeVersion">NodeVersion</a>: <i>String</i>
    <a href="#privateipv6googleaccess" title="PrivateIpv6GoogleAccess">PrivateIpv6GoogleAccess</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>: <i>Boolean</i>
    <a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>: <i>
      - <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a></i>
    <a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
    <a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>: <i>
      - <a href="addonsconfigdefinition.md">AddonsConfigDefinition</a></i>
    <a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>: <i>
      - <a href="authenticatorgroupsconfigdefinition.md">AuthenticatorGroupsConfigDefinition</a></i>
    <a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>: <i>
      - <a href="clusterautoscalingdefinition.md">ClusterAutoscalingDefinition</a></i>
    <a href="#databaseencryption" title="DatabaseEncryption">DatabaseEncryption</a>: <i>
      - <a href="databaseencryptiondefinition.md">DatabaseEncryptionDefinition</a></i>
    <a href="#defaultsnatstatus" title="DefaultSnatStatus">DefaultSnatStatus</a>: <i>
      - <a href="defaultsnatstatusdefinition.md">DefaultSnatStatusDefinition</a></i>
    <a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>: <i>
      - <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a></i>
    <a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>: <i>
      - <a href="maintenancepolicydefinition.md">MaintenancePolicyDefinition</a></i>
    <a href="#masterauth" title="MasterAuth">MasterAuth</a>: <i>
      - <a href="masterauthdefinition.md">MasterAuthDefinition</a></i>
    <a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>: <i>
      - <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a></i>
    <a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>
      - <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a></i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - <a href="nodeconfigdefinition.md">NodeConfigDefinition</a></i>
    <a href="#nodepool" title="NodePool">NodePool</a>: <i>
      - <a href="nodepooldefinition.md">NodePoolDefinition</a></i>
    <a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>: <i>
      - <a href="podsecuritypolicyconfigdefinition.md">PodSecurityPolicyConfigDefinition</a></i>
    <a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>: <i>
      - <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a></i>
    <a href="#releasechannel" title="ReleaseChannel">ReleaseChannel</a>: <i>
      - <a href="releasechanneldefinition.md">ReleaseChannelDefinition</a></i>
    <a href="#resourceusageexportconfig" title="ResourceUsageExportConfig">ResourceUsageExportConfig</a>: <i>
      - <a href="resourceusageexportconfigdefinition.md">ResourceUsageExportConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>: <i>
      - <a href="verticalpodautoscalingdefinition.md">VerticalPodAutoscalingDefinition</a></i>
    <a href="#workloadidentityconfig" title="WorkloadIdentityConfig">WorkloadIdentityConfig</a>: <i>
      - <a href="workloadidentityconfigdefinition.md">WorkloadIdentityConfigDefinition</a></i>
</pre>

## Properties

#### ClusterIpv4Cidr

The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatapathProvider

The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation.

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

#### EnableAutopilot

Enable Autopilot for this cluster. Defaults to `false`.
Note that when this option is enabled, certain features of Standard GKE are not available.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#comparison)
for available features.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBinaryAuthorization

Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIntranodeVisibility

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

#### EnableShieldedNodes

Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTpu

Whether to enable Cloud TPU resources in this cluster.
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

#### NetworkingMode

Determines whether alias IPs or routes will be used for pod IPs in the cluster.
Options are `VPC_NATIVE` or `ROUTES`. `VPC_NATIVE` enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
and requires the `ip_allocation_policy` block to be defined. By default when this field is unspecified, GKE will create a `ROUTES`-based cluster.

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

#### PrivateIpv6GoogleAccess

The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

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

_Type_: List of <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddonsConfig

_Required_: No

_Type_: List of <a href="addonsconfigdefinition.md">AddonsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticatorGroupsConfig

_Required_: No

_Type_: List of <a href="authenticatorgroupsconfigdefinition.md">AuthenticatorGroupsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAutoscaling

_Required_: No

_Type_: List of <a href="clusterautoscalingdefinition.md">ClusterAutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseEncryption

_Required_: No

_Type_: List of <a href="databaseencryptiondefinition.md">DatabaseEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSnatStatus

_Required_: No

_Type_: List of <a href="defaultsnatstatusdefinition.md">DefaultSnatStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationPolicy

_Required_: No

_Type_: List of <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenancePolicy

_Required_: No

_Type_: List of <a href="maintenancepolicydefinition.md">MaintenancePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuth

_Required_: No

_Type_: List of <a href="masterauthdefinition.md">MasterAuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuthorizedNetworksConfig

_Required_: No

_Type_: List of <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No

_Type_: List of <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: No

_Type_: List of <a href="nodepooldefinition.md">NodePoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSecurityPolicyConfig

_Required_: No

_Type_: List of <a href="podsecuritypolicyconfigdefinition.md">PodSecurityPolicyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateClusterConfig

_Required_: No

_Type_: List of <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseChannel

_Required_: No

_Type_: List of <a href="releasechanneldefinition.md">ReleaseChannelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceUsageExportConfig

_Required_: No

_Type_: List of <a href="resourceusageexportconfigdefinition.md">ResourceUsageExportConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerticalPodAutoscaling

_Required_: No

_Type_: List of <a href="verticalpodautoscalingdefinition.md">VerticalPodAutoscalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadIdentityConfig

_Required_: No

_Type_: List of <a href="workloadidentityconfigdefinition.md">WorkloadIdentityConfigDefinition</a>

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

#### SelfLink

Returns the <code>SelfLink</code> value.

#### ServicesIpv4Cidr

Returns the <code>ServicesIpv4Cidr</code> value.

#### TpuIpv4CidrBlock

Returns the <code>TpuIpv4CidrBlock</code> value.

