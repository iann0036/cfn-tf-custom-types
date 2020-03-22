# Terraform::Panos::PanoramaIpsecTunnel

This resource allows you to add/update/delete Panorama IPSec tunnels
for templates.

A large number of params have prefixes:

* `ak` - Auto key
* `mk` - Manual key
* `gps` - GlobalProtect Satellite

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaIpsecTunnel",
    "Properties" : {
        "<a href="#akikegateway" title="AkIkeGateway">AkIkeGateway</a>" : <i>String</i>,
        "<a href="#akipseccryptoprofile" title="AkIpsecCryptoProfile">AkIpsecCryptoProfile</a>" : <i>String</i>,
        "<a href="#antireplay" title="AntiReplay">AntiReplay</a>" : <i>Boolean</i>,
        "<a href="#copyflowlabel" title="CopyFlowLabel">CopyFlowLabel</a>" : <i>Boolean</i>,
        "<a href="#copytos" title="CopyTos">CopyTos</a>" : <i>Boolean</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>" : <i>Boolean</i>,
        "<a href="#enabletunnelmonitor" title="EnableTunnelMonitor">EnableTunnelMonitor</a>" : <i>Boolean</i>,
        "<a href="#gpscertificateprofile" title="GpsCertificateProfile">GpsCertificateProfile</a>" : <i>String</i>,
        "<a href="#gpsinterface" title="GpsInterface">GpsInterface</a>" : <i>String</i>,
        "<a href="#gpsinterfacefloatingipipv4" title="GpsInterfaceFloatingIpIpv4">GpsInterfaceFloatingIpIpv4</a>" : <i>String</i>,
        "<a href="#gpsinterfacefloatingipipv6" title="GpsInterfaceFloatingIpIpv6">GpsInterfaceFloatingIpIpv6</a>" : <i>String</i>,
        "<a href="#gpsinterfaceipipv4" title="GpsInterfaceIpIpv4">GpsInterfaceIpIpv4</a>" : <i>String</i>,
        "<a href="#gpsinterfaceipipv6" title="GpsInterfaceIpIpv6">GpsInterfaceIpIpv6</a>" : <i>String</i>,
        "<a href="#gpslocalcertificate" title="GpsLocalCertificate">GpsLocalCertificate</a>" : <i>String</i>,
        "<a href="#gpsportaladdress" title="GpsPortalAddress">GpsPortalAddress</a>" : <i>String</i>,
        "<a href="#gpspreferipv6" title="GpsPreferIpv6">GpsPreferIpv6</a>" : <i>Boolean</i>,
        "<a href="#gpspublishconnectedroutes" title="GpsPublishConnectedRoutes">GpsPublishConnectedRoutes</a>" : <i>Boolean</i>,
        "<a href="#gpspublishroutes" title="GpsPublishRoutes">GpsPublishRoutes</a>" : <i>[ String, ... ]</i>,
        "<a href="#mkauthkey" title="MkAuthKey">MkAuthKey</a>" : <i>String</i>,
        "<a href="#mkauthtype" title="MkAuthType">MkAuthType</a>" : <i>String</i>,
        "<a href="#mkespencryptionkey" title="MkEspEncryptionKey">MkEspEncryptionKey</a>" : <i>String</i>,
        "<a href="#mkespencryptiontype" title="MkEspEncryptionType">MkEspEncryptionType</a>" : <i>String</i>,
        "<a href="#mkinterface" title="MkInterface">MkInterface</a>" : <i>String</i>,
        "<a href="#mklocaladdressfloatingip" title="MkLocalAddressFloatingIp">MkLocalAddressFloatingIp</a>" : <i>String</i>,
        "<a href="#mklocaladdressip" title="MkLocalAddressIp">MkLocalAddressIp</a>" : <i>String</i>,
        "<a href="#mklocalspi" title="MkLocalSpi">MkLocalSpi</a>" : <i>String</i>,
        "<a href="#mkprotocol" title="MkProtocol">MkProtocol</a>" : <i>String</i>,
        "<a href="#mkremoteaddress" title="MkRemoteAddress">MkRemoteAddress</a>" : <i>String</i>,
        "<a href="#mkremotespi" title="MkRemoteSpi">MkRemoteSpi</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#tunnelinterface" title="TunnelInterface">TunnelInterface</a>" : <i>String</i>,
        "<a href="#tunnelmonitordestinationip" title="TunnelMonitorDestinationIp">TunnelMonitorDestinationIp</a>" : <i>String</i>,
        "<a href="#tunnelmonitorprofile" title="TunnelMonitorProfile">TunnelMonitorProfile</a>" : <i>String</i>,
        "<a href="#tunnelmonitorproxyid" title="TunnelMonitorProxyId">TunnelMonitorProxyId</a>" : <i>String</i>,
        "<a href="#tunnelmonitorsourceip" title="TunnelMonitorSourceIp">TunnelMonitorSourceIp</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaIpsecTunnel
Properties:
    <a href="#akikegateway" title="AkIkeGateway">AkIkeGateway</a>: <i>String</i>
    <a href="#akipseccryptoprofile" title="AkIpsecCryptoProfile">AkIpsecCryptoProfile</a>: <i>String</i>
    <a href="#antireplay" title="AntiReplay">AntiReplay</a>: <i>Boolean</i>
    <a href="#copyflowlabel" title="CopyFlowLabel">CopyFlowLabel</a>: <i>Boolean</i>
    <a href="#copytos" title="CopyTos">CopyTos</a>: <i>Boolean</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enableipv6" title="EnableIpv6">EnableIpv6</a>: <i>Boolean</i>
    <a href="#enabletunnelmonitor" title="EnableTunnelMonitor">EnableTunnelMonitor</a>: <i>Boolean</i>
    <a href="#gpscertificateprofile" title="GpsCertificateProfile">GpsCertificateProfile</a>: <i>String</i>
    <a href="#gpsinterface" title="GpsInterface">GpsInterface</a>: <i>String</i>
    <a href="#gpsinterfacefloatingipipv4" title="GpsInterfaceFloatingIpIpv4">GpsInterfaceFloatingIpIpv4</a>: <i>String</i>
    <a href="#gpsinterfacefloatingipipv6" title="GpsInterfaceFloatingIpIpv6">GpsInterfaceFloatingIpIpv6</a>: <i>String</i>
    <a href="#gpsinterfaceipipv4" title="GpsInterfaceIpIpv4">GpsInterfaceIpIpv4</a>: <i>String</i>
    <a href="#gpsinterfaceipipv6" title="GpsInterfaceIpIpv6">GpsInterfaceIpIpv6</a>: <i>String</i>
    <a href="#gpslocalcertificate" title="GpsLocalCertificate">GpsLocalCertificate</a>: <i>String</i>
    <a href="#gpsportaladdress" title="GpsPortalAddress">GpsPortalAddress</a>: <i>String</i>
    <a href="#gpspreferipv6" title="GpsPreferIpv6">GpsPreferIpv6</a>: <i>Boolean</i>
    <a href="#gpspublishconnectedroutes" title="GpsPublishConnectedRoutes">GpsPublishConnectedRoutes</a>: <i>Boolean</i>
    <a href="#gpspublishroutes" title="GpsPublishRoutes">GpsPublishRoutes</a>: <i>
      - String</i>
    <a href="#mkauthkey" title="MkAuthKey">MkAuthKey</a>: <i>String</i>
    <a href="#mkauthtype" title="MkAuthType">MkAuthType</a>: <i>String</i>
    <a href="#mkespencryptionkey" title="MkEspEncryptionKey">MkEspEncryptionKey</a>: <i>String</i>
    <a href="#mkespencryptiontype" title="MkEspEncryptionType">MkEspEncryptionType</a>: <i>String</i>
    <a href="#mkinterface" title="MkInterface">MkInterface</a>: <i>String</i>
    <a href="#mklocaladdressfloatingip" title="MkLocalAddressFloatingIp">MkLocalAddressFloatingIp</a>: <i>String</i>
    <a href="#mklocaladdressip" title="MkLocalAddressIp">MkLocalAddressIp</a>: <i>String</i>
    <a href="#mklocalspi" title="MkLocalSpi">MkLocalSpi</a>: <i>String</i>
    <a href="#mkprotocol" title="MkProtocol">MkProtocol</a>: <i>String</i>
    <a href="#mkremoteaddress" title="MkRemoteAddress">MkRemoteAddress</a>: <i>String</i>
    <a href="#mkremotespi" title="MkRemoteSpi">MkRemoteSpi</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#tunnelinterface" title="TunnelInterface">TunnelInterface</a>: <i>String</i>
    <a href="#tunnelmonitordestinationip" title="TunnelMonitorDestinationIp">TunnelMonitorDestinationIp</a>: <i>String</i>
    <a href="#tunnelmonitorprofile" title="TunnelMonitorProfile">TunnelMonitorProfile</a>: <i>String</i>
    <a href="#tunnelmonitorproxyid" title="TunnelMonitorProxyId">TunnelMonitorProxyId</a>: <i>String</i>
    <a href="#tunnelmonitorsourceip" title="TunnelMonitorSourceIp">TunnelMonitorSourceIp</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AkIkeGateway

IKE gateway name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AkIpsecCryptoProfile

IPSec crypto profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiReplay

Set to `true` to enable Anti-Replay check
on this tunnel.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyFlowLabel

Set to `true` to copy IPv6
flow label for 6in6 tunnel from inner packet to IPSec packet (not recommended).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyTos

Set to `true` to copy IP TOS bits from inner
packet to IPSec packet (not recommended).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Set to `true` to disable this
IPSec tunnel.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

Set to `true` to enable IPv6.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTunnelMonitor

Enable tunnel monitoring on this tunnel.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsCertificateProfile

Profile for authenticating
GlobalProtect gateway certificates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterface

Interface to communicate with portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceFloatingIpIpv4

Floating IPv4
address in HA Active-Active configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceFloatingIpIpv6

Floating IPv6
address in HA Active-Active configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceIpIpv4

specify exact IP address if interface
has multiple addresses (IPv4).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceIpIpv6

specify exact IP address if interface
has multiple addresses (IPv6).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsLocalCertificate

GlobalProtect satellite certificate
file name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPortalAddress

GlobalProtect portal address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPreferIpv6

Prefer to register the
portal in IPv6. Only applicable to FQDN portal-address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPublishConnectedRoutes

Set to `true` to to publish
connected and static routes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPublishRoutes

Specify list of routes to publish
to Global Protect Gateway.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkAuthKey

The auth key for the given auth type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkAuthType

Authentication algorithm.  Valid values are
`md5`, `sha1`, `sha256`, `sha384`, `sha512`, or `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkEspEncryptionKey

The encryption key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkEspEncryptionType

The encryption algorithm.  Valid values
are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, `aes-256-cbc`, or `null`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalAddressFloatingIp

Floating IP address in HA
Active-Active configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalAddressIp

Specify exact IP address if interface
has multiple addresses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalSpi

Outbound SPI, hex format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkProtocol

Manual key protocol.  Valid valies are
`esp` or `ah`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkRemoteAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkRemoteSpi

Inbound SPI, hex format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelInterface

The tunnel interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorDestinationIp

Destination IP to send ICMP probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorProfile

Tunnel monitor profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorProxyId

Which proxy-id (or
proxy-id-v6) the monitoring traffic will use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorSourceIp

Source IP to send ICMP probe.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type.  Valid values are `auto-key` (the default),
`manual-key`, or `global-protect-satellite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### MkAuthKeyEnc

Returns the <code>MkAuthKeyEnc</code> value.

#### MkEspEncryptionKeyEnc

Returns the <code>MkEspEncryptionKeyEnc</code> value.

