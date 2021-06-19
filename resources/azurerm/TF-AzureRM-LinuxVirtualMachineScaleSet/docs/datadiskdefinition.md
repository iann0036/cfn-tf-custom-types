# TF::AzureRM::LinuxVirtualMachineScaleSet DataDiskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
    "<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>" : <i>String</i>,
    "<a href="#diskiopsreadwrite" title="DiskIopsReadWrite">DiskIopsReadWrite</a>" : <i>Double</i>,
    "<a href="#diskmbpsreadwrite" title="DiskMbpsReadWrite">DiskMbpsReadWrite</a>" : <i>Double</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#lun" title="Lun">Lun</a>" : <i>Double</i>,
    "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>,
    "<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>: <i>String</i>
<a href="#diskiopsreadwrite" title="DiskIopsReadWrite">DiskIopsReadWrite</a>: <i>Double</i>
<a href="#diskmbpsreadwrite" title="DiskMbpsReadWrite">DiskMbpsReadWrite</a>: <i>Double</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#lun" title="Lun">Lun</a>: <i>Double</i>
<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Caching

The type of Caching which should be used for this Data Disk. Possible values are `None`, `ReadOnly` and `ReadWrite`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOption

The create option which should be used for this Data Disk. Possible values are `Empty` and `FromImage`. Defaults to `Empty`. (`FromImage` should only be used if the source image includes data disks).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionSetId

The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskIopsReadWrite

Specifies the Read-Write IOPS for this Data Disk. Only settable for UltraSSD disks.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskMbpsReadWrite

Specifies the bandwidth in MB per second for this Data Disk. Only settable for UltraSSD disks.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

The size of the Data Disk which should be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lun

The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

The Type of Storage Account which should back this Data Disk. Possible values include `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` and `UltraSSD_LRS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcceleratorEnabled

Should Write Accelerator be enabled for this Data Disk? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

