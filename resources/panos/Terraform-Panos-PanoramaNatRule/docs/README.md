# Terraform::Panos::PanoramaNatRule

This resource allows you to add/update/delete Panorama NAT rules.

~> **Note:** This resource has been deprecated.  Please use
`panos_panorama_nat_rule_group` instead.

~> **Note:** `panos_panorama_nat_policy` is known as `panos_panorama_nat_rule`.

The prefix `sat` stands for "Source Address Translation" while the prefix "dat"
stands for "Destination Address Translation".  The order of the params in
this resource and their naming matches how the params are presented in
the GUI.  Thus, having a GUI window open while creating your resource
definition will simplify the process.

Note that while many of the params for this resource are optional in an
absolute sense, depending on what type of NAT you wish to configure, certain
params may become necessary to correctly configure the NAT rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaNatRule",
    "Properties" : {
        "<a href="#dataddress" title="DatAddress">DatAddress</a>" : <i>String</i>,
        "<a href="#datdynamicdistribution" title="DatDynamicDistribution">DatDynamicDistribution</a>" : <i>String</i>,
        "<a href="#datport" title="DatPort">DatPort</a>" : <i>Double</i>,
        "<a href="#dattype" title="DatType">DatType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationzone" title="DestinationZone">DestinationZone</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#negatetarget" title="NegateTarget">NegateTarget</a>" : <i>Boolean</i>,
        "<a href="#rulebase" title="Rulebase">Rulebase</a>" : <i>String</i>,
        "<a href="#sataddresstype" title="SatAddressType">SatAddressType</a>" : <i>String</i>,
        "<a href="#satfallbackinterface" title="SatFallbackInterface">SatFallbackInterface</a>" : <i>String</i>,
        "<a href="#satfallbackipaddress" title="SatFallbackIpAddress">SatFallbackIpAddress</a>" : <i>String</i>,
        "<a href="#satfallbackiptype" title="SatFallbackIpType">SatFallbackIpType</a>" : <i>String</i>,
        "<a href="#satfallbacktranslatedaddresses" title="SatFallbackTranslatedAddresses">SatFallbackTranslatedAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#satfallbacktype" title="SatFallbackType">SatFallbackType</a>" : <i>String</i>,
        "<a href="#satinterface" title="SatInterface">SatInterface</a>" : <i>String</i>,
        "<a href="#satipaddress" title="SatIpAddress">SatIpAddress</a>" : <i>String</i>,
        "<a href="#satstaticbidirectional" title="SatStaticBiDirectional">SatStaticBiDirectional</a>" : <i>Boolean</i>,
        "<a href="#satstatictranslatedaddress" title="SatStaticTranslatedAddress">SatStaticTranslatedAddress</a>" : <i>String</i>,
        "<a href="#sattranslatedaddresses" title="SatTranslatedAddresses">SatTranslatedAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#sattype" title="SatType">SatType</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcezones" title="SourceZones">SourceZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tointerface" title="ToInterface">ToInterface</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="target.md">Target</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaNatRule
Properties:
    <a href="#dataddress" title="DatAddress">DatAddress</a>: <i>String</i>
    <a href="#datdynamicdistribution" title="DatDynamicDistribution">DatDynamicDistribution</a>: <i>String</i>
    <a href="#datport" title="DatPort">DatPort</a>: <i>Double</i>
    <a href="#dattype" title="DatType">DatType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
    <a href="#destinationzone" title="DestinationZone">DestinationZone</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#negatetarget" title="NegateTarget">NegateTarget</a>: <i>Boolean</i>
    <a href="#rulebase" title="Rulebase">Rulebase</a>: <i>String</i>
    <a href="#sataddresstype" title="SatAddressType">SatAddressType</a>: <i>String</i>
    <a href="#satfallbackinterface" title="SatFallbackInterface">SatFallbackInterface</a>: <i>String</i>
    <a href="#satfallbackipaddress" title="SatFallbackIpAddress">SatFallbackIpAddress</a>: <i>String</i>
    <a href="#satfallbackiptype" title="SatFallbackIpType">SatFallbackIpType</a>: <i>String</i>
    <a href="#satfallbacktranslatedaddresses" title="SatFallbackTranslatedAddresses">SatFallbackTranslatedAddresses</a>: <i>
      - String</i>
    <a href="#satfallbacktype" title="SatFallbackType">SatFallbackType</a>: <i>String</i>
    <a href="#satinterface" title="SatInterface">SatInterface</a>: <i>String</i>
    <a href="#satipaddress" title="SatIpAddress">SatIpAddress</a>: <i>String</i>
    <a href="#satstaticbidirectional" title="SatStaticBiDirectional">SatStaticBiDirectional</a>: <i>Boolean</i>
    <a href="#satstatictranslatedaddress" title="SatStaticTranslatedAddress">SatStaticTranslatedAddress</a>: <i>String</i>
    <a href="#sattranslatedaddresses" title="SatTranslatedAddresses">SatTranslatedAddresses</a>: <i>
      - String</i>
    <a href="#sattype" title="SatType">SatType</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
    <a href="#sourcezones" title="SourceZones">SourceZones</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#tointerface" title="ToInterface">ToInterface</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="target.md">Target</a></i>
</pre>

## Properties

#### DatAddress

Destination address translation's address.  Requires
`dat_type` be set to "static" or "dynamic".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatDynamicDistribution

Distribution algorithm
for destination address pool.  The PAN-OS 8.1 GUI doesn't seem to set this
anywhere, but this is added here for completeness' sake.  Requires `dat_type`
of "dynamic".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatPort

Destination address translation's port number.  Requires
`dat_type` be set to "static" or "dynamic".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatType

Destination address translation type.  This should
be either `static` or `dynamic`.  The `dynamic` option is only available on
PAN-OS 8.1+.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddresses

List of destination address(es).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationZone

The destination zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group to put the NAT rule into
(default: `shared`).

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

#### Rulebase

The rulebase.  This can be `pre-rulebase` (default),
`post-rulebase`, or `rulebase`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatAddressType

Source address translation address type.
This can be `interface-address` or `translated-address`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackInterface

Source address translation fallback
interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackIpAddress

The source address translation
fallback IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackIpType

Source address translation fallback
IP type.  This can be `ip` or `floating`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackTranslatedAddresses

Source address translation
list of fallback translated addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatFallbackType

Source address translation fallback type.
This can be `none`, `interface-address`, or `translated-address`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatInterface

Source address translation interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatIpAddress

Source address translation IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatStaticBiDirectional

Set to `true` to enable
bi-directional source address translation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatStaticTranslatedAddress

The statically translated source
address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatTranslatedAddresses

Source address translation list of
translated addresses.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SatType

Type of source address translation.  This can be
`none` (default), `dynamic-ip-and-port`, `dynamic-ip`, or `static-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Service (default: `any`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

List of source address(es).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceZones

The list of source zone(s).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of administrative tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToInterface

Egress interface from route lookup (default:
`any`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

. NAT type.  This can be `ipv4` (default), `nat64`, or
`nptv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="target.md">Target</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

