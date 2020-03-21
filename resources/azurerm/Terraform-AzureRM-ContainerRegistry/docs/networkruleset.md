# Terraform::AzureRM::ContainerRegistry NetworkRuleSet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprule" title="IpRule">IpRule</a>" : <i>[ &lt;a href=&#34;networkruleset-iprule.md&#34;&gt;IpRule&lt;/a&gt;, ... ]</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>[ &lt;a href=&#34;networkruleset-virtualnetwork.md&#34;&gt;VirtualNetwork&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprule" title="IpRule">IpRule</a>: <i>
      - &lt;a href=&#34;networkruleset-iprule.md&#34;&gt;IpRule&lt;/a&gt;</i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>
      - &lt;a href=&#34;networkruleset-virtualnetwork.md&#34;&gt;VirtualNetwork&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultAction

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRule

_Required_: No
_Type_: List of &lt;a href=&#34;networkruleset-iprule.md&#34;&gt;IpRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: No
_Type_: List of &lt;a href=&#34;networkruleset-virtualnetwork.md&#34;&gt;VirtualNetwork&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

