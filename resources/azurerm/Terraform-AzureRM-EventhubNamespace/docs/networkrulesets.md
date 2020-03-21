# Terraform::AzureRM::EventhubNamespace NetworkRulesets

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprule" title="IpRule">IpRule</a>" : <i>[ &lt;a href=&#34;networkrulesets-iprule.md&#34;&gt;IpRule&lt;/a&gt;, ... ]</i>,
    "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ &lt;a href=&#34;networkrulesets-virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprule" title="IpRule">IpRule</a>: <i>
      - &lt;a href=&#34;networkrulesets-iprule.md&#34;&gt;IpRule&lt;/a&gt;</i>
<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - &lt;a href=&#34;networkrulesets-virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultAction

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRule

_Required_: No
_Type_: List of &lt;a href=&#34;networkrulesets-iprule.md&#34;&gt;IpRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No
_Type_: List of &lt;a href=&#34;networkrulesets-virtualnetworkrule.md&#34;&gt;VirtualNetworkRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

