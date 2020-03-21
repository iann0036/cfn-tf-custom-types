# Terraform::AzureRM::EventhubNamespace NetworkRulesets

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprule" title="IpRule">IpRule</a>" : <i>[ <a href="networkrulesets-iprule.md">IpRule</a>, ... ]</i>,
    "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ <a href="networkrulesets-virtualnetworkrule.md">VirtualNetworkRule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprule" title="IpRule">IpRule</a>: <i>
      - <a href="networkrulesets-iprule.md">IpRule</a></i>
<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - <a href="networkrulesets-virtualnetworkrule.md">VirtualNetworkRule</a></i>
</pre>

## Properties

#### DefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRule

_Required_: No

_Type_: List of <a href="networkrulesets-iprule.md">IpRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No

_Type_: List of <a href="networkrulesets-virtualnetworkrule.md">VirtualNetworkRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

