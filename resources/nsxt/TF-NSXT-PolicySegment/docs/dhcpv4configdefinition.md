# TF::NSXT::PolicySegment DhcpV4ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
    "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
    "<a href="#serveraddress" title="ServerAddress">ServerAddress</a>" : <i>String</i>,
    "<a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>" : <i>[ <a href="dhcpgenericoptiondefinition.md">DhcpGenericOptionDefinition</a>, ... ]</i>,
    "<a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>" : <i>[ <a href="dhcpoption121definition.md">DhcpOption121Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
<a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
<a href="#serveraddress" title="ServerAddress">ServerAddress</a>: <i>String</i>
<a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>: <i>
      - <a href="dhcpgenericoptiondefinition.md">DhcpGenericOptionDefinition</a></i>
<a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>: <i>
      - <a href="dhcpoption121definition.md">DhcpOption121Definition</a></i>
</pre>

## Properties

#### DnsServers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpGenericOption

_Required_: No

_Type_: List of <a href="dhcpgenericoptiondefinition.md">DhcpGenericOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption121

_Required_: No

_Type_: List of <a href="dhcpoption121definition.md">DhcpOption121Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

