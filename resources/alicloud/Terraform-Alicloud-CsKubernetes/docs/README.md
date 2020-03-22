# Terraform::Alicloud::CsKubernetes

This resource will help you to manage a Kubernetes Cluster in Alibaba Cloud Kubernetes Service. 

-> **NOTE:** Kubernetes cluster only supports VPC network and it can access internet while creating kubernetes cluster.
A Nat Gateway and configuring a SNAT for it can ensure one VPC network access internet. If there is no nat gateway in the
VPC, you can set `new_nat_gateway` to "true" to create one automatically.

-> **NOTE:** Each kubernetes cluster contains 3 master nodes and those number cannot be changed at now.

-> **NOTE:** Creating kubernetes cluster need to install several packages and it will cost about 15 minutes. Please be patient.

-> **NOTE:** From version 1.9.4, the provider supports to download kube config, client certificate, client key and cluster ca certificate
after creating cluster successfully, and you can put them into the specified location, like '~/.kube/config'.

-> **NOTE:** From version 1.16.0, the provider supports Multiple Availability Zones Kubernetes Cluster. To create a cluster of this kind, you must specify 3 or 5 items in `master_vswitch_ids` and `master_instance_types`.

-> **NOTE:** From version 1.20.0, the provider supports disabling internet load balancer for API Server by setting `false` to `slb_internet_enabled`.

