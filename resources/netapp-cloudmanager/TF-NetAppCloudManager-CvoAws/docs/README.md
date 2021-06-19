# TF::NetAppCloudManager::CvoAws

Provides an netapp-cloudmanager_cvo_aws resource. This can be used to create a new Cloud Volume ONTAP system in AWS (single node or an HA pair).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::CvoAws",
    "Properties" : {
        "<a href="#backupvolumestocbs" title="BackupVolumesToCbs">BackupVolumesToCbs</a>" : <i>Boolean</i>,
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#cloudprovideraccount" title="CloudProviderAccount">CloudProviderAccount</a>" : <i>String</i>,
        "<a href="#clusterfloatingip" title="ClusterFloatingIp">ClusterFloatingIp</a>" : <i>String</i>,
        "<a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>" : <i>String</i>,
        "<a href="#datafloatingip" title="DataFloatingIp">DataFloatingIp</a>" : <i>String</i>,
        "<a href="#datafloatingip2" title="DataFloatingIp2">DataFloatingIp2</a>" : <i>String</i>,
        "<a href="#ebsvolumesize" title="EbsVolumeSize">EbsVolumeSize</a>" : <i>Double</i>,
        "<a href="#ebsvolumesizeunit" title="EbsVolumeSizeUnit">EbsVolumeSizeUnit</a>" : <i>String</i>,
        "<a href="#ebsvolumetype" title="EbsVolumeType">EbsVolumeType</a>" : <i>String</i>,
        "<a href="#enablecompliance" title="EnableCompliance">EnableCompliance</a>" : <i>Boolean</i>,
        "<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>" : <i>Boolean</i>,
        "<a href="#failovermode" title="FailoverMode">FailoverMode</a>" : <i>String</i>,
        "<a href="#instanceprofilename" title="InstanceProfileName">InstanceProfileName</a>" : <i>String</i>,
        "<a href="#instancetenancy" title="InstanceTenancy">InstanceTenancy</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
        "<a href="#isha" title="IsHa">IsHa</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#mediatorassignpublicip" title="MediatorAssignPublicIp">MediatorAssignPublicIp</a>" : <i>Boolean</i>,
        "<a href="#mediatorkeypairname" title="MediatorKeyPairName">MediatorKeyPairName</a>" : <i>String</i>,
        "<a href="#mediatorsubnetid" title="MediatorSubnetId">MediatorSubnetId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#node1subnetid" title="Node1SubnetId">Node1SubnetId</a>" : <i>String</i>,
        "<a href="#node2subnetid" title="Node2SubnetId">Node2SubnetId</a>" : <i>String</i>,
        "<a href="#nssaccount" title="NssAccount">NssAccount</a>" : <i>String</i>,
        "<a href="#ontapversion" title="OntapVersion">OntapVersion</a>" : <i>String</i>,
        "<a href="#optimizednetworkutilization" title="OptimizedNetworkUtilization">OptimizedNetworkUtilization</a>" : <i>Boolean</i>,
        "<a href="#platformserialnumber" title="PlatformSerialNumber">PlatformSerialNumber</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#routetableids" title="RouteTableIds">RouteTableIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#svmfloatingip" title="SvmFloatingIp">SvmFloatingIp</a>" : <i>String</i>,
        "<a href="#svmpassword" title="SvmPassword">SvmPassword</a>" : <i>String</i>,
        "<a href="#throughput" title="Throughput">Throughput</a>" : <i>Double</i>,
        "<a href="#tierlevel" title="TierLevel">TierLevel</a>" : <i>String</i>,
        "<a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>" : <i>Boolean</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>,
        "<a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>" : <i>String</i>,
        "<a href="#awstag" title="AwsTag">AwsTag</a>" : <i>[ <a href="awstagdefinition.md">AwsTagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::CvoAws
Properties:
    <a href="#backupvolumestocbs" title="BackupVolumesToCbs">BackupVolumesToCbs</a>: <i>Boolean</i>
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#cloudprovideraccount" title="CloudProviderAccount">CloudProviderAccount</a>: <i>String</i>
    <a href="#clusterfloatingip" title="ClusterFloatingIp">ClusterFloatingIp</a>: <i>String</i>
    <a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>: <i>String</i>
    <a href="#datafloatingip" title="DataFloatingIp">DataFloatingIp</a>: <i>String</i>
    <a href="#datafloatingip2" title="DataFloatingIp2">DataFloatingIp2</a>: <i>String</i>
    <a href="#ebsvolumesize" title="EbsVolumeSize">EbsVolumeSize</a>: <i>Double</i>
    <a href="#ebsvolumesizeunit" title="EbsVolumeSizeUnit">EbsVolumeSizeUnit</a>: <i>String</i>
    <a href="#ebsvolumetype" title="EbsVolumeType">EbsVolumeType</a>: <i>String</i>
    <a href="#enablecompliance" title="EnableCompliance">EnableCompliance</a>: <i>Boolean</i>
    <a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>: <i>Boolean</i>
    <a href="#failovermode" title="FailoverMode">FailoverMode</a>: <i>String</i>
    <a href="#instanceprofilename" title="InstanceProfileName">InstanceProfileName</a>: <i>String</i>
    <a href="#instancetenancy" title="InstanceTenancy">InstanceTenancy</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#iops" title="Iops">Iops</a>: <i>Double</i>
    <a href="#isha" title="IsHa">IsHa</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#mediatorassignpublicip" title="MediatorAssignPublicIp">MediatorAssignPublicIp</a>: <i>Boolean</i>
    <a href="#mediatorkeypairname" title="MediatorKeyPairName">MediatorKeyPairName</a>: <i>String</i>
    <a href="#mediatorsubnetid" title="MediatorSubnetId">MediatorSubnetId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#node1subnetid" title="Node1SubnetId">Node1SubnetId</a>: <i>String</i>
    <a href="#node2subnetid" title="Node2SubnetId">Node2SubnetId</a>: <i>String</i>
    <a href="#nssaccount" title="NssAccount">NssAccount</a>: <i>String</i>
    <a href="#ontapversion" title="OntapVersion">OntapVersion</a>: <i>String</i>
    <a href="#optimizednetworkutilization" title="OptimizedNetworkUtilization">OptimizedNetworkUtilization</a>: <i>Boolean</i>
    <a href="#platformserialnumber" title="PlatformSerialNumber">PlatformSerialNumber</a>: <i>String</i>
    <a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>: <i>String</i>
    <a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#routetableids" title="RouteTableIds">RouteTableIds</a>: <i>
      - String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#svmfloatingip" title="SvmFloatingIp">SvmFloatingIp</a>: <i>String</i>
    <a href="#svmpassword" title="SvmPassword">SvmPassword</a>: <i>String</i>
    <a href="#throughput" title="Throughput">Throughput</a>: <i>Double</i>
    <a href="#tierlevel" title="TierLevel">TierLevel</a>: <i>String</i>
    <a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>: <i>Boolean</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
    <a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>: <i>String</i>
    <a href="#awstag" title="AwsTag">AwsTag</a>: <i>
      - <a href="awstagdefinition.md">AwsTagDefinition</a></i>
</pre>

## Properties

#### BackupVolumesToCbs

Automatically enable back up of all volumes to S3 [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityTier

Whether to enable data tiering for the first data aggregate: ['S3','NONE']. The default is 'S3'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderAccount

The cloud provider credentials id to use when deploying the Cloud Volumes ONTAP system. You can find the ID in Cloud Manager from the Settings > Credentials page. If not specified, Cloud Manager uses the instance profile of the Connector.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterFloatingIp

For HA FloatingIP, the cluster management floating IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataEncryptionType

The type of encryption to use for the working environment: ['AWS', 'NONE']. The default is 'AWS'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFloatingIp

For HA FloatingIP, the data floating IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFloatingIp2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsVolumeSize

EBS volume size for the first data aggregate. For GB, the unit can be: [100 or 500]. For TB, the unit can be: [1,2,4,8,16]. The default is '1' .

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsVolumeSizeUnit

['GB' or 'TB']. The default is 'TB'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsVolumeType

The EBS volume type for the first data aggregate ['gp3', 'gp2','io1','st1','sc1']. The default is 'gp2'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCompliance

Enable the Cloud Compliance service on the working environment [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitoring

Enable the Monitoring service on the working environment [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverMode

For HA, the failover mode for the HA pair: ['PrivateIP', 'FloatingIP']. 'PrivateIP' is for a single availability zone and 'FloatingIP' is for multiple availability zones.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProfileName

The instance profile name for the working environment. If not provided, Cloud Manager creates the instance profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTenancy

The EC2 instance tenancy: ['default','dedicated']. The default is 'default'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The instance type to use, which depends on the license type: Explore:['m5.xlarge'], Standard:['m5.2xlarge','r5.xlarge'], Premium:['m5.4xlarge','r5.2xlarge','c4.8xlarge'], BYOL: all instance types defined for PayGo. For more supported instance types, refer to Cloud Volumes ONTAP Release Notes. The default is 'm5.2xlarge'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

Provisioned IOPS. Required only when 'ebs_volume_type' is 'io1' or 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHa

Indicate whether the working environment is an HA pair or not [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

The type of license to use. For single node: ['cot-explore-paygo','cot-standard-paygo', 'cot-premium-paygo', 'cot-premium-byol']. For HA: ['ha-cot-explore-paygo','ha-cot-standard-paygo','ha-cot-premium-paygo','ha-cot-premium-byol']. The default is 'cot-standard-paygo'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediatorAssignPublicIp

bool option to assign public IP. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediatorKeyPairName

For HA, the key pair name for the mediator instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediatorSubnetId

For HA, the subnet ID of the mediator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Volumes ONTAP working environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node1SubnetId

For HA, the subnet ID of the first node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node2SubnetId

For HA, the subnet ID of the second node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssAccount

The NetApp Support Site account ID to use with this Cloud Volumes ONTAP system. If the license type is BYOL and an NSS account isn't provided, Cloud Manager tries to use the first existing NSS account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OntapVersion

The required ONTAP version. Ignored if 'use_latest_version' is set to true. The default is to use the latest version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptimizedNetworkUtilization

Use optimized network utilization [true, false]. The default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformSerialNumber

The serial number for the cluster. This is required when 'license_type' is set 'cot-premium-byol'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformSerialNumberNode1

For HA BYOL, the serial number for the first node. This is required when using 'ha-cot-premium-byol'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformSerialNumberNode2

For HA BYOL, the serial number for the second node. This is required when using 'ha-cot-premium-byol'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region where the working environment will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableIds

For HA FloatingIP, the list of route table IDs that will be updated with the floating IPs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The ID of the security group for the working environment. If not provided, Cloud Manager creates the security group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The subnet id where the working environment will be created. Required when single mode only.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmFloatingIp

For HA FloatingIP, the SVM management floating IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmPassword

The admin password for Cloud Volumes ONTAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throughput

Required only when 'ebs_volume_type' is 'gp3'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierLevel

The tiering level when 'capacity_tier' is set to 'S3' ['normal','ia','ia-single','intelligent']. The default is 'normal'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLatestVersion

Indicates whether to use the latest available ONTAP version. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID where the working environment will be created. If this argument isn't provided, the VPC will be calculated by using the provided subnet ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

The ID of the Cloud Manager workspace where you want to deploy Cloud Volumes ONTAP. If not provided, Cloud Manager uses the first workspace. You can find the ID from the Workspace tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WritingSpeedState

The write speed setting for Cloud Volumes ONTAP: ['NORMAL','HIGH']. The default is 'NORMAL'. This argument is not relevant for HA pairs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsTag

_Required_: No

_Type_: List of <a href="awstagdefinition.md">AwsTagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

