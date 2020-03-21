# Terraform::Alicloud::CsKubernetes

CloudFormation equivalent of alicloud_cs_kubernetes

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CsKubernetes",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#clientcert" title="ClientCert">ClientCert</a>" : <i>String</i>,
        "<a href="#clientkey" title="ClientKey">ClientKey</a>" : <i>String</i>,
        "<a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>" : <i>String</i>,
        "<a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>" : <i>String</i>,
        "<a href="#connections" title="Connections">Connections</a>" : <i>[ &lt;a href=&#34;connections.md&#34;&gt;Connections&lt;/a&gt;, ... ]</i>,
        "<a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>" : <i>String</i>,
        "<a href="#enablessh" title="EnableSsh">EnableSsh</a>" : <i>Boolean</i>,
        "<a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>" : <i>Boolean</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>" : <i>Boolean</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ &lt;a href=&#34;kmsencryptioncontext.md&#34;&gt;KmsEncryptionContext&lt;/a&gt;, ... ]</i>,
        "<a href="#kubeconfig" title="KubeConfig">KubeConfig</a>" : <i>String</i>,
        "<a href="#masterautorenew" title="MasterAutoRenew">MasterAutoRenew</a>" : <i>Boolean</i>,
        "<a href="#masterautorenewperiod" title="MasterAutoRenewPeriod">MasterAutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#masterdiskcategory" title="MasterDiskCategory">MasterDiskCategory</a>" : <i>String</i>,
        "<a href="#masterdisksize" title="MasterDiskSize">MasterDiskSize</a>" : <i>Double</i>,
        "<a href="#masterinstancechargetype" title="MasterInstanceChargeType">MasterInstanceChargeType</a>" : <i>String</i>,
        "<a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>" : <i>String</i>,
        "<a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#masternodes" title="MasterNodes">MasterNodes</a>" : <i>[ &lt;a href=&#34;masternodes.md&#34;&gt;MasterNodes&lt;/a&gt;, ... ]</i>,
        "<a href="#masterperiod" title="MasterPeriod">MasterPeriod</a>" : <i>Double</i>,
        "<a href="#masterperiodunit" title="MasterPeriodUnit">MasterPeriodUnit</a>" : <i>String</i>,
        "<a href="#mastervswitchids" title="MasterVswitchIds">MasterVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>" : <i>String</i>,
        "<a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>" : <i>Boolean</i>,
        "<a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>" : <i>Double</i>,
        "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#podcidr" title="PodCidr">PodCidr</a>" : <i>String</i>,
        "<a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxymode" title="ProxyMode">ProxyMode</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>" : <i>String</i>,
        "<a href="#slbid" title="SlbId">SlbId</a>" : <i>String</i>,
        "<a href="#slbinternet" title="SlbInternet">SlbInternet</a>" : <i>String</i>,
        "<a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>" : <i>Boolean</i>,
        "<a href="#slbintranet" title="SlbIntranet">SlbIntranet</a>" : <i>String</i>,
        "<a href="#userca" title="UserCa">UserCa</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
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
        "<a href="#workernodes" title="WorkerNodes">WorkerNodes</a>" : <i>[ &lt;a href=&#34;workernodes.md&#34;&gt;WorkerNodes&lt;/a&gt;, ... ]</i>,
        "<a href="#workernumber" title="WorkerNumber">WorkerNumber</a>" : <i>Double</i>,
        "<a href="#workernumbers" title="WorkerNumbers">WorkerNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#workerperiod" title="WorkerPeriod">WorkerPeriod</a>" : <i>Double</i>,
        "<a href="#workerperiodunit" title="WorkerPeriodUnit">WorkerPeriodUnit</a>" : <i>String</i>,
        "<a href="#workervswitchids" title="WorkerVswitchIds">WorkerVswitchIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#addons" title="Addons">Addons</a>" : <i>[ &lt;a href=&#34;addons.md&#34;&gt;Addons&lt;/a&gt;, ... ]</i>,
        "<a href="#logconfig" title="LogConfig">LogConfig</a>" : <i>[ &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CsKubernetes
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#clientcert" title="ClientCert">ClientCert</a>: <i>String</i>
    <a href="#clientkey" title="ClientKey">ClientKey</a>: <i>String</i>
    <a href="#clustercacert" title="ClusterCaCert">ClusterCaCert</a>: <i>String</i>
    <a href="#clusternetworktype" title="ClusterNetworkType">ClusterNetworkType</a>: <i>String</i>
    <a href="#connections" title="Connections">Connections</a>: <i>
      - &lt;a href=&#34;connections.md&#34;&gt;Connections&lt;/a&gt;</i>
    <a href="#cpupolicy" title="CpuPolicy">CpuPolicy</a>: <i>String</i>
    <a href="#enablessh" title="EnableSsh">EnableSsh</a>: <i>Boolean</i>
    <a href="#forceupdate" title="ForceUpdate">ForceUpdate</a>: <i>Boolean</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#installcloudmonitor" title="InstallCloudMonitor">InstallCloudMonitor</a>: <i>Boolean</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - &lt;a href=&#34;kmsencryptioncontext.md&#34;&gt;KmsEncryptionContext&lt;/a&gt;</i>
    <a href="#kubeconfig" title="KubeConfig">KubeConfig</a>: <i>String</i>
    <a href="#masterautorenew" title="MasterAutoRenew">MasterAutoRenew</a>: <i>Boolean</i>
    <a href="#masterautorenewperiod" title="MasterAutoRenewPeriod">MasterAutoRenewPeriod</a>: <i>Double</i>
    <a href="#masterdiskcategory" title="MasterDiskCategory">MasterDiskCategory</a>: <i>String</i>
    <a href="#masterdisksize" title="MasterDiskSize">MasterDiskSize</a>: <i>Double</i>
    <a href="#masterinstancechargetype" title="MasterInstanceChargeType">MasterInstanceChargeType</a>: <i>String</i>
    <a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>: <i>String</i>
    <a href="#masterinstancetypes" title="MasterInstanceTypes">MasterInstanceTypes</a>: <i>
      - String</i>
    <a href="#masternodes" title="MasterNodes">MasterNodes</a>: <i>
      - &lt;a href=&#34;masternodes.md&#34;&gt;MasterNodes&lt;/a&gt;</i>
    <a href="#masterperiod" title="MasterPeriod">MasterPeriod</a>: <i>Double</i>
    <a href="#masterperiodunit" title="MasterPeriodUnit">MasterPeriodUnit</a>: <i>String</i>
    <a href="#mastervswitchids" title="MasterVswitchIds">MasterVswitchIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#natgatewayid" title="NatGatewayId">NatGatewayId</a>: <i>String</i>
    <a href="#newnatgateway" title="NewNatGateway">NewNatGateway</a>: <i>Boolean</i>
    <a href="#nodecidrmask" title="NodeCidrMask">NodeCidrMask</a>: <i>Double</i>
    <a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#podcidr" title="PodCidr">PodCidr</a>: <i>String</i>
    <a href="#podvswitchids" title="PodVswitchIds">PodVswitchIds</a>: <i>
      - String</i>
    <a href="#proxymode" title="ProxyMode">ProxyMode</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#servicecidr" title="ServiceCidr">ServiceCidr</a>: <i>String</i>
    <a href="#slbid" title="SlbId">SlbId</a>: <i>String</i>
    <a href="#slbinternet" title="SlbInternet">SlbInternet</a>: <i>String</i>
    <a href="#slbinternetenabled" title="SlbInternetEnabled">SlbInternetEnabled</a>: <i>Boolean</i>
    <a href="#slbintranet" title="SlbIntranet">SlbIntranet</a>: <i>String</i>
    <a href="#userca" title="UserCa">UserCa</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
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
    <a href="#workernodes" title="WorkerNodes">WorkerNodes</a>: <i>
      - &lt;a href=&#34;workernodes.md&#34;&gt;WorkerNodes&lt;/a&gt;</i>
    <a href="#workernumber" title="WorkerNumber">WorkerNumber</a>: <i>Double</i>
    <a href="#workernumbers" title="WorkerNumbers">WorkerNumbers</a>: <i>
      - Double</i>
    <a href="#workerperiod" title="WorkerPeriod">WorkerPeriod</a>: <i>Double</i>
    <a href="#workerperiodunit" title="WorkerPeriodUnit">WorkerPeriodUnit</a>: <i>String</i>
    <a href="#workervswitchids" title="WorkerVswitchIds">WorkerVswitchIds</a>: <i>
      - String</i>
    <a href="#addons" title="Addons">Addons</a>: <i>
      - &lt;a href=&#34;addons.md&#34;&gt;Addons&lt;/a&gt;</i>
    <a href="#logconfig" title="LogConfig">LogConfig</a>: <i>
      - &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

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

