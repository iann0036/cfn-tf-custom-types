# TF::TencentCloud::KubernetesCluster

Provide a resource to create a kubernetes cluster.

~> **NOTE:** To use the custom Kubernetes component startup parameter function (parameter `extra_args`), you need to submit a ticket for application.
~> **NOTE:**  We recommend the usage of one cluster without worker config + node pool to manage cluster and nodes. It's a more flexible way than manage worker config with tencentcloud_kubernetes_cluster, tencentcloud_kubernetes_scale_worker or exist node management of `tencentcloud_kubernetes_attachment`. Cause some unchangeable parameters of `worker_config` may cause the whole cluster resource `force new`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::KubernetesCluster",
    "Properties" : {
        "<a href="#basepodnum" title="BasePodNum">BasePodNum</a>" : <i>Double</i>,
        "<a href="#claimexpiredseconds" title="ClaimExpiredSeconds">ClaimExpiredSeconds</a>" : <i>Double</i>,
        "<a href="#clusterasenabled" title="ClusterAsEnabled">ClusterAsEnabled</a>" : <i>Boolean</i>,
        "<a href="#clustercidr" title="ClusterCidr">ClusterCidr</a>" : <i>String</i>,
        "<a href="#clusterdeploytype" title="ClusterDeployType">ClusterDeployType</a>" : <i>String</i>,
        "<a href="#clusterdesc" title="ClusterDesc">ClusterDesc</a>" : <i>String</i>,
        "<a href="#clusterinternet" title="ClusterInternet">ClusterInternet</a>" : <i>Boolean</i>,
        "<a href="#clusterintranet" title="ClusterIntranet">ClusterIntranet</a>" : <i>Boolean</i>,
        "<a href="#clusterintranetsubnetid" title="ClusterIntranetSubnetId">ClusterIntranetSubnetId</a>" : <i>String</i>,
        "<a href="#clusteripvs" title="ClusterIpvs">ClusterIpvs</a>" : <i>Boolean</i>,
        "<a href="#clustermaxpodnum" title="ClusterMaxPodNum">ClusterMaxPodNum</a>" : <i>Double</i>,
        "<a href="#clustermaxservicenum" title="ClusterMaxServiceNum">ClusterMaxServiceNum</a>" : <i>Double</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#clusteros" title="ClusterOs">ClusterOs</a>" : <i>String</i>,
        "<a href="#clusterostype" title="ClusterOsType">ClusterOsType</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>" : <i>String</i>,
        "<a href="#enablecustomizedpodcidr" title="EnableCustomizedPodCidr">EnableCustomizedPodCidr</a>" : <i>Boolean</i>,
        "<a href="#enisubnetids" title="EniSubnetIds">EniSubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ String, ... ]</i>,
        "<a href="#globedesiredpodnum" title="GlobeDesiredPodNum">GlobeDesiredPodNum</a>" : <i>Double</i>,
        "<a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>" : <i>Boolean</i>,
        "<a href="#isnonstaticipmode" title="IsNonStaticIpMode">IsNonStaticIpMode</a>" : <i>Boolean</i>,
        "<a href="#kubeproxymode" title="KubeProxyMode">KubeProxyMode</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#mounttarget" title="MountTarget">MountTarget</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#nodenametype" title="NodeNameType">NodeNameType</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#unschedulable" title="Unschedulable">Unschedulable</a>" : <i>Double</i>,
        "<a href="#upgradeinstancesfollowcluster" title="UpgradeInstancesFollowCluster">UpgradeInstancesFollowCluster</a>" : <i>Boolean</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#clusterextraargs" title="ClusterExtraArgs">ClusterExtraArgs</a>" : <i>[ <a href="clusterextraargsdefinition.md">ClusterExtraArgsDefinition</a>, ... ]</i>,
        "<a href="#existinstance" title="ExistInstance">ExistInstance</a>" : <i>[ <a href="existinstancedefinition.md">ExistInstanceDefinition</a>, ... ]</i>,
        "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="masterconfigdefinition.md">MasterConfigDefinition</a>, ... ]</i>,
        "<a href="#nodepoolglobalconfig" title="NodePoolGlobalConfig">NodePoolGlobalConfig</a>" : <i>[ <a href="nodepoolglobalconfigdefinition.md">NodePoolGlobalConfigDefinition</a>, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::KubernetesCluster
Properties:
    <a href="#basepodnum" title="BasePodNum">BasePodNum</a>: <i>Double</i>
    <a href="#claimexpiredseconds" title="ClaimExpiredSeconds">ClaimExpiredSeconds</a>: <i>Double</i>
    <a href="#clusterasenabled" title="ClusterAsEnabled">ClusterAsEnabled</a>: <i>Boolean</i>
    <a href="#clustercidr" title="ClusterCidr">ClusterCidr</a>: <i>String</i>
    <a href="#clusterdeploytype" title="ClusterDeployType">ClusterDeployType</a>: <i>String</i>
    <a href="#clusterdesc" title="ClusterDesc">ClusterDesc</a>: <i>String</i>
    <a href="#clusterinternet" title="ClusterInternet">ClusterInternet</a>: <i>Boolean</i>
    <a href="#clusterintranet" title="ClusterIntranet">ClusterIntranet</a>: <i>Boolean</i>
    <a href="#clusterintranetsubnetid" title="ClusterIntranetSubnetId">ClusterIntranetSubnetId</a>: <i>String</i>
    <a href="#clusteripvs" title="ClusterIpvs">ClusterIpvs</a>: <i>Boolean</i>
    <a href="#clustermaxpodnum" title="ClusterMaxPodNum">ClusterMaxPodNum</a>: <i>Double</i>
    <a href="#clustermaxservicenum" title="ClusterMaxServiceNum">ClusterMaxServiceNum</a>: <i>Double</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#clusteros" title="ClusterOs">ClusterOs</a>: <i>String</i>
    <a href="#clusterostype" title="ClusterOsType">ClusterOsType</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>: <i>String</i>
    <a href="#enablecustomizedpodcidr" title="EnableCustomizedPodCidr">EnableCustomizedPodCidr</a>: <i>Boolean</i>
    <a href="#enisubnetids" title="EniSubnetIds">EniSubnetIds</a>: <i>
      - String</i>
    <a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - String</i>
    <a href="#globedesiredpodnum" title="GlobeDesiredPodNum">GlobeDesiredPodNum</a>: <i>Double</i>
    <a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>: <i>Boolean</i>
    <a href="#isnonstaticipmode" title="IsNonStaticIpMode">IsNonStaticIpMode</a>: <i>Boolean</i>
    <a href="#kubeproxymode" title="KubeProxyMode">KubeProxyMode</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>: <i>
      - String</i>
    <a href="#mounttarget" title="MountTarget">MountTarget</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#nodenametype" title="NodeNameType">NodeNameType</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#unschedulable" title="Unschedulable">Unschedulable</a>: <i>Double</i>
    <a href="#upgradeinstancesfollowcluster" title="UpgradeInstancesFollowCluster">UpgradeInstancesFollowCluster</a>: <i>Boolean</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#clusterextraargs" title="ClusterExtraArgs">ClusterExtraArgs</a>: <i>
      - <a href="clusterextraargsdefinition.md">ClusterExtraArgsDefinition</a></i>
    <a href="#existinstance" title="ExistInstance">ExistInstance</a>: <i>
      - <a href="existinstancedefinition.md">ExistInstanceDefinition</a></i>
    <a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="masterconfigdefinition.md">MasterConfigDefinition</a></i>
    <a href="#nodepoolglobalconfig" title="NodePoolGlobalConfig">NodePoolGlobalConfig</a>: <i>
      - <a href="nodepoolglobalconfigdefinition.md">NodePoolGlobalConfigDefinition</a></i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfigdefinition.md">WorkerConfigDefinition</a></i>
</pre>

## Properties

#### BasePodNum

The number of basic pods. valid when enable_customized_pod_cidr=true.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClaimExpiredSeconds

Claim expired seconds to recycle ENI. This field can only set when field `network_type` is 'VPC-CNI'. `claim_expired_seconds` must greater or equal than 300 and less than 15768000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAsEnabled

Indicates whether to enable cluster node auto scaler. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterCidr

A network address block of the cluster. Different from vpc cidr and cidr of other clusters within this vpc. Must be in  10./192.168/172.[16-31] segments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDeployType

Deployment type of the cluster, the available values include: 'MANAGED_CLUSTER' and 'INDEPENDENT_CLUSTER'. Default is 'MANAGED_CLUSTER'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDesc

Description of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterInternet

Open internet access or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIntranet

Open intranet access or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIntranetSubnetId

Subnet id who can access this independent cluster, this field must and can only set  when `cluster_intranet` is true. `cluster_intranet_subnet_id` can not modify once be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpvs

Indicates whether `ipvs` is enabled. Default is true. False means `iptables` is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMaxPodNum

The maximum number of Pods per node in the cluster. Default is 256. Must be a multiple of 16 and large than 32.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMaxServiceNum

The maximum number of services in the cluster. Default is 256. Must be a multiple of 16.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

Name of the cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterOs

Operating system of the cluster, the available values include: 'centos7.6.0_x64','ubuntu18.04.1x86_64','tlinux2.4x86_64'. Default is 'tlinux2.4x86_64'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterOsType

Image type of the cluster os, the available values include: 'GENERAL'. Default is 'GENERAL'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

Version of the cluster, Default is '1.10.5'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRuntime

Runtime type of the cluster, the available values include: 'docker' and 'containerd'. Default is 'docker'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

Indicates whether cluster deletion protection is enabled. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerGraphPath

Docker graph path. Default is `/var/lib/docker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCustomizedPodCidr

Whether to enable the custom mode of node podCIDR size. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EniSubnetIds

Subnet Ids for cluster with VPC-CNI network mode. This field can only set when field `network_type` is 'VPC-CNI'. `eni_subnet_ids` can not empty once be set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

Custom parameter information related to the node.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobeDesiredPodNum

Indicate to set desired pod number in node. valid when enable_customized_pod_cidr=true, and it takes effect for all nodes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreClusterCidrConflict

Indicates whether to ignore the cluster cidr conflict error. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsNonStaticIpMode

Indicates whether non-static ip mode is enabled. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeProxyMode

Cluster kube-proxy mode, the available values include: 'kube-proxy-bpf'. Default is not set.When set to kube-proxy-bpf, cluster version greater than 1.14 and with Tencent Linux 2.4 is required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

Labels of tke cluster nodes.

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedClusterInternetSecurityPolicies

Security policies for managed cluster internet, like:'192.168.1.0/24' or '113.116.51.27', '0.0.0.0/0' means all. This field can only set when field `cluster_deploy_type` is 'MANAGED_CLUSTER' and `cluster_internet` is true. `managed_cluster_internet_security_policies` can not delete or empty once be set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTarget

Mount target. Default is not mounting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Cluster network type, GR or VPC-CNI. Default is GR.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNameType

Node name type of Cluster, the available values include: 'lan-ip' and 'hostname', Default is 'lan-ip'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Project ID, default value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

A network address block of the service. Different from vpc cidr and cidr of other clusters within this vpc. Must be in  10./192.168/172.[16-31] segments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of the cluster.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unschedulable

Sets whether the joining node participates in the schedule. Default is '0'. Participate in scheduling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeInstancesFollowCluster

Indicates whether upgrade all instances when cluster_version change. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Vpc Id of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterExtraArgs

_Required_: No

_Type_: List of <a href="clusterextraargsdefinition.md">ClusterExtraArgsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExistInstance

_Required_: No

_Type_: List of <a href="existinstancedefinition.md">ExistInstanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of <a href="masterconfigdefinition.md">MasterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePoolGlobalConfig

_Required_: No

_Type_: List of <a href="nodepoolglobalconfigdefinition.md">NodePoolGlobalConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of <a href="workerconfigdefinition.md">WorkerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificationAuthority

Returns the <code>CertificationAuthority</code> value.

#### ClusterExternalEndpoint

Returns the <code>ClusterExternalEndpoint</code> value.

#### ClusterNodeNum

Returns the <code>ClusterNodeNum</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### Id

Returns the <code>Id</code> value.

#### KubeConfig

Returns the <code>KubeConfig</code> value.

#### Password

Returns the <code>Password</code> value.

#### PgwEndpoint

Returns the <code>PgwEndpoint</code> value.

#### SecurityPolicy

Returns the <code>SecurityPolicy</code> value.

#### UserName

Returns the <code>UserName</code> value.

#### WorkerInstancesList

Returns the <code>WorkerInstancesList</code> value.

