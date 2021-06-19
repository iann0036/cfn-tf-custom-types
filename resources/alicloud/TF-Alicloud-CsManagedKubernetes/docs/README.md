# TF::Alicloud::CsManagedKubernetes

This resource will help you to manage a ManagedKubernetes Cluster in Alibaba Cloud Kubernetes Service. 

-> **NOTE:** Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `new_nat_gateway` to "true" to create one automatically.

-> **NOTE:** Creating kubernetes cluster need to install several packages and it will cost about 15 minutes. Please be patient.

-> **NOTE:** From version 1.9.4, the provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** From version 1.20.0, the provider supports disabling internet load balancer for API Server by setting `false` to `slb_internet_enabled`.

-> **NOTE:** If you want to manage Kubernetes, you can use [Kubernete...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CsManagedKubernetes",
    "Properties" : {
        "<a href="#apiaudiences" title="ApiAudiences">ApiAudiences</a>" : <i>[ String, ... ]</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#clientcert" title="ClientCert">ClientCert</a>" : <i>String</i>,
        "<a href="#clientkey" title="ClientKey">ClientKey</a>" : <i>String</i>,
        "<a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>" : <i>String</i>,
        "<a href="#clusterdomain" title="ClusterDomain">ClusterDomain</a>" : <i>String</i>,
        "<a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>" : <i>String</i>,
        "<a href="#clusterspec" title="ClusterSpec">ClusterSpec</a>" : <i>String</i>,
        "<a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>" : <i>String</i>,
        "<a href="#customsan" title="CustomSan">CustomSan</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#enablessh" title="EnableSsh">EnableSsh</a>" : <i>Boolean</i>,
        "<a href="#encryptionproviderkey" title="EncryptionProviderKey">EncryptionProviderKey</a>" : <i>String</i>,
        "<a href="#excludeautoscalernodes" title="ExcludeAutoscalerNodes">ExcludeAutoscalerNodes</a>" : <i>Boolean</i>,
        "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Boolean</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>" : <i>Boolean</i>,
        "<a href="#isenterprisesecuritygroup" title="IsEnterpriseSecurityGroup">IsEnterpriseSecurityGroup</a>" : <i>Boolean</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>, ... ]</i>,
        "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>String</i>,
        "<a href="#loadbalancerspec" title="LoadBalancerSpec">LoadBalancerSpec</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>" : <i>Boolean</i>,
        "<a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>" : <i>Double</i>,
        "<a href="#nodenamemode" title="NodeNameMode">NodeNameMode</a>" : <i>String</i>,
        "<a href="#nodeportrange" title="NodePortRange">NodePortRange</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
        "<a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxymode" title="ProxyMode">ProxyMode</a>" : <i>String</i>,
        "<a href="#rdsinstances" title="RdsInstances">RdsInstances</a>" : <i>[ String, ... ]</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>[ <a href="runtimedefinition.md">RuntimeDefinition</a>, ... ]</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#serviceaccountissuer" title="ServiceAccountIssuer">ServiceAccountIssuer</a>" : <i>String</i>,
        "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
        "<a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#userca" title="UserCa">UserCa</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vswitchids" title="VswitchIds">VswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#workerautorenew" title="WorkerAutoRenew">WorkerAutoRenew</a>" : <i>Boolean</i>,
        "<a href="#workerautorenewperiod" title="WorkerAutoRenewPeriod">WorkerAutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#workerdatadiskcategory" title="WorkerDataDiskCategory">WorkerDataDiskCategory</a>" : <i>String</i>,
        "<a href="#workerdatadisksize" title="WorkerDataDiskSize">WorkerDataDiskSize</a>" : <i>Double</i>,
        "<a href="#workerdiskcategory" title="WorkerDiskCategory">WorkerDiskCategory</a>" : <i>String</i>,
        "<a href="#workerdiskperformancelevel" title="WorkerDiskPerformanceLevel">WorkerDiskPerformanceLevel</a>" : <i>String</i>,
        "<a href="#workerdisksize" title="WorkerDiskSize">WorkerDiskSize</a>" : <i>Double</i>,
        "<a href="#workerdisksnapshotpolicyid" title="WorkerDiskSnapshotPolicyId">WorkerDiskSnapshotPolicyId</a>" : <i>String</i>,
        "<a href="#workerinstancechargetype" title="WorkerInstanceChargeType">WorkerInstanceChargeType</a>" : <i>String</i>,
        "<a href="#workerinstancetype" title="WorkerInstanceType">WorkerInstanceType</a>" : <i>String</i>,
        "<a href="#workerinstancetypes" title="WorkerInstanceTypes">WorkerInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#workernumber" title="WorkerNumber">WorkerNumber</a>" : <i>Double</i>,
        "<a href="#workernumbers" title="WorkerNumbers">WorkerNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#workerperiod" title="WorkerPeriod">WorkerPeriod</a>" : <i>Double</i>,
        "<a href="#workerperiodunit" title="WorkerPeriodUnit">WorkerPeriodUnit</a>" : <i>String</i>,
        "<a href="#workervswitchids" title="WorkerVswitchIds">WorkerVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#addons" title="Addons">Addons</a>" : <i>[ <a href="addonsdefinition.md">AddonsDefinition</a>, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfigdefinition.md">LogConfigDefinition</a>, ... ]</i>,
        "<a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>" : <i>[ <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>, ... ]</i>,
        "<a href="#taints" title="Taints">Taints</a>" : <i>[ <a href="taintsdefinition.md">TaintsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#workerdatadisks" title="WorkerDataDisks">WorkerDataDisks</a>" : <i>[ <a href="workerdatadisksdefinition.md">WorkerDataDisksDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CsManagedKubernetes
Properties:
    <a href="#apiaudiences" title="ApiAudiences">ApiAudiences</a>: <i>
      - String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#clientcert" title="ClientCert">ClientCert</a>: <i>String</i>
    <a href="#clientkey" title="ClientKey">ClientKey</a>: <i>String</i>
    <a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>: <i>String</i>
    <a href="#clusterdomain" title="ClusterDomain">ClusterDomain</a>: <i>String</i>
    <a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>: <i>String</i>
    <a href="#clusterspec" title="ClusterSpec">ClusterSpec</a>: <i>String</i>
    <a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>: <i>String</i>
    <a href="#customsan" title="CustomSan">CustomSan</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#enablessh" title="EnableSsh">EnableSsh</a>: <i>Boolean</i>
    <a href="#encryptionproviderkey" title="EncryptionProviderKey">EncryptionProviderKey</a>: <i>String</i>
    <a href="#excludeautoscalernodes" title="ExcludeAutoscalerNodes">ExcludeAutoscalerNodes</a>: <i>Boolean</i>
    <a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Boolean</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>: <i>Boolean</i>
    <a href="#isenterprisesecuritygroup" title="IsEnterpriseSecurityGroup">IsEnterpriseSecurityGroup</a>: <i>Boolean</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a></i>
    <a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>String</i>
    <a href="#loadbalancerspec" title="LoadBalancerSpec">LoadBalancerSpec</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>: <i>Boolean</i>
    <a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>: <i>Double</i>
    <a href="#nodenamemode" title="NodeNameMode">NodeNameMode</a>: <i>String</i>
    <a href="#nodeportrange" title="NodePortRange">NodePortRange</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
    <a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>: <i>
      - String</i>
    <a href="#proxymode" title="ProxyMode">ProxyMode</a>: <i>String</i>
    <a href="#rdsinstances" title="RdsInstances">RdsInstances</a>: <i>
      - String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>
      - <a href="runtimedefinition.md">RuntimeDefinition</a></i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#serviceaccountissuer" title="ServiceAccountIssuer">ServiceAccountIssuer</a>: <i>String</i>
    <a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
    <a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#userca" title="UserCa">UserCa</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vswitchids" title="VswitchIds">VswitchIds</a>: <i>
      - String</i>
    <a href="#workerautorenew" title="WorkerAutoRenew">WorkerAutoRenew</a>: <i>Boolean</i>
    <a href="#workerautorenewperiod" title="WorkerAutoRenewPeriod">WorkerAutoRenewPeriod</a>: <i>Double</i>
    <a href="#workerdatadiskcategory" title="WorkerDataDiskCategory">WorkerDataDiskCategory</a>: <i>String</i>
    <a href="#workerdatadisksize" title="WorkerDataDiskSize">WorkerDataDiskSize</a>: <i>Double</i>
    <a href="#workerdiskcategory" title="WorkerDiskCategory">WorkerDiskCategory</a>: <i>String</i>
    <a href="#workerdiskperformancelevel" title="WorkerDiskPerformanceLevel">WorkerDiskPerformanceLevel</a>: <i>String</i>
    <a href="#workerdisksize" title="WorkerDiskSize">WorkerDiskSize</a>: <i>Double</i>
    <a href="#workerdisksnapshotpolicyid" title="WorkerDiskSnapshotPolicyId">WorkerDiskSnapshotPolicyId</a>: <i>String</i>
    <a href="#workerinstancechargetype" title="WorkerInstanceChargeType">WorkerInstanceChargeType</a>: <i>String</i>
    <a href="#workerinstancetype" title="WorkerInstanceType">WorkerInstanceType</a>: <i>String</i>
    <a href="#workerinstancetypes" title="WorkerInstanceTypes">WorkerInstanceTypes</a>: <i>
      - String</i>
    <a href="#workernumber" title="WorkerNumber">WorkerNumber</a>: <i>Double</i>
    <a href="#workernumbers" title="WorkerNumbers">WorkerNumbers</a>: <i>
      - Double</i>
    <a href="#workerperiod" title="WorkerPeriod">WorkerPeriod</a>: <i>Double</i>
    <a href="#workerperiodunit" title="WorkerPeriodUnit">WorkerPeriodUnit</a>: <i>String</i>
    <a href="#workervswitchids" title="WorkerVswitchIds">WorkerVswitchIds</a>: <i>
      - String</i>
    <a href="#addons" title="Addons">Addons</a>: <i>
      - <a href="addonsdefinition.md">AddonsDefinition</a></i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfigdefinition.md">LogConfigDefinition</a></i>
    <a href="#maintenancewindow" title="MaintenanceWindow">MaintenanceWindow</a>: <i>
      - <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a></i>
    <a href="#taints" title="Taints">Taints</a>: <i>
      - <a href="taintsdefinition.md">TaintsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#workerdatadisks" title="WorkerDataDisks">WorkerDataDisks</a>: <i>
      - <a href="workerdatadisksdefinition.md">WorkerDataDisksDefinition</a></i>
</pre>

## Properties

#### ApiAudiences

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterCaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterNetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterSpec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSan

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsh

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionProviderKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeAutoscalerNodes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceUpdate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallCloudMonitor

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnterpriseSecurityGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionContext

_Required_: No

_Type_: List of <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerSpec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewNatGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeCidrMask

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNameMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePortRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodVswitchIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RdsInstances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: No

_Type_: List of <a href="runtimedefinition.md">RuntimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountIssuer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbInternetEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerAutoRenew

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerAutoRenewPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDataDiskCategory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDataDiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDiskCategory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDiskPerformanceLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDiskSnapshotPolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerInstanceChargeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerInstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerInstanceTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNumbers

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerPeriodUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerVswitchIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addons

_Required_: No

_Type_: List of <a href="addonsdefinition.md">AddonsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfigdefinition.md">LogConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintenanceWindow

_Required_: No

_Type_: List of <a href="maintenancewindowdefinition.md">MaintenanceWindowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Taints

_Required_: No

_Type_: List of <a href="taintsdefinition.md">TaintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerDataDisks

_Required_: No

_Type_: List of <a href="workerdatadisksdefinition.md">WorkerDataDisksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CertificateAuthority

Returns the <code>CertificateAuthority</code> value.

#### Connections

Returns the <code>Connections</code> value.

#### Id

Returns the <code>Id</code> value.

#### NatGatewayId

Returns the <code>NatGatewayId</code> value.

#### SlbId

Returns the <code>SlbId</code> value.

#### SlbInternet

Returns the <code>SlbInternet</code> value.

#### SlbIntranet

Returns the <code>SlbIntranet</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### WorkerNodes

Returns the <code>WorkerNodes</code> value.

#### WorkerRamRoleName

Returns the <code>WorkerRamRoleName</code> value.

