# TF::Packet::Device IpAddressDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>Double</i>,
    "<a href="#reservationids" title="ReservationIds">ReservationIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cidr" title="Cidr">Cidr</a>: <i>Double</i>
<a href="#reservationids" title="ReservationIds">ReservationIds</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Cidr

CIDR suffix for IP address block to be assigned, i.e. amount of addresses.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservationIds

String of UUID of [IP block reservations](reserved_ip_block.md) from which the public IPv4 address should be taken.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

One of [`private_ipv4`, `public_ipv4`, `public_ipv6`].

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

