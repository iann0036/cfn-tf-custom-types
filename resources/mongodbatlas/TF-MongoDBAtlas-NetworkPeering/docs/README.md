# TF::MongoDBAtlas::NetworkPeering

`mongodbatlas_network_peering` provides a Network Peering Connection resource. The resource lets you create, edit and delete network peering connections. The resource requires your Project ID.  

Ensure you have first created a network container if it is required for your configuration.  See the network_container resource documentation to determine if you need a network container first.  Examples for creating both container and peering resource are shown below as well as examples for creating the peering connection only.

~> **GCP AND AZURE ONLY:** Connect via Peering Only mode is deprecated, so no longer needed.  See [disable Peering Only mode](https://docs.atlas.mongodb.com/reference/faq/connection-changes/#disable-peering-mode) for details and [private_ip_mode](https://www.terraform.io/docs/providers/mongodbatlas/r/private_ip_mode.html) to disable.

~> **AZURE ONLY:** To create the peering request with an Azure VNET, you must grant Atlas the following permissions on the virtual network.
    Microsoft.N...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::NetworkPeering",
    "Properties" : {
        "<a href="#accepterregionname" title="AccepterRegionName">AccepterRegionName</a>" : <i>String</i>,
        "<a href="#atlascidrblock" title="AtlasCidrBlock">AtlasCidrBlock</a>" : <i>String</i>,
        "<a href="#atlasgcpprojectid" title="AtlasGcpProjectId">AtlasGcpProjectId</a>" : <i>String</i>,
        "<a href="#atlasvpcname" title="AtlasVpcName">AtlasVpcName</a>" : <i>String</i>,
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#azuredirectoryid" title="AzureDirectoryId">AzureDirectoryId</a>" : <i>String</i>,
        "<a href="#azuresubscriptionid" title="AzureSubscriptionId">AzureSubscriptionId</a>" : <i>String</i>,
        "<a href="#containerid" title="ContainerId">ContainerId</a>" : <i>String</i>,
        "<a href="#gcpprojectid" title="GcpProjectId">GcpProjectId</a>" : <i>String</i>,
        "<a href="#networkname" title="NetworkName">NetworkName</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#providername" title="ProviderName">ProviderName</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#routetablecidrblock" title="RouteTableCidrBlock">RouteTableCidrBlock</a>" : <i>String</i>,
        "<a href="#vnetname" title="VnetName">VnetName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::NetworkPeering
Properties:
    <a href="#accepterregionname" title="AccepterRegionName">AccepterRegionName</a>: <i>String</i>
    <a href="#atlascidrblock" title="AtlasCidrBlock">AtlasCidrBlock</a>: <i>String</i>
    <a href="#atlasgcpprojectid" title="AtlasGcpProjectId">AtlasGcpProjectId</a>: <i>String</i>
    <a href="#atlasvpcname" title="AtlasVpcName">AtlasVpcName</a>: <i>String</i>
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#azuredirectoryid" title="AzureDirectoryId">AzureDirectoryId</a>: <i>String</i>
    <a href="#azuresubscriptionid" title="AzureSubscriptionId">AzureSubscriptionId</a>: <i>String</i>
    <a href="#containerid" title="ContainerId">ContainerId</a>: <i>String</i>
    <a href="#gcpprojectid" title="GcpProjectId">GcpProjectId</a>: <i>String</i>
    <a href="#networkname" title="NetworkName">NetworkName</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#providername" title="ProviderName">ProviderName</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#routetablecidrblock" title="RouteTableCidrBlock">RouteTableCidrBlock</a>: <i>String</i>
    <a href="#vnetname" title="VnetName">VnetName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AccepterRegionName

Specifies the AWS region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtlasCidrBlock

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtlasGcpProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AtlasVpcName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccountId

AWS Account ID of the owner of the peer VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureDirectoryId

Unique identifier for an Azure AD directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureSubscriptionId

Unique identifier of the Azure subscription in which the VNet resides.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerId

Unique identifier of the MongoDB Atlas container for the provider (GCP) or provider/region (AWS, AZURE). You can create an MongoDB Atlas container using the network_container resource or it can be obtained from the cluster returned values if a cluster has been created before the first container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProjectId

GCP project ID of the owner of the network peer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkName

Name of the network peer to which Atlas connects.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the MongoDB Atlas project to create the database user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderName

Cloud provider to whom the peering connection is being made. (Possible Values `AWS`, `AZURE`, `GCP`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

Name of your Azure resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableCidrBlock

AWS VPC CIDR block or subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetName

Name of your Azure VNet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Unique identifier of the AWS peer VPC (Note: this is **not** the same as the Atlas AWS VPC that is returned by the network_container resource).

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

#### AtlasId

Returns the <code>AtlasId</code> value.

#### ConnectionId

Returns the <code>ConnectionId</code> value.

#### ErrorMessage

Returns the <code>ErrorMessage</code> value.

#### ErrorState

Returns the <code>ErrorState</code> value.

#### ErrorStateName

Returns the <code>ErrorStateName</code> value.

#### Id

Returns the <code>Id</code> value.

#### PeerId

Returns the <code>PeerId</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusName

Returns the <code>StatusName</code> value.

