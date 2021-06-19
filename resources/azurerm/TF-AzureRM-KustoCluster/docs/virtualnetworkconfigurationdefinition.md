# TF::AzureRM::KustoCluster VirtualNetworkConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datamanagementpublicipid" title="DataManagementPublicIpId">DataManagementPublicIpId</a>" : <i>String</i>,
    "<a href="#enginepublicipid" title="EnginePublicIpId">EnginePublicIpId</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#datamanagementpublicipid" title="DataManagementPublicIpId">DataManagementPublicIpId</a>: <i>String</i>
<a href="#enginepublicipid" title="EnginePublicIpId">EnginePublicIpId</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### DataManagementPublicIpId

Data management's service public IP address resource id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnginePublicIpId

Engine service's public IP address resource id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The subnet resource id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

