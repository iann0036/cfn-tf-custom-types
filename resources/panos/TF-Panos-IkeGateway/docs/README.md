# TF::Panos::IkeGateway

This resource allows you to add/update/delete IKE gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::IkeGateway",
    "Properties" : {
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#certbaseurl" title="CertBaseUrl">CertBaseUrl</a>" : <i>String</i>,
        "<a href="#certenablehashandurl" title="CertEnableHashAndUrl">CertEnableHashAndUrl</a>" : <i>Boolean</i>,
        "<a href="#certenablestrictvalidation" title="CertEnableStrictValidation">CertEnableStrictValidation</a>" : <i>Boolean</i>,
        "<a href="#certpermitpayloadmismatch" title="CertPermitPayloadMismatch">CertPermitPayloadMismatch</a>" : <i>Boolean</i>,
        "<a href="#certprofile" title="CertProfile">CertProfile</a>" : <i>String</i>,
        "<a href="#certusemanagementassource" title="CertUseManagementAsSource">CertUseManagementAsSource</a>" : <i>Boolean</i>,
        "<a href="#deadpeerdetectioninterval" title="DeadPeerDetectionInterval">DeadPeerDetectionInterval</a>" : <i>Double</i>,
        "<a href="#deadpeerdetectionretry" title="DeadPeerDetectionRetry">DeadPeerDetectionRetry</a>" : <i>Double</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>" : <i>Boolean</i>,
        "<a href="#enablefragmentation" title="EnableFragmentation">EnableFragmentation</a>" : <i>Boolean</i>,
        "<a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>" : <i>Boolean</i>,
        "<a href="#enablelivenesscheck" title="EnableLivenessCheck">EnableLivenessCheck</a>" : <i>Boolean</i>,
        "<a href="#enablenattraversal" title="EnableNatTraversal">EnableNatTraversal</a>" : <i>Boolean</i>,
        "<a href="#enablepassivemode" title="EnablePassiveMode">EnablePassiveMode</a>" : <i>Boolean</i>,
        "<a href="#ikev1cryptoprofile" title="Ikev1CryptoProfile">Ikev1CryptoProfile</a>" : <i>String</i>,
        "<a href="#ikev1exchangemode" title="Ikev1ExchangeMode">Ikev1ExchangeMode</a>" : <i>String</i>,
        "<a href="#ikev2cookievalidation" title="Ikev2CookieValidation">Ikev2CookieValidation</a>" : <i>Boolean</i>,
        "<a href="#ikev2cryptoprofile" title="Ikev2CryptoProfile">Ikev2CryptoProfile</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#livenesscheckinterval" title="LivenessCheckInterval">LivenessCheckInterval</a>" : <i>Double</i>,
        "<a href="#localcert" title="LocalCert">LocalCert</a>" : <i>String</i>,
        "<a href="#localidtype" title="LocalIdType">LocalIdType</a>" : <i>String</i>,
        "<a href="#localidvalue" title="LocalIdValue">LocalIdValue</a>" : <i>String</i>,
        "<a href="#localipaddresstype" title="LocalIpAddressType">LocalIpAddressType</a>" : <i>String</i>,
        "<a href="#localipaddressvalue" title="LocalIpAddressValue">LocalIpAddressValue</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nattraversalenableudpchecksum" title="NatTraversalEnableUdpChecksum">NatTraversalEnableUdpChecksum</a>" : <i>Boolean</i>,
        "<a href="#nattraversalkeepalive" title="NatTraversalKeepAlive">NatTraversalKeepAlive</a>" : <i>Double</i>,
        "<a href="#peeridcheck" title="PeerIdCheck">PeerIdCheck</a>" : <i>String</i>,
        "<a href="#peeridtype" title="PeerIdType">PeerIdType</a>" : <i>String</i>,
        "<a href="#peeridvalue" title="PeerIdValue">PeerIdValue</a>" : <i>String</i>,
        "<a href="#peeriptype" title="PeerIpType">PeerIpType</a>" : <i>String</i>,
        "<a href="#peeripvalue" title="PeerIpValue">PeerIpValue</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::IkeGateway
Properties:
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#certbaseurl" title="CertBaseUrl">CertBaseUrl</a>: <i>String</i>
    <a href="#certenablehashandurl" title="CertEnableHashAndUrl">CertEnableHashAndUrl</a>: <i>Boolean</i>
    <a href="#certenablestrictvalidation" title="CertEnableStrictValidation">CertEnableStrictValidation</a>: <i>Boolean</i>
    <a href="#certpermitpayloadmismatch" title="CertPermitPayloadMismatch">CertPermitPayloadMismatch</a>: <i>Boolean</i>
    <a href="#certprofile" title="CertProfile">CertProfile</a>: <i>String</i>
    <a href="#certusemanagementassource" title="CertUseManagementAsSource">CertUseManagementAsSource</a>: <i>Boolean</i>
    <a href="#deadpeerdetectioninterval" title="DeadPeerDetectionInterval">DeadPeerDetectionInterval</a>: <i>Double</i>
    <a href="#deadpeerdetectionretry" title="DeadPeerDetectionRetry">DeadPeerDetectionRetry</a>: <i>Double</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enabledeadpeerdetection" title="EnableDeadPeerDetection">EnableDeadPeerDetection</a>: <i>Boolean</i>
    <a href="#enablefragmentation" title="EnableFragmentation">EnableFragmentation</a>: <i>Boolean</i>
    <a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>: <i>Boolean</i>
    <a href="#enablelivenesscheck" title="EnableLivenessCheck">EnableLivenessCheck</a>: <i>Boolean</i>
    <a href="#enablenattraversal" title="EnableNatTraversal">EnableNatTraversal</a>: <i>Boolean</i>
    <a href="#enablepassivemode" title="EnablePassiveMode">EnablePassiveMode</a>: <i>Boolean</i>
    <a href="#ikev1cryptoprofile" title="Ikev1CryptoProfile">Ikev1CryptoProfile</a>: <i>String</i>
    <a href="#ikev1exchangemode" title="Ikev1ExchangeMode">Ikev1ExchangeMode</a>: <i>String</i>
    <a href="#ikev2cookievalidation" title="Ikev2CookieValidation">Ikev2CookieValidation</a>: <i>Boolean</i>
    <a href="#ikev2cryptoprofile" title="Ikev2CryptoProfile">Ikev2CryptoProfile</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#livenesscheckinterval" title="LivenessCheckInterval">LivenessCheckInterval</a>: <i>Double</i>
    <a href="#localcert" title="LocalCert">LocalCert</a>: <i>String</i>
    <a href="#localidtype" title="LocalIdType">LocalIdType</a>: <i>String</i>
    <a href="#localidvalue" title="LocalIdValue">LocalIdValue</a>: <i>String</i>
    <a href="#localipaddresstype" title="LocalIpAddressType">LocalIpAddressType</a>: <i>String</i>
    <a href="#localipaddressvalue" title="LocalIpAddressValue">LocalIpAddressValue</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nattraversalenableudpchecksum" title="NatTraversalEnableUdpChecksum">NatTraversalEnableUdpChecksum</a>: <i>Boolean</i>
    <a href="#nattraversalkeepalive" title="NatTraversalKeepAlive">NatTraversalKeepAlive</a>: <i>Double</i>
    <a href="#peeridcheck" title="PeerIdCheck">PeerIdCheck</a>: <i>String</i>
    <a href="#peeridtype" title="PeerIdType">PeerIdType</a>: <i>String</i>
    <a href="#peeridvalue" title="PeerIdValue">PeerIdValue</a>: <i>String</i>
    <a href="#peeriptype" title="PeerIpType">PeerIpType</a>: <i>String</i>
    <a href="#peeripvalue" title="PeerIpValue">PeerIpValue</a>: <i>String</i>
    <a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### AuthType

The auth type.  Valid values are `pre-shared-key`
(the default), or `certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertBaseUrl

The host and directory part of URL for local
certificates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertEnableHashAndUrl

Set to `true` to use
hash-and-url for local certificate.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertEnableStrictValidation

Set to `true` to enable
strict validation of peer's extended key use.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertPermitPayloadMismatch

Set to `true` to permit
peer identification and certificate payload identification mismatch.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertProfile

Profile for certificate valdiation during IKE
negotiation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertUseManagementAsSource

Set to `true` to
use management interface IP as source to retrieve http certificates.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadPeerDetectionInterval

The dead peer detection interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadPeerDetectionRetry

Number of retries before disconnection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Set to `true` to disable.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeadPeerDetection

Set to `true` to enable dead
peer detection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFragmentation

Set to `true` to enable fragmentation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

Enable IPv6 or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLivenessCheck

Set to `true` to
enable sending empty information liveness check message.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNatTraversal

Set to `true` to enable NAT
traversal.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePassiveMode

Set to `true` to enable passive
mode (responder only).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev1CryptoProfile

IKEv1 crypto profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev1ExchangeMode

The IKEv1 exchange mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2CookieValidation

Set to `true` to require cookie.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2CryptoProfile

IKEv2 crypto profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

The interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessCheckInterval

Delay interval before
sending probing packets (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalCert

The local certificate name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIdType

The local ID type.  Valid values are `ipaddr`,
`fqdn`, `ufqdn`, `keyid`, or `dn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIdValue

The local ID value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddressType

The local IP address type.  Valid
values for this are `ip`, `floating-ip`, or an empty string (the default)
which is `None`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddressValue

The IP address if `local_ip_address_type`
is set to `ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTraversalEnableUdpChecksum

Set to `true` to enable
NAT traversal UDP checksum.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTraversalKeepAlive

Sending interval for NAT
keep-alive packets (in seconds).  For versions 6.1 - 8.1, this param, if specified,
should be a multiple of 10 between 10 and 3600 to be valid.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdCheck

Enable peer ID wildcard match for certificate
authentication.  Valid values are `exact` or `wildcard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdType

The peer ID type.  Valid values are `ipaddr`,
`fqdn`, `ufqdn`, `keyid`, or `dn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdValue

The peer ID value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpType

The peer IP type.  Valid values are `ip`,
`dynamic`, and `fqdn` (PANOS 8.1+).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpValue

The peer IP value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKey

The pre-shared key value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The IKE gateway version.  Valid values are
`ikev1`, (the default), `ikev2`, or `ikev2-preferred`.  For PAN-OS 6.1, only
`ikev1` is acceptable.

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

#### Id

Returns the <code>Id</code> value.

#### PreSharedKeyEnc

Returns the <code>PreSharedKeyEnc</code> value.