#### ClusterNetworkType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connections

_Required_: No

_Type_: List of &lt;a href=&#34;connections.md&#34;&gt;Connections&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;kmsencryptioncontext.md&#34;&gt;KmsEncryptionContext&lt;/a&gt;

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

#### MasterNodes

_Required_: No

_Type_: List of &lt;a href=&#34;masternodes.md&#34;&gt;MasterNodes&lt;/a&gt;

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

#### NatGatewayId

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

#### SecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbInternet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbInternetEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbIntranet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

#### WorkerNodes

_Required_: No

_Type_: List of &lt;a href=&#34;workernodes.md&#34;&gt;WorkerNodes&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;addons.md&#34;&gt;Addons&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogConfig

_Required_: No

_Type_: List of &lt;a href=&#34;logconfig.md&#34;&gt;LogConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

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

Returns the &lt;code&gt;Connections&lt;/code&gt; value.

#### MasterNodes

Returns the &lt;code&gt;MasterNodes&lt;/code&gt; value.

#### NatGatewayId

Returns the &lt;code&gt;NatGatewayId&lt;/code&gt; value.

#### SecurityGroupId

Returns the &lt;code&gt;SecurityGroupId&lt;/code&gt; value.

#### SlbId

Returns the &lt;code&gt;SlbId&lt;/code&gt; value.

#### SlbInternet

Returns the &lt;code&gt;SlbInternet&lt;/code&gt; value.

#### SlbIntranet

Returns the &lt;code&gt;SlbIntranet&lt;/code&gt; value.

#### VpcId

Returns the &lt;code&gt;VpcId&lt;/code&gt; value.

#### WorkerNodes

Returns the &lt;code&gt;WorkerNodes&lt;/code&gt; value.

