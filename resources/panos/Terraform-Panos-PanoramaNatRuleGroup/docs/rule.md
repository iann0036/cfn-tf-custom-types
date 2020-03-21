# Terraform::Panos::PanoramaNatRuleGroup Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#negatetarget" title="NegateTarget">NegateTarget</a>" : <i>Boolean</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ <a href="rule-originalpacket.md">OriginalPacket</a>, ... ]</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ <a href="rule-target.md">Target</a>, ... ]</i>,
    "<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>" : <i>[ <a href="rule-translatedpacket.md">TranslatedPacket</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#negatetarget" title="NegateTarget">NegateTarget</a>: <i>Boolean</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>: <i>
      - <a href="rule-originalpacket.md">OriginalPacket</a></i>
<a href="#target" title="Target">Target</a>: <i>
      - <a href="rule-target.md">Target</a></i>
<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>: <i>
      - <a href="rule-translatedpacket.md">TranslatedPacket</a></i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Set to `true` to disable this rule.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The NAT rule's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateTarget

Instead of applying the rule for the
given serial numbers, apply it to everything except them.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of administrative tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

. NAT type.  This can be `ipv4` (default), `nat64`, or
`nptv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPacket

_Required_: No

_Type_: List of <a href="rule-originalpacket.md">OriginalPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="rule-target.md">Target</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPacket

_Required_: No

_Type_: List of <a href="rule-translatedpacket.md">TranslatedPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

