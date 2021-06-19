# TF::Panos::PanoramaBgpPeer

This resource allows you to add/update/delete a Panorama BGP peer.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaBgpPeer",
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
Type: TF::Panos::PanoramaBgpPeer
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

Set the AFI for this
peer.  Valid values are `ipv4` or `ipv6`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowIncomingConnections

Allow incoming connections
(default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowOutgoingConnections

Allow outgoing connections
(default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthProfile

Auth profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

BFD profile.  This can be a specific
BFD profile name, `None` (disables BFD), or `Inherit-vr-global-setting`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpPeerGroup

The BGP peer group to put this peer into.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable or not (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMpBgp

Enable MP BGP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSenderSideLoopDetection

Enable
sender side loop detection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldTime

Hold time, in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleHoldTime

Idle hold time, in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncomingConnectionsRemotePort

Restrict remote port for
incoming BGP connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveInterval

Keep alive interval, in
seconds (default: `30`).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressInterface

Interface to accept BGP session.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressIp

Specify exact IP address if interface has
multiple addresses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrefixes

Maximum of prefixes to receive from the
peer.  This can be a number such as `"5000"` (default) or `unlimited`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRouteAdvertisementInterval

Minimum
route advertisement interval, in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiHop

IP TTL value used for sending BGP packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenDelayTime

Open delay time, in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutgoingConnectionsLocalPort

Use specific local
port for outgoing BGP connections.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAddressIp

Peer IP address configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAs

Peer AS number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringType

Peering type that affects NOPEER
community value handling.  Valid values are `unspecified` (default) or
`bilateral`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReflectorClient

This peer is reflector client.  Valid
values are `non-client`, `client`, or `meshed-client`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubsequentAddressFamilyMulticast

Enable
multicast subsequent address family for this peer.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubsequentAddressFamilyUnicast

Enable
unicast subsequent address family for this peer.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

The virtual router to add this BGP
peer to.

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

