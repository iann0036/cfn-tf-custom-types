# TF::Packet::ReservedIpBlock

Provides a resource to create and manage blocks of reserved IP addresses in a project.

When a user provisions first device in a facility, Equinix Metal API automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
The IPv6 and private IPv4 blocks can't be created, only imported. With this resource, it's possible to create either public IPv4 blocks or global IPv4 blocks.

Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.

Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Packet::ReservedIpBlock",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#facility" title="Facility">Facility</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#quantity" title="Quantity">Quantity</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Packet::ReservedIpBlock
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#facility" title="Facility">Facility</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#quantity" title="Quantity">Quantity</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Description

Arbitrary description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facility

Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The packet project ID where to allocate the address block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quantity

The number of allocated /32 addresses, a power of 2.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Either "global_ipv4" or "public_ipv4", defaults to "public_ipv4" for backward compatibility.

_Required_: No

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

#### CidrNotation

Returns the <code>CidrNotation</code> value.

#### Gateway

Returns the <code>Gateway</code> value.

#### Global

Returns the <code>Global</code> value.

#### Id

Returns the <code>Id</code> value.

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

