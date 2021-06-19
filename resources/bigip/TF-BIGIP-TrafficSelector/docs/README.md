# TF::BIGIP::TrafficSelector

`bigip_traffic_selector` Manage IPSec Traffic Selectors on BIG-IP

Resources should be named with their "full path". The full path is the combination of the partition + name (example: /Common/test-selector)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::TrafficSelector",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destinationaddress" title="DestinationAddress">DestinationAddress</a>" : <i>String</i>,
        "<a href="#destinationport" title="DestinationPort">DestinationPort</a>" : <i>Double</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>Double</i>,
        "<a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#sourceaddress" title="SourceAddress">SourceAddress</a>" : <i>String</i>,
        "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::TrafficSelector
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destinationaddress" title="DestinationAddress">DestinationAddress</a>: <i>String</i>
    <a href="#destinationport" title="DestinationPort">DestinationPort</a>: <i>Double</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>Double</i>
    <a href="#ipsecpolicy" title="IpsecPolicy">IpsecPolicy</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#sourceaddress" title="SourceAddress">SourceAddress</a>: <i>String</i>
    <a href="#sourceport" title="SourcePort">SourcePort</a>: <i>Double</i>
</pre>

## Properties

#### Description

Description of the traffic selector.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddress

Specifies the host or network IP address to which the application traffic is destined.When creating a new traffic selector, this parameter is required.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPort

Specifies the IP port used by the application. The default value is `All Ports (0)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

Specifies whether the traffic selector applies to inbound or outbound traffic, or both. The default value is `Both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

Specifies the network protocol to use for this traffic. The default value is `All Protocols (255)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPolicy

Specifies the IPsec policy that tells the BIG-IP system how to handle the packets.When creating a new traffic selector, if this parameter is not specified, the default is `default-ipsec-policy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the IPSec traffic-selector,it should be "full path".The full path is the combination of the partition + name of the IPSec traffic-selector.(For example `/Common/test-selector`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

Specifies the order in which traffic is matched, if traffic can be matched to multiple traffic selectors.Traffic is matched to the traffic selector with the highest priority (lowest order number).
When creating a new traffic selector, if this parameter is not specified, the default is `last`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddress

Specifies the host or network IP address from which the application traffic originates.When creating a new traffic selector, this parameter is required.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

Specifies the IP port used by the application. The default value is `All Ports (0)`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

