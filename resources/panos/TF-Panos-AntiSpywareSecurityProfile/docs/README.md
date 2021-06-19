# TF::Panos::AntiSpywareSecurityProfile

Manages anti-spyware security profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::AntiSpywareSecurityProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#packetcapture" title="PacketCapture">PacketCapture</a>" : <i>String</i>,
        "<a href="#sinkholeipv4address" title="SinkholeIpv4Address">SinkholeIpv4Address</a>" : <i>String</i>,
        "<a href="#sinkholeipv6address" title="SinkholeIpv6Address">SinkholeIpv6Address</a>" : <i>String</i>,
        "<a href="#threatexceptions" title="ThreatExceptions">ThreatExceptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#botnetlist" title="BotnetList">BotnetList</a>" : <i>[ <a href="botnetlistdefinition.md">BotnetListDefinition</a>, ... ]</i>,
        "<a href="#dnscategory" title="DnsCategory">DnsCategory</a>" : <i>[ <a href="dnscategorydefinition.md">DnsCategoryDefinition</a>, ... ]</i>,
        "<a href="#exception" title="Exception">Exception</a>" : <i>[ <a href="exceptiondefinition.md">ExceptionDefinition</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#whitelist" title="WhiteList">WhiteList</a>" : <i>[ <a href="whitelistdefinition.md">WhiteListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::AntiSpywareSecurityProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#packetcapture" title="PacketCapture">PacketCapture</a>: <i>String</i>
    <a href="#sinkholeipv4address" title="SinkholeIpv4Address">SinkholeIpv4Address</a>: <i>String</i>
    <a href="#sinkholeipv6address" title="SinkholeIpv6Address">SinkholeIpv6Address</a>: <i>String</i>
    <a href="#threatexceptions" title="ThreatExceptions">ThreatExceptions</a>: <i>
      - String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#botnetlist" title="BotnetList">BotnetList</a>: <i>
      - <a href="botnetlistdefinition.md">BotnetListDefinition</a></i>
    <a href="#dnscategory" title="DnsCategory">DnsCategory</a>: <i>
      - <a href="dnscategorydefinition.md">DnsCategoryDefinition</a></i>
    <a href="#exception" title="Exception">Exception</a>: <i>
      - <a href="exceptiondefinition.md">ExceptionDefinition</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#whitelist" title="WhiteList">WhiteList</a>: <i>
      - <a href="whitelistdefinition.md">WhiteListDefinition</a></i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group location (default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketCapture

Packet capture setting.  Valid values
are `disable`, `single-packet`, or `extended-capture`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinkholeIpv4Address

IPv4 sinkhole address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinkholeIpv6Address

IPv6 sinkhole address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatExceptions

List of threat exceptions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys location (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BotnetList

_Required_: No

_Type_: List of <a href="botnetlistdefinition.md">BotnetListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsCategory

_Required_: No

_Type_: List of <a href="dnscategorydefinition.md">DnsCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exception

_Required_: No

_Type_: List of <a href="exceptiondefinition.md">ExceptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteList

_Required_: No

_Type_: List of <a href="whitelistdefinition.md">WhiteListDefinition</a>

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

