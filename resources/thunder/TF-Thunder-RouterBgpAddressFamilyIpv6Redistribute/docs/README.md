# TF::Thunder::RouterBgpAddressFamilyIpv6Redistribute

`thunder_router_bgp_address_family_ipv6_redistribute` Provides details about thunder router bgp address family ipv6 redistribute

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterBgpAddressFamilyIpv6Redistribute",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>String</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#connectedcfg" title="ConnectedCfg">ConnectedCfg</a>" : <i>[ <a href="connectedcfgdefinition.md">ConnectedCfgDefinition</a>, ... ]</i>,
        "<a href="#floatingipcfg" title="FloatingIpCfg">FloatingIpCfg</a>" : <i>[ <a href="floatingipcfgdefinition.md">FloatingIpCfgDefinition</a>, ... ]</i>,
        "<a href="#ipnatcfg" title="IpNatCfg">IpNatCfg</a>" : <i>[ <a href="ipnatcfgdefinition.md">IpNatCfgDefinition</a>, ... ]</i>,
        "<a href="#ipnatlistcfg" title="IpNatListCfg">IpNatListCfg</a>" : <i>[ <a href="ipnatlistcfgdefinition.md">IpNatListCfgDefinition</a>, ... ]</i>,
        "<a href="#isiscfg" title="IsisCfg">IsisCfg</a>" : <i>[ <a href="isiscfgdefinition.md">IsisCfgDefinition</a>, ... ]</i>,
        "<a href="#lw4o6cfg" title="Lw4o6Cfg">Lw4o6Cfg</a>" : <i>[ <a href="lw4o6cfgdefinition.md">Lw4o6CfgDefinition</a>, ... ]</i>,
        "<a href="#nat64cfg" title="Nat64Cfg">Nat64Cfg</a>" : <i>[ <a href="nat64cfgdefinition.md">Nat64CfgDefinition</a>, ... ]</i>,
        "<a href="#natmapcfg" title="NatMapCfg">NatMapCfg</a>" : <i>[ <a href="natmapcfgdefinition.md">NatMapCfgDefinition</a>, ... ]</i>,
        "<a href="#ospfcfg" title="OspfCfg">OspfCfg</a>" : <i>[ <a href="ospfcfgdefinition.md">OspfCfgDefinition</a>, ... ]</i>,
        "<a href="#ripcfg" title="RipCfg">RipCfg</a>" : <i>[ <a href="ripcfgdefinition.md">RipCfgDefinition</a>, ... ]</i>,
        "<a href="#staticcfg" title="StaticCfg">StaticCfg</a>" : <i>[ <a href="staticcfgdefinition.md">StaticCfgDefinition</a>, ... ]</i>,
        "<a href="#staticnatcfg" title="StaticNatCfg">StaticNatCfg</a>" : <i>[ <a href="staticnatcfgdefinition.md">StaticNatCfgDefinition</a>, ... ]</i>,
        "<a href="#vip" title="Vip">Vip</a>" : <i>[ <a href="vipdefinition.md">VipDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RouterBgpAddressFamilyIpv6Redistribute
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>String</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#connectedcfg" title="ConnectedCfg">ConnectedCfg</a>: <i>
      - <a href="connectedcfgdefinition.md">ConnectedCfgDefinition</a></i>
    <a href="#floatingipcfg" title="FloatingIpCfg">FloatingIpCfg</a>: <i>
      - <a href="floatingipcfgdefinition.md">FloatingIpCfgDefinition</a></i>
    <a href="#ipnatcfg" title="IpNatCfg">IpNatCfg</a>: <i>
      - <a href="ipnatcfgdefinition.md">IpNatCfgDefinition</a></i>
    <a href="#ipnatlistcfg" title="IpNatListCfg">IpNatListCfg</a>: <i>
      - <a href="ipnatlistcfgdefinition.md">IpNatListCfgDefinition</a></i>
    <a href="#isiscfg" title="IsisCfg">IsisCfg</a>: <i>
      - <a href="isiscfgdefinition.md">IsisCfgDefinition</a></i>
    <a href="#lw4o6cfg" title="Lw4o6Cfg">Lw4o6Cfg</a>: <i>
      - <a href="lw4o6cfgdefinition.md">Lw4o6CfgDefinition</a></i>
    <a href="#nat64cfg" title="Nat64Cfg">Nat64Cfg</a>: <i>
      - <a href="nat64cfgdefinition.md">Nat64CfgDefinition</a></i>
    <a href="#natmapcfg" title="NatMapCfg">NatMapCfg</a>: <i>
      - <a href="natmapcfgdefinition.md">NatMapCfgDefinition</a></i>
    <a href="#ospfcfg" title="OspfCfg">OspfCfg</a>: <i>
      - <a href="ospfcfgdefinition.md">OspfCfgDefinition</a></i>
    <a href="#ripcfg" title="RipCfg">RipCfg</a>: <i>
      - <a href="ripcfgdefinition.md">RipCfgDefinition</a></i>
    <a href="#staticcfg" title="StaticCfg">StaticCfg</a>: <i>
      - <a href="staticcfgdefinition.md">StaticCfgDefinition</a></i>
    <a href="#staticnatcfg" title="StaticNatCfg">StaticNatCfg</a>: <i>
      - <a href="staticnatcfgdefinition.md">StaticNatCfgDefinition</a></i>
    <a href="#vip" title="Vip">Vip</a>: <i>
      - <a href="vipdefinition.md">VipDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectedCfg

_Required_: No

_Type_: List of <a href="connectedcfgdefinition.md">ConnectedCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIpCfg

_Required_: No

_Type_: List of <a href="floatingipcfgdefinition.md">FloatingIpCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNatCfg

_Required_: No

_Type_: List of <a href="ipnatcfgdefinition.md">IpNatCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNatListCfg

_Required_: No

_Type_: List of <a href="ipnatlistcfgdefinition.md">IpNatListCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisCfg

_Required_: No

_Type_: List of <a href="isiscfgdefinition.md">IsisCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lw4o6Cfg

_Required_: No

_Type_: List of <a href="lw4o6cfgdefinition.md">Lw4o6CfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat64Cfg

_Required_: No

_Type_: List of <a href="nat64cfgdefinition.md">Nat64CfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatMapCfg

_Required_: No

_Type_: List of <a href="natmapcfgdefinition.md">NatMapCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfCfg

_Required_: No

_Type_: List of <a href="ospfcfgdefinition.md">OspfCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RipCfg

_Required_: No

_Type_: List of <a href="ripcfgdefinition.md">RipCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticCfg

_Required_: No

_Type_: List of <a href="staticcfgdefinition.md">StaticCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticNatCfg

_Required_: No

_Type_: List of <a href="staticnatcfgdefinition.md">StaticNatCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vip

_Required_: No

_Type_: List of <a href="vipdefinition.md">VipDefinition</a>

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

