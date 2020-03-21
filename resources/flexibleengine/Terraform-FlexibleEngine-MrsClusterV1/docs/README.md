# Terraform::FlexibleEngine::MrsClusterV1

CloudFormation equivalent of flexibleengine_mrs_cluster_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::MrsClusterV1",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#availablezoneid" title="AvailableZoneId">AvailableZoneId</a>" : <i>String</i>,
        "<a href="#availablezonename" title="AvailableZoneName">AvailableZoneName</a>" : <i>String</i>,
        "<a href="#billingtype" title="BillingType">BillingType</a>" : <i>Double</i>,
        "<a href="#chargingstarttime" title="ChargingStartTime">ChargingStartTime</a>" : <i>String</i>,
        "<a href="#clusteradminsecret" title="ClusterAdminSecret">ClusterAdminSecret</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#clusterstate" title="ClusterState">ClusterState</a>" : <i>String</i>,
        "<a href="#clustertype" title="ClusterType">ClusterType</a>" : <i>Double</i>,
        "<a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>" : <i>String</i>,
        "<a href="#corenodenum" title="CoreNodeNum">CoreNodeNum</a>" : <i>Double</i>,
        "<a href="#corenodeproductid" title="CoreNodeProductId">CoreNodeProductId</a>" : <i>String</i>,
        "<a href="#corenodesize" title="CoreNodeSize">CoreNodeSize</a>" : <i>String</i>,
        "<a href="#corenodespecid" title="CoreNodeSpecId">CoreNodeSpecId</a>" : <i>String</i>,
        "<a href="#createat" title="CreateAt">CreateAt</a>" : <i>String</i>,
        "<a href="#deploymentid" title="DeploymentId">DeploymentId</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
        "<a href="#errorinfo" title="ErrorInfo">ErrorInfo</a>" : <i>String</i>,
        "<a href="#externalalternateip" title="ExternalAlternateIp">ExternalAlternateIp</a>" : <i>String</i>,
        "<a href="#externalip" title="ExternalIp">ExternalIp</a>" : <i>String</i>,
        "<a href="#fee" title="Fee">Fee</a>" : <i>String</i>,
        "<a href="#hadoopversion" title="HadoopVersion">HadoopVersion</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#internalip" title="InternalIp">InternalIp</a>" : <i>String</i>,
        "<a href="#logcollection" title="LogCollection">LogCollection</a>" : <i>Double</i>,
        "<a href="#masternodeip" title="MasterNodeIp">MasterNodeIp</a>" : <i>String</i>,
        "<a href="#masternodenum" title="MasterNodeNum">MasterNodeNum</a>" : <i>Double</i>,
        "<a href="#masternodeproductid" title="MasterNodeProductId">MasterNodeProductId</a>" : <i>String</i>,
        "<a href="#masternodesize" title="MasterNodeSize">MasterNodeSize</a>" : <i>String</i>,
        "<a href="#masternodespecid" title="MasterNodeSpecId">MasterNodeSpecId</a>" : <i>String</i>,
        "<a href="#nodepubliccertname" title="NodePublicCertName">NodePublicCertName</a>" : <i>String</i>,
        "<a href="#orderid" title="OrderId">OrderId</a>" : <i>String</i>,
        "<a href="#privateipfirst" title="PrivateIpFirst">PrivateIpFirst</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#safemode" title="SafeMode">SafeMode</a>" : <i>Double</i>,
        "<a href="#securitygroupsid" title="SecurityGroupsId">SecurityGroupsId</a>" : <i>String</i>,
        "<a href="#slavesecuritygroupsid" title="SlaveSecurityGroupsId">SlaveSecurityGroupsId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#updateat" title="UpdateAt">UpdateAt</a>" : <i>String</i>,
        "<a href="#vnc" title="Vnc">Vnc</a>" : <i>String</i>,
        "<a href="#volumesize" title="VolumeSize">VolumeSize</a>" : <i>Double</i>,
        "<a href="#volumetype" title="VolumeType">VolumeType</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#addjobs" title="AddJobs">AddJobs</a>" : <i>[ &lt;a href=&#34;addjobs.md&#34;&gt;AddJobs&lt;/a&gt;, ... ]</i>,
        "<a href="#componentlist" title="ComponentList">ComponentList</a>" : <i>[ &lt;a href=&#34;componentlist.md&#34;&gt;ComponentList&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::MrsClusterV1
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#availablezoneid" title="AvailableZoneId">AvailableZoneId</a>: <i>String</i>
    <a href="#availablezonename" title="AvailableZoneName">AvailableZoneName</a>: <i>String</i>
    <a href="#billingtype" title="BillingType">BillingType</a>: <i>Double</i>
    <a href="#chargingstarttime" title="ChargingStartTime">ChargingStartTime</a>: <i>String</i>
    <a href="#clusteradminsecret" title="ClusterAdminSecret">ClusterAdminSecret</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#clusterstate" title="ClusterState">ClusterState</a>: <i>String</i>
    <a href="#clustertype" title="ClusterType">ClusterType</a>: <i>Double</i>
    <a href="#clusterversion" title="ClusterVersion">ClusterVersion</a>: <i>String</i>
    <a href="#corenodenum" title="CoreNodeNum">CoreNodeNum</a>: <i>Double</i>
    <a href="#corenodeproductid" title="CoreNodeProductId">CoreNodeProductId</a>: <i>String</i>
    <a href="#corenodesize" title="CoreNodeSize">CoreNodeSize</a>: <i>String</i>
    <a href="#corenodespecid" title="CoreNodeSpecId">CoreNodeSpecId</a>: <i>String</i>
    <a href="#createat" title="CreateAt">CreateAt</a>: <i>String</i>
    <a href="#deploymentid" title="DeploymentId">DeploymentId</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>String</i>
    <a href="#errorinfo" title="ErrorInfo">ErrorInfo</a>: <i>String</i>
    <a href="#externalalternateip" title="ExternalAlternateIp">ExternalAlternateIp</a>: <i>String</i>
    <a href="#externalip" title="ExternalIp">ExternalIp</a>: <i>String</i>
    <a href="#fee" title="Fee">Fee</a>: <i>String</i>
    <a href="#hadoopversion" title="HadoopVersion">HadoopVersion</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#internalip" title="InternalIp">InternalIp</a>: <i>String</i>
    <a href="#logcollection" title="LogCollection">LogCollection</a>: <i>Double</i>
    <a href="#masternodeip" title="MasterNodeIp">MasterNodeIp</a>: <i>String</i>
    <a href="#masternodenum" title="MasterNodeNum">MasterNodeNum</a>: <i>Double</i>
    <a href="#masternodeproductid" title="MasterNodeProductId">MasterNodeProductId</a>: <i>String</i>
    <a href="#masternodesize" title="MasterNodeSize">MasterNodeSize</a>: <i>String</i>
    <a href="#masternodespecid" title="MasterNodeSpecId">MasterNodeSpecId</a>: <i>String</i>
    <a href="#nodepubliccertname" title="NodePublicCertName">NodePublicCertName</a>: <i>String</i>
    <a href="#orderid" title="OrderId">OrderId</a>: <i>String</i>
    <a href="#privateipfirst" title="PrivateIpFirst">PrivateIpFirst</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#safemode" title="SafeMode">SafeMode</a>: <i>Double</i>
    <a href="#securitygroupsid" title="SecurityGroupsId">SecurityGroupsId</a>: <i>String</i>
    <a href="#slavesecuritygroupsid" title="SlaveSecurityGroupsId">SlaveSecurityGroupsId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#updateat" title="UpdateAt">UpdateAt</a>: <i>String</i>
    <a href="#vnc" title="Vnc">Vnc</a>: <i>String</i>
    <a href="#volumesize" title="VolumeSize">VolumeSize</a>: <i>Double</i>
    <a href="#volumetype" title="VolumeType">VolumeType</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#addjobs" title="AddJobs">AddJobs</a>: <i>
      - &lt;a href=&#34;addjobs.md&#34;&gt;AddJobs&lt;/a&gt;</i>
    <a href="#componentlist" title="ComponentList">ComponentList</a>: <i>
      - &lt;a href=&#34;componentlist.md&#34;&gt;ComponentList&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableZoneName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargingStartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAdminSecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeNum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeProductId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreNodeSpecId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorInfo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalAlternateIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fee

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HadoopVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCollection

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeNum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeProductId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterNodeSpecId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodePublicCertName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpFirst

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeMode

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupsId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaveSecurityGroupsId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateAt

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vnc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddJobs

