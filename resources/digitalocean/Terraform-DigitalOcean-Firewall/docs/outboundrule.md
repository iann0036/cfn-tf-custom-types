# Terraform::DigitalOcean::Firewall OutboundRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationdropletids" title="DestinationDropletIds">DestinationDropletIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#destinationloadbalanceruids" title="DestinationLoadBalancerUids">DestinationLoadBalancerUids</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationtags" title="DestinationTags">DestinationTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#portrange" title="PortRange">PortRange</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
<a href="#destinationdropletids" title="DestinationDropletIds">DestinationDropletIds</a>: <i>
      - Double</i>
<a href="#destinationloadbalanceruids" title="DestinationLoadBalancerUids">DestinationLoadBalancerUids</a>: <i>
      - String</i>
<a href="#destinationtags" title="DestinationTags">DestinationTags</a>: <i>
      - String</i>
<a href="#portrange" title="PortRange">PortRange</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### DestinationAddresses

An array of strings containing the IPv4
addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the
outbound traffic will be allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationDropletIds

An array containing the IDs of
the Droplets to which the outbound traffic will be allowed.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationLoadBalancerUids

An array containing the IDs
of the Load Balancers to which the outbound traffic will be allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationTags

An array containing the names of Tags
corresponding to groups of Droplets to which the outbound traffic will
be allowed.
traffic.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

