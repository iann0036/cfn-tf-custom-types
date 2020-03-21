# Terraform::Panos::PanoramaIkeGateway

CloudFormation equivalent of panos_panorama_ike_gateway

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaIkeGateway",
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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaIkeGateway
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### AuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertBaseUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertEnableHashAndUrl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertEnableStrictValidation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertPermitPayloadMismatch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertUseManagementAsSource

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadPeerDetectionInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadPeerDetectionRetry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeadPeerDetection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFragmentation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLivenessCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNatTraversal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePassiveMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev1CryptoProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev1ExchangeMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2CookieValidation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ikev2CryptoProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessCheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIdType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIdValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpAddressValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTraversalEnableUdpChecksum

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTraversalKeepAlive

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdCheck

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIdValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerIpValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

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

#### PreSharedKeyEnc

Returns the <code>PreSharedKeyEnc</code> value.

