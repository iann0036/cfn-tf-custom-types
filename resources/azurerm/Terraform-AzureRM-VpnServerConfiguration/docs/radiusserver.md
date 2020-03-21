# Terraform::AzureRM::VpnServerConfiguration RadiusServer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#secret" title="Secret">Secret</a>" : <i>String</i>,
    "<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>" : <i>[ <a href="radiusserver-clientrootcertificate.md">ClientRootCertificate</a>, ... ]</i>,
    "<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>" : <i>[ <a href="radiusserver-serverrootcertificate.md">ServerRootCertificate</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#secret" title="Secret">Secret</a>: <i>String</i>
<a href="#clientrootcertificate" title="ClientRootCertificate">ClientRootCertificate</a>: <i>
      - <a href="radiusserver-clientrootcertificate.md">ClientRootCertificate</a></i>
<a href="#serverrootcertificate" title="ServerRootCertificate">ServerRootCertificate</a>: <i>
      - <a href="radiusserver-serverrootcertificate.md">ServerRootCertificate</a></i>
</pre>

## Properties

#### Address

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRootCertificate

_Required_: No

_Type_: List of <a href="radiusserver-clientrootcertificate.md">ClientRootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerRootCertificate

_Required_: No

_Type_: List of <a href="radiusserver-serverrootcertificate.md">ServerRootCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

