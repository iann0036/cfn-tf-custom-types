# Terraform::AzureRM::WindowsVirtualMachine OsDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>,
    "<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>" : <i>Boolean</i>,
    "<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>" : <i>[ &lt;a href=&#34;osdisk-diffdisksettings.md&#34;&gt;DiffDiskSettings&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>: <i>Boolean</i>
<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>: <i>
      - &lt;a href=&#34;osdisk-diffdisksettings.md&#34;&gt;DiffDiskSettings&lt;/a&gt;</i>
</pre>

## Properties

#### Caching

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionSetId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcceleratorEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffDiskSettings

_Required_: No
_Type_: List of &lt;a href=&#34;osdisk-diffdisksettings.md&#34;&gt;DiffDiskSettings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

