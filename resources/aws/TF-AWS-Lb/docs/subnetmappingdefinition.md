# TF::AWS::Lb SubnetMappingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationid" title="AllocationId">AllocationId</a>" : <i>String</i>,
    "<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>" : <i>String</i>,
    "<a href="#privateipv4address" title="PrivateIpv4Address">PrivateIpv4Address</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allocationid" title="AllocationId">AllocationId</a>: <i>String</i>
<a href="#ipv6address" title="Ipv6Address">Ipv6Address</a>: <i>String</i>
<a href="#privateipv4address" title="PrivateIpv4Address">PrivateIpv4Address</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### AllocationId

The allocation ID of the Elastic IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6Address

An ipv6 address within the subnet to assign to the internet-facing load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpv4Address

A private ipv4 address within the subnet to assign to the internal-facing load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The id of the subnet of which to attach to the load balancer. You can specify only one subnet per Availability Zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

