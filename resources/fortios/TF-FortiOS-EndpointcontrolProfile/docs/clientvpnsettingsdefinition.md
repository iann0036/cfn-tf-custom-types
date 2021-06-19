# TF::FortiOS::EndpointcontrolProfile ClientVpnSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authmethod" title="AuthMethod">AuthMethod</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#presharedkey" title="PresharedKey">PresharedKey</a>" : <i>String</i>,
    "<a href="#remotegw" title="RemoteGw">RemoteGw</a>" : <i>String</i>,
    "<a href="#sslvpnaccessport" title="SslvpnAccessPort">SslvpnAccessPort</a>" : <i>Double</i>,
    "<a href="#sslvpnrequirecertificate" title="SslvpnRequireCertificate">SslvpnRequireCertificate</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#vpnconfigurationcontent" title="VpnConfigurationContent">VpnConfigurationContent</a>" : <i>String</i>,
    "<a href="#vpnconfigurationname" title="VpnConfigurationName">VpnConfigurationName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authmethod" title="AuthMethod">AuthMethod</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#presharedkey" title="PresharedKey">PresharedKey</a>: <i>String</i>
<a href="#remotegw" title="RemoteGw">RemoteGw</a>: <i>String</i>
<a href="#sslvpnaccessport" title="SslvpnAccessPort">SslvpnAccessPort</a>: <i>Double</i>
<a href="#sslvpnrequirecertificate" title="SslvpnRequireCertificate">SslvpnRequireCertificate</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#vpnconfigurationcontent" title="VpnConfigurationContent">VpnConfigurationContent</a>: <i>String</i>
<a href="#vpnconfigurationname" title="VpnConfigurationName">VpnConfigurationName</a>: <i>String</i>
</pre>

## Properties

#### AuthMethod

Authentication method. Valid values: `psk`, `certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

VPN name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PresharedKey

Pre-shared secret for PSK authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGw

IP address or FQDN of the remote VPN gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnAccessPort

SSL VPN access port (1 - 65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnRequireCertificate

Enable/disable requiring SSL VPN client certificate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

VPN type (IPsec or SSL VPN). Valid values: `ipsec`, `ssl`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnConfigurationContent

Content of VPN configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnConfigurationName

Name of VPN configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

