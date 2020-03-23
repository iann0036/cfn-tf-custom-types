# Terraform::AWS::DxHostedPrivateVirtualInterface

Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DxHostedPrivateVirtualInterface",
    "Properties" : {
        "<a href="#addressfamily" title="AddressFamily">AddressFamily</a>" : <i>String</i>,
        "<a href="#amazonaddress" title="AmazonAddress">AmazonAddress</a>" : <i>String</i>,
        "<a href="#bgpasn" title="BgpAsn">BgpAsn</a>" : <i>Double</i>,
        "<a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>" : <i>String</i>,
        "<a href="#connectionid" title="ConnectionId">ConnectionId</a>" : <i>String</i>,
        "<a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owneraccountid" title="OwnerAccountId">OwnerAccountId</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DxHostedPrivateVirtualInterface
Properties:
    <a href="#addressfamily" title="AddressFamily">AddressFamily</a>: <i>String</i>
    <a href="#amazonaddress" title="AmazonAddress">AmazonAddress</a>: <i>String</i>
    <a href="#bgpasn" title="BgpAsn">BgpAsn</a>: <i>Double</i>
    <a href="#bgpauthkey" title="BgpAuthKey">BgpAuthKey</a>: <i>String</i>
    <a href="#connectionid" title="ConnectionId">ConnectionId</a>: <i>String</i>
    <a href="#customeraddress" title="CustomerAddress">CustomerAddress</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owneraccountid" title="OwnerAccountId">OwnerAccountId</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AddressFamily

The address family for the BGP peer. `ipv4 ` or `ipv6`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmazonAddress

The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAsn

The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpAuthKey

The authentication key for BGP configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionId

The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAddress

The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for the virtual interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerAccountId

The AWS account that will own the new virtual interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

The VLAN ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AmazonSideAsn

Returns the <code>AmazonSideAsn</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### AwsDevice

Returns the <code>AwsDevice</code> value.

#### Id

Returns the <code>Id</code> value.

#### JumboFrameCapable

Returns the <code>JumboFrameCapable</code> value.

