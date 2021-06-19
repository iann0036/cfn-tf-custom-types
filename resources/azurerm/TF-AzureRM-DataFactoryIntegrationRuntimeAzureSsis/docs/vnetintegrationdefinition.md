# TF::AzureRM::DataFactoryIntegrationRuntimeAzureSsis VnetIntegrationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
    "<a href="#vnetid" title="VnetId">VnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
<a href="#vnetid" title="VnetId">VnetId</a>: <i>String</i>
</pre>

## Properties

#### SubnetName

Name of the subnet to which the nodes of the Azure-SSIS Integration Runtime will be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetId

ID of the virtual network to which the nodes of the Azure-SSIS Integration Runtime will be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

