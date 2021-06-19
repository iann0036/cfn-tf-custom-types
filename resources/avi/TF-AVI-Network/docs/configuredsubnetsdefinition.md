# TF::AVI::Network ConfiguredSubnetsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>[ <a href="prefixdefinition.md">PrefixDefinition</a>, ... ]</i>,
    "<a href="#staticipranges" title="StaticIpRanges">StaticIpRanges</a>" : <i>[ <a href="staticiprangesdefinition.md">StaticIpRangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prefix" title="Prefix">Prefix</a>: <i>
      - <a href="prefixdefinition.md">PrefixDefinition</a></i>
<a href="#staticipranges" title="StaticIpRanges">StaticIpRanges</a>: <i>
      - <a href="staticiprangesdefinition.md">StaticIpRangesDefinition</a></i>
</pre>

## Properties

#### Prefix

_Required_: No

_Type_: List of <a href="prefixdefinition.md">PrefixDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpRanges

_Required_: No

_Type_: List of <a href="staticiprangesdefinition.md">StaticIpRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

