# TF::Thunder::InterfaceVeIp

`thunder_interface_ve_ip` Provides details about thunder interface ve ip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::InterfaceVeIp",
    "Properties" : {
        "<a href="#allowpromiscuousvip" title="AllowPromiscuousVip">AllowPromiscuousVip</a>" : <i>Double</i>,
        "<a href="#client" title="Client">Client</a>" : <i>Double</i>,
        "<a href="#dhcp" title="Dhcp">Dhcp</a>" : <i>Double</i>,
        "<a href="#generatemembershipquery" title="GenerateMembershipQuery">GenerateMembershipQuery</a>" : <i>Double</i>,
        "<a href="#ifnum" title="Ifnum">Ifnum</a>" : <i>Double</i>,
        "<a href="#inside" title="Inside">Inside</a>" : <i>Double</i>,
        "<a href="#maxresptime" title="MaxRespTime">MaxRespTime</a>" : <i>Double</i>,
        "<a href="#outside" title="Outside">Outside</a>" : <i>Double</i>,
        "<a href="#queryinterval" title="QueryInterval">QueryInterval</a>" : <i>Double</i>,
        "<a href="#server" title="Server">Server</a>" : <i>Double</i>,
        "<a href="#slbpartitionredirect" title="SlbPartitionRedirect">SlbPartitionRedirect</a>" : <i>Double</i>,
        "<a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#addresslist" title="AddressList">AddressList</a>" : <i>[ <a href="addresslistdefinition.md">AddressListDefinition</a>, ... ]</i>,
        "<a href="#helperaddresslist" title="HelperAddressList">HelperAddressList</a>" : <i>[ <a href="helperaddresslistdefinition.md">HelperAddressListDefinition</a>, ... ]</i>,
        "<a href="#ospf" title="Ospf">Ospf</a>" : <i>[ <a href="ospfdefinition.md">OspfDefinition</a>, ... ]</i>,
        "<a href="#rip" title="Rip">Rip</a>" : <i>[ <a href="ripdefinition.md">RipDefinition</a>, ... ]</i>,
        "<a href="#router" title="Router">Router</a>" : <i>[ <a href="routerdefinition.md">RouterDefinition</a>, ... ]</i>,
        "<a href="#statefulfirewall" title="StatefulFirewall">StatefulFirewall</a>" : <i>[ <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::InterfaceVeIp
Properties:
    <a href="#allowpromiscuousvip" title="AllowPromiscuousVip">AllowPromiscuousVip</a>: <i>Double</i>
    <a href="#client" title="Client">Client</a>: <i>Double</i>
    <a href="#dhcp" title="Dhcp">Dhcp</a>: <i>Double</i>
    <a href="#generatemembershipquery" title="GenerateMembershipQuery">GenerateMembershipQuery</a>: <i>Double</i>
    <a href="#ifnum" title="Ifnum">Ifnum</a>: <i>Double</i>
    <a href="#inside" title="Inside">Inside</a>: <i>Double</i>
    <a href="#maxresptime" title="MaxRespTime">MaxRespTime</a>: <i>Double</i>
    <a href="#outside" title="Outside">Outside</a>: <i>Double</i>
    <a href="#queryinterval" title="QueryInterval">QueryInterval</a>: <i>Double</i>
    <a href="#server" title="Server">Server</a>: <i>Double</i>
    <a href="#slbpartitionredirect" title="SlbPartitionRedirect">SlbPartitionRedirect</a>: <i>Double</i>
    <a href="#ttlignore" title="TtlIgnore">TtlIgnore</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#addresslist" title="AddressList">AddressList</a>: <i>
      - <a href="addresslistdefinition.md">AddressListDefinition</a></i>
    <a href="#helperaddresslist" title="HelperAddressList">HelperAddressList</a>: <i>
      - <a href="helperaddresslistdefinition.md">HelperAddressListDefinition</a></i>
    <a href="#ospf" title="Ospf">Ospf</a>: <i>
      - <a href="ospfdefinition.md">OspfDefinition</a></i>
    <a href="#rip" title="Rip">Rip</a>: <i>
      - <a href="ripdefinition.md">RipDefinition</a></i>
    <a href="#router" title="Router">Router</a>: <i>
      - <a href="routerdefinition.md">RouterDefinition</a></i>
    <a href="#statefulfirewall" title="StatefulFirewall">StatefulFirewall</a>: <i>
      - <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a></i>
</pre>

## Properties

#### AllowPromiscuousVip

Allow traffic to be associated with promiscuous VIP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Client

Client facing interface for IPv4/v6 traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dhcp

Use DHCP to configure IP address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GenerateMembershipQuery

Enable Membership Query.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ifnum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Inside

Inside (private) interface for stateful firewall.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRespTime

Maximum Response Time (Max Response Time (Default is 100)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Outside

Outside (public) interface for stateful firewall.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryInterval

1 - 255 (Default is 125).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Server facing interface for IPv4/v6 traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbPartitionRedirect

Redirect SLB traffic across partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TtlIgnore

Ignore TTL decrement for a received packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressList

_Required_: No

_Type_: List of <a href="addresslistdefinition.md">AddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelperAddressList

_Required_: No

_Type_: List of <a href="helperaddresslistdefinition.md">HelperAddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf

_Required_: No

_Type_: List of <a href="ospfdefinition.md">OspfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rip

_Required_: No

_Type_: List of <a href="ripdefinition.md">RipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Router

_Required_: No

_Type_: List of <a href="routerdefinition.md">RouterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulFirewall

_Required_: No

_Type_: List of <a href="statefulfirewalldefinition.md">StatefulFirewallDefinition</a>

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

