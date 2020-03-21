# Terraform::OpenTelekomCloud::NetworkingPortV2 FixedIp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### IpAddress

IP address desired in the subnet for this port. If
you don't specify `ip_address`, an available IP address from the specified
subnet will be allocated to this port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet in which to allocate IP address for
this port.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

