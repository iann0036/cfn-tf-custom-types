# TF::BIGIP::NetIkePeer

`bigip_net_ike_peer` Manages a ike_peer configuration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::NetIkePeer",
    "Properties" : {
        "<a href="#appservice" title="AppService">AppService</a>" : <i>String</i>,
        "<a href="#cacertfile" title="CaCertFile">CaCertFile</a>" : <i>String</i>,
        "<a href="#crlfile" title="CrlFile">CrlFile</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dpddelay" title="DpdDelay">DpdDelay</a>" : <i>Double</i>,
        "<a href="#generatepolicy" title="GeneratePolicy">GeneratePolicy</a>" : <i>String</i>,
        "<a href="#lifetime" title="Lifetime">Lifetime</a>" : <i>Double</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#mycertfile" title="MyCertFile">MyCertFile</a>" : <i>String</i>,
        "<a href="#mycertkeyfile" title="MyCertKeyFile">MyCertKeyFile</a>" : <i>String</i>,
        "<a href="#mycertkeypassphrase" title="MyCertKeyPassphrase">MyCertKeyPassphrase</a>" : <i>String</i>,
        "<a href="#myidtype" title="MyIdType">MyIdType</a>" : <i>String</i>,
        "<a href="#myidvalue" title="MyIdValue">MyIdValue</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nattraversal" title="NatTraversal">NatTraversal</a>" : <i>String</i>,
        "<a href="#passive" title="Passive">Passive</a>" : <i>String</i>,
        "<a href="#peerscertfile" title="PeersCertFile">PeersCertFile</a>" : <i>String</i>,
        "<a href="#peerscerttype" title="PeersCertType">PeersCertType</a>" : <i>String</i>,
        "<a href="#peersidtype" title="PeersIdType">PeersIdType</a>" : <i>String</i>,
        "<a href="#peersidvalue" title="PeersIdValue">PeersIdValue</a>" : <i>String</i>,
        "<a href="#phase1authmethod" title="Phase1AuthMethod">Phase1AuthMethod</a>" : <i>String</i>,
        "<a href="#phase1encryptalgorithm" title="Phase1EncryptAlgorithm">Phase1EncryptAlgorithm</a>" : <i>String</i>,
        "<a href="#phase1hashalgorithm" title="Phase1HashAlgorithm">Phase1HashAlgorithm</a>" : <i>String</i>,
        "<a href="#phase1perfectforwardsecrecy" title="Phase1PerfectForwardSecrecy">Phase1PerfectForwardSecrecy</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PresharedKey">PresharedKey</a>" : <i>String</i>,
        "<a href="#presharedkeyencrypted" title="PresharedKeyEncrypted">PresharedKeyEncrypted</a>" : <i>String</i>,
        "<a href="#prf" title="Prf">Prf</a>" : <i>String</i>,
        "<a href="#proxysupport" title="ProxySupport">ProxySupport</a>" : <i>String</i>,
        "<a href="#remoteaddress" title="RemoteAddress">RemoteAddress</a>" : <i>String</i>,
        "<a href="#replaywindowsize" title="ReplayWindowSize">ReplayWindowSize</a>" : <i>Double</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#trafficselector" title="TrafficSelector">TrafficSelector</a>" : <i>[ String, ... ]</i>,
        "<a href="#verifycert" title="VerifyCert">VerifyCert</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::NetIkePeer
Properties:
    <a href="#appservice" title="AppService">AppService</a>: <i>String</i>
    <a href="#cacertfile" title="CaCertFile">CaCertFile</a>: <i>String</i>
    <a href="#crlfile" title="CrlFile">CrlFile</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dpddelay" title="DpdDelay">DpdDelay</a>: <i>Double</i>
    <a href="#generatepolicy" title="GeneratePolicy">GeneratePolicy</a>: <i>String</i>
    <a href="#lifetime" title="Lifetime">Lifetime</a>: <i>Double</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#mycertfile" title="MyCertFile">MyCertFile</a>: <i>String</i>
    <a href="#mycertkeyfile" title="MyCertKeyFile">MyCertKeyFile</a>: <i>String</i>
    <a href="#mycertkeypassphrase" title="MyCertKeyPassphrase">MyCertKeyPassphrase</a>: <i>String</i>
    <a href="#myidtype" title="MyIdType">MyIdType</a>: <i>String</i>
    <a href="#myidvalue" title="MyIdValue">MyIdValue</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nattraversal" title="NatTraversal">NatTraversal</a>: <i>String</i>
    <a href="#passive" title="Passive">Passive</a>: <i>String</i>
    <a href="#peerscertfile" title="PeersCertFile">PeersCertFile</a>: <i>String</i>
    <a href="#peerscerttype" title="PeersCertType">PeersCertType</a>: <i>String</i>
    <a href="#peersidtype" title="PeersIdType">PeersIdType</a>: <i>String</i>
    <a href="#peersidvalue" title="PeersIdValue">PeersIdValue</a>: <i>String</i>
    <a href="#phase1authmethod" title="Phase1AuthMethod">Phase1AuthMethod</a>: <i>String</i>
    <a href="#phase1encryptalgorithm" title="Phase1EncryptAlgorithm">Phase1EncryptAlgorithm</a>: <i>String</i>
    <a href="#phase1hashalgorithm" title="Phase1HashAlgorithm">Phase1HashAlgorithm</a>: <i>String</i>
    <a href="#phase1perfectforwardsecrecy" title="Phase1PerfectForwardSecrecy">Phase1PerfectForwardSecrecy</a>: <i>String</i>
    <a href="#presharedkey" title="PresharedKey">PresharedKey</a>: <i>String</i>
    <a href="#presharedkeyencrypted" title="PresharedKeyEncrypted">PresharedKeyEncrypted</a>: <i>String</i>
    <a href="#prf" title="Prf">Prf</a>: <i>String</i>
    <a href="#proxysupport" title="ProxySupport">ProxySupport</a>: <i>String</i>
    <a href="#remoteaddress" title="RemoteAddress">RemoteAddress</a>: <i>String</i>
    <a href="#replaywindowsize" title="ReplayWindowSize">ReplayWindowSize</a>: <i>Double</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#trafficselector" title="TrafficSelector">TrafficSelector</a>: <i>
      - String</i>
    <a href="#verifycert" title="VerifyCert">VerifyCert</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>
      - String</i>
</pre>

## Properties

#### AppService

The application service that the object belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCertFile

the trusted root and intermediate certificate authorities.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlFile

Specifies the file name of the Certificate Revocation List. Only supported in IKEv1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpdDelay

Specifies the number of seconds between Dead Peer Detection messages.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeneratePolicy

Enable or disable the generation of Security Policy Database entries(SPD) when the device is the responder of the IKE remote node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifetime

Defines the lifetime in minutes of an IKE SA which will be proposed in the phase 1 negotiations.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

Defines the exchange mode for phase 1 when racoon is the initiator, or the acceptable exchange mode when racoon is the responder.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MyCertFile

Specifies the name of the certificate file object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MyCertKeyFile

Specifies the name of the certificate key file object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MyCertKeyPassphrase

Specifies the passphrase of the key used for my-cert-key-file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MyIdType

Specifies the identifier type sent to the remote host to use in the phase 1 negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MyIdValue

Specifies the identifier value sent to the remote host in the phase 1 negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the ike_peer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTraversal

Enables use of the NAT-Traversal IPsec extension.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passive

Specifies whether the local IKE agent can be the initiator of the IKE negotiation with this ike-peer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeersCertFile

Specifies the peer’s certificate for authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeersCertType

Specifies that the only peers-cert-type supported is certfile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeersIdType

Specifies which of address, fqdn, asn1dn, user-fqdn or keyid-tag types to use as peers-id-type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeersIdValue

Specifies the peer’s identifier to be received.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1AuthMethod

Specifies the authentication method used for phase 1 negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1EncryptAlgorithm

Specifies the encryption algorithm used for the isakmp phase 1 negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1HashAlgorithm

Defines the hash algorithm used for the isakmp phase 1 negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phase1PerfectForwardSecrecy

Defines the Diffie-Hellman group for key exchange to provide perfect forward secrecy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresharedKey

Specifies the preshared key for ISAKMP SAs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresharedKeyEncrypted

Display the encrypted preshared-key for the IKE remote node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prf

Specifies the pseudo-random function used to derive keying material for all cryptographic operations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxySupport

If this value is enabled, both values of ID payloads in the phase 2 exchange are used as the addresses of end-point of IPsec-SAs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAddress

Specifies the IP address of the IKE remote node.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplayWindowSize

Specifies the replay window size of the IPsec SAs negotiated with the IKE remote node.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

Enables or disables this IKE remote node.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficSelector

Specifies the names of the traffic-selector objects associated with this ike-peer.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyCert

Specifies whether to verify the certificate chain of the remote peer based on the trusted certificates in ca-cert-file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specifies which version of IKE to be used.

_Required_: No

_Type_: List of String

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

