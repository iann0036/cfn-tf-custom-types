# TF::AzureRM::ServicebusNamespaceNetworkRuleSet NetworkRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ignoremissingvnetserviceendpoint" title="IgnoreMissingVnetServiceEndpoint">IgnoreMissingVnetServiceEndpoint</a>" : <i>Boolean</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ignoremissingvnetserviceendpoint" title="IgnoreMissingVnetServiceEndpoint">IgnoreMissingVnetServiceEndpoint</a>: <i>Boolean</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### IgnoreMissingVnetServiceEndpoint

Should the ServiceBus Namespace Network Rule Set ignore missing Virtual Network Service Endpoint option in the Subnet? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The Subnet ID which should be able to access this ServiceBus Namespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

