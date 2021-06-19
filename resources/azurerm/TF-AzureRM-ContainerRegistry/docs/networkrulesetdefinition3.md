# TF::AzureRM::ContainerRegistry NetworkRuleSetDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>String</i>,
    "<a href="#iprule" title="IpRule">IpRule</a>" : <i>[ <a href="networkrulesetdefinition.md">NetworkRuleSetDefinition</a>, ... ]</i>,
    "<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>" : <i>[ <a href="networkrulesetdefinition2.md">NetworkRuleSetDefinition2</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>String</i>
<a href="#iprule" title="IpRule">IpRule</a>: <i>
      - <a href="networkrulesetdefinition.md">NetworkRuleSetDefinition</a></i>
<a href="#virtualnetwork" title="VirtualNetwork">VirtualNetwork</a>: <i>
      - <a href="networkrulesetdefinition2.md">NetworkRuleSetDefinition2</a></i>
</pre>

## Properties

#### DefaultAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRule

_Required_: No

_Type_: List of <a href="networkrulesetdefinition.md">NetworkRuleSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetwork

_Required_: No

_Type_: List of <a href="networkrulesetdefinition2.md">NetworkRuleSetDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

