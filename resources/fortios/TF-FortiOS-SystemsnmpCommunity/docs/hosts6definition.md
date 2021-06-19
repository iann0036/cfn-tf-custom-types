# TF::FortiOS::SystemsnmpCommunity Hosts6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hadirect" title="HaDirect">HaDirect</a>" : <i>String</i>,
    "<a href="#hosttype" title="HostType">HostType</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>String</i>,
    "<a href="#sourceipv6" title="SourceIpv6">SourceIpv6</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hadirect" title="HaDirect">HaDirect</a>: <i>String</i>
<a href="#hosttype" title="HostType">HostType</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ipv6" title="Ipv6">Ipv6</a>: <i>String</i>
<a href="#sourceipv6" title="SourceIpv6">SourceIpv6</a>: <i>String</i>
</pre>

## Properties

#### HaDirect

Enable/disable direct management of HA cluster members. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostType

Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. Valid values: `any`, `query`, `trap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Host6 entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

SNMP manager IPv6 address prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIpv6

Source IPv6 address for SNMP traps.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

