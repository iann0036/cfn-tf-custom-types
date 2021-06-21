# TF::AzureRM::CognitiveAccount NetworkAclsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprules" title="IpRules">IpRules</a>" : <i>[ String, ... ]</i>,
    "<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprules" title="IpRules">IpRules</a>: <i>
      - String</i>
<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>: <i>
      - String</i>
</pre>

## Properties

#### DefaultAction

The Default Action to use when no rules match from `ip_rules` / `virtual_network_subnet_ids`. Possible values are `Allow` and `Deny`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRules

One or more IP Addresses, or CIDR Blocks which should be able to access the Cognitive Account.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkSubnetIds

One or more Subnet ID's which should be able to access this Cognitive Account.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
