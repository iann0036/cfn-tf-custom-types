# Terraform::AzureStack::VirtualMachine StorageDataDisk

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
    "<a href="#vhduri" title="VhdUri">VhdUri</a>" : <i>String</i>
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
</pre>

## Properties

#### Caching

Specifies the caching requirements.

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

Specifies the logical unit number of the data disk.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskId

Specifies the ID of an Existing Managed Disk which should be attached to this Virtual Machine. When this field is set `create_option` must be set to `Attach`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskType

Specifies the type of managed disk to create. Possible values are either `Standard_LRS` or `Premium_LRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the data disk.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhdUri

Specifies the URI of the VHD file backing this Unmanaged Data Disk. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

