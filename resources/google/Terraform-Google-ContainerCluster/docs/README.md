# Terraform::Google::ContainerCluster

CloudFormation equivalent of google_container_cluster

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMaxPodsPerNode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBinaryAuthorization

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIntranodeVisibility

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKubernetesAlpha

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLegacyAbac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTpu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinMasterVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitoringService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeLocations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDefaultNodePool

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLabels

_Required_: No

_Type_: List of <a href="resourcelabels.md">ResourceLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

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

