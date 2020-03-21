# Terraform::Spotinst::ElastigroupGcp NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>" : <i>[ &lt;a href=&#34;networkinterface-accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;, ... ]</i>,
    "<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>" : <i>[ &lt;a href=&#34;networkinterface-aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#accessconfigs" title="AccessConfigs">AccessConfigs</a>: <i>
      - &lt;a href=&#34;networkinterface-accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;</i>
<a href="#aliasipranges" title="AliasIpRanges">AliasIpRanges</a>: <i>
      - &lt;a href=&#34;networkinterface-aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;</i>
</pre>

## Properties

#### Network

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessConfigs

_Required_: No
_Type_: List of &lt;a href=&#34;networkinterface-accessconfigs.md&#34;&gt;AccessConfigs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AliasIpRanges

_Required_: No
_Type_: List of &lt;a href=&#34;networkinterface-aliasipranges.md&#34;&gt;AliasIpRanges&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

