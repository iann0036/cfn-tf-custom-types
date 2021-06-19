# TF::Aviatrix::CloudnTransitGatewayAttachment

The **aviatrix_cloudn_transit_gateway_attachment** resource allows the creation and management of CloudN Transit Gateway Attachments. This resource is available as of provider version R2.19+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::CloudnTransitGatewayAttachment",
    "Properties" : {
        "<a href="#cloudnbgpasn" title="CloudnBgpAsn">CloudnBgpAsn</a>" : <i>String</i>,
        "<a href="#cloudnlaninterfaceneighborbgpasn" title="CloudnLanInterfaceNeighborBgpAsn">CloudnLanInterfaceNeighborBgpAsn</a>" : <i>String</i>,
        "<a href="#cloudnlaninterfaceneighborip" title="CloudnLanInterfaceNeighborIp">CloudnLanInterfaceNeighborIp</a>" : <i>String</i>,
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
        "<a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>" : <i>Boolean</i>,
        "<a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>" : <i>Boolean</i>,
        "<a href="#enableoverprivatenetwork" title="EnableOverPrivateNetwork">EnableOverPrivateNetwork</a>" : <i>Boolean</i>,
        "<a href="#transitgatewaybgpasn" title="TransitGatewayBgpAsn">TransitGatewayBgpAsn</a>" : <i>String</i>,
        "<a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::CloudnTransitGatewayAttachment
Properties:
    <a href="#cloudnbgpasn" title="CloudnBgpAsn">CloudnBgpAsn</a>: <i>String</i>
    <a href="#cloudnlaninterfaceneighborbgpasn" title="CloudnLanInterfaceNeighborBgpAsn">CloudnLanInterfaceNeighborBgpAsn</a>: <i>String</i>
    <a href="#cloudnlaninterfaceneighborip" title="CloudnLanInterfaceNeighborIp">CloudnLanInterfaceNeighborIp</a>: <i>String</i>
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
    <a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>: <i>Boolean</i>
    <a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>: <i>Boolean</i>
    <a href="#enableoverprivatenetwork" title="EnableOverPrivateNetwork">EnableOverPrivateNetwork</a>: <i>Boolean</i>
    <a href="#transitgatewaybgpasn" title="TransitGatewayBgpAsn">TransitGatewayBgpAsn</a>: <i>String</i>
    <a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>: <i>String</i>
</pre>

## Properties

#### CloudnBgpAsn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudnLanInterfaceNeighborBgpAsn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudnLanInterfaceNeighborIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeadPeerDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableJumboFrame

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableOverPrivateNetwork

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayBgpAsn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayName

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

#### Id

Returns the <code>Id</code> value.

