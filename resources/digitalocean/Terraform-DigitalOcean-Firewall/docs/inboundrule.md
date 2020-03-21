# Terraform::DigitalOcean::Firewall InboundRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcedropletids" title="SourceDropletIds">SourceDropletIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#sourceloadbalanceruids" title="SourceLoadBalancerUids">SourceLoadBalancerUids</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcetags" title="SourceTags">SourceTags</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#portrange" title="PortRange">PortRange</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourcedropletids" title="SourceDropletIds">SourceDropletIds</a>: <i>
      - Double</i>
<a href="#sourceloadbalanceruids" title="SourceLoadBalancerUids">SourceLoadBalancerUids</a>: <i>
      - String</i>
<a href="#sourcetags" title="SourceTags">SourceTags</a>: <i>
      - String</i>
</pre>

## Properties

#### PortRange

The ports on which traffic will be allowed
specified as a string containing a single port, a range (e.g. "8000-9000"),
or "1-65535" to open all ports for a protocol. Required for when protocol is
`tcp` or `udp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The type of traffic to be allowed.
This may be one of "tcp", "udp", or "icmp".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

An array of strings containing the IPv4
addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs from which the
inbound traffic will be accepted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDropletIds

An array containing the IDs of
the Droplets from which the inbound traffic will be accepted.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceLoadBalancerUids

An array containing the IDs
of the Load Balancers from which the inbound traffic will be accepted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceTags

An array containing the names of Tags
corresponding to groups of Droplets from which the inbound traffic
will be accepted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

