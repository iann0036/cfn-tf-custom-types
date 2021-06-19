# TF::AzureRM::ManagedDisk EncryptionSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>, ... ]</i>,
    "<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>" : <i>[ <a href="keyencryptionkeydefinition.md">KeyEncryptionKeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a></i>
<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>: <i>
      - <a href="keyencryptionkeydefinition.md">KeyEncryptionKeyDefinition</a></i>
</pre>

## Properties

#### Enabled

Is Encryption enabled on this Managed Disk? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyEncryptionKey

_Required_: No

_Type_: List of <a href="keyencryptionkeydefinition.md">KeyEncryptionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

