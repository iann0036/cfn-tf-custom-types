# TF::ACI::L3outFloatingSvi

Manages ACI L3out Floating SVI

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L3outFloatingSvi",
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
        "<a href="#nodedn" title="NodeDn">NodeDn</a>" : <i>String</i>,
        "<a href="#relationl3extrsdynpathatt" title="RelationL3extRsDynPathAtt">RelationL3extRsDynPathAtt</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetdscp" title="TargetDscp">TargetDscp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L3outFloatingSvi
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
    <a href="#nodedn" title="NodeDn">NodeDn</a>: <i>String</i>
    <a href="#relationl3extrsdynpathatt" title="RelationL3extRsDynPathAtt">RelationL3extRsDynPathAtt</a>: <i>
      - String</i>
    <a href="#targetdscp" title="TargetDscp">TargetDscp</a>: <i>String</i>
</pre>

## Properties

#### Addr

Peer address for L3out floating SVI object.
- `annotation` - (Optional) Annotation for L3out floating SVI object.
- `description` - (Optional) Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotation

Annotation for L3out floating SVI object.
- `description` - (Optional) Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autostate

Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encap

Port encapsulation for L3out floating SVI object.
- `addr` - (Optional) Peer address for L3out floating SVI object.
- `annotation` - (Optional) Annotation for L3out floating SVI object.
- `description` - (Optional) Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncapScope

Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IfInstT

Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Dad

IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LlAddr

Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalInterfaceProfileDn

Distinguished name of parent logical interface profile object.
- `node_dn` - (Required) Distinguished name of the node for L3out floating SVI object.
- `encap` - (Required) Port encapsulation for L3out floating SVI object.
- `addr` - (Optional) Peer address for L3out floating SVI object.
- `annotation` - (Optional) Annotation for L3out floating SVI object.
- `description` - (Optional) Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeDn

Distinguished name of the node for L3out floating SVI object.
- `encap` - (Required) Port encapsulation for L3out floating SVI object.
- `addr` - (Optional) Peer address for L3out floating SVI object.
- `annotation` - (Optional) Annotation for L3out floating SVI object.
- `description` - (Optional) Description for L3out floating SVI object.
- `autostate` - (Optional) Autostate for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "disabled".
- `encap_scope` - (Optional) Encap scope for L3out floating SVI object. Allowed values are "ctx" and "local". Default value is "local".
- `if_inst_t` - (Optional) Interface type for L3out floating SVI object. Allowed values are "ext-svi", "l3-port", "sub-interface" and "unspecified". Default value is "unspecified".
- `ipv6_dad` - (Optional) IPv6 dad for L3out floating SVI object. Allowed values are "disabled" and "enabled". Default value is "enabled".
- `ll_addr` - (Optional) Link local address for L3out floating SVI object.
- `mac` - (Optional) MAC address for L3out floating SVI object.
- `mode` - (Optional) BGP domain mode for L3out floating SVI object. Allowed values are "native", "regular" and "untagged". Default value is "regular".
- `mtu` - (Optional) Administrative MTU port on the aggregated interface for L3out floating SVI object.
- `target_dscp` - (Optional) Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelationL3extRsDynPathAtt

Relation to class infraDomP. Cardinality - N_TO_M. Type - Set of String.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDscp

Target DSCP for L3out floating SVI object. Allowed values are "AF11", "AF12", "AF13", "AF21", "AF22", "AF23", "AF31", "AF32", "AF33", "AF41", "AF42", "AF43", "CS0", "CS1", "CS2", "CS3", "CS4", "CS5", "CS6", "CS7", "EF", "VA" and "unspecified". Default value is "unspecified".

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

