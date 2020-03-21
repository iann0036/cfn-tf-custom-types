# Terraform::AzureStack::VirtualMachineScaleSet StorageProfileOsDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caching" title="Caching">Caching</a>" : <i>String</i>,
    "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
    "<a href="#vhdcontainers" title="VhdContainers">VhdContainers</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#caching" title="Caching">Caching</a>: <i>String</i>
<a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#manageddisktype" title="ManagedDiskType">ManagedDiskType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#ostype" title="OsType">OsType</a>: <i>String</i>
<a href="#vhdcontainers" title="VhdContainers">VhdContainers</a>: <i>
      - String</i>
</pre>

## Properties

#### Caching

Specifies the caching requirements. Possible values include: `None` (default), `ReadOnly`, `ReadWrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateOption

Specifies how the virtual machine should be created. The only possible option is `FromImage`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

Specifies the blob uri for user image. A virtual machine scale set creates an os disk in the same container as the user image.
Updating the osDisk image causes the existing disk to be deleted and a new one created with the new image. If the VM scale set is in Manual upgrade mode then the virtual machines are not updated until they have manualUpgrade applied to them.
When setting this field `os_type` needs to be specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedDiskType

Specifies the type of managed disk to create. Value you must be either `Standard_LRS` or `Premium_LRS`. Cannot be used when `vhd_containers` or `image` is specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the disk name. Must be specified when using unmanaged disk ('managed_disk_type' property not set).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Specifies the operating system Type, valid values are windows, linux.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VhdContainers

Specifies the vhd uri. Cannot be used when `image` or `managed_disk_type` is specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

