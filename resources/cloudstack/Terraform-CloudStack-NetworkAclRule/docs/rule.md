# Terraform::CloudStack::NetworkAclRule Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>[ String, ... ]</i>,
    "<a href="#icmpcode" title="IcmpCode">IcmpCode</a>" : <i>Double</i>,
    "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#traffictype" title="TrafficType">TrafficType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#cidrlist" title="CidrList">CidrList</a>: <i>
      - String</i>
<a href="#icmpcode" title="IcmpCode">IcmpCode</a>: <i>Double</i>
<a href="#icmptype" title="IcmpType">IcmpType</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#traffictype" title="TrafficType">TrafficType</a>: <i>String</i>
</pre>

## Properties

#### Action

The action for the rule. Valid options are: `allow` and
`deny` (defaults allow).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrList

A CIDR list to allow access to the given ports.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpCode

The ICMP code to allow, or `-1` to allow `any`. This
can only be specified if the protocol is ICMP. (defaults 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

The ICMP type to allow, or `-1` to allow `any`. This
can only be specified if the protocol is ICMP. (defaults 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

List of ports and/or port ranges to allow. This can only
be specified if the protocol is TCP, UDP, ALL or a valid protocol number.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The name of the protocol to allow. Valid options are:
`tcp`, `udp`, `icmp`, `all` or a valid protocol number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficType

The traffic type for the rule. Valid options are:
`ingress` or `egress` (defaults ingress).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

