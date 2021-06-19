# TF::NetAppCloudManager::CvoGcp

Provides a netapp-cloudmanager_cvo_gcp resource. This can be used to create a new Cloud Volume ONTAP system in GCP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::CvoGcp",
    "Properties" : {
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>" : <i>String</i>,
        "<a href="#firewallrule" title="FirewallRule">FirewallRule</a>" : <i>String</i>,
        "<a href="#gcpencryptionparameters" title="GcpEncryptionParameters">GcpEncryptionParameters</a>" : <i>String</i>,
        "<a href="#gcpserviceaccount" title="GcpServiceAccount">GcpServiceAccount</a>" : <i>String</i>,
        "<a href="#gcpvolumesize" title="GcpVolumeSize">GcpVolumeSize</a>" : <i>Double</i>,
        "<a href="#gcpvolumesizeunit" title="GcpVolumeSizeUnit">GcpVolumeSizeUnit</a>" : <i>String</i>,
        "<a href="#gcpvolumetype" title="GcpVolumeType">GcpVolumeType</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isha" title="IsHa">IsHa</a>" : <i>Boolean</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#mediatorzone" title="MediatorZone">MediatorZone</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkprojectid" title="NetworkProjectId">NetworkProjectId</a>" : <i>String</i>,
        "<a href="#node1zone" title="Node1Zone">Node1Zone</a>" : <i>String</i>,
        "<a href="#node2zone" title="Node2Zone">Node2Zone</a>" : <i>String</i>,
        "<a href="#nssaccount" title="NssAccount">NssAccount</a>" : <i>String</i>,
        "<a href="#ontapversion" title="OntapVersion">OntapVersion</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#subnet0nodeanddataconnectivity" title="Subnet0NodeAndDataConnectivity">Subnet0NodeAndDataConnectivity</a>" : <i>String</i>,
        "<a href="#subnet1clusterconnectivity" title="Subnet1ClusterConnectivity">Subnet1ClusterConnectivity</a>" : <i>String</i>,
        "<a href="#subnet2haconnectivity" title="Subnet2HaConnectivity">Subnet2HaConnectivity</a>" : <i>String</i>,
        "<a href="#subnet3datareplication" title="Subnet3DataReplication">Subnet3DataReplication</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#svmpassword" title="SvmPassword">SvmPassword</a>" : <i>String</i>,
        "<a href="#tierlevel" title="TierLevel">TierLevel</a>" : <i>String</i>,
        "<a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>" : <i>Boolean</i>,
        "<a href="#vpc0firewallrulename" title="Vpc0FirewallRuleName">Vpc0FirewallRuleName</a>" : <i>String</i>,
        "<a href="#vpc0nodeanddataconnectivity" title="Vpc0NodeAndDataConnectivity">Vpc0NodeAndDataConnectivity</a>" : <i>String</i>,
        "<a href="#vpc1clusterconnectivity" title="Vpc1ClusterConnectivity">Vpc1ClusterConnectivity</a>" : <i>String</i>,
        "<a href="#vpc1firewallrulename" title="Vpc1FirewallRuleName">Vpc1FirewallRuleName</a>" : <i>String</i>,
        "<a href="#vpc2firewallrulename" title="Vpc2FirewallRuleName">Vpc2FirewallRuleName</a>" : <i>String</i>,
        "<a href="#vpc2haconnectivity" title="Vpc2HaConnectivity">Vpc2HaConnectivity</a>" : <i>String</i>,
        "<a href="#vpc3datareplication" title="Vpc3DataReplication">Vpc3DataReplication</a>" : <i>String</i>,
        "<a href="#vpc3firewallrulename" title="Vpc3FirewallRuleName">Vpc3FirewallRuleName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>,
        "<a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#gcplabel" title="GcpLabel">GcpLabel</a>" : <i>[ <a href="gcplabeldefinition.md">GcpLabelDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::CvoGcp
Properties:
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>: <i>String</i>
    <a href="#firewallrule" title="FirewallRule">FirewallRule</a>: <i>String</i>
    <a href="#gcpencryptionparameters" title="GcpEncryptionParameters">GcpEncryptionParameters</a>: <i>String</i>
    <a href="#gcpserviceaccount" title="GcpServiceAccount">GcpServiceAccount</a>: <i>String</i>
    <a href="#gcpvolumesize" title="GcpVolumeSize">GcpVolumeSize</a>: <i>Double</i>
    <a href="#gcpvolumesizeunit" title="GcpVolumeSizeUnit">GcpVolumeSizeUnit</a>: <i>String</i>
    <a href="#gcpvolumetype" title="GcpVolumeType">GcpVolumeType</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isha" title="IsHa">IsHa</a>: <i>Boolean</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#mediatorzone" title="MediatorZone">MediatorZone</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkprojectid" title="NetworkProjectId">NetworkProjectId</a>: <i>String</i>
    <a href="#node1zone" title="Node1Zone">Node1Zone</a>: <i>String</i>
    <a href="#node2zone" title="Node2Zone">Node2Zone</a>: <i>String</i>
    <a href="#nssaccount" title="NssAccount">NssAccount</a>: <i>String</i>
    <a href="#ontapversion" title="OntapVersion">OntapVersion</a>: <i>String</i>
    <a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>: <i>String</i>
    <a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#subnet0nodeanddataconnectivity" title="Subnet0NodeAndDataConnectivity">Subnet0NodeAndDataConnectivity</a>: <i>String</i>
    <a href="#subnet1clusterconnectivity" title="Subnet1ClusterConnectivity">Subnet1ClusterConnectivity</a>: <i>String</i>
    <a href="#subnet2haconnectivity" title="Subnet2HaConnectivity">Subnet2HaConnectivity</a>: <i>String</i>
    <a href="#subnet3datareplication" title="Subnet3DataReplication">Subnet3DataReplication</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#svmpassword" title="SvmPassword">SvmPassword</a>: <i>String</i>
    <a href="#tierlevel" title="TierLevel">TierLevel</a>: <i>String</i>
    <a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>: <i>Boolean</i>
    <a href="#vpc0firewallrulename" title="Vpc0FirewallRuleName">Vpc0FirewallRuleName</a>: <i>String</i>
    <a href="#vpc0nodeanddataconnectivity" title="Vpc0NodeAndDataConnectivity">Vpc0NodeAndDataConnectivity</a>: <i>String</i>
    <a href="#vpc1clusterconnectivity" title="Vpc1ClusterConnectivity">Vpc1ClusterConnectivity</a>: <i>String</i>
    <a href="#vpc1firewallrulename" title="Vpc1FirewallRuleName">Vpc1FirewallRuleName</a>: <i>String</i>
    <a href="#vpc2firewallrulename" title="Vpc2FirewallRuleName">Vpc2FirewallRuleName</a>: <i>String</i>
    <a href="#vpc2haconnectivity" title="Vpc2HaConnectivity">Vpc2HaConnectivity</a>: <i>String</i>
    <a href="#vpc3datareplication" title="Vpc3DataReplication">Vpc3DataReplication</a>: <i>String</i>
    <a href="#vpc3firewallrulename" title="Vpc3FirewallRuleName">Vpc3FirewallRuleName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
    <a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#gcplabel" title="GcpLabel">GcpLabel</a>: <i>
      - <a href="gcplabeldefinition.md">GcpLabelDefinition</a></i>
</pre>

## Properties

#### CapacityTier

Indicates the type of data tiering to use: ['cloudStorage', 'NONE']. The default is 'cloudStorage'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataEncryptionType

The type of data encryption to use for the working environment: ['GCP', 'NONE']. The default is 'GCP'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallRule

The name of the firewall rule for Cloud Volumes ONTAP. If not provided, Cloud Manager generates the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpEncryptionParameters

Required if using gcp encryption with custom key. Key format is 'projects/default-project/locations/global/keyRings/test/cryptoKeys/key1'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpServiceAccount

The gcp_service_account email in order to enable tiering of cold data to Google Cloud Storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpVolumeSize

The GCP volume size for the first data aggregate. For GB, the unit can be: [100 or 500]. For TB, the unit can be: [1,2,4,8]. The default is '1' .

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpVolumeSizeUnit

['GB' or 'TB']. The default is 'TB'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpVolumeType

The type of the storage for the first data aggregate: ['pd-standard', 'pd-ssd']. The default is 'pd-ssd'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of instance to use, which depends on the license type you choose: Explore:['custom-4-16384'], Standard:['n1-standard-8'], Premium:['n1-standard-32'], BYOL: all instance types defined for PayGo. For more supported instance types, refer to Cloud Volumes ONTAP Release Notes. default is 'n1-standard-8' .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHa

Indicate whether the working environment is an HA pair or not [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

The type of license to use. For single node: ['gcp-cot-explore-paygo', 'gcp-cot-standard-paygo', 'gcp-cot-premium-paygo', 'gcp-cot-premium-byol'], For HA: ['gcp-ha-cot-explore-paygo', 'gcp-ha-cot-standard-paygo', 'gcp-ha-cot-premium-paygo', 'gcp-ha-cot-premium-byol']. The default is 'gcp-cot-standard-paygo'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediatorZone

Zone for mediator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Volumes ONTAP working environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkProjectId

The project id in GCP associated with the Subnet. If not provided, it’s assumed that the Subnet is within the previously specified project id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node1Zone

Zone for node 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node2Zone

Zone for node 2.

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

#### PlatformSerialNumberNode1

For HA BYOL, the serial number for the first node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformSerialNumberNode2

For HA BYOL, the serial number for the second node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the GCP project.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

The serial number for the system. Required when using 'gcp-cot-premium-byol'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet0NodeAndDataConnectivity

Subnet path for nic1, requered for node and data connectivity. If using shared VPC, netwrok_project_id must be provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet1ClusterConnectivity

Subnet path for nic2, required for cluster connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet2HaConnectivity

Subnet path for nic3, required for HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet3DataReplication

Subnet path for nic4, required for data replication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The name of the subnet for Cloud Volumes ONTAP. The default is: 'default'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmPassword

The admin password for Cloud Volumes ONTAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierLevel

In case capacity_tier is cloudStorage, this argument indicates the tiering level: ['standard', 'nearline', 'coldline']. The default is: 'standard'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLatestVersion

Indicates whether to use the latest available ONTAP version. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc0FirewallRuleName

Firewall rule name for vpc1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc0NodeAndDataConnectivity

VPC path for nic1, required for node and data connectivity. If using shared VPC, netwrok_project_id must be provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc1ClusterConnectivity

VPC path for nic2, required for cluster connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc1FirewallRuleName

Firewall rule name for vpc2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc2FirewallRuleName

Firewall rule name for vpc3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc2HaConnectivity

VPC path for nic3, required for HA connectivity.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc3DataReplication

VPC path for nic4, required for data replication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc3FirewallRuleName

Firewall rule name for vpc4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The name of the VPC.

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

#### Zone

The zone of the region where the working environment will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpLabel

_Required_: No

_Type_: List of <a href="gcplabeldefinition.md">GcpLabelDefinition</a>

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

