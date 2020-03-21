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
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="rule-destination.md">Destination</a>, ... ]</i>,
    "<a href="#forwarding" title="Forwarding">Forwarding</a>" : <i>[ <a href="rule-forwarding.md">Forwarding</a>, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="rule-source.md">Source</a>, ... ]</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ <a href="rule-target.md">Target</a>, ... ]</i>
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
      - <a href="rule-destination.md">Destination</a></i>
<a href="#forwarding" title="Forwarding">Forwarding</a>: <i>
      - <a href="rule-forwarding.md">Forwarding</a></i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="rule-source.md">Source</a></i>
<a href="#target" title="Target">Target</a>: <i>
      - <a href="rule-target.md">Target</a></i>
</pre>

## Properties

#### ActiveActiveDeviceBinding

The active-active device binding.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The rule description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Set to `true` to disable this rule.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateTarget

Instead of applying the rule for the
given serial numbers, apply it to everything except them.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

The schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags for this rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

The UUID for the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="rule-destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forwarding

_Required_: No

_Type_: List of <a href="rule-forwarding.md">Forwarding</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="rule-source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="rule-target.md">Target</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

