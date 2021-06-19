# TF::FortiOS::WirelesscontrollerAccesscontrollist Layer3Ipv4RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>String</i>,
    "<a href="#dstport" title="Dstport">Dstport</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
    "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>Double</i>,
    "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>String</i>,
    "<a href="#srcport" title="Srcport">Srcport</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>String</i>
<a href="#dstport" title="Dstport">Dstport</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
<a href="#ruleid" title="RuleId">RuleId</a>: <i>Double</i>
<a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>String</i>
<a href="#srcport" title="Srcport">Srcport</a>: <i>Double</i>
</pre>

## Properties

#### Action

Policy action (allow | deny). Valid values: `allow`, `deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

Destination IP address (any | local-LAN | IPv4 address[/<network mask | mask length>], default = any).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstport

Destination port (0 - 65535, default = 0, meaning any).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol type as defined by IANA (0 - 255, default = 255, meaning any).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

Rule ID (1 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

Source IP address (any | local-LAN | IPv4 address[/<network mask | mask length>], default = any).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcport

Source port (0 - 65535, default = 0, meaning any).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

