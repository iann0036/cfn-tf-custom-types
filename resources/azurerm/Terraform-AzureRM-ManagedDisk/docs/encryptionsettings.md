# Terraform::AzureRM::ManagedDisk EncryptionSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="encryptionsettings-diskencryptionkey.md">DiskEncryptionKey</a>, ... ]</i>,
    "<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>" : <i>[ <a href="encryptionsettings-keyencryptionkey.md">KeyEncryptionKey</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="encryptionsettings-diskencryptionkey.md">DiskEncryptionKey</a></i>
<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>: <i>
      - <a href="encryptionsettings-keyencryptionkey.md">KeyEncryptionKey</a></i>
</pre>

## Properties

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="encryptionsettings-diskencryptionkey.md">DiskEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyEncryptionKey

_Required_: No

_Type_: List of <a href="encryptionsettings-keyencryptionkey.md">KeyEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

