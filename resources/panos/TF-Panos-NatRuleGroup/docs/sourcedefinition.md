# TF::Panos::NatRuleGroup SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dynamicip" title="DynamicIp">DynamicIp</a>" : <i>[ <a href="dynamicipdefinition.md">DynamicIpDefinition</a>, ... ]</i>,
    "<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>" : <i>[ <a href="dynamicipandportdefinition.md">DynamicIpAndPortDefinition</a>, ... ]</i>,
    "<a href="#staticip" title="StaticIp">StaticIp</a>" : <i>[ <a href="staticipdefinition.md">StaticIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dynamicip" title="DynamicIp">DynamicIp</a>: <i>
      - <a href="dynamicipdefinition.md">DynamicIpDefinition</a></i>
<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>: <i>
      - <a href="dynamicipandportdefinition.md">DynamicIpAndPortDefinition</a></i>
<a href="#staticip" title="StaticIp">StaticIp</a>: <i>
      - <a href="staticipdefinition.md">StaticIpDefinition</a></i>
</pre>

## Properties

#### DynamicIp

_Required_: No

_Type_: List of <a href="dynamicipdefinition.md">DynamicIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIpAndPort

_Required_: No

_Type_: List of <a href="dynamicipandportdefinition.md">DynamicIpAndPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIp

_Required_: No

_Type_: List of <a href="staticipdefinition.md">StaticIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

