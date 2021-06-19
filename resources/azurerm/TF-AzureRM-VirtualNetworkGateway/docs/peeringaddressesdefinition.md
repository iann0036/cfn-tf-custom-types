# TF::AzureRM::VirtualNetworkGateway PeeringAddressesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apipaaddresses" title="ApipaAddresses">ApipaAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#ipconfigurationname" title="IpConfigurationName">IpConfigurationName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#apipaaddresses" title="ApipaAddresses">ApipaAddresses</a>: <i>
      - String</i>
<a href="#ipconfigurationname" title="IpConfigurationName">IpConfigurationName</a>: <i>String</i>
</pre>

## Properties

#### ApipaAddresses

A list of Azure custom APIPA addresses assigned to the BGP peer of the Virtual Network Gateway.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfigurationName

The name of the IP configuration of this Virtual Network Gateway. In case there are multiple `ip_configuration` blocks defined, this property is **required** to specify.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

