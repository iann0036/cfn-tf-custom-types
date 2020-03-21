# Terraform::AzureRM::ManagedDisk EncryptionSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ &lt;a href=&#34;encryptionsettings-diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;, ... ]</i>,
    "<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>" : <i>[ &lt;a href=&#34;encryptionsettings-keyencryptionkey.md&#34;&gt;KeyEncryptionKey&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - &lt;a href=&#34;encryptionsettings-diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;</i>
<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>: <i>
      - &lt;a href=&#34;encryptionsettings-keyencryptionkey.md&#34;&gt;KeyEncryptionKey&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No
_Type_: List of &lt;a href=&#34;encryptionsettings-diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyEncryptionKey

_Required_: No
_Type_: List of &lt;a href=&#34;encryptionsettings-keyencryptionkey.md&#34;&gt;KeyEncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

