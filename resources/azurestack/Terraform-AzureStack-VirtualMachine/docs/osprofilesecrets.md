# Terraform::AzureStack::VirtualMachine OsProfileSecrets

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>" : <i>String</i>,
    "<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>" : <i>[ <a href="osprofilesecrets-vaultcertificates.md">VaultCertificates</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>: <i>String</i>
<a href="#vaultcertificates" title="VaultCertificates">VaultCertificates</a>: <i>
      - <a href="osprofilesecrets-vaultcertificates.md">VaultCertificates</a></i>
</pre>

## Properties

#### SourceVaultId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VaultCertificates

_Required_: No

_Type_: List of <a href="osprofilesecrets-vaultcertificates.md">VaultCertificates</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

