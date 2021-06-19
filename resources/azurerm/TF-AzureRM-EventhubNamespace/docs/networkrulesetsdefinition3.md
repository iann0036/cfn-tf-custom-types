# TF::AzureRM::EventhubNamespace NetworkRulesetsDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprule" title="IpRule">IpRule</a>" : <i>[ <a href="networkrulesetsdefinition.md">NetworkRulesetsDefinition</a>, ... ]</i>,
    "<a href="#trustedserviceaccessenabled" title="TrustedServiceAccessEnabled">TrustedServiceAccessEnabled</a>" : <i>Boolean</i>,
    "<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>" : <i>[ <a href="networkrulesetsdefinition2.md">NetworkRulesetsDefinition2</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprule" title="IpRule">IpRule</a>: <i>
      - <a href="networkrulesetsdefinition.md">NetworkRulesetsDefinition</a></i>
<a href="#trustedserviceaccessenabled" title="TrustedServiceAccessEnabled">TrustedServiceAccessEnabled</a>: <i>Boolean</i>
<a href="#virtualnetworkrule" title="VirtualNetworkRule">VirtualNetworkRule</a>: <i>
      - <a href="networkrulesetsdefinition2.md">NetworkRulesetsDefinition2</a></i>
</pre>

## Properties

#### DefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRule

_Required_: No

_Type_: List of <a href="networkrulesetsdefinition.md">NetworkRulesetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedServiceAccessEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkRule

_Required_: No

_Type_: List of <a href="networkrulesetsdefinition2.md">NetworkRulesetsDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

