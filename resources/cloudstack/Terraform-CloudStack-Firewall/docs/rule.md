# Terraform::CloudStack::Firewall Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidrlist" title="CidrList">CidrList</a>" : <i>[ String, ... ]</i>,
    "<a href="#icmpcode" title="IcmpCode">IcmpCode</a>" : <i>Double</i>,
    "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>Double</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cidrlist" title="CidrList">CidrList</a>: <i>
      - String</i>
<a href="#icmpcode" title="IcmpCode">IcmpCode</a>: <i>Double</i>
<a href="#icmptype" title="IcmpType">IcmpType</a>: <i>Double</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### CidrList

A CIDR list to allow access to the given ports.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpCode

The ICMP code to allow. This can only be specified if
the protocol is ICMP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

The ICMP type to allow. This can only be specified if
the protocol is ICMP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

List of ports and/or port ranges to allow. This can only
be specified if the protocol is TCP or UDP.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The name of the protocol to allow. Valid options are:
`tcp`, `udp` and `icmp`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

