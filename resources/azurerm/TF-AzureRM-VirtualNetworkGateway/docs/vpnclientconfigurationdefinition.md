# TF::AzureRM::VirtualNetworkGateway VpnClientConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aadaudience" title="AadAudience">AadAudience</a>" : <i>String</i>,
    "<a href="#aadissuer" title="AadIssuer">AadIssuer</a>" : <i>String</i>,
    "<a href="#aadtenant" title="AadTenant">AadTenant</a>" : <i>String</i>,
    "<a href="#addressspace" title="AddressSpace">AddressSpace</a>" : <i>[ String, ... ]</i>,
    "<a href="#radiusserveraddress" title="RadiusServerAddress">RadiusServerAddress</a>" : <i>String</i>,
    "<a href="#radiusserversecret" title="RadiusServerSecret">RadiusServerSecret</a>" : <i>String</i>,
    "<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>" : <i>[ <a href="revokedcertificatedefinition.md">RevokedCertificateDefinition</a>, ... ]</i>,
    "<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>" : <i>[ <a href="rootcertificatedefinition.md">RootCertificateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aadaudience" title="AadAudience">AadAudience</a>: <i>String</i>
<a href="#aadissuer" title="AadIssuer">AadIssuer</a>: <i>String</i>
<a href="#aadtenant" title="AadTenant">AadTenant</a>: <i>String</i>
<a href="#addressspace" title="AddressSpace">AddressSpace</a>: <i>
      - String</i>
<a href="#radiusserveraddress" title="RadiusServerAddress">RadiusServerAddress</a>: <i>String</i>
<a href="#radiusserversecret" title="RadiusServerSecret">RadiusServerSecret</a>: <i>String</i>
<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>: <i>
      - String</i>
<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>: <i>
      - <a href="revokedcertificatedefinition.md">RevokedCertificateDefinition</a></i>
<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>: <i>
      - <a href="rootcertificatedefinition.md">RootCertificateDefinition</a></i>
</pre>

## Properties

#### AadAudience

The client id of the Azure VPN application.
See [Create an Active Directory (AD) tenant for P2S OpenVPN protocol connections](https://docs.microsoft.com/en-gb/azure/vpn-gateway/openvpn-azure-ad-tenant-multi-app) for values
This setting is incompatible with the use of
`root_certificate` and `revoked_certificate`, `radius_server_address`, and `radius_server_secret`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadIssuer

The STS url for your tenant
This setting is incompatible with the use of
`root_certificate` and `revoked_certificate`, `radius_server_address`, and `radius_server_secret`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AadTenant

AzureAD Tenant URL
This setting is incompatible with the use of
`root_certificate` and `revoked_certificate`, `radius_server_address`, and `radius_server_secret`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressSpace

The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServerAddress

The address of the Radius server.
This setting is incompatible with the use of
`aad_tenant`, `aad_audience`, `aad_issuer`, `root_certificate` and `revoked_certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RadiusServerSecret

The secret used by the Radius server.
This setting is incompatible with the use of
`aad_tenant`, `aad_audience`, `aad_issuer`, `root_certificate` and `revoked_certificate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientProtocols

List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.
Values `SSTP` and `IkeV2` are incompatible with the use of
`aad_tenant`, `aad_audience` and `aad_issuer`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokedCertificate

_Required_: No

_Type_: List of <a href="revokedcertificatedefinition.md">RevokedCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootCertificate

_Required_: No

_Type_: List of <a href="rootcertificatedefinition.md">RootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

