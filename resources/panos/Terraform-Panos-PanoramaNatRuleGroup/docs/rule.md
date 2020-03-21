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
    "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ &lt;a href=&#34;rule-originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;, ... ]</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;, ... ]</i>,
    "<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>" : <i>[ &lt;a href=&#34;rule-translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;rule-originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;</i>
<a href="#target" title="Target">Target</a>: <i>
      - &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;</i>
<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>: <i>
      - &lt;a href=&#34;rule-translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateTarget

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPacket

_Required_: No
_Type_: List of &lt;a href=&#34;rule-originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No
_Type_: List of &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPacket

_Required_: No
_Type_: List of &lt;a href=&#34;rule-translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

