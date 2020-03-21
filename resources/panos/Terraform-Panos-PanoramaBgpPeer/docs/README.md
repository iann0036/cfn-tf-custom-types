# Terraform::Panos::PanoramaBgpPeer

CloudFormation equivalent of panos_panorama_bgp_peer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaBgpPeer",
    "Properties" : {
        "<a href="#addressfamilytype" title="AddressFamilyType">AddressFamilyType</a>" : <i>String</i>,
        "<a href="#allowincomingconnections" title="AllowIncomingConnections">AllowIncomingConnections</a>" : <i>Boolean</i>,
        "<a href="#allowoutgoingconnections" title="AllowOutgoingConnections">AllowOutgoingConnections</a>" : <i>Boolean</i>,
        "<a href="#authprofile" title="AuthProfile">AuthProfile</a>" : <i>String</i>,
        "<a href="#bfdprofile" title="BfdProfile">BfdProfile</a>" : <i>String</i>,
        "<a href="#bgppeergroup" title="BgpPeerGroup">BgpPeerGroup</a>" : <i>String</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#enablempbgp" title="EnableMpBgp">EnableMpBgp</a>" : <i>Boolean</i>,
        "<a href="#enablesendersideloopdetection" title="EnableSenderSideLoopDetection">EnableSenderSideLoopDetection</a>" : <i>Boolean</i>,
        "<a href="#holdtime" title="HoldTime">HoldTime</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#idleholdtime" title="IdleHoldTime">IdleHoldTime</a>" : <i>Double</i>,
        "<a href="#incomingconnectionsremoteport" title="IncomingConnectionsRemotePort">IncomingConnectionsRemotePort</a>" : <i>Double</i>,
        "<a href="#keepaliveinterval" title="KeepAliveInterval">KeepAliveInterval</a>" : <i>Double</i>,
        "<a href="#localaddressinterface" title="LocalAddressInterface">LocalAddressInterface</a>" : <i>String</i>,
        "<a href="#localaddressip" title="LocalAddressIp">LocalAddressIp</a>" : <i>String</i>,
        "<a href="#maxprefixes" title="MaxPrefixes">MaxPrefixes</a>" : <i>String</i>,
        "<a href="#minrouteadvertisementinterval" title="MinRouteAdvertisementInterval">MinRouteAdvertisementInterval</a>" : <i>Double</i>,
        "<a href="#multihop" title="MultiHop">MultiHop</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#opendelaytime" title="OpenDelayTime">OpenDelayTime</a>" : <i>Double</i>,
        "<a href="#outgoingconnectionslocalport" title="OutgoingConnectionsLocalPort">OutgoingConnectionsLocalPort</a>" : <i>Double</i>,
        "<a href="#peeraddressip" title="PeerAddressIp">PeerAddressIp</a>" : <i>String</i>,
        "<a href="#peeras" title="PeerAs">PeerAs</a>" : <i>String</i>,
        "<a href="#peeringtype" title="PeeringType">PeeringType</a>" : <i>String</i>,
        "<a href="#reflectorclient" title="ReflectorClient">ReflectorClient</a>" : <i>String</i>,
        "<a href="#subsequentaddressfamilymulticast" title="SubsequentAddressFamilyMulticast">SubsequentAddressFamilyMulticast</a>" : <i>Boolean</i>,
        "<a href="#subsequentaddressfamilyunicast" title="SubsequentAddressFamilyUnicast">SubsequentAddressFamilyUnicast</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaBgpPeer
Properties:
    <a href="#addressfamilytype" title="AddressFamilyType">AddressFamilyType</a>: <i>String</i>
    <a href="#allowincomingconnections" title="AllowIncomingConnections">AllowIncomingConnections</a>: <i>Boolean</i>
    <a href="#allowoutgoingconnections" title="AllowOutgoingConnections">AllowOutgoingConnections</a>: <i>Boolean</i>
    <a href="#authprofile" title="AuthProfile">AuthProfile</a>: <i>String</i>
    <a href="#bfdprofile" title="BfdProfile">BfdProfile</a>: <i>String</i>
    <a href="#bgppeergroup" title="BgpPeerGroup">BgpPeerGroup</a>: <i>String</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#enablempbgp" title="EnableMpBgp">EnableMpBgp</a>: <i>Boolean</i>
    <a href="#enablesendersideloopdetection" title="EnableSenderSideLoopDetection">EnableSenderSideLoopDetection</a>: <i>Boolean</i>
    <a href="#holdtime" title="HoldTime">HoldTime</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#idleholdtime" title="IdleHoldTime">IdleHoldTime</a>: <i>Double</i>
    <a href="#incomingconnectionsremoteport" title="IncomingConnectionsRemotePort">IncomingConnectionsRemotePort</a>: <i>Double</i>
    <a href="#keepaliveinterval" title="KeepAliveInterval">KeepAliveInterval</a>: <i>Double</i>
    <a href="#localaddressinterface" title="LocalAddressInterface">LocalAddressInterface</a>: <i>String</i>
    <a href="#localaddressip" title="LocalAddressIp">LocalAddressIp</a>: <i>String</i>
    <a href="#maxprefixes" title="MaxPrefixes">MaxPrefixes</a>: <i>String</i>
    <a href="#minrouteadvertisementinterval" title="MinRouteAdvertisementInterval">MinRouteAdvertisementInterval</a>: <i>Double</i>
    <a href="#multihop" title="MultiHop">MultiHop</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#opendelaytime" title="OpenDelayTime">OpenDelayTime</a>: <i>Double</i>
    <a href="#outgoingconnectionslocalport" title="OutgoingConnectionsLocalPort">OutgoingConnectionsLocalPort</a>: <i>Double</i>
    <a href="#peeraddressip" title="PeerAddressIp">PeerAddressIp</a>: <i>String</i>
    <a href="#peeras" title="PeerAs">PeerAs</a>: <i>String</i>
    <a href="#peeringtype" title="PeeringType">PeeringType</a>: <i>String</i>
    <a href="#reflectorclient" title="ReflectorClient">ReflectorClient</a>: <i>String</i>
    <a href="#subsequentaddressfamilymulticast" title="SubsequentAddressFamilyMulticast">SubsequentAddressFamilyMulticast</a>: <i>Boolean</i>
    <a href="#subsequentaddressfamilyunicast" title="SubsequentAddressFamilyUnicast">SubsequentAddressFamilyUnicast</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AddressFamilyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIncomingConnections

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowOutgoingConnections

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeerGroup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMpBgp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSenderSideLoopDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleHoldTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingConnectionsRemotePort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressInterface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrefixes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRouteAdvertisementInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiHop

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenDelayTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingConnectionsLocalPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAddressIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReflectorClient

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubsequentAddressFamilyMulticast

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubsequentAddressFamilyUnicast

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

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

