# TF::FortiOS::SwitchcontrollerManagedswitch MirrorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dst" title="Dst">Dst</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#switchingpacket" title="SwitchingPacket">SwitchingPacket</a>" : <i>String</i>,
    "<a href="#srcegress" title="SrcEgress">SrcEgress</a>" : <i>[ <a href="srcegressdefinition.md">SrcEgressDefinition</a>, ... ]</i>,
    "<a href="#srcingress" title="SrcIngress">SrcIngress</a>" : <i>[ <a href="srcingressdefinition.md">SrcIngressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dst" title="Dst">Dst</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#switchingpacket" title="SwitchingPacket">SwitchingPacket</a>: <i>String</i>
<a href="#srcegress" title="SrcEgress">SrcEgress</a>: <i>
      - <a href="srcegressdefinition.md">SrcEgressDefinition</a></i>
<a href="#srcingress" title="SrcIngress">SrcIngress</a>: <i>
      - <a href="srcingressdefinition.md">SrcIngressDefinition</a></i>
</pre>

## Properties

#### Dst

Destination port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Mirror name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Active/inactive mirror configuration. Valid values: `active`, `inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingPacket

Enable/disable switching functionality when mirroring. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcEgress

_Required_: No

_Type_: List of <a href="srcegressdefinition.md">SrcEgressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrcIngress

_Required_: No

_Type_: List of <a href="srcingressdefinition.md">SrcIngressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

