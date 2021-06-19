# TF::NetAppCloudManager::ConnectorAzure

Provides a netapp-cloudmanager_connector_azure resource. This can be used to create a new Cloud Manager Connector in AZURE.
The environment needs to be configured with the proper credentials before it can be used (az login).
The minimum required policy can be found at [Connector deployment policy for Azure](https://s3.amazonaws.com/occm-sample-policies/Policy_for_Setup_As_Service_Azure.json)

In order for the Connector to create a Cloud Volumes ONTAP system, it requires a role assignment. This can be done with azurerm provider. The following role is required: [Cloud Manager policy for Azure](https://occm-sample-policies.s3.amazonaws.com/Policy_for_cloud_Manager_Azure_3.8.7.json)


<!---
i think we need to create section for terraform and point to there
-->

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NetAppCloudManager::ConnectorAzure",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
        "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
        "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networksecuritygroupname" title="NetworkSecurityGroupName">NetworkSecurityGroupName</a>" : <i>String</i>,
        "<a href="#networksecurityresourcegroup" title="NetworkSecurityResourceGroup">NetworkSecurityResourceGroup</a>" : <i>String</i>,
        "<a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>" : <i>String</i>,
        "<a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>" : <i>String</i>,
        "<a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>" : <i>String</i>,
        "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>" : <i>String</i>,
        "<a href="#virtualmachinesize" title="VirtualMachineSize">VirtualMachineSize</a>" : <i>String</i>,
        "<a href="#vnetid" title="VnetId">VnetId</a>" : <i>String</i>,
        "<a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NetAppCloudManager::ConnectorAzure
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
    <a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
    <a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networksecuritygroupname" title="NetworkSecurityGroupName">NetworkSecurityGroupName</a>: <i>String</i>
    <a href="#networksecurityresourcegroup" title="NetworkSecurityResourceGroup">NetworkSecurityResourceGroup</a>: <i>String</i>
    <a href="#proxycertificates" title="ProxyCertificates">ProxyCertificates</a>: <i>
      - String</i>
    <a href="#proxypassword" title="ProxyPassword">ProxyPassword</a>: <i>String</i>
    <a href="#proxyurl" title="ProxyUrl">ProxyUrl</a>: <i>String</i>
    <a href="#proxyusername" title="ProxyUserName">ProxyUserName</a>: <i>String</i>
    <a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionId">SubscriptionId</a>: <i>String</i>
    <a href="#virtualmachinesize" title="VirtualMachineSize">VirtualMachineSize</a>: <i>String</i>
    <a href="#vnetid" title="VnetId">VnetId</a>: <i>String</i>
    <a href="#vnetresourcegroup" title="VnetResourceGroup">VnetResourceGroup</a>: <i>String</i>
</pre>

## Properties

#### AccountId

The NetApp account ID that the Connector will be associated with. If not provided, Cloud Manager uses the first account. If no account exists, Cloud Manager creates a new account. You can find the account ID in the account tab of Cloud Manager at [https://cloudmanager.netapp.com](https://cloudmanager.netapp.com).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminPassword

The password for the Connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

The user name for the Connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIpAddress

Indicates whether to associate the public IP address to the virtual machine.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

The name of the company of the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location where the Cloud Manager Connector will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Cloud Manager Connector.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupName

The name of the security group for the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityResourceGroup

The resource group in Azure associated with the security group. If not provided, it’s assumed that the security group is within the previously specified resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyCertificates

The proxy certificates. A list of certificate file names.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPassword

The proxy password, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUrl

The proxy URL, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyUserName

The proxy user name, if using a proxy to connect to the internet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

The resource group in Azure where the resources will be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The name of the subnet for the virtual machine.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscriptionId

The ID of the Azure subscription.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineSize

The virtual machine type. (for example, Standard_D2s_v3). At least 4 CPU and 16 GB of memory are required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetId

The name of the virtual network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetResourceGroup

The resource group in Azure associated with the virtual network. If not provided, it’s assumed that the VNet is within the previously specified resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClientId

Returns the <code>ClientId</code> value.

#### Id

Returns the <code>Id</code> value.

