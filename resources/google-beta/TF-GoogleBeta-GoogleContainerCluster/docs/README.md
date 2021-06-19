# TF::GoogleBeta::GoogleContainerCluster

CloudFormation equivalent of google_container_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleContainerCluster",
    "Properties" : {
        "<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>" : <i>String</i>,
        "<a href="#datapathprovider" title="DatapathProvider">DatapathProvider</a>" : <i>String</i>,
        "<a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enableautopilot" title="EnableAutopilot">EnableAutopilot</a>" : <i>Boolean</i>,
        "<a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>" : <i>Boolean</i>,
        "<a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>" : <i>Boolean</i>,
        "<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>" : <i>Boolean</i>,
        "<a href="#enablel4ilbsubsetting" title="EnableL4IlbSubsetting">EnableL4IlbSubsetting</a>" : <i>Boolean</i>,
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
        "<a href="#clustertelemetry" title="ClusterTelemetry">ClusterTelemetry</a>" : <i>[ <a href="clustertelemetrydefinition.md">ClusterTelemetryDefinition</a>, ... ]</i>,
        "<a href="#confidentialnodes" title="ConfidentialNodes">ConfidentialNodes</a>" : <i>[ <a href="confidentialnodesdefinition.md">ConfidentialNodesDefinition</a>, ... ]</i>,
        "<a href="#databaseencryption" title="DatabaseEncryption">DatabaseEncryption</a>" : <i>[ <a href="databaseencryptiondefinition.md">DatabaseEncryptionDefinition</a>, ... ]</i>,
        "<a href="#defaultsnatstatus" title="DefaultSnatStatus">DefaultSnatStatus</a>" : <i>[ <a href="defaultsnatstatusdefinition.md">DefaultSnatStatusDefinition</a>, ... ]</i>,
        "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>[ <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a>, ... ]</i>,
        "<a href="#maintenancepolicy" title="MaintenancePolicy">MaintenancePolicy</a>" : <i>[ <a href="maintenancepolicydefinition.md">MaintenancePolicyDefinition</a>, ... ]</i>,
        "<a href="#masterauth" title="MasterAuth">MasterAuth</a>" : <i>[ <a href="masterauthdefinition.md">MasterAuthDefinition</a>, ... ]</i>,
        "<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>" : <i>[ <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a>, ... ]</i>,
        "<a href="#networkpolicy" title="NetworkPolicy">NetworkPolicy</a>" : <i>[ <a href="networkpolicydefinition.md">NetworkPolicyDefinition</a>, ... ]</i>,
        "<a href="#nodeconfig" title="NodeConfig">NodeConfig</a>" : <i>[ <a href="nodeconfigdefinition.md">NodeConfigDefinition</a>, ... ]</i>,
        "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>[ <a href="nodepooldefinition.md">NodePoolDefinition</a>, ... ]</i>,
        "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>, ... ]</i>,
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
Type: TF::GoogleBeta::GoogleContainerCluster
Properties:
    <a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>: <i>String</i>
    <a href="#datapathprovider" title="DatapathProvider">DatapathProvider</a>: <i>String</i>
    <a href="#defaultmaxpodspernode" title="DefaultMaxPodsPerNode">DefaultMaxPodsPerNode</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enableautopilot" title="EnableAutopilot">EnableAutopilot</a>: <i>Boolean</i>
    <a href="#enablebinaryauthorization" title="EnableBinaryAuthorization">EnableBinaryAuthorization</a>: <i>Boolean</i>
    <a href="#enableintranodevisibility" title="EnableIntranodeVisibility">EnableIntranodeVisibility</a>: <i>Boolean</i>
    <a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>: <i>Boolean</i>
    <a href="#enablel4ilbsubsetting" title="EnableL4IlbSubsetting">EnableL4IlbSubsetting</a>: <i>Boolean</i>
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
    <a href="#clustertelemetry" title="ClusterTelemetry">ClusterTelemetry</a>: <i>
      - <a href="clustertelemetrydefinition.md">ClusterTelemetryDefinition</a></i>
    <a href="#confidentialnodes" title="ConfidentialNodes">ConfidentialNodes</a>: <i>
      - <a href="confidentialnodesdefinition.md">ConfidentialNodesDefinition</a></i>
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
    <a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a></i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatapathProvider

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

#### EnableAutopilot

_Required_: No

_Type_: Boolean

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

#### EnableL4IlbSubsetting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLegacyAbac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableShieldedNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTpu

_Required_: No

_Type_: Boolean

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

#### NetworkingMode

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

#### PrivateIpv6GoogleAccess

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoveDefaultNodePool

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceLabels

_Required_: No

_Type_: List of <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

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

#### ClusterTelemetry

_Required_: No

_Type_: List of <a href="clustertelemetrydefinition.md">ClusterTelemetryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidentialNodes

_Required_: No

_Type_: List of <a href="confidentialnodesdefinition.md">ConfidentialNodesDefinition</a>

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

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>

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

