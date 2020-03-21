# Terraform::Packet::IpAttachment

Provides a resource to attach elastic IP subnets to devices.

To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
one of your reserved blocks in the same project and facility as the target device.

For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31' and 147.229.10.154/31; or 4 subnets
with mask prefix length 32. More about the elastic IP subnets is [here](https://www.packet.com/developers/docs/network/basic/elastic-ips/).

Device and reserved block must be in the same facility.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::IpAttachment",
    "Properties" : {
        "<a href="#cidrnotation" title="CidrNotation">CidrNotation</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::IpAttachment
Properties:
    <a href="#cidrnotation" title="CidrNotation">CidrNotation</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
</pre>

## Properties

#### CidrNotation

CIDR notation of subnet from block reserved in the same
project and facility as the device.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

ID of device to which to assign the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Address

Returns the <code>Address</code> value.

#### AddressFamily

Returns the <code>AddressFamily</code> value.

#### Cidr

Returns the <code>Cidr</code> value.

#### Gateway

Returns the <code>Gateway</code> value.

#### Global

Returns the <code>Global</code> value.

#### Manageable

Returns the <code>Manageable</code> value.

#### Management

Returns the <code>Management</code> value.

#### Netmask

Returns the <code>Netmask</code> value.

#### Network

Returns the <code>Network</code> value.

#### Public

Returns the <code>Public</code> value.

