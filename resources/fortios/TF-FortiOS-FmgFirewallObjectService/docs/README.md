# TF::FortiOS::FmgFirewallObjectService

This resource supports Create/Read/Update/Delete firewall object service for FortiManager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgFirewallObjectService",
    "Properties" : {
        "<a href="#adom" title="Adom">Adom</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#icmpcode" title="IcmpCode">IcmpCode</a>" : <i>Double</i>,
        "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>Double</i>,
        "<a href="#iprange" title="Iprange">Iprange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>" : <i>Double</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#sctpportrange" title="SctpPortrange">SctpPortrange</a>" : <i>[ String, ... ]</i>,
        "<a href="#tcpportrange" title="TcpPortrange">TcpPortrange</a>" : <i>[ String, ... ]</i>,
        "<a href="#udpportrange" title="UdpPortrange">UdpPortrange</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgFirewallObjectService
Properties:
    <a href="#adom" title="Adom">Adom</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#icmpcode" title="IcmpCode">IcmpCode</a>: <i>Double</i>
    <a href="#icmptype" title="IcmpType">IcmpType</a>: <i>Double</i>
    <a href="#iprange" title="Iprange">Iprange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>: <i>Double</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#sctpportrange" title="SctpPortrange">SctpPortrange</a>: <i>
      - String</i>
    <a href="#tcpportrange" title="TcpPortrange">TcpPortrange</a>: <i>
      - String</i>
    <a href="#udpportrange" title="UdpPortrange">UdpPortrange</a>: <i>
      - String</i>
</pre>

## Properties

#### Adom

ADOM name. default is 'root'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Service category. Enum: ["", "File Access", "Authentication", "Email", "General", "Network Services", "Remote Access", "Tunneling", "VoIP, Messaging & Other Applications", "Web Access", "Web Proxy"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

Fully qualified domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpCode

ICMP Code.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

ICMP Type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iprange

Start and end of the IP range associated with service. Ip or Ip range(eg: 1.1.1.1-1.1.1.100).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Custom service name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol type. Enum: ["TCP/UDP/SCTP", "ICMP", "ICMP6", "IP"].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolNumber

IP protocol number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpPortrange

SCTP port ranges. e.g: ["dst-port-range:src-port-range"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpPortrange

TCP port ranges. e.g: ["dst-port-range:src-port-range"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpPortrange

UDP port ranges. e.g: ["dst-port-range:src-port-range"].

_Required_: No

_Type_: List of String

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

