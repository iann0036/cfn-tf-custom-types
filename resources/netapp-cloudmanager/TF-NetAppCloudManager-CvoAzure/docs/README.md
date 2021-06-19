# TF::NetAppCloudManager::CvoAzure

Provides an netapp-cloudmanager_cvo_azure resource. This can be used to create a new Cloud Volume ONTAP on Azure (Single or HA).
Requires existence of a Cloud Manager Connector with a role assigned to create Cloud Volumes ONTAP. 'azurerm' provider can be used to create the role and role assignment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::CvoAzure",
    "Properties" : {
        "<a href="#allowdeployinexistingrg" title="AllowDeployInExistingRg">AllowDeployInExistingRg</a>" : <i>Boolean</i>,
        "<a href="#backupvolumestocbs" title="BackupVolumesToCbs">BackupVolumesToCbs</a>" : <i>Boolean</i>,
        "<a href="#capacitytier" title="CapacityTier">CapacityTier</a>" : <i>String</i>,
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#cloudprovideraccount" title="CloudProviderAccount">CloudProviderAccount</a>" : <i>String</i>,
        "<a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>" : <i>String</i>,
        "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
        "<a href="#disksizeunit" title="DiskSizeUnit">DiskSizeUnit</a>" : <i>String</i>,
        "<a href="#enablecompliance" title="EnableCompliance">EnableCompliance</a>" : <i>Boolean</i>,
        "<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>" : <i>Boolean</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isha" title="IsHa">IsHa</a>" : <i>Boolean</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nssaccount" title="NssAccount">NssAccount</a>" : <i>String</i>,
        "<a href="#ontapversion" title="OntapVersion">OntapVersion</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>" : <i>String</i>,
        "<a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#serialnumber" title="SerialNumber">SerialNumber</a>" : <i>String</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#svmpassword" title="SvmPassword">SvmPassword</a>" : <i>String</i>,
        "<a href="#tierlevel" title="TierLevel">TierLevel</a>" : <i>String</i>,
        "<a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>" : <i>Boolean</i>,
        "<a href="#vnetid" title="VnetId">VnetId</a>" : <i>String</i>,
        "<a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>" : <i>String</i>,
        "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>,
        "<a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>" : <i>String</i>,
        "<a href="#azuretag" title="AzureTag">AzureTag</a>" : <i>[ <a href="azuretagdefinition.md">AzureTagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::CvoAzure
Properties:
    <a href="#allowdeployinexistingrg" title="AllowDeployInExistingRg">AllowDeployInExistingRg</a>: <i>Boolean</i>
    <a href="#backupvolumestocbs" title="BackupVolumesToCbs">BackupVolumesToCbs</a>: <i>Boolean</i>
    <a href="#capacitytier" title="CapacityTier">CapacityTier</a>: <i>String</i>
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#cloudprovideraccount" title="CloudProviderAccount">CloudProviderAccount</a>: <i>String</i>
    <a href="#dataencryptiontype" title="DataEncryptionType">DataEncryptionType</a>: <i>String</i>
    <a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
    <a href="#disksizeunit" title="DiskSizeUnit">DiskSizeUnit</a>: <i>String</i>
    <a href="#enablecompliance" title="EnableCompliance">EnableCompliance</a>: <i>Boolean</i>
    <a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>: <i>Boolean</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isha" title="IsHa">IsHa</a>: <i>Boolean</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nssaccount" title="NssAccount">NssAccount</a>: <i>String</i>
    <a href="#ontapversion" title="OntapVersion">OntapVersion</a>: <i>String</i>
    <a href="#platformserialnumbernode1" title="PlatformSerialNumberNode1">PlatformSerialNumberNode1</a>: <i>String</i>
    <a href="#platformserialnumbernode2" title="PlatformSerialNumberNode2">PlatformSerialNumberNode2</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#serialnumber" title="SerialNumber">SerialNumber</a>: <i>String</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#svmpassword" title="SvmPassword">SvmPassword</a>: <i>String</i>
    <a href="#tierlevel" title="TierLevel">TierLevel</a>: <i>String</i>
    <a href="#uselatestversion" title="UseLatestVersion">UseLatestVersion</a>: <i>Boolean</i>
    <a href="#vnetid" title="VnetId">VnetId</a>: <i>String</i>
    <a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>: <i>String</i>
    <a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
    <a href="#writingspeedstate" title="WritingSpeedState">WritingSpeedState</a>: <i>String</i>
    <a href="#azuretag" title="AzureTag">AzureTag</a>: <i>
      - <a href="azuretagdefinition.md">AzureTagDefinition</a></i>
</pre>

## Properties

#### AllowDeployInExistingRg

Indicates if to allow creation in existing resource group, Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupVolumesToCbs

Automatically enable back up of all volumes to Azure Blob [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityTier

Whether to enable data tiering for the first data aggregate: ['Blob', 'NONE']. The default is 'BLOB'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

The CIDR of the VNET.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The client ID of the Cloud Manager Connector. You can find the ID from a previous create Connector action as shown in the example, or from the Connector tab on [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudProviderAccount

The cloud provider credentials id to use when deploying the Cloud Volumes ONTAP system. You can find the ID in Cloud Manager from the Settings > Credentials page. If not specified, Cloud Manager uses the managed service identity of the Connector virtual machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataEncryptionType

The type of encryption to use for the working environment: ['AZURE', 'NONE']. The default is 'AZURE'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSize

Azure volume size for the first data aggregate. For GB, the unit can be: [100 or 500]. For TB, the unit can be: [1,2,4,8,16]. The default is '1' .

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeUnit

['GB' or 'TB']. The default is 'TB'.

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

#### InstanceType

The type of instance to use, which depends on the license type you chose: Explore:['Standard_DS3_v2'], Standard:['Standard_DS4_v2,Standard_DS13_v2,Standard_L8s_v2'], Premium:['Standard_DS5_v2','Standard_DS14_v2'], BYOL: all instance types defined for PayGo. For more supported instance types, refer to Cloud Volumes ONTAP Release Notes. The default is 'Standard_DS4_v2' .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHa

Indicate whether the working environment is an HA pair or not [true, false]. The default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

The type of license to be use. For single node: ['azure-cot-explore-paygo', 'azure-cot-standard-paygo', 'azure-cot-premium-paygo', 'azure-cot-premium-byol']. For HA: ['azure-ha-cot-standard-paygo', 'azure-ha-cot-premium-paygo', 'azure-ha-cot-premium-byol']. The default is 'azure-cot-standard-paygo'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the working environment will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Volumes ONTAP working environment.

_Required_: Yes

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

#### ResourceGroup

The resource_group where Cloud Volumes ONTAP will be created. If not provided, Cloud Manager creates the resource group (name of the working environment with suffix '-rg').

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The name of the security group (full identifier: /subscriptions/xxxxxx/resourceGroups/rg_westus/providers/Microsoft.Network/networkSecurityGroups/CVO-SG). If not provided, Cloud Manager creates the security group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialNumber

The serial number for the cluster. Required when using one of these: ['azure-cot-premium-byol' or 'azure-ha-cot-premium-byol'].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

The type of storage for the first data aggregate: ['Premium_LRS', 'Standard_LRS', 'StandardSSD_LRS']. The default is 'Premium_LRS'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The name of the subnet for the Cloud Volumes ONTAP system.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

The ID of the Azure subscription.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmPassword

The admin password for Cloud Volumes ONTAP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TierLevel

If capacity_tier is Blob, this argument indicates the tiering level: ['normal', 'cool']. The default is: 'normal'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLatestVersion

Indicates whether to use the latest available ONTAP version. The default is 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetId

The name of the virtual network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetResourceGroup

The resource group in Azure associated to the virtual network.

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

#### AzureTag

_Required_: No

_Type_: List of <a href="azuretagdefinition.md">AzureTagDefinition</a>

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

