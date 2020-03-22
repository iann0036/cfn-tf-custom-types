# Terraform::OCI::CoreNetworkSecurityGroupSecurityRule

This resource provides the Network Security Group Security Rule resource in Oracle Cloud Infrastructure Core service.

Adds a security rule to the specified network security group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreNetworkSecurityGroupSecurityRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#stateless" title="Stateless">Stateless</a>" : <i>Boolean</i>,
        "<a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>" : <i>[ <a href="icmpoptions.md">IcmpOptions</a>, ... ]</i>,
        "<a href="#tcpoptions" title="TcpOptions">TcpOptions</a>" : <i>[ <a href="tcpoptions.md">TcpOptions</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#udpoptions" title="UdpOptions">UdpOptions</a>" : <i>[ <a href="udpoptions.md">UdpOptions</a>, ... ]</i>,
        "<a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>" : <i>[ <a href="destinationportrange.md">DestinationPortRange</a>, ... ]</i>,
        "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>[ <a href="sourceportrange.md">SourcePortRange</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreNetworkSecurityGroupSecurityRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
    <a href="#stateless" title="Stateless">Stateless</a>: <i>Boolean</i>
    <a href="#icmpoptions" title="IcmpOptions">IcmpOptions</a>: <i>
      - <a href="icmpoptions.md">IcmpOptions</a></i>
    <a href="#tcpoptions" title="TcpOptions">TcpOptions</a>: <i>
      - <a href="tcpoptions.md">TcpOptions</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#udpoptions" title="UdpOptions">UdpOptions</a>: <i>
      - <a href="udpoptions.md">UdpOptions</a></i>
    <a href="#destinationportrange" title="DestinationPortRange">DestinationPortRange</a>: <i>
      - <a href="destinationportrange.md">DestinationPortRange</a></i>
    <a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>
      - <a href="sourceportrange.md">SourcePortRange</a></i>
</pre>

## Properties

#### Description

An optional description of your choice for the rule. Avoid entering confidential information.
* `destination` - (Optional) Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Conceptually, this is the range of IP addresses that a packet originating from the instance can go to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

Type of destination for the rule. Required if `direction` = `EGRESS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.
* `icmp_options` - (Optional) Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code as defined in:
* [ICMP Parameters](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml)
* [ICMPv6 Parameters](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the network security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The transport protocol. Specify either `all` or an IPv4 protocol number as defined in [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). Options are supported only for ICMP ("1"), TCP ("6"), UDP ("17"), and ICMPv6 ("58").
* `source` - (Optional) Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Conceptually, this is the range of IP addresses that a packet coming into the instance can come from.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

Type of source for the rule. Required if `direction` = `INGRESS`.
* `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.
* `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a [Service](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Service/) (the rule is for traffic coming from a particular `Service` through a service gateway).
* `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a [NetworkSecurityGroup](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
* `stateless` - (Optional) A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.
* `tcp_options` - (Optional) Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.
* `destination_port_range` - (Optional) An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `source_port_range` - (Optional) An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `udp_options` - (Optional) Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.
* `destination_port_range` - (Optional) An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `source_port_range` - (Optional) An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateless

A stateless rule allows traffic in one direction. Remember to add a corresponding stateless rule in the other direction if you need to support bidirectional traffic. For example, if egress traffic allows TCP destination port 80, there should be an ingress rule to allow TCP source port 80. Defaults to false, which means the rule is stateful and a corresponding rule is not necessary for bidirectional traffic.
* `tcp_options` - (Optional) Optional and valid only for TCP. Use to specify particular destination ports for TCP rules. If you specify TCP as the protocol but omit this object, then all destination ports are allowed.
* `destination_port_range` - (Optional) An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `source_port_range` - (Optional) An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `udp_options` - (Optional) Optional and valid only for UDP. Use to specify particular destination ports for UDP rules. If you specify UDP as the protocol but omit this object, then all destination ports are allowed.
* `destination_port_range` - (Optional) An inclusive range of allowed destination ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.
* `source_port_range` - (Optional) An inclusive range of allowed source ports. Use the same number for the min and max to indicate a single port. Defaults to all ports if not specified.
* `max` - (Required) The maximum port number. Must not be lower than the minimum port number. To specify a single port number, set both the min and max to the same value.
* `min` - (Required) The minimum port number. Must not be greater than the maximum port number.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpOptions

_Required_: No

_Type_: List of <a href="icmpoptions.md">IcmpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpOptions

_Required_: No

_Type_: List of <a href="tcpoptions.md">TcpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpOptions

_Required_: No

_Type_: List of <a href="udpoptions.md">UdpOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPortRange

_Required_: No

_Type_: List of <a href="destinationportrange.md">DestinationPortRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

_Required_: No

_Type_: List of <a href="sourceportrange.md">SourcePortRange</a>

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

#### IsValid

Returns the <code>IsValid</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

