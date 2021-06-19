# TF::AzureRM::DatabricksWorkspace CustomParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>" : <i>Boolean</i>,
    "<a href="#privatesubnetname" title="PrivateSubnetName">PrivateSubnetName</a>" : <i>String</i>,
    "<a href="#publicsubnetname" title="PublicSubnetName">PublicSubnetName</a>" : <i>String</i>,
    "<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#nopublicip" title="NoPublicIp">NoPublicIp</a>: <i>Boolean</i>
<a href="#privatesubnetname" title="PrivateSubnetName">PrivateSubnetName</a>: <i>String</i>
<a href="#publicsubnetname" title="PublicSubnetName">PublicSubnetName</a>: <i>String</i>
<a href="#virtualnetworkid" title="VirtualNetworkId">VirtualNetworkId</a>: <i>String</i>
</pre>

## Properties

#### NoPublicIp

Are public IP Addresses not allowed?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateSubnetName

The name of the Private Subnet within the Virtual Network. Required if `virtual_network_id` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicSubnetName

The name of the Public Subnet within the Virtual Network. Required if `virtual_network_id` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkId

The ID of a Virtual Network where this Databricks Cluster should be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

