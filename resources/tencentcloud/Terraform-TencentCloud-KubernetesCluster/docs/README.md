# Terraform::TencentCloud::KubernetesCluster

CloudFormation equivalent of tencentcloud_kubernetes_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::KubernetesCluster",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#certificationauthority" title="CertificationAuthority">CertificationAuthority</a>" : <i>String</i>,
        "<a href="#clustercidr" title="ClusterCidr">ClusterCidr</a>" : <i>String</i>,
        "<a href="#clusterdeploytype" title="ClusterDeployType">ClusterDeployType</a>" : <i>String</i>,
        "<a href="#clusterdesc" title="ClusterDesc">ClusterDesc</a>" : <i>String</i>,
        "<a href="#clusterexternalendpoint" title="ClusterExternalEndpoint">ClusterExternalEndpoint</a>" : <i>String</i>,
        "<a href="#clusterinternet" title="ClusterInternet">ClusterInternet</a>" : <i>Boolean</i>,
        "<a href="#clusterintranet" title="ClusterIntranet">ClusterIntranet</a>" : <i>Boolean</i>,
        "<a href="#clusterintranetsubnetid" title="ClusterIntranetSubnetId">ClusterIntranetSubnetId</a>" : <i>String</i>,
        "<a href="#clusteripvs" title="ClusterIpvs">ClusterIpvs</a>" : <i>Boolean</i>,
        "<a href="#clustermaxpodnum" title="ClusterMaxPodNum">ClusterMaxPodNum</a>" : <i>Double</i>,
        "<a href="#clustermaxservicenum" title="ClusterMaxServiceNum">ClusterMaxServiceNum</a>" : <i>Double</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#clusternodenum" title="ClusterNodeNum">ClusterNodeNum</a>" : <i>Double</i>,
        "<a href="#clusteros" title="ClusterOs">ClusterOs</a>" : <i>String</i>,
        "<a href="#clusterostype" title="ClusterOsType">ClusterOsType</a>" : <i>String</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>" : <i>Boolean</i>,
        "<a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#pgwendpoint" title="PgwEndpoint">PgwEndpoint</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#workerinstanceslist" title="WorkerInstancesList">WorkerInstancesList</a>" : <i>[ &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;, ... ]</i>,
        "<a href="#masterconfig" title="MasterConfig">MasterConfig</a>" : <i>[ &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>" : <i>[ &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::KubernetesCluster
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#certificationauthority" title="CertificationAuthority">CertificationAuthority</a>: <i>String</i>
    <a href="#clustercidr" title="ClusterCidr">ClusterCidr</a>: <i>String</i>
    <a href="#clusterdeploytype" title="ClusterDeployType">ClusterDeployType</a>: <i>String</i>
    <a href="#clusterdesc" title="ClusterDesc">ClusterDesc</a>: <i>String</i>
    <a href="#clusterexternalendpoint" title="ClusterExternalEndpoint">ClusterExternalEndpoint</a>: <i>String</i>
    <a href="#clusterinternet" title="ClusterInternet">ClusterInternet</a>: <i>Boolean</i>
    <a href="#clusterintranet" title="ClusterIntranet">ClusterIntranet</a>: <i>Boolean</i>
    <a href="#clusterintranetsubnetid" title="ClusterIntranetSubnetId">ClusterIntranetSubnetId</a>: <i>String</i>
    <a href="#clusteripvs" title="ClusterIpvs">ClusterIpvs</a>: <i>Boolean</i>
    <a href="#clustermaxpodnum" title="ClusterMaxPodNum">ClusterMaxPodNum</a>: <i>Double</i>
    <a href="#clustermaxservicenum" title="ClusterMaxServiceNum">ClusterMaxServiceNum</a>: <i>Double</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#clusternodenum" title="ClusterNodeNum">ClusterNodeNum</a>: <i>Double</i>
    <a href="#clusteros" title="ClusterOs">ClusterOs</a>: <i>String</i>
    <a href="#clusterostype" title="ClusterOsType">ClusterOsType</a>: <i>String</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#ignoreclustercidrconflict" title="IgnoreClusterCidrConflict">IgnoreClusterCidrConflict</a>: <i>Boolean</i>
    <a href="#managedclusterinternetsecuritypolicies" title="ManagedClusterInternetSecurityPolicies">ManagedClusterInternetSecurityPolicies</a>: <i>
      - String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#pgwendpoint" title="PgwEndpoint">PgwEndpoint</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#workerinstanceslist" title="WorkerInstancesList">WorkerInstancesList</a>: <i>
      - &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;</i>
    <a href="#masterconfig" title="MasterConfig">MasterConfig</a>: <i>
      - &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;</i>
    <a href="#workerconfig" title="WorkerConfig">WorkerConfig</a>: <i>
      - &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;</i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificationAuthority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### ClusterExternalEndpoint

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

#### ClusterNodeNum

_Required_: No

_Type_: Double

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

#### Domain

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

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgwEndpoint

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicy

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerInstancesList

_Required_: No

_Type_: List of &lt;a href=&#34;workerinstanceslist.md&#34;&gt;WorkerInstancesList&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;masterconfig.md&#34;&gt;MasterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerConfig

_Required_: No

_Type_: List of &lt;a href=&#34;workerconfig.md&#34;&gt;WorkerConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of &lt;a href=&#34;datadisk.md&#34;&gt;DataDisk&lt;/a&gt;

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

Returns the &lt;code&gt;CertificationAuthority&lt;/code&gt; value.

#### ClusterExternalEndpoint

Returns the &lt;code&gt;ClusterExternalEndpoint&lt;/code&gt; value.

#### ClusterNodeNum

Returns the &lt;code&gt;ClusterNodeNum&lt;/code&gt; value.

#### Domain

Returns the &lt;code&gt;Domain&lt;/code&gt; value.

#### Password

Returns the &lt;code&gt;Password&lt;/code&gt; value.

#### PgwEndpoint

Returns the &lt;code&gt;PgwEndpoint&lt;/code&gt; value.

#### SecurityPolicy

Returns the &lt;code&gt;SecurityPolicy&lt;/code&gt; value.

#### UserName

Returns the &lt;code&gt;UserName&lt;/code&gt; value.

#### WorkerInstancesList

Returns the &lt;code&gt;WorkerInstancesList&lt;/code&gt; value.

