# TF::AVI::Serviceenginegroup RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#inputinterface" title="InputInterface">InputInterface</a>" : <i>String</i>,
    "<a href="#outputinterface" title="OutputInterface">OutputInterface</a>" : <i>String</i>,
    "<a href="#proto" title="Proto">Proto</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
    "<a href="#dnatip" title="DnatIp">DnatIp</a>" : <i>[ <a href="dnatipdefinition.md">DnatIpDefinition</a>, ... ]</i>,
    "<a href="#dstip" title="DstIp">DstIp</a>" : <i>[ <a href="dstipdefinition.md">DstIpDefinition</a>, ... ]</i>,
    "<a href="#dstport" title="DstPort">DstPort</a>" : <i>[ <a href="dstportdefinition.md">DstPortDefinition</a>, ... ]</i>,
    "<a href="#srcip" title="SrcIp">SrcIp</a>" : <i>[ <a href="srcipdefinition.md">SrcIpDefinition</a>, ... ]</i>,
    "<a href="#srcport" title="SrcPort">SrcPort</a>" : <i>[ <a href="srcportdefinition.md">SrcPortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#inputinterface" title="InputInterface">InputInterface</a>: <i>String</i>
<a href="#outputinterface" title="OutputInterface">OutputInterface</a>: <i>String</i>
<a href="#proto" title="Proto">Proto</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>String</i>
<a href="#dnatip" title="DnatIp">DnatIp</a>: <i>
      - <a href="dnatipdefinition.md">DnatIpDefinition</a></i>
<a href="#dstip" title="DstIp">DstIp</a>: <i>
      - <a href="dstipdefinition.md">DstIpDefinition</a></i>
<a href="#dstport" title="DstPort">DstPort</a>: <i>
      - <a href="dstportdefinition.md">DstPortDefinition</a></i>
<a href="#srcip" title="SrcIp">SrcIp</a>: <i>
      - <a href="srcipdefinition.md">SrcIpDefinition</a></i>
<a href="#srcport" title="SrcPort">SrcPort</a>: <i>
      - <a href="srcportdefinition.md">SrcPortDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proto

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnatIp

_Required_: No

_Type_: List of <a href="dnatipdefinition.md">DnatIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIp

_Required_: No

_Type_: List of <a href="dstipdefinition.md">DstIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPort

_Required_: No

_Type_: List of <a href="dstportdefinition.md">DstPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIp

_Required_: No

_Type_: List of <a href="srcipdefinition.md">SrcIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcPort

_Required_: No

_Type_: List of <a href="srcportdefinition.md">SrcPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