_Required_: No

_Type_: List of &lt;a href=&#34;addjobs.md&#34;&gt;AddJobs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComponentList

_Required_: No

_Type_: List of &lt;a href=&#34;componentlist.md&#34;&gt;ComponentList&lt;/a&gt;

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

#### AvailableZoneName

Returns the &lt;code&gt;AvailableZoneName&lt;/code&gt; value.

#### ChargingStartTime

Returns the &lt;code&gt;ChargingStartTime&lt;/code&gt; value.

#### ClusterId

Returns the &lt;code&gt;ClusterId&lt;/code&gt; value.

#### ClusterState

Returns the &lt;code&gt;ClusterState&lt;/code&gt; value.

#### CoreNodeProductId

Returns the &lt;code&gt;CoreNodeProductId&lt;/code&gt; value.

#### CoreNodeSpecId

Returns the &lt;code&gt;CoreNodeSpecId&lt;/code&gt; value.

#### CreateAt

Returns the &lt;code&gt;CreateAt&lt;/code&gt; value.

#### DeploymentId

Returns the &lt;code&gt;DeploymentId&lt;/code&gt; value.

#### Duration

Returns the &lt;code&gt;Duration&lt;/code&gt; value.

#### ErrorInfo

Returns the &lt;code&gt;ErrorInfo&lt;/code&gt; value.

