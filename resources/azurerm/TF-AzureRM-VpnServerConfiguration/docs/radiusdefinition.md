# TF::AzureRM::VpnServerConfiguration RadiusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a>, ... ]</i>,
    "<a href="#server" title="Server">Server</a>" : <i>[ <a href="serverdefinition.md">ServerDefinition</a>, ... ]</i>,
    "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a></i>
<a href="#server" title="Server">Server</a>: <i>
      - <a href="serverdefinition.md">ServerDefinition</a></i>
<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a></i>
</pre>

## Properties

#### ClientRootCertificate

_Required_: No

_Type_: List of <a href="clientrootcertificatedefinition.md">ClientRootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: List of <a href="serverdefinition.md">ServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No

_Type_: List of <a href="serverrootcertificatedefinition.md">ServerRootCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

