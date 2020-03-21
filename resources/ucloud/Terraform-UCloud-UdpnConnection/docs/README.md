# Terraform::UCloud::UdpnConnection

UDPN (UCloud Dedicated Private Network)，you can use Dedicated Private Network to achieve high-speed, stable, secure, and dedicated communications between different data centers. The most frequent scenario is to create network connection of clusters across regions.

~> **VPC Peering Connections with UDPN Connection** The cross-region Dedicated Private Network must be established if the two VPCs located in different regions are expected to be connected.

~> **Note** The additional packet head will be added and included in the overall length of packet due to the tunneling UDPN adopted. Since the number of the bytes of packet head is fixed, the bigger data packet is, the less usage will be taken for the packet head.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::UdpnConnection",
    "Properties" : {
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#peerregion" title="PeerRegion">PeerRegion</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::UdpnConnection
Properties:
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#peerregion" title="PeerRegion">PeerRegion</a>: <i>String</i>
</pre>

## Properties

#### Bandwidth

Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). range from 2 - 1000M. The default value is "1".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

Charge type. Possible values are: "year" as pay by year, "month" as pay by month, "dynamic" as pay by hour. The default value is "month".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration that you will buy the resource, the default value is "1". It is not required when "dynamic" (pay by hour), the value is "0" when pay by month and the instance will be valid till the last day of that month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerRegion

The correspondent region of dedicated connection, please refer to the region and [availability zone list](https://docs.ucloud.cn/api/summary/regionlist) and [UDPN price list](https://docs.ucloud.cn/network/udpn/udpn_price).

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

