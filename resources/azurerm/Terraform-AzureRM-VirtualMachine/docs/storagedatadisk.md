# Terraform::AzureRM::VirtualMachine StorageDataDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#lun" title="Lun">Lun</a>" : <i>Double</i>,
    "<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>" : <i>String</i>,
    "<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#vhduri" title="VhdUri">VhdUri</a>" : <i>String</i>,
    "<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#lun" title="Lun">Lun</a>: <i>Double</i>
<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>: <i>String</i>
<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#vhduri" title="VhdUri">VhdUri</a>: <i>String</i>
<a href="#writeacceleratorenabled" title="WriteAcceleratorEnabled">WriteAcceleratorEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Caching

Specifies the caching requirements for the Data Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOption

Specifies how the data disk should be created. Possible values are `Attach`, `FromImage` and `Empty`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

Specifies the size of the data disk in gigabytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lun

Specifies the logical unit number of the data disk. This needs to be unique within all the Data Disks on the Virtual Machine.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskId

Specifies the ID of an Existing Managed Disk which should be attached to this Virtual Machine. When this field is set `create_option` must be set to `Attach`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskType

Specifies the type of managed disk to create. Possible values are either `Standard_LRS`, `StandardSSD_LRS`, `Premium_LRS` or `UltraSSD_LRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Data Disk.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhdUri

Specifies the URI of the VHD file backing this Unmanaged Data Disk. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteAcceleratorEnabled

Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

