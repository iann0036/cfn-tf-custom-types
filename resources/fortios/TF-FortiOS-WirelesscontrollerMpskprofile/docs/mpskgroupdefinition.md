# TF::FortiOS::WirelesscontrollerMpskprofile MpskGroupDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>,
    "<a href="#vlantype" title="VlanType">VlanType</a>" : <i>String</i>,
    "<a href="#mpskkey" title="MpskKey">MpskKey</a>" : <i>[ <a href="mpskkeydefinition.md">MpskKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
<a href="#vlantype" title="VlanType">VlanType</a>: <i>String</i>
<a href="#mpskkey" title="MpskKey">MpskKey</a>: <i>
      - <a href="mpskkeydefinition.md">MpskKeyDefinition</a></i>
</pre>

## Properties

#### Name

MPSK group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

Optional VLAN ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanType

MPSK group VLAN options. Valid values: `no-vlan`, `fixed-vlan`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MpskKey

_Required_: No

_Type_: List of <a href="mpskkeydefinition.md">MpskKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