-> **NOTE:** If you want to manage Kubernetes, you can use [Kubernetes Provider](https://www.terraform.io/docs/providers/kubernetes/index.html).

-> **NOTE:** You need to activate several other products and confirm Authorization Policy used by Container Service before using this resource.
Please refer to the `Authorization management` and `Cluster management` sections in the [Document Center](https://www.alibabacloud.com/help/doc-detail/86488.htm).

-> **NOTE:** From version 1.75.0, Some parameters have been removed from resource,You can check them below and re-import the cluster if necessary.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CsKubernetes",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#clientcert" title="ClientCert">ClientCert</a>" : <i>String</i>,
        "<a href="#clientkey" title="ClientKey">ClientKey</a>" : <i>String</i>,
        "<a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>" : <i>String</i>,
        "<a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>" : <i>String</i>,
        "<a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>" : <i>String</i>,
        "<a href="#enablessh" title="EnableSsh">EnableSsh</a>" : <i>Boolean</i>,
        "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Boolean</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>" : <i>Boolean</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ <a href="kmsencryptioncontext.md">KmsEncryptionContext</a>, ... ]</i>,
        "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>String</i>,
        "<a href="#masterautorenew" title="MasterAutoRenew">MasterAutoRenew</a>" : <i>Boolean</i>,
        "<a href="#masterautorenewperiod" title="MasterAutoRenewPeriod">MasterAutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#masterdiskcategory" title="MasterDiskCategory">MasterDiskCategory</a>" : <i>String</i>,
        "<a href="#masterdisksize" title="MasterDiskSize">MasterDiskSize</a>" : <i>Double</i>,
        "<a href="#masterinstancechargetype" title="MasterInstanceChargeType">MasterInstanceChargeType</a>" : <i>String</i>,
        "<a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>" : <i>String</i>,
        "<a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#masterperiod" title="MasterPeriod">MasterPeriod</a>" : <i>Double</i>,
        "<a href="#masterperiodunit" title="MasterPeriodUnit">MasterPeriodUnit</a>" : <i>String</i>,
        "<a href="#mastervswitchids" title="MasterVswitchIds">MasterVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>" : <i>Boolean</i>,
        "<a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>" : <i>Double</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
        "<a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxymode" title="ProxyMode">ProxyMode</a>" : <i>String</i>,
        "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
        "<a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>" : <i>Boolean</i>,
        "<a href="#userca" title="UserCa">UserCa</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#vswitchids" title="VswitchIds">VswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#workerautorenew" title="WorkerAutoRenew">WorkerAutoRenew</a>" : <i>Boolean</i>,
        "<a href="#workerautorenewperiod" title="WorkerAutoRenewPeriod">WorkerAutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#workerdatadiskcategory" title="WorkerDataDiskCategory">WorkerDataDiskCategory</a>" : <i>String</i>,
        "<a href="#workerdatadisksize" title="WorkerDataDiskSize">WorkerDataDiskSize</a>" : <i>Double</i>,
        "<a href="#workerdiskcategory" title="WorkerDiskCategory">WorkerDiskCategory</a>" : <i>String</i>,
        "<a href="#workerdisksize" title="WorkerDiskSize">WorkerDiskSize</a>" : <i>Double</i>,
        "<a href="#workerinstancechargetype" title="WorkerInstanceChargeType">WorkerInstanceChargeType</a>" : <i>String</i>,
        "<a href="#workerinstancetype" title="WorkerInstanceType">WorkerInstanceType</a>" : <i>String</i>,
        "<a href="#workerinstancetypes" title="WorkerInstanceTypes">WorkerInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#workernumber" title="WorkerNumber">WorkerNumber</a>" : <i>Double</i>,
        "<a href="#workernumbers" title="WorkerNumbers">WorkerNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#workerperiod" title="WorkerPeriod">WorkerPeriod</a>" : <i>Double</i>,
        "<a href="#workerperiodunit" title="WorkerPeriodUnit">WorkerPeriodUnit</a>" : <i>String</i>,
        "<a href="#workervswitchids" title="WorkerVswitchIds">WorkerVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#addons" title="Addons">Addons</a>" : <i>[ <a href="addons.md">Addons</a>, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ <a href="logconfig.md">LogConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CsKubernetes
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#clientcert" title="ClientCert">ClientCert</a>: <i>String</i>
    <a href="#clientkey" title="ClientKey">ClientKey</a>: <i>String</i>
    <a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>: <i>String</i>
    <a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>: <i>String</i>
    <a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>: <i>String</i>
    <a href="#enablessh" title="EnableSsh">EnableSsh</a>: <i>Boolean</i>
    <a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Boolean</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>: <i>Boolean</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - <a href="kmsencryptioncontext.md">KmsEncryptionContext</a></i>
    <a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>String</i>
    <a href="#masterautorenew" title="MasterAutoRenew">MasterAutoRenew</a>: <i>Boolean</i>
    <a href="#masterautorenewperiod" title="MasterAutoRenewPeriod">MasterAutoRenewPeriod</a>: <i>Double</i>
    <a href="#masterdiskcategory" title="MasterDiskCategory">MasterDiskCategory</a>: <i>String</i>
    <a href="#masterdisksize" title="MasterDiskSize">MasterDiskSize</a>: <i>Double</i>
    <a href="#masterinstancechargetype" title="MasterInstanceChargeType">MasterInstanceChargeType</a>: <i>String</i>
    <a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>: <i>String</i>
    <a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>: <i>
      - String</i>
    <a href="#masterperiod" title="MasterPeriod">MasterPeriod</a>: <i>Double</i>
    <a href="#masterperiodunit" title="MasterPeriodUnit">MasterPeriodUnit</a>: <i>String</i>
    <a href="#mastervswitchids" title="MasterVswitchIds">MasterVswitchIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>: <i>Boolean</i>
    <a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>: <i>Double</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
    <a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>: <i>
      - String</i>
    <a href="#proxymode" title="ProxyMode">ProxyMode</a>: <i>String</i>
    <a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
    <a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>: <i>Boolean</i>
    <a href="#userca" title="UserCa">UserCa</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#vswitchids" title="VswitchIds">VswitchIds</a>: <i>
      - String</i>
    <a href="#workerautorenew" title="WorkerAutoRenew">WorkerAutoRenew</a>: <i>Boolean</i>
    <a href="#workerautorenewperiod" title="WorkerAutoRenewPeriod">WorkerAutoRenewPeriod</a>: <i>Double</i>
    <a href="#workerdatadiskcategory" title="WorkerDataDiskCategory">WorkerDataDiskCategory</a>: <i>String</i>
    <a href="#workerdatadisksize" title="WorkerDataDiskSize">WorkerDataDiskSize</a>: <i>Double</i>
    <a href="#workerdiskcategory" title="WorkerDiskCategory">WorkerDiskCategory</a>: <i>String</i>
    <a href="#workerdisksize" title="WorkerDiskSize">WorkerDiskSize</a>: <i>Double</i>
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
      - <a href="addons.md">Addons</a></i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - <a href="logconfig.md">LogConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

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

#### ClusterNetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsh

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

_Type_: List of <a href="kmsencryptioncontext.md">KmsEncryptionContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAutoRenew

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterAutoRenewPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterDiskCategory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterDiskSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceChargeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceTypes

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterPeriodUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterVswitchIds

_Required_: Yes

_Type_: List of String

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

#### Nodes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

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

#### ServiceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbInternetEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

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

#### WorkerDiskSize

_Required_: No

_Type_: Double

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

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkerNumber

_Required_: Yes

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

_Type_: List of <a href="addons.md">Addons</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of <a href="logconfig.md">LogConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Connections

Returns the <code>Connections</code> value.

#### Id

Returns the <code>Id</code> value.

#### MasterNodes

Returns the <code>MasterNodes</code> value.

#### NatGatewayId

Returns the <code>NatGatewayId</code> value.

#### SecurityGroupId

Returns the <code>SecurityGroupId</code> value.

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

