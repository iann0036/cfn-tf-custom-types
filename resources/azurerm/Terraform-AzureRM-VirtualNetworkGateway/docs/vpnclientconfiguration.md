# Terraform::AzureRM::VirtualNetworkGateway VpnClientConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressspace" title="AddressSpace">AddressSpace</a>" : <i>[ String, ... ]</i>,
    "<a href="#radiusserveraddress" title="RadiusServerAddress">RadiusServerAddress</a>" : <i>String</i>,
    "<a href="#radiusserversecret" title="RadiusServerSecret">RadiusServerSecret</a>" : <i>String</i>,
    "<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>" : <i>[ <a href="vpnclientconfiguration-revokedcertificate.md">RevokedCertificate</a>, ... ]</i>,
    "<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>" : <i>[ <a href="vpnclientconfiguration-rootcertificate.md">RootCertificate</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addressspace" title="AddressSpace">AddressSpace</a>: <i>
      - String</i>
<a href="#radiusserveraddress" title="RadiusServerAddress">RadiusServerAddress</a>: <i>String</i>
<a href="#radiusserversecret" title="RadiusServerSecret">RadiusServerSecret</a>: <i>String</i>
<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>: <i>
      - String</i>
<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>: <i>
      - <a href="vpnclientconfiguration-revokedcertificate.md">RevokedCertificate</a></i>
<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>: <i>
      - <a href="vpnclientconfiguration-rootcertificate.md">RootCertificate</a></i>
</pre>

## Properties

#### AddressSpace

The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServerAddress

The address of the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServerSecret

The secret used by the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientProtocols

List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokedCertificate

_Required_: No

_Type_: List of <a href="vpnclientconfiguration-revokedcertificate.md">RevokedCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootCertificate

_Required_: No

_Type_: List of <a href="vpnclientconfiguration-rootcertificate.md">RootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

