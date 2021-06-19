# TF::ACI::L3outPathAttachment

Manages ACI L3-out Path Attachment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outPathAttachment",
    "Properties" : {
        "<a href="#addr" title="Addr">Addr</a>" : <i>String</i>,
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#autostate" title="Autostate">Autostate</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encap" title="Encap">Encap</a>" : <i>String</i>,
        "<a href="#encapscope" title="EncapScope">EncapScope</a>" : <i>String</i>,
        "<a href="#ifinstt" title="IfInstT">IfInstT</a>" : <i>String</i>,
        "<a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>" : <i>String</i>,
        "<a href="#lladdr" title="LlAddr">LlAddr</a>" : <i>String</i>,
        "<a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>" : <i>String</i>,
        "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>String</i>,
        "<a href="#targetdn" title="TargetDn">TargetDn</a>" : <i>String</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outPathAttachment
Properties:
    <a href="#addr" title="Addr">Addr</a>: <i>String</i>
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#autostate" title="Autostate">Autostate</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encap" title="Encap">Encap</a>: <i>String</i>
    <a href="#encapscope" title="EncapScope">EncapScope</a>: <i>String</i>
    <a href="#ifinstt" title="IfInstT">IfInstT</a>: <i>String</i>
    <a href="#ipv6dad" title="Ipv6Dad">Ipv6Dad</a>: <i>String</i>
    <a href="#lladdr" title="LlAddr">LlAddr</a>: <i>String</i>
    <a href="#logicalinterfaceprofiledn" title="LogicalInterfaceProfileDn">LogicalInterfaceProfileDn</a>: <i>String</i>
    <a href="#mac" title="Mac">Mac</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>String</i>
    <a href="#targetdn" title="TargetDn">TargetDn</a>: <i>String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
</pre>

## Properties

#### Addr

The IP address of the path attached to the layer 3 outside profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for object L3-out Path Attachment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autostate

Autostate for object L3-out Path Attachment.
Allowed values: "disabled", "enabled". Default value: "disabled".
- `encap` - (Optional) The encapsulation of the path attached to the layer 3 outside profile. Encap should be set to "unknown" if the value of if_inst_t is "l3-port".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encap

The encapsulation of the path attached to the layer 3 outside profile. Encap should be set to "unknown" if the value of if_inst_t is "l3-port".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncapScope

The encapsulation scope for object L3-out Path Attachment.
Allowed values: "ctx", "local". Default value: "local".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfInstT

Interface type.
Allowed values: "ext-svi", "l3-port", "sub-interface", "unspecified".
- `addr` - (Optional) The IP address of the path attached to the layer 3 outside profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Dad

IPv6-Dad for object L3-out Path Attachment.
Allowed values: "disabled", "enabled". Default value: "enabled".
- `ll_addr` - (Optional) The override of the system generated IPv6 link-local address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LlAddr

The override of the system generated IPv6 link-local address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalInterfaceProfileDn

Distinguished name of parent logical interface profile object.
- `target_dn` - (Required) The logical interface identifier.
- `if_inst_t` - (Required) Interface type.
Allowed values: "ext-svi", "l3-port", "sub-interface", "unspecified".
- `addr` - (Optional) The IP address of the path attached to the layer 3 outside profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

The MAC address of the path attached to the layer 3 outside profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

BGP Domain mode.
Allowed values: "native", "regular", "untagged". Default value: "regular".
- `mtu` - (Optional) The maximum transmit unit of the external network.
Default value: "inherit".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The maximum transmit unit of the external network.
Default value: "inherit".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDn

The logical interface identifier.
- `if_inst_t` - (Required) Interface type.
Allowed values: "ext-svi", "l3-port", "sub-interface", "unspecified".
- `addr` - (Optional) The IP address of the path attached to the layer 3 outside profile.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

The target differentiated service code point (DSCP) of the path attached to the layer 3 outside profile. Default value: "unspecified".
Allowed values: "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA", "unspecified". Default value: "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

