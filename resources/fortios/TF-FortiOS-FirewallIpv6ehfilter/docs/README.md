# TF::FortiOS::FirewallIpv6ehfilter

Configure IPv6 extension header filter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallIpv6ehfilter",
    "Properties" : {
        "<a href="#auth" title="Auth">Auth</a>" : <i>String</i>,
        "<a href="#destopt" title="DestOpt">DestOpt</a>" : <i>String</i>,
        "<a href="#fragment" title="Fragment">Fragment</a>" : <i>String</i>,
        "<a href="#hdopttype" title="HdoptType">HdoptType</a>" : <i>Double</i>,
        "<a href="#hopopt" title="HopOpt">HopOpt</a>" : <i>String</i>,
        "<a href="#nonext" title="NoNext">NoNext</a>" : <i>String</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>String</i>,
        "<a href="#routingtype" title="RoutingType">RoutingType</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallIpv6ehfilter
Properties:
    <a href="#auth" title="Auth">Auth</a>: <i>String</i>
    <a href="#destopt" title="DestOpt">DestOpt</a>: <i>String</i>
    <a href="#fragment" title="Fragment">Fragment</a>: <i>String</i>
    <a href="#hdopttype" title="HdoptType">HdoptType</a>: <i>Double</i>
    <a href="#hopopt" title="HopOpt">HopOpt</a>: <i>String</i>
    <a href="#nonext" title="NoNext">NoNext</a>: <i>String</i>
    <a href="#routing" title="Routing">Routing</a>: <i>String</i>
    <a href="#routingtype" title="RoutingType">RoutingType</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Auth

Enable/disable blocking packets with the Authentication header (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestOpt

Enable/disable blocking packets with Destination Options headers (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fragment

Enable/disable blocking packets with the Fragment header (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HdoptType

Block specific Hop-by-Hop and/or Destination Option types (max. 7 types, each between 0 and 255, default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HopOpt

Enable/disable blocking packets with the Hop-by-Hop Options header (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoNext

Enable/disable blocking packets with the No Next header (default = disable) Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

Enable/disable blocking packets with Routing headers (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingType

Block specific Routing header types (max. 7 types, each between 0 and 255, default =  0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