#### ExternalAlternateIp

Returns the &lt;code&gt;ExternalAlternateIp&lt;/code&gt; value.

#### ExternalIp

Returns the &lt;code&gt;ExternalIp&lt;/code&gt; value.

#### Fee

Returns the &lt;code&gt;Fee&lt;/code&gt; value.

#### HadoopVersion

Returns the &lt;code&gt;HadoopVersion&lt;/code&gt; value.

#### InstanceId

Returns the &lt;code&gt;InstanceId&lt;/code&gt; value.

#### InternalIp

Returns the &lt;code&gt;InternalIp&lt;/code&gt; value.

#### MasterNodeIp

Returns the &lt;code&gt;MasterNodeIp&lt;/code&gt; value.

#### MasterNodeProductId

Returns the &lt;code&gt;MasterNodeProductId&lt;/code&gt; value.

#### MasterNodeSpecId

Returns the &lt;code&gt;MasterNodeSpecId&lt;/code&gt; value.

#### OrderId

Returns the &lt;code&gt;OrderId&lt;/code&gt; value.

#### PrivateIpFirst

Returns the &lt;code&gt;PrivateIpFirst&lt;/code&gt; value.

#### Remark

Returns the &lt;code&gt;Remark&lt;/code&gt; value.

#### SecurityGroupsId

Returns the &lt;code&gt;SecurityGroupsId&lt;/code&gt; value.

#### SlaveSecurityGroupsId

Returns the &lt;code&gt;SlaveSecurityGroupsId&lt;/code&gt; value.

#### TenantId

Returns the &lt;code&gt;TenantId&lt;/code&gt; value.

#### UpdateAt

Returns the &lt;code&gt;UpdateAt&lt;/code&gt; value.

#### Vnc

Returns the &lt;code&gt;Vnc&lt;/code&gt; value.

