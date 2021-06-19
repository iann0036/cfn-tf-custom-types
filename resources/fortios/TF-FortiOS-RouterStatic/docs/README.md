# TF::FortiOS::RouterStatic

Configure IPv4 static routing tables.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterStatic",
    "Properties" : {
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
        "<a href="#blackhole" title="Blackhole">Blackhole</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#device" title="Device">Device</a>" : <i>String</i>,
        "<a href="#distance" title="Distance">Distance</a>" : <i>Double</i>,
        "<a href="#dst" title="Dst">Dst</a>" : <i>String</i>,
        "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>String</i>,
        "<a href="#dynamicgateway" title="DynamicGateway">DynamicGateway</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#internetservice" title="InternetService">InternetService</a>" : <i>Double</i>,
        "<a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>" : <i>String</i>,
        "<a href="#linkmonitorexempt" title="LinkMonitorExempt">LinkMonitorExempt</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#sdwan" title="Sdwan">Sdwan</a>" : <i>String</i>,
        "<a href="#seqnum" title="SeqNum">SeqNum</a>" : <i>Double</i>,
        "<a href="#src" title="Src">Src</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#virtualwanlink" title="VirtualWanLink">VirtualWanLink</a>" : <i>String</i>,
        "<a href="#vrf" title="Vrf">Vrf</a>" : <i>Double</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterStatic
Properties:
    <a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
    <a href="#blackhole" title="Blackhole">Blackhole</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#device" title="Device">Device</a>: <i>String</i>
    <a href="#distance" title="Distance">Distance</a>: <i>Double</i>
    <a href="#dst" title="Dst">Dst</a>: <i>String</i>
    <a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>String</i>
    <a href="#dynamicgateway" title="DynamicGateway">DynamicGateway</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#internetservice" title="InternetService">InternetService</a>: <i>Double</i>
    <a href="#internetservicecustom" title="InternetServiceCustom">InternetServiceCustom</a>: <i>String</i>
    <a href="#linkmonitorexempt" title="LinkMonitorExempt">LinkMonitorExempt</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#sdwan" title="Sdwan">Sdwan</a>: <i>String</i>
    <a href="#seqnum" title="SeqNum">SeqNum</a>: <i>Double</i>
    <a href="#src" title="Src">Src</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#virtualwanlink" title="VirtualWanLink">VirtualWanLink</a>: <i>String</i>
    <a href="#vrf" title="Vrf">Vrf</a>: <i>Double</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Bfd

Enable/disable Bidirectional Forwarding Detection (BFD). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blackhole

Enable/disable black hole. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Device

Gateway out interface or tunnel.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

Administrative distance (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dst

Destination IP and mask for this route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

Name of firewall address or address group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicGateway

Enable use of dynamic gateway retrieved from a DHCP or PPP server. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Gateway IP for this route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetService

Application ID in the Internet service database.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetServiceCustom

Application name in the Internet service custom database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkMonitorExempt

Enable/disable withdrawing this route when link monitor or health check is down. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Administrative priority (0 - 4294967295).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdwan

Enable/disable egress through SD-WAN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeqNum

Sequence number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Src

Source prefix for this route.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this static route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualWanLink

Enable/disable egress through the virtual-wan-link. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrf

Virtual Routing Forwarding ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Administrative weight (0 - 255).

_Required_: No

_Type_: Double

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

