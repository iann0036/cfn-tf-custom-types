# TF::FortiOS::Systemdhcp6Server

Configure DHCPv6 servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Systemdhcp6Server",
    "Properties" : {
        "<a href="#dnssearchlist" title="DnsSearchList">DnsSearchList</a>" : <i>String</i>,
        "<a href="#dnsserver1" title="DnsServer1">DnsServer1</a>" : <i>String</i>,
        "<a href="#dnsserver2" title="DnsServer2">DnsServer2</a>" : <i>String</i>,
        "<a href="#dnsserver3" title="DnsServer3">DnsServer3</a>" : <i>String</i>,
        "<a href="#dnsserver4" title="DnsServer4">DnsServer4</a>" : <i>String</i>,
        "<a href="#dnsservice" title="DnsService">DnsService</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fosid" title="Fosid">Fosid</a>" : <i>Double</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#ipmode" title="IpMode">IpMode</a>" : <i>String</i>,
        "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
        "<a href="#option1" title="Option1">Option1</a>" : <i>String</i>,
        "<a href="#option2" title="Option2">Option2</a>" : <i>String</i>,
        "<a href="#option3" title="Option3">Option3</a>" : <i>String</i>,
        "<a href="#prefixmode" title="PrefixMode">PrefixMode</a>" : <i>String</i>,
        "<a href="#rapidcommit" title="RapidCommit">RapidCommit</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#upstreaminterface" title="UpstreamInterface">UpstreamInterface</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#iprange" title="IpRange">IpRange</a>" : <i>[ <a href="iprangedefinition.md">IpRangeDefinition</a>, ... ]</i>,
        "<a href="#prefixrange" title="PrefixRange">PrefixRange</a>" : <i>[ <a href="prefixrangedefinition.md">PrefixRangeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Systemdhcp6Server
Properties:
    <a href="#dnssearchlist" title="DnsSearchList">DnsSearchList</a>: <i>String</i>
    <a href="#dnsserver1" title="DnsServer1">DnsServer1</a>: <i>String</i>
    <a href="#dnsserver2" title="DnsServer2">DnsServer2</a>: <i>String</i>
    <a href="#dnsserver3" title="DnsServer3">DnsServer3</a>: <i>String</i>
    <a href="#dnsserver4" title="DnsServer4">DnsServer4</a>: <i>String</i>
    <a href="#dnsservice" title="DnsService">DnsService</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fosid" title="Fosid">Fosid</a>: <i>Double</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#ipmode" title="IpMode">IpMode</a>: <i>String</i>
    <a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
    <a href="#option1" title="Option1">Option1</a>: <i>String</i>
    <a href="#option2" title="Option2">Option2</a>: <i>String</i>
    <a href="#option3" title="Option3">Option3</a>: <i>String</i>
    <a href="#prefixmode" title="PrefixMode">PrefixMode</a>: <i>String</i>
    <a href="#rapidcommit" title="RapidCommit">RapidCommit</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#upstreaminterface" title="UpstreamInterface">UpstreamInterface</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#iprange" title="IpRange">IpRange</a>: <i>
      - <a href="iprangedefinition.md">IpRangeDefinition</a></i>
    <a href="#prefixrange" title="PrefixRange">PrefixRange</a>: <i>
      - <a href="prefixrangedefinition.md">PrefixRangeDefinition</a></i>
</pre>

## Properties

#### DnsSearchList

DNS search list options. Valid values: `delegated`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer1

DNS server 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer2

DNS server 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer3

DNS server 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServer4

DNS server 4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsService

Options for assigning DNS servers to DHCPv6 clients. Valid values: `delegated`, `default`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Domain name suffix for the IP addresses that the DHCP server assigns to clients.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fosid

ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

DHCP server can assign IP configurations to clients connected to this interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMode

Method used to assign client IP. Valid values: `range`, `delegated`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

Lease time in seconds, 0 means unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option1

Option 1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option2

Option 2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Option3

Option 3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixMode

Assigning a prefix from a DHCPv6 client or RA. Valid values: `dhcp6`, `ra`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RapidCommit

Enable/disable allow/disallow rapid commit. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this DHCPv6 configuration. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Subnet or subnet-id if the IP mode is delegated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpstreamInterface

Interface name from where delegated information is provided.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

_Required_: No

_Type_: List of <a href="iprangedefinition.md">IpRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixRange

_Required_: No

_Type_: List of <a href="prefixrangedefinition.md">PrefixRangeDefinition</a>

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

