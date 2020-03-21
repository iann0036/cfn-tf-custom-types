# Terraform::Google::ContainerCluster

CloudFormation equivalent of google_container_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ContainerCluster",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#additionalzones" title="AdditionalZones">AdditionalZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>" : <i>String</i>,
        "<a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>" : <i>Boolean</i>,
        "<a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>" : <i>Boolean</i>,
        "<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>" : <i>Boolean</i>,
        "<a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>" : <i>Boolean</i>,
        "<a href="#enabletpu" title="EnableTpu">EnableTpu</a>" : <i>Boolean</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>" : <i>Double</i>,
        "<a href="#instancegroupurls" title="InstanceGroupUrls">InstanceGroupUrls</a>" : <i>[ String, ... ]</i>,
        "<a href="#labelfingerprint" title="LabelFingerprint">LabelFingerprint</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#loggingservice" title="LoggingService">LoggingService</a>" : <i>String</i>,
        "<a href="#masterversion" title="MasterVersion">MasterVersion</a>" : <i>String</i>,
        "<a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>" : <i>String</i>,
        "<a href="#monitoringservice" title="MonitoringService">MonitoringService</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#nodelocations" title="NodeLocations">NodeLocations</a>" : <i>[ String, ... ]</i>,
        "<a href="#nodeversion" title="NodeVersion">NodeVersion</a>" : <i>String</i>,
        "<a href="#operation" title="Operation">Operation</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>" : <i>Boolean</i>,
        "<a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>" : <i>[ &lt;a href=&#34;resourcelabels.md&#34;&gt;ResourceLabels&lt;/a&gt;, ... ]</i>,
        "<a href="#servicesipv4cidr" title="ServicesIpv4Cidr">ServicesIpv4Cidr</a>" : <i>String</i>,
        "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>" : <i>[ &lt;a href=&#34;addonsconfig.md&#34;&gt;AddonsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>" : <i>[ &lt;a href=&#34;authenticatorgroupsconfig.md&#34;&gt;AuthenticatorGroupsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>" : <i>[ &lt;a href=&#34;clusterautoscaling.md&#34;&gt;ClusterAutoscaling&lt;/a&gt;, ... ]</i>,
        "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>[ &lt;a href=&#34;ipallocationpolicy.md&#34;&gt;IpAllocationPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>" : <i>[ &lt;a href=&#34;maintenancepolicy.md&#34;&gt;MaintenancePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#masterauth" title="MasterAuth">MasterAuth</a>" : <i>[ &lt;a href=&#34;masterauth.md&#34;&gt;MasterAuth&lt;/a&gt;, ... ]</i>,
        "<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>" : <i>[ &lt;a href=&#34;masterauthorizednetworksconfig.md&#34;&gt;MasterAuthorizedNetworksConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>[ &lt;a href=&#34;networkpolicy.md&#34;&gt;NetworkPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ &lt;a href=&#34;nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ &lt;a href=&#34;nodepool.md&#34;&gt;NodePool&lt;/a&gt;, ... ]</i>,
        "<a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>" : <i>[ &lt;a href=&#34;podsecuritypolicyconfig.md&#34;&gt;PodSecurityPolicyConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>" : <i>[ &lt;a href=&#34;privateclusterconfig.md&#34;&gt;PrivateClusterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>" : <i>[ &lt;a href=&#34;verticalpodautoscaling.md&#34;&gt;VerticalPodAutoscaling&lt;/a&gt;, ... ]</i>,
        "<a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>" : <i>[ &lt;a href=&#34;horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;, ... ]</i>,
        "<a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>" : <i>[ &lt;a href=&#34;httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;, ... ]</i>,
        "<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>" : <i>[ &lt;a href=&#34;kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;, ... ]</i>,
        "<a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>" : <i>[ &lt;a href=&#34;networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>" : <i>[ &lt;a href=&#34;autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;, ... ]</i>,
        "<a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>" : <i>[ &lt;a href=&#34;resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;, ... ]</i>,
        "<a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>" : <i>[ &lt;a href=&#34;dailymaintenancewindow.md&#34;&gt;DailyMaintenanceWindow&lt;/a&gt;, ... ]</i>,
        "<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>" : <i>[ &lt;a href=&#34;clientcertificateconfig.md&#34;&gt;ClientCertificateConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ &lt;a href=&#34;cidrblocks.md&#34;&gt;CidrBlocks&lt;/a&gt;, ... ]</i>,
        "<a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>" : <i>[ &lt;a href=&#34;sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>" : <i>[ &lt;a href=&#34;shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>" : <i>[ &lt;a href=&#34;workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>[ &lt;a href=&#34;autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;, ... ]</i>,
        "<a href="#management" title="Management">Management</a>" : <i>[ &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ContainerCluster
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#initialnodecount" title="InitialNodeCount">InitialNodeCount</a>: <i>Double</i>
    <a href="#instancegroupurls" title="InstanceGroupUrls">InstanceGroupUrls</a>: <i>
      - String</i>
    <a href="#labelfingerprint" title="LabelFingerprint">LabelFingerprint</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#loggingservice" title="LoggingService">LoggingService</a>: <i>String</i>
    <a href="#masterversion" title="MasterVersion">MasterVersion</a>: <i>String</i>
    <a href="#minmasterversion" title="MinMasterVersion">MinMasterVersion</a>: <i>String</i>
    <a href="#monitoringservice" title="MonitoringService">MonitoringService</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#nodelocations" title="NodeLocations">NodeLocations</a>: <i>
      - String</i>
    <a href="#nodeversion" title="NodeVersion">NodeVersion</a>: <i>String</i>
    <a href="#operation" title="Operation">Operation</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#removedefaultnodepool" title="RemoveDefaultNodePool">RemoveDefaultNodePool</a>: <i>Boolean</i>
    <a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>: <i>
      - &lt;a href=&#34;resourcelabels.md&#34;&gt;ResourceLabels&lt;/a&gt;</i>
    <a href="#servicesipv4cidr" title="ServicesIpv4Cidr">ServicesIpv4Cidr</a>: <i>String</i>
    <a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#addonsconfig" title="AddonsConfig">AddonsConfig</a>: <i>
      - &lt;a href=&#34;addonsconfig.md&#34;&gt;AddonsConfig&lt;/a&gt;</i>
    <a href="#authenticatorgroupsconfig" title="AuthenticatorGroupsConfig">AuthenticatorGroupsConfig</a>: <i>
      - &lt;a href=&#34;authenticatorgroupsconfig.md&#34;&gt;AuthenticatorGroupsConfig&lt;/a&gt;</i>
    <a href="#clusterautoscaling" title="ClusterAutoscaling">ClusterAutoscaling</a>: <i>
      - &lt;a href=&#34;clusterautoscaling.md&#34;&gt;ClusterAutoscaling&lt;/a&gt;</i>
    <a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>: <i>
      - &lt;a href=&#34;ipallocationpolicy.md&#34;&gt;IpAllocationPolicy&lt;/a&gt;</i>
    <a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>: <i>
      - &lt;a href=&#34;maintenancepolicy.md&#34;&gt;MaintenancePolicy&lt;/a&gt;</i>
    <a href="#masterauth" title="MasterAuth">MasterAuth</a>: <i>
      - &lt;a href=&#34;masterauth.md&#34;&gt;MasterAuth&lt;/a&gt;</i>
    <a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>: <i>
      - &lt;a href=&#34;masterauthorizednetworksconfig.md&#34;&gt;MasterAuthorizedNetworksConfig&lt;/a&gt;</i>
    <a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>: <i>
      - &lt;a href=&#34;networkpolicy.md&#34;&gt;NetworkPolicy&lt;/a&gt;</i>
    <a href="#nodeconfig" title="NodeConfig">NodeConfig</a>: <i>
      - &lt;a href=&#34;nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;</i>
    <a href="#nodepool" title="NodePool">NodePool</a>: <i>
      - &lt;a href=&#34;nodepool.md&#34;&gt;NodePool&lt;/a&gt;</i>
    <a href="#podsecuritypolicyconfig" title="PodSecurityPolicyConfig">PodSecurityPolicyConfig</a>: <i>
      - &lt;a href=&#34;podsecuritypolicyconfig.md&#34;&gt;PodSecurityPolicyConfig&lt;/a&gt;</i>
    <a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>: <i>
      - &lt;a href=&#34;privateclusterconfig.md&#34;&gt;PrivateClusterConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#verticalpodautoscaling" title="VerticalPodAutoscaling">VerticalPodAutoscaling</a>: <i>
      - &lt;a href=&#34;verticalpodautoscaling.md&#34;&gt;VerticalPodAutoscaling&lt;/a&gt;</i>
    <a href="#horizontalpodautoscaling" title="HorizontalPodAutoscaling">HorizontalPodAutoscaling</a>: <i>
      - &lt;a href=&#34;horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;</i>
    <a href="#httploadbalancing" title="HttpLoadBalancing">HttpLoadBalancing</a>: <i>
      - &lt;a href=&#34;httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;</i>
    <a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>: <i>
      - &lt;a href=&#34;kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;</i>
    <a href="#networkpolicyconfig" title="NetworkPolicyConfig">NetworkPolicyConfig</a>: <i>
      - &lt;a href=&#34;networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;</i>
    <a href="#autoprovisioningdefaults" title="AutoProvisioningDefaults">AutoProvisioningDefaults</a>: <i>
      - &lt;a href=&#34;autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;</i>
    <a href="#resourcelimits" title="ResourceLimits">ResourceLimits</a>: <i>
      - &lt;a href=&#34;resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;</i>
    <a href="#dailymaintenancewindow" title="DailyMaintenanceWindow">DailyMaintenanceWindow</a>: <i>
      - &lt;a href=&#34;dailymaintenancewindow.md&#34;&gt;DailyMaintenanceWindow&lt;/a&gt;</i>
    <a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>: <i>
      - &lt;a href=&#34;clientcertificateconfig.md&#34;&gt;ClientCertificateConfig&lt;/a&gt;</i>
    <a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - &lt;a href=&#34;cidrblocks.md&#34;&gt;CidrBlocks&lt;/a&gt;</i>
    <a href="#sandboxconfig" title="SandboxConfig">SandboxConfig</a>: <i>
      - &lt;a href=&#34;sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;</i>
    <a href="#shieldedinstanceconfig" title="ShieldedInstanceConfig">ShieldedInstanceConfig</a>: <i>
      - &lt;a href=&#34;shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;</i>
    <a href="#workloadmetadataconfig" title="WorkloadMetadataConfig">WorkloadMetadataConfig</a>: <i>
      - &lt;a href=&#34;workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;</i>
    <a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>
      - &lt;a href=&#34;autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;</i>
    <a href="#management" title="Management">Management</a>: <i>
      - &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Endpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceGroupUrls

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelFingerprint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterVersion

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

#### Operation

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

_Type_: List of &lt;a href=&#34;resourcelabels.md&#34;&gt;ResourceLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicesIpv4Cidr

_Required_: No

_Type_: String

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

_Type_: List of &lt;a href=&#34;addonsconfig.md&#34;&gt;AddonsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticatorGroupsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;authenticatorgroupsconfig.md&#34;&gt;AuthenticatorGroupsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAutoscaling

_Required_: No

_Type_: List of &lt;a href=&#34;clusterautoscaling.md&#34;&gt;ClusterAutoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;ipallocationpolicy.md&#34;&gt;IpAllocationPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenancePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;maintenancepolicy.md&#34;&gt;MaintenancePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuth

_Required_: No

_Type_: List of &lt;a href=&#34;masterauth.md&#34;&gt;MasterAuth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuthorizedNetworksConfig

_Required_: No

_Type_: List of &lt;a href=&#34;masterauthorizednetworksconfig.md&#34;&gt;MasterAuthorizedNetworksConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;networkpolicy.md&#34;&gt;NetworkPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeConfig

_Required_: No

_Type_: List of &lt;a href=&#34;nodeconfig.md&#34;&gt;NodeConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: No

_Type_: List of &lt;a href=&#34;nodepool.md&#34;&gt;NodePool&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSecurityPolicyConfig

_Required_: No

_Type_: List of &lt;a href=&#34;podsecuritypolicyconfig.md&#34;&gt;PodSecurityPolicyConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateClusterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;privateclusterconfig.md&#34;&gt;PrivateClusterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerticalPodAutoscaling

_Required_: No

_Type_: List of &lt;a href=&#34;verticalpodautoscaling.md&#34;&gt;VerticalPodAutoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HorizontalPodAutoscaling

_Required_: No

_Type_: List of &lt;a href=&#34;horizontalpodautoscaling.md&#34;&gt;HorizontalPodAutoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLoadBalancing

_Required_: No

_Type_: List of &lt;a href=&#34;httploadbalancing.md&#34;&gt;HttpLoadBalancing&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesDashboard

_Required_: No

_Type_: List of &lt;a href=&#34;kubernetesdashboard.md&#34;&gt;KubernetesDashboard&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkPolicyConfig

_Required_: No

_Type_: List of &lt;a href=&#34;networkpolicyconfig.md&#34;&gt;NetworkPolicyConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoProvisioningDefaults

_Required_: No

_Type_: List of &lt;a href=&#34;autoprovisioningdefaults.md&#34;&gt;AutoProvisioningDefaults&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLimits

_Required_: No

_Type_: List of &lt;a href=&#34;resourcelimits.md&#34;&gt;ResourceLimits&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyMaintenanceWindow

_Required_: No

_Type_: List of &lt;a href=&#34;dailymaintenancewindow.md&#34;&gt;DailyMaintenanceWindow&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateConfig

_Required_: No

_Type_: List of &lt;a href=&#34;clientcertificateconfig.md&#34;&gt;ClientCertificateConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlocks

_Required_: No

_Type_: List of &lt;a href=&#34;cidrblocks.md&#34;&gt;CidrBlocks&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxConfig

_Required_: No

_Type_: List of &lt;a href=&#34;sandboxconfig.md&#34;&gt;SandboxConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShieldedInstanceConfig

_Required_: No

_Type_: List of &lt;a href=&#34;shieldedinstanceconfig.md&#34;&gt;ShieldedInstanceConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkloadMetadataConfig

_Required_: No

_Type_: List of &lt;a href=&#34;workloadmetadataconfig.md&#34;&gt;WorkloadMetadataConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No

_Type_: List of &lt;a href=&#34;autoscaling.md&#34;&gt;Autoscaling&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Management

_Required_: No

_Type_: List of &lt;a href=&#34;management.md&#34;&gt;Management&lt;/a&gt;

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

Returns the &lt;code&gt;Endpoint&lt;/code&gt; value.

#### InstanceGroupUrls

Returns the &lt;code&gt;InstanceGroupUrls&lt;/code&gt; value.

#### LabelFingerprint

Returns the &lt;code&gt;LabelFingerprint&lt;/code&gt; value.

#### MasterVersion

Returns the &lt;code&gt;MasterVersion&lt;/code&gt; value.

#### Operation

Returns the &lt;code&gt;Operation&lt;/code&gt; value.

#### ServicesIpv4Cidr

Returns the &lt;code&gt;ServicesIpv4Cidr&lt;/code&gt; value.

