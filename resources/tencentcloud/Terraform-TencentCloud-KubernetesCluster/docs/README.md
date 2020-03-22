# Terraform::TencentCloud::KubernetesCluster

Provide a resource to create a kubernetes cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::KubernetesCluster",
    "Properties" : {
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
        "<a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>" : <i>Boolean</i>,
        "<a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ <a href="masterconfig.md">MasterConfig</a>, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ <a href="workerconfig.md">WorkerConfig</a>, ... ]</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadisk.md">DataDisk</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::KubernetesCluster
Properties:
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
    <a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>: <i>Boolean</i>
    <a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>: <i>
      - String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - <a href="masterconfig.md">MasterConfig</a></i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - <a href="workerconfig.md">WorkerConfig</a></i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadisk.md">DataDisk</a></i>
</pre>

## Properties

#### ClusterCidr

A network address block of the cluster. Different from vpc cidr and cidr of other clusters within this vpc. Must be in  10./192.168/172.[16-31] segments.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDeployType

Deployment type of the cluster, the available values include: 'MANAGED_CLUSTER' and 'INDEPENDENT_CLUSTER', Default is 'MANAGED_CLUSTER'.

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

Indicates whether ipvs is enabled. Default is true.

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

Operating system of the cluster, the available values include: 'centos7.2x86_64','centos7.6x86_64','ubuntu16.04.1 LTSx86_64','ubuntu18.04.1 LTSx86_64'. Default is 'ubuntu16.04.1 LTSx86_64'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterOsType

Image type of the cluster os, the available values include: 'DOCKER_CUSTOMIZE','GENERAL'. Default is 'GENERAL'. 'DOCKER_CUSTOMIZE' means 'TKE-Optimized'. Only 'centos7.6x86_64' or 'ubuntu18.04.1 LTSx86_64' support 'DOCKER_CUSTOMIZE' now.

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

#### IgnoreClusterCidrConflict

Indicates whether to ignore the cluster cidr conflict error. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedClusterInternetSecurityPolicies

Security policies for managed cluster internet, like:'192.168.1.0/24' or '113.116.51.27', '0.0.0.0/0' means all. This field can only set when field `cluster_deploy_type` is 'MANAGED_CLUSTER' and `cluster_internet` is true. `managed_cluster_internet_security_policies` can not delete or empty once be set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Project ID, default value is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of the cluster.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Vpc Id of the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of <a href="masterconfig.md">MasterConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of <a href="workerconfig.md">WorkerConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

