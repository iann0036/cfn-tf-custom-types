# TF::Spotinst::ElastigroupGke NetworkInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>" : <i>[ <a href="accessconfigsdefinition.md">AccessConfigsDefinition</a>, ... ]</i>,
    "<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>" : <i>[ <a href="aliasiprangesdefinition.md">AliasIpRangesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>: <i>
      - <a href="accessconfigsdefinition.md">AccessConfigsDefinition</a></i>
<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>: <i>
      - <a href="aliasiprangesdefinition.md">AliasIpRangesDefinition</a></i>
</pre>

## Properties

#### Network

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfigs

_Required_: No

_Type_: List of <a href="accessconfigsdefinition.md">AccessConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRanges

_Required_: No

_Type_: List of <a href="aliasiprangesdefinition.md">AliasIpRangesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

