# TF::Thunder::InterfaceVe

`thunder_interface_ve` Provides details about thunder interface ve

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::InterfaceVe",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#ifnum" title="Ifnum">Ifnum</a>" : <i>Double</i>,
        "<a href="#l3vlanfwddisable" title="L3VlanFwdDisable">L3VlanFwdDisable</a>" : <i>Double</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#trapsource" title="TrapSource">TrapSource</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#accesslist" title="AccessList">AccessList</a>" : <i>[ <a href="accesslistdefinition.md">AccessListDefinition</a>, ... ]</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>[ <a href="bfddefinition.md">BfdDefinition</a>, ... ]</i>,
        "<a href="#ddos" title="Ddos">Ddos</a>" : <i>[ <a href="ddosdefinition.md">DdosDefinition</a>, ... ]</i>,
        "<a href="#icmpratelimit" title="IcmpRateLimit">IcmpRateLimit</a>" : <i>[ <a href="icmpratelimitdefinition.md">IcmpRateLimitDefinition</a>, ... ]</i>,
        "<a href="#icmpv6ratelimit" title="Icmpv6RateLimit">Icmpv6RateLimit</a>" : <i>[ <a href="icmpv6ratelimitdefinition.md">Icmpv6RateLimitDefinition</a>, ... ]</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>,
        "<a href="#isis" title="Isis">Isis</a>" : <i>[ <a href="isisdefinition.md">IsisDefinition</a>, ... ]</i>,
        "<a href="#lw4o6" title="Lw4o6">Lw4o6</a>" : <i>[ <a href="lw4o6definition.md">Lw4o6Definition</a>, ... ]</i>,
        "<a href="#map" title="Map">Map</a>" : <i>[ <a href="mapdefinition.md">MapDefinition</a>, ... ]</i>,
        "<a href="#nptv6" title="Nptv6">Nptv6</a>" : <i>[ <a href="nptv6definition.md">Nptv6Definition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::InterfaceVe
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#ifnum" title="Ifnum">Ifnum</a>: <i>Double</i>
    <a href="#l3vlanfwddisable" title="L3VlanFwdDisable">L3VlanFwdDisable</a>: <i>Double</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#trapsource" title="TrapSource">TrapSource</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#accesslist" title="AccessList">AccessList</a>: <i>
      - <a href="accesslistdefinition.md">AccessListDefinition</a></i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>
      - <a href="bfddefinition.md">BfdDefinition</a></i>
    <a href="#ddos" title="Ddos">Ddos</a>: <i>
      - <a href="ddosdefinition.md">DdosDefinition</a></i>
    <a href="#icmpratelimit" title="IcmpRateLimit">IcmpRateLimit</a>: <i>
      - <a href="icmpratelimitdefinition.md">IcmpRateLimitDefinition</a></i>
    <a href="#icmpv6ratelimit" title="Icmpv6RateLimit">Icmpv6RateLimit</a>: <i>
      - <a href="icmpv6ratelimitdefinition.md">Icmpv6RateLimitDefinition</a></i>
    <a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
    <a href="#isis" title="Isis">Isis</a>: <i>
      - <a href="isisdefinition.md">IsisDefinition</a></i>
    <a href="#lw4o6" title="Lw4o6">Lw4o6</a>: <i>
      - <a href="lw4o6definition.md">Lw4o6Definition</a></i>
    <a href="#map" title="Map">Map</a>: <i>
      - <a href="mapdefinition.md">MapDefinition</a></i>
    <a href="#nptv6" title="Nptv6">Nptv6</a>: <i>
      - <a href="nptv6definition.md">Nptv6Definition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### Action

‘enable’: Enable Router Advertisements on this interface; ‘disable’: Disable Router Advertisements on this interface;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ifnum

Virtual ethernet interface number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3VlanFwdDisable

Disable L3 forwarding between VLANs for incoming packets on this interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

OSPF interface MTU (MTU size).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrapSource

The trap source.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessList

_Required_: No

_Type_: List of <a href="accesslistdefinition.md">AccessListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

_Required_: No

_Type_: List of <a href="bfddefinition.md">BfdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ddos

_Required_: No

_Type_: List of <a href="ddosdefinition.md">DdosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpRateLimit

_Required_: No

_Type_: List of <a href="icmpratelimitdefinition.md">IcmpRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6RateLimit

_Required_: No

_Type_: List of <a href="icmpv6ratelimitdefinition.md">Icmpv6RateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isis

_Required_: No

_Type_: List of <a href="isisdefinition.md">IsisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lw4o6

_Required_: No

_Type_: List of <a href="lw4o6definition.md">Lw4o6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Map

_Required_: No

_Type_: List of <a href="mapdefinition.md">MapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nptv6

_Required_: No

_Type_: List of <a href="nptv6definition.md">Nptv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

