# Terraform::AzureRM::KeyVault NetworkAcls

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bypass" title="Bypass">Bypass</a>" : <i>String</i>,
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprules" title="IpRules">IpRules</a>" : <i>[ String, ... ]</i>,
    "<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bypass" title="Bypass">Bypass</a>: <i>String</i>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprules" title="IpRules">IpRules</a>: <i>
      - String</i>
<a href="#virtualnetworksubnetids" title="VirtualNetworkSubnetIds">VirtualNetworkSubnetIds</a>: <i>
      - String</i>
</pre>

## Properties

#### Bypass

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRules

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkSubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

