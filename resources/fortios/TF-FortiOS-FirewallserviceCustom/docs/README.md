# TF::FortiOS::FirewallserviceCustom

Configure custom services.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallserviceCustom",
    "Properties" : {
        "<a href="#appservicetype" title="AppServiceType">AppServiceType</a>" : <i>String</i>,
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#checkresetrange" title="CheckResetRange">CheckResetRange</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#helper" title="Helper">Helper</a>" : <i>String</i>,
        "<a href="#icmpcode" title="Icmpcode">Icmpcode</a>" : <i>Double</i>,
        "<a href="#icmptype" title="Icmptype">Icmptype</a>" : <i>Double</i>,
        "<a href="#iprange" title="Iprange">Iprange</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>" : <i>Double</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#sctpportrange" title="SctpPortrange">SctpPortrange</a>" : <i>String</i>,
        "<a href="#sessionttl" title="SessionTtl">SessionTtl</a>" : <i>Double</i>,
        "<a href="#tcphalfclosetimer" title="TcpHalfcloseTimer">TcpHalfcloseTimer</a>" : <i>Double</i>,
        "<a href="#tcphalfopentimer" title="TcpHalfopenTimer">TcpHalfopenTimer</a>" : <i>Double</i>,
        "<a href="#tcpportrange" title="TcpPortrange">TcpPortrange</a>" : <i>String</i>,
        "<a href="#tcptimewaittimer" title="TcpTimewaitTimer">TcpTimewaitTimer</a>" : <i>Double</i>,
        "<a href="#udpidletimer" title="UdpIdleTimer">UdpIdleTimer</a>" : <i>Double</i>,
        "<a href="#udpportrange" title="UdpPortrange">UdpPortrange</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#appcategory" title="AppCategory">AppCategory</a>" : <i>[ <a href="appcategorydefinition.md">AppCategoryDefinition</a>, ... ]</i>,
        "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallserviceCustom
Properties:
    <a href="#appservicetype" title="AppServiceType">AppServiceType</a>: <i>String</i>
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#checkresetrange" title="CheckResetRange">CheckResetRange</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#helper" title="Helper">Helper</a>: <i>String</i>
    <a href="#icmpcode" title="Icmpcode">Icmpcode</a>: <i>Double</i>
    <a href="#icmptype" title="Icmptype">Icmptype</a>: <i>Double</i>
    <a href="#iprange" title="Iprange">Iprange</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>: <i>Double</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#sctpportrange" title="SctpPortrange">SctpPortrange</a>: <i>String</i>
    <a href="#sessionttl" title="SessionTtl">SessionTtl</a>: <i>Double</i>
    <a href="#tcphalfclosetimer" title="TcpHalfcloseTimer">TcpHalfcloseTimer</a>: <i>Double</i>
    <a href="#tcphalfopentimer" title="TcpHalfopenTimer">TcpHalfopenTimer</a>: <i>Double</i>
    <a href="#tcpportrange" title="TcpPortrange">TcpPortrange</a>: <i>String</i>
    <a href="#tcptimewaittimer" title="TcpTimewaitTimer">TcpTimewaitTimer</a>: <i>Double</i>
    <a href="#udpidletimer" title="UdpIdleTimer">UdpIdleTimer</a>: <i>Double</i>
    <a href="#udpportrange" title="UdpPortrange">UdpPortrange</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#appcategory" title="AppCategory">AppCategory</a>: <i>
      - <a href="appcategorydefinition.md">AppCategoryDefinition</a></i>
    <a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
</pre>

## Properties

#### AppServiceType

Application service type. Valid values: `disable`, `app-id`, `app-category`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

Service category.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckResetRange

Configure the type of ICMP error message verification. Valid values: `disable`, `strict`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of icon on the GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

Fully qualified domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Helper

Helper name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpcode

ICMP code.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmptype

ICMP type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iprange

Start and end of the IP range associated with service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Custom service name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol type based on IANA numbers. Valid values: `TCP/UDP/SCTP`, `ICMP`, `ICMP6`, `IP`, `HTTP`, `FTP`, `CONNECT`, `SOCKS-TCP`, `SOCKS-UDP`, `ALL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolNumber

IP protocol number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Enable/disable web proxy service. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SctpPortrange

Multiple SCTP port ranges.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTtl

Session TTL (300 - 604800, 0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpHalfcloseTimer

Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpHalfopenTimer

Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpPortrange

Multiple TCP port ranges.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpTimewaitTimer

Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpIdleTimer

UDP half close timeout (0 - 86400 sec, 0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpPortrange

Multiple UDP port ranges.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Enable/disable the visibility of the service on the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppCategory

_Required_: No

_Type_: List of <a href="appcategorydefinition.md">AppCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

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

