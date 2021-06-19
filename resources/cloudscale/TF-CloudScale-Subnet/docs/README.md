# TF::CloudScale::Subnet

Provides a cloudscale.ch Subnet resource. This can be used to create, modify, and delete subnets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CloudScale::Subnet",
    "Properties" : {
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#dnsservers" title="DnsServers">DnsServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#gatewayaddress" title="GatewayAddress">GatewayAddress</a>" : <i>String</i>,
        "<a href="#networkuuid" title="NetworkUuid">NetworkUuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CloudScale::Subnet
Properties:
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#dnsservers" title="DnsServers">DnsServers</a>: <i>
      - String</i>
    <a href="#gatewayaddress" title="GatewayAddress">GatewayAddress</a>: <i>String</i>
    <a href="#networkuuid" title="NetworkUuid">NetworkUuid</a>: <i>String</i>
</pre>

## Properties

#### Cidr

The address range in CIDR notation. Must be at least /24.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsServers

A list of DNS resolver IP addresses, that act as DNS servers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayAddress

The gateway address of the subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkUuid

The network of the subnet.

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

#### Href

Returns the <code>Href</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetworkHref

Returns the <code>NetworkHref</code> value.

#### NetworkName

Returns the <code>NetworkName</code> value.

