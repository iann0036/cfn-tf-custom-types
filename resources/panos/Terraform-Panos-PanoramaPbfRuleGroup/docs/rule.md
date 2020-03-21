# Terraform::Panos::PanoramaPbfRuleGroup Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activeactivedevicebinding" title="ActiveActiveDeviceBinding">ActiveActiveDeviceBinding</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#negatetarget" title="NegateTarget">NegateTarget</a>" : <i>Boolean</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
    "<a href="#forwarding" title="Forwarding">Forwarding</a>" : <i>[ &lt;a href=&#34;rule-forwarding.md&#34;&gt;Forwarding&lt;/a&gt;, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#activeactivedevicebinding" title="ActiveActiveDeviceBinding">ActiveActiveDeviceBinding</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#negatetarget" title="NegateTarget">NegateTarget</a>: <i>Boolean</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;</i>
<a href="#forwarding" title="Forwarding">Forwarding</a>: <i>
      - &lt;a href=&#34;rule-forwarding.md&#34;&gt;Forwarding&lt;/a&gt;</i>
<a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;</i>
<a href="#target" title="Target">Target</a>: <i>
      - &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;</i>
</pre>

## Properties

#### ActiveActiveDeviceBinding

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Schedule

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No
_Type_: List of &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forwarding

_Required_: No
_Type_: List of &lt;a href=&#34;rule-forwarding.md&#34;&gt;Forwarding&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No
_Type_: List of &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No
_Type_: List of &lt;a href=&#34;rule-target.md&#34;&gt;Target&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

