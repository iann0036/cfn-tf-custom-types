# Terraform::TencentCloud::KubernetesCluster

CloudFormation equivalent of tencentcloud_kubernetes_cluster

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDeployType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDesc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterInternet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIntranet

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIntranetSubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterIpvs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMaxPodNum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterMaxServiceNum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterOs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterOsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRuntime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreClusterCidrConflict

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedClusterInternetSecurityPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

