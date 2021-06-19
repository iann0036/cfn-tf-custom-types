# TF::Rancher2::Cluster GkeConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>" : <i>String</i>,
    "<a href="#credential" title="Credential">Credential</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#enablealphafeature" title="EnableAlphaFeature">EnableAlphaFeature</a>" : <i>Boolean</i>,
    "<a href="#enableautorepair" title="EnableAutoRepair">EnableAutoRepair</a>" : <i>Boolean</i>,
    "<a href="#enableautoupgrade" title="EnableAutoUpgrade">EnableAutoUpgrade</a>" : <i>Boolean</i>,
    "<a href="#enablehorizontalpodautoscaling" title="EnableHorizontalPodAutoscaling">EnableHorizontalPodAutoscaling</a>" : <i>Boolean</i>,
    "<a href="#enablehttploadbalancing" title="EnableHttpLoadBalancing">EnableHttpLoadBalancing</a>" : <i>Boolean</i>,
    "<a href="#enablekubernetesdashboard" title="EnableKubernetesDashboard">EnableKubernetesDashboard</a>" : <i>Boolean</i>,
    "<a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>" : <i>Boolean</i>,
    "<a href="#enablemasterauthorizednetwork" title="EnableMasterAuthorizedNetwork">EnableMasterAuthorizedNetwork</a>" : <i>Boolean</i>,
    "<a href="#enablenetworkpolicyconfig" title="EnableNetworkPolicyConfig">EnableNetworkPolicyConfig</a>" : <i>Boolean</i>,
    "<a href="#enablenodepoolautoscaling" title="EnableNodepoolAutoscaling">EnableNodepoolAutoscaling</a>" : <i>Boolean</i>,
    "<a href="#enableprivateendpoint" title="EnablePrivateEndpoint">EnablePrivateEndpoint</a>" : <i>Boolean</i>,
    "<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>" : <i>Boolean</i>,
    "<a href="#enablestackdriverlogging" title="EnableStackdriverLogging">EnableStackdriverLogging</a>" : <i>Boolean</i>,
    "<a href="#enablestackdrivermonitoring" title="EnableStackdriverMonitoring">EnableStackdriverMonitoring</a>" : <i>Boolean</i>,
    "<a href="#imagetype" title="ImageType">ImageType</a>" : <i>String</i>,
    "<a href="#ippolicyclusteripv4cidrblock" title="IpPolicyClusterIpv4CidrBlock">IpPolicyClusterIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#ippolicyclustersecondaryrangename" title="IpPolicyClusterSecondaryRangeName">IpPolicyClusterSecondaryRangeName</a>" : <i>String</i>,
    "<a href="#ippolicycreatesubnetwork" title="IpPolicyCreateSubnetwork">IpPolicyCreateSubnetwork</a>" : <i>Boolean</i>,
    "<a href="#ippolicynodeipv4cidrblock" title="IpPolicyNodeIpv4CidrBlock">IpPolicyNodeIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#ippolicyservicesipv4cidrblock" title="IpPolicyServicesIpv4CidrBlock">IpPolicyServicesIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#ippolicyservicessecondaryrangename" title="IpPolicyServicesSecondaryRangeName">IpPolicyServicesSecondaryRangeName</a>" : <i>String</i>,
    "<a href="#ippolicysubnetworkname" title="IpPolicySubnetworkName">IpPolicySubnetworkName</a>" : <i>String</i>,
    "<a href="#issueclientcertificate" title="IssueClientCertificate">IssueClientCertificate</a>" : <i>Boolean</i>,
    "<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>" : <i>Boolean</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>, ... ]</i>,
    "<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>" : <i>Double</i>,
    "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
    "<a href="#machinetype" title="MachineType">MachineType</a>" : <i>String</i>,
    "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>String</i>,
    "<a href="#masterauthorizednetworkcidrblocks" title="MasterAuthorizedNetworkCidrBlocks">MasterAuthorizedNetworkCidrBlocks</a>" : <i>[ String, ... ]</i>,
    "<a href="#masteripv4cidrblock" title="MasterIpv4CidrBlock">MasterIpv4CidrBlock</a>" : <i>String</i>,
    "<a href="#masterversion" title="MasterVersion">MasterVersion</a>" : <i>String</i>,
    "<a href="#maxnodecount" title="MaxNodeCount">MaxNodeCount</a>" : <i>Double</i>,
    "<a href="#minnodecount" title="MinNodeCount">MinNodeCount</a>" : <i>Double</i>,
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#nodecount" title="NodeCount">NodeCount</a>" : <i>Double</i>,
    "<a href="#nodepool" title="NodePool">NodePool</a>" : <i>String</i>,
    "<a href="#nodeversion" title="NodeVersion">NodeVersion</a>" : <i>String</i>,
    "<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#preemptible" title="Preemptible">Preemptible</a>" : <i>Boolean</i>,
    "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>" : <i>[ <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a>, ... ]</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#subnetwork" title="SubNetwork">SubNetwork</a>" : <i>String</i>,
    "<a href="#taints" title="Taints">Taints</a>" : <i>[ String, ... ]</i>,
    "<a href="#useipaliases" title="UseIpAliases">UseIpAliases</a>" : <i>Boolean</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clusteripv4cidr" title="ClusterIpv4Cidr">ClusterIpv4Cidr</a>: <i>String</i>
