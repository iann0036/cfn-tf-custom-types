# Terraform::AzureStack::VirtualMachine StorageOsDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#imageuri" title="ImageUri">ImageUri</a>" : <i>String</i>,
    "<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>" : <i>String</i>,
    "<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
    "<a href="#vhduri" title="VhdUri">VhdUri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#imageuri" title="ImageUri">ImageUri</a>: <i>String</i>
<a href="#manageddiskid" title="ManagedDiskId">ManagedDiskId</a>: <i>String</i>
<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#ostype" title="OsType">OsType</a>: <i>String</i>
<a href="#vhduri" title="VhdUri">VhdUri</a>: <i>String</i>
</pre>

## Properties

#### Caching

Specifies the caching requirements for the OS Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOption

Specifies how the OS Disk should be created. Possible values are `Attach` (managed disks only) and `FromImage`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

Specifies the size of the os disk in gigabytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageUri

Specifies the image_uri in the form publisherName:offer:skus:version. `image_uri` can also specify the [VHD uri](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image) of a custom VM image to clone. When cloning a custom disk image the `os_type` documented below becomes required.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskId

Specifies the ID of an existing Managed Disk which should be attached as the OS Disk of this Virtual Machine. If this is set then the `create_option` must be set to `Attach`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskType

Specifies the type of Managed Disk which should be created. Possible values are `Standard_LRS` or `Premium_LRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the disk name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Specifies the Operating System on the OS Disk. Possible values are `Linux` and `Windows`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhdUri

Specifies the URI of the VHD file backing this Unmanaged OS Disk. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

