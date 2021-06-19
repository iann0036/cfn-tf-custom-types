# TF::Rancher2::Cluster GkeConfigV2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusteripv4cidrblock" title="ClusterIpv4CidrBlock">ClusterIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>" : <i>Boolean</i>,
    "<a href="#googlecredentialsecret" title="GoogleCredentialSecret">GoogleCredentialSecret</a>" : <i>String</i>,
    "<a href="#imported" title="Imported">Imported</a>" : <i>Boolean</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>, ... ]</i>,
    "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
    "<a href="#loggingservice" title="LoggingService">LoggingService</a>" : <i>String</i>,
    "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>String</i>,
    "<a href="#monitoringservice" title="MonitoringService">MonitoringService</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#networkpolicyenabled" title="NetworkPolicyEnabled">NetworkPolicyEnabled</a>" : <i>Boolean</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
    "<a href="#clusteraddons" title="ClusterAddons">ClusterAddons</a>" : <i>[ <a href="clusteraddonsdefinition.md">ClusterAddonsDefinition</a>, ... ]</i>,
    "<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>" : <i>[ <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a>, ... ]</i>,
    "<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>" : <i>[ <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a>, ... ]</i>,
    "<a href="#nodepools" title="NodePools">NodePools</a>" : <i>[ <a href="nodepoolsdefinition.md">NodePoolsDefinition</a>, ... ]</i>,
    "<a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>" : <i>[ <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clusteripv4cidrblock" title="ClusterIpv4CidrBlock">ClusterIpv4CidrBlock</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enablekubernetesalpha" title="EnableKubernetesAlpha">EnableKubernetesAlpha</a>: <i>Boolean</i>
<a href="#googlecredentialsecret" title="GoogleCredentialSecret">GoogleCredentialSecret</a>: <i>String</i>
<a href="#imported" title="Imported">Imported</a>: <i>Boolean</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a></i>
<a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
<a href="#loggingservice" title="LoggingService">LoggingService</a>: <i>String</i>
<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>String</i>
<a href="#monitoringservice" title="MonitoringService">MonitoringService</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#networkpolicyenabled" title="NetworkPolicyEnabled">NetworkPolicyEnabled</a>: <i>Boolean</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
<a href="#clusteraddons" title="ClusterAddons">ClusterAddons</a>: <i>
      - <a href="clusteraddonsdefinition.md">ClusterAddonsDefinition</a></i>
<a href="#ipallocationpolicy" title="IpAllocationPolicy">IpAllocationPolicy</a>: <i>
      - <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a></i>
<a href="#masterauthorizednetworksconfig" title="MasterAuthorizedNetworksConfig">MasterAuthorizedNetworksConfig</a>: <i>
      - <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a></i>
<a href="#nodepools" title="NodePools">NodePools</a>: <i>
      - <a href="nodepoolsdefinition.md">NodePoolsDefinition</a></i>
<a href="#privateclusterconfig" title="PrivateClusterConfig">PrivateClusterConfig</a>: <i>
      - <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a></i>
</pre>

## Properties

#### ClusterIpv4CidrBlock

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKubernetesAlpha

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleCredentialSecret

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

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

#### NetworkPolicyEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

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

#### ClusterAddons

_Required_: No

_Type_: List of <a href="clusteraddonsdefinition.md">ClusterAddonsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationPolicy

_Required_: No

_Type_: List of <a href="ipallocationpolicydefinition.md">IpAllocationPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuthorizedNetworksConfig

_Required_: No

_Type_: List of <a href="masterauthorizednetworksconfigdefinition.md">MasterAuthorizedNetworksConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePools

_Required_: No

_Type_: List of <a href="nodepoolsdefinition.md">NodePoolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateClusterConfig

_Required_: No

_Type_: List of <a href="privateclusterconfigdefinition.md">PrivateClusterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

