# TF::AzureStack::VirtualMachineScaleSet OsProfileSecretsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>" : <i>String</i>,
    "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ <a href="vaultcertificatesdefinition.md">VaultCertificatesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>: <i>String</i>
<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - <a href="vaultcertificatesdefinition.md">VaultCertificatesDefinition</a></i>
</pre>

## Properties

#### SourceVaultId

Specifies the key vault to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultCertificates

_Required_: No

_Type_: List of <a href="vaultcertificatesdefinition.md">VaultCertificatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

