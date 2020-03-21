# Terraform::Panos::IpsecTunnel

CloudFormation equivalent of panos_ipsec_tunnel

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::IpsecTunnel",
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
Type: Terraform::Panos::IpsecTunnel
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
    <a href="#tunnelinterface" title="TunnelInterface">TunnelInterface</a>: <i>String</i>
    <a href="#tunnelmonitordestinationip" title="TunnelMonitorDestinationIp">TunnelMonitorDestinationIp</a>: <i>String</i>
    <a href="#tunnelmonitorprofile" title="TunnelMonitorProfile">TunnelMonitorProfile</a>: <i>String</i>
    <a href="#tunnelmonitorproxyid" title="TunnelMonitorProxyId">TunnelMonitorProxyId</a>: <i>String</i>
    <a href="#tunnelmonitorsourceip" title="TunnelMonitorSourceIp">TunnelMonitorSourceIp</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AkIkeGateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AkIpsecCryptoProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiReplay

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyFlowLabel

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyTos

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableIpv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTunnelMonitor

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsCertificateProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceFloatingIpIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceFloatingIpIpv6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceIpIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsInterfaceIpIpv6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsLocalCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPortalAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPreferIpv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPublishConnectedRoutes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpsPublishRoutes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkAuthKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkAuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkEspEncryptionKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkEspEncryptionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkInterface

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalAddressFloatingIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalAddressIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkLocalSpi

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkRemoteAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MkRemoteSpi

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelInterface

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorDestinationIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorProxyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelMonitorSourceIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

#### MkAuthKeyEnc

Returns the <code>MkAuthKeyEnc</code> value.

#### MkEspEncryptionKeyEnc

Returns the <code>MkEspEncryptionKeyEnc</code> value.

