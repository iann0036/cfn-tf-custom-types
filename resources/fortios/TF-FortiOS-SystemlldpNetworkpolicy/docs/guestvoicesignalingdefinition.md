# TF::FortiOS::SystemlldpNetworkpolicy GuestVoiceSignalingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dscp" title="Dscp">Dscp</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
    "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dscp" title="Dscp">Dscp</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>String</i>
<a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
</pre>

## Properties

#### Dscp

Differentiated Services Code Point (DSCP) value to advertise.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable advertising this policy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

Advertise tagged or untagged traffic. Valid values: `none`, `dot1q`, `dot1p`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

802.1Q VLAN ID to advertise (1 - 4094).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

