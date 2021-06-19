# TF::FortiOS::SystemNat64

Configure NAT64.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemNat64",
    "Properties" : {
        "<a href="#alwayssynthesizeaaaarecord" title="AlwaysSynthesizeAaaaRecord">AlwaysSynthesizeAaaaRecord</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#generateipv6fragmentheader" title="GenerateIpv6FragmentHeader">GenerateIpv6FragmentHeader</a>" : <i>String</i>,
        "<a href="#nat46forceipv4packetforwarding" title="Nat46ForceIpv4PacketForwarding">Nat46ForceIpv4PacketForwarding</a>" : <i>String</i>,
        "<a href="#nat64prefix" title="Nat64Prefix">Nat64Prefix</a>" : <i>String</i>,
        "<a href="#secondaryprefixstatus" title="SecondaryPrefixStatus">SecondaryPrefixStatus</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#secondaryprefix" title="SecondaryPrefix">SecondaryPrefix</a>" : <i>[ <a href="secondaryprefixdefinition.md">SecondaryPrefixDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemNat64
Properties:
    <a href="#alwayssynthesizeaaaarecord" title="AlwaysSynthesizeAaaaRecord">AlwaysSynthesizeAaaaRecord</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#generateipv6fragmentheader" title="GenerateIpv6FragmentHeader">GenerateIpv6FragmentHeader</a>: <i>String</i>
    <a href="#nat46forceipv4packetforwarding" title="Nat46ForceIpv4PacketForwarding">Nat46ForceIpv4PacketForwarding</a>: <i>String</i>
    <a href="#nat64prefix" title="Nat64Prefix">Nat64Prefix</a>: <i>String</i>
    <a href="#secondaryprefixstatus" title="SecondaryPrefixStatus">SecondaryPrefixStatus</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#secondaryprefix" title="SecondaryPrefix">SecondaryPrefix</a>: <i>
      - <a href="secondaryprefixdefinition.md">SecondaryPrefixDefinition</a></i>
</pre>

## Properties

#### AlwaysSynthesizeAaaaRecord

Enable/disable AAAA record synthesis (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateIpv6FragmentHeader

Enable/disable IPv6 fragment header generation. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat46ForceIpv4PacketForwarding

Enable/disable mandatory IPv4 packet forwarding in nat46. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat64Prefix

NAT64 prefix must be ::/96 (default = 64:ff9b::/96).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPrefixStatus

Enable/disable secondary NAT64 prefix. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable NAT64 (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryPrefix

_Required_: No

_Type_: List of <a href="secondaryprefixdefinition.md">SecondaryPrefixDefinition</a>

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

