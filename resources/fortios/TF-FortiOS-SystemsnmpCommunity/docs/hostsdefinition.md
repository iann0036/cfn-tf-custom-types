# TF::FortiOS::SystemsnmpCommunity HostsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hadirect" title="HaDirect">HaDirect</a>" : <i>String</i>,
    "<a href="#hosttype" title="HostType">HostType</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hadirect" title="HaDirect">HaDirect</a>: <i>String</i>
<a href="#hosttype" title="HostType">HostType</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
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

Host entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IPv4 address of the SNMP manager (host).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IPv4 address for SNMP traps.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

