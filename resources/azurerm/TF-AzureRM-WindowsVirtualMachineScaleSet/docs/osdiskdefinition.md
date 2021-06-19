# TF::AzureRM::WindowsVirtualMachineScaleSet OsDiskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>,
    "<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>" : <i>Boolean</i>,
    "<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>" : <i>[ <a href="diffdisksettingsdefinition.md">DiffDiskSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>: <i>Boolean</i>
<a href="#diffdisksettings" title="DiffDiskSettings">DiffDiskSettings</a>: <i>
      - <a href="diffdisksettingsdefinition.md">DiffDiskSettingsDefinition</a></i>
</pre>

## Properties

#### Caching

The Type of Caching which should be used for the Internal OS Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionSetId

The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

The Type of Storage Account which should back this the Internal OS Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS` and `Premium_LRS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcceleratorEnabled

Should Write Accelerator be Enabled for this OS Disk? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiffDiskSettings

_Required_: No

_Type_: List of <a href="diffdisksettingsdefinition.md">DiffDiskSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