<a href="#credential" title="Credential">Credential</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#enablealphafeature" title="EnableAlphaFeature">EnableAlphaFeature</a>: <i>Boolean</i>
<a href="#enableautorepair" title="EnableAutoRepair">EnableAutoRepair</a>: <i>Boolean</i>
<a href="#enableautoupgrade" title="EnableAutoUpgrade">EnableAutoUpgrade</a>: <i>Boolean</i>
<a href="#enablehorizontalpodautoscaling" title="EnableHorizontalPodAutoscaling">EnableHorizontalPodAutoscaling</a>: <i>Boolean</i>
<a href="#enablehttploadbalancing" title="EnableHttpLoadBalancing">EnableHttpLoadBalancing</a>: <i>Boolean</i>
<a href="#enablekubernetesdashboard" title="EnableKubernetesDashboard">EnableKubernetesDashboard</a>: <i>Boolean</i>
<a href="#enablelegacyabac" title="EnableLegacyAbac">EnableLegacyAbac</a>: <i>Boolean</i>
<a href="#enablemasterauthorizednetwork" title="EnableMasterAuthorizedNetwork">EnableMasterAuthorizedNetwork</a>: <i>Boolean</i>
<a href="#enablenetworkpolicyconfig" title="EnableNetworkPolicyConfig">EnableNetworkPolicyConfig</a>: <i>Boolean</i>
<a href="#enablenodepoolautoscaling" title="EnableNodepoolAutoscaling">EnableNodepoolAutoscaling</a>: <i>Boolean</i>
<a href="#enableprivateendpoint" title="EnablePrivateEndpoint">EnablePrivateEndpoint</a>: <i>Boolean</i>
<a href="#enableprivatenodes" title="EnablePrivateNodes">EnablePrivateNodes</a>: <i>Boolean</i>
<a href="#enablestackdriverlogging" title="EnableStackdriverLogging">EnableStackdriverLogging</a>: <i>Boolean</i>
<a href="#enablestackdrivermonitoring" title="EnableStackdriverMonitoring">EnableStackdriverMonitoring</a>: <i>Boolean</i>
<a href="#imagetype" title="ImageType">ImageType</a>: <i>String</i>
<a href="#ippolicyclusteripv4cidrblock" title="IpPolicyClusterIpv4CidrBlock">IpPolicyClusterIpv4CidrBlock</a>: <i>String</i>
<a href="#ippolicyclustersecondaryrangename" title="IpPolicyClusterSecondaryRangeName">IpPolicyClusterSecondaryRangeName</a>: <i>String</i>
<a href="#ippolicycreatesubnetwork" title="IpPolicyCreateSubnetwork">IpPolicyCreateSubnetwork</a>: <i>Boolean</i>
<a href="#ippolicynodeipv4cidrblock" title="IpPolicyNodeIpv4CidrBlock">IpPolicyNodeIpv4CidrBlock</a>: <i>String</i>
<a href="#ippolicyservicesipv4cidrblock" title="IpPolicyServicesIpv4CidrBlock">IpPolicyServicesIpv4CidrBlock</a>: <i>String</i>
<a href="#ippolicyservicessecondaryrangename" title="IpPolicyServicesSecondaryRangeName">IpPolicyServicesSecondaryRangeName</a>: <i>String</i>
<a href="#ippolicysubnetworkname" title="IpPolicySubnetworkName">IpPolicySubnetworkName</a>: <i>String</i>
<a href="#issueclientcertificate" title="IssueClientCertificate">IssueClientCertificate</a>: <i>Boolean</i>
<a href="#kubernetesdashboard" title="KubernetesDashboard">KubernetesDashboard</a>: <i>Boolean</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a></i>
<a href="#localssdcount" title="LocalSsdCount">LocalSsdCount</a>: <i>Double</i>
<a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
<a href="#machinetype" title="MachineType">MachineType</a>: <i>String</i>
<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>String</i>
<a href="#masterauthorizednetworkcidrblocks" title="MasterAuthorizedNetworkCidrBlocks">MasterAuthorizedNetworkCidrBlocks</a>: <i>
      - String</i>
