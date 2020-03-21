# Terraform::AzureRM::ManagedDisk KeyEncryptionKey

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyurl" title="KeyUrl">KeyUrl</a>" : <i>String</i>,
    "<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keyurl" title="KeyUrl">KeyUrl</a>: <i>String</i>
<a href="#sourcevaultid" title="SourceVaultId">SourceVaultId</a>: <i>String</i>
</pre>

## Properties

#### KeyUrl

The URL to the Key Vault Key used as the Key Encryption Key. This can be found as `id` on the `azurerm_key_vault_key` resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVaultId

The ID of the source Key Vault.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

