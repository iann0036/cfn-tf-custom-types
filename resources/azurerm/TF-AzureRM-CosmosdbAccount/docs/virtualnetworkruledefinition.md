# TF::AzureRM::CosmosdbAccount VirtualNetworkRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#ignoremissingvnetserviceendpoint" title="IgnoreMissingVnetServiceEndpoint">IgnoreMissingVnetServiceEndpoint</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#ignoremissingvnetserviceendpoint" title="IgnoreMissingVnetServiceEndpoint">IgnoreMissingVnetServiceEndpoint</a>: <i>Boolean</i>
</pre>

## Properties

#### Id

The ID of the virtual network subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreMissingVnetServiceEndpoint

If set to true, the specified subnet will be added as a virtual network rule even if its CosmosDB service endpoint is not active. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