<a href="#masteripv4cidrblock" title="MasterIpv4CidrBlock">MasterIpv4CidrBlock</a>: <i>String</i>
<a href="#masterversion" title="MasterVersion">MasterVersion</a>: <i>String</i>
<a href="#maxnodecount" title="MaxNodeCount">MaxNodeCount</a>: <i>Double</i>
<a href="#minnodecount" title="MinNodeCount">MinNodeCount</a>: <i>Double</i>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#nodecount" title="NodeCount">NodeCount</a>: <i>Double</i>
<a href="#nodepool" title="NodePool">NodePool</a>: <i>String</i>
<a href="#nodeversion" title="NodeVersion">NodeVersion</a>: <i>String</i>
<a href="#oauthscopes" title="OauthScopes">OauthScopes</a>: <i>
      - String</i>
<a href="#preemptible" title="Preemptible">Preemptible</a>: <i>Boolean</i>
<a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#resourcelabels" title="ResourceLabels">ResourceLabels</a>: <i>
      - <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a></i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#subnetwork" title="SubNetwork">SubNetwork</a>: <i>String</i>
<a href="#taints" title="Taints">Taints</a>: <i>
      - String</i>
<a href="#useipaliases" title="UseIpAliases">UseIpAliases</a>: <i>Boolean</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### ClusterIpv4Cidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credential

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAlphaFeature

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoRepair

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAutoUpgrade

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHorizontalPodAutoscaling

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttpLoadBalancing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKubernetesDashboard

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLegacyAbac

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMasterAuthorizedNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNetworkPolicyConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNodepoolAutoscaling

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateEndpoint

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePrivateNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStackdriverLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStackdriverMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyClusterIpv4CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyClusterSecondaryRangeName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyCreateSubnetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyNodeIpv4CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyServicesIpv4CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicyServicesSecondaryRangeName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPolicySubnetworkName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IssueClientCertificate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesDashboard

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="clusterregistrationtokendefinition2.md">ClusterRegistrationTokenDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalSsdCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAuthorizedNetworkCidrBlocks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterIpv4CidrBlock

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePool

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OauthScopes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preemptible

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

#### ResourceLabels

_Required_: No

_Type_: List of <a href="resourcelabelsdefinition.md">ResourceLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubNetwork

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taints

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIpAliases

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

