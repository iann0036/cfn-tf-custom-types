# Terraform::Panos::NatRuleGroup Source

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dynamicip" title="DynamicIp">DynamicIp</a>" : <i>[ <a href="source-dynamicip.md">DynamicIp</a>, ... ]</i>,
    "<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>" : <i>[ <a href="source-dynamicipandport.md">DynamicIpAndPort</a>, ... ]</i>,
    "<a href="#staticip" title="StaticIp">StaticIp</a>" : <i>[ <a href="source-staticip.md">StaticIp</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dynamicip" title="DynamicIp">DynamicIp</a>: <i>
      - <a href="source-dynamicip.md">DynamicIp</a></i>
<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>: <i>
      - <a href="source-dynamicipandport.md">DynamicIpAndPort</a></i>
<a href="#staticip" title="StaticIp">StaticIp</a>: <i>
      - <a href="source-staticip.md">StaticIp</a></i>
</pre>

## Properties

#### DynamicIp

_Required_: No

_Type_: List of <a href="source-dynamicip.md">DynamicIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIpAndPort

_Required_: No

_Type_: List of <a href="source-dynamicipandport.md">DynamicIpAndPort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIp

_Required_: No

_Type_: List of <a href="source-staticip.md">StaticIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

