# TF::AzureStack::VirtualNetworkGateway VpnClientConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressspace" title="AddressSpace">AddressSpace</a>" : <i>[ String, ... ]</i>,
    "<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>" : <i>[ <a href="revokedcertificatedefinition.md">RevokedCertificateDefinition</a>, ... ]</i>,
    "<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>" : <i>[ <a href="rootcertificatedefinition.md">RootCertificateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addressspace" title="AddressSpace">AddressSpace</a>: <i>
      - String</i>
<a href="#vpnclientprotocols" title="VpnClientProtocols">VpnClientProtocols</a>: <i>
      - String</i>
<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>: <i>
      - <a href="revokedcertificatedefinition.md">RevokedCertificateDefinition</a></i>
<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>: <i>
      - <a href="rootcertificatedefinition.md">RootCertificateDefinition</a></i>
</pre>

## Properties

#### AddressSpace

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientProtocols

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

