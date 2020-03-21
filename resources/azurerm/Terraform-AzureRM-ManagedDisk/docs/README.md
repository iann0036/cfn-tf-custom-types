# Terraform::AzureRM::ManagedDisk

Manages a managed disk.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ManagedDisk",
    "Properties" : {
        "<a href="#createoption" title="CreateOption">CreateOption</a>" : <i>String</i>,
        "<a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>" : <i>String</i>,
        "<a href="#diskiopsreadwrite" title="DiskIopsReadWrite">DiskIopsReadWrite</a>" : <i>Double</i>,
        "<a href="#diskmbpsreadwrite" title="DiskMbpsReadWrite">DiskMbpsReadWrite</a>" : <i>Double</i>,
        "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
        "<a href="#imagereferenceid" title="ImageReferenceId">ImageReferenceId</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sourceresourceid" title="SourceResourceId">SourceResourceId</a>" : <i>String</i>,
        "<a href="#sourceuri" title="SourceUri">SourceUri</a>" : <i>String</i>,
        "<a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>" : <i>String</i>,
        "<a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#zones" title="Zones">Zones</a>" : <i>[ String, ... ]</i>,
        "<a href="#encryptionsettings" title="EncryptionSettings">EncryptionSettings</a>" : <i>[ <a href="encryptionsettings.md">EncryptionSettings</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="diskencryptionkey.md">DiskEncryptionKey</a>, ... ]</i>,
        "<a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>" : <i>[ <a href="keyencryptionkey.md">KeyEncryptionKey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ManagedDisk
Properties:
    <a href="#createoption" title="CreateOption">CreateOption</a>: <i>String</i>
    <a href="#diskencryptionsetid" title="DiskEncryptionSetId">DiskEncryptionSetId</a>: <i>String</i>
    <a href="#diskiopsreadwrite" title="DiskIopsReadWrite">DiskIopsReadWrite</a>: <i>Double</i>
    <a href="#diskmbpsreadwrite" title="DiskMbpsReadWrite">DiskMbpsReadWrite</a>: <i>Double</i>
    <a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
    <a href="#imagereferenceid" title="ImageReferenceId">ImageReferenceId</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sourceresourceid" title="SourceResourceId">SourceResourceId</a>: <i>String</i>
    <a href="#sourceuri" title="SourceUri">SourceUri</a>: <i>String</i>
    <a href="#storageaccountid" title="StorageAccountId">StorageAccountId</a>: <i>String</i>
    <a href="#storageaccounttype" title="StorageAccountType">StorageAccountType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#zones" title="Zones">Zones</a>: <i>
      - String</i>
    <a href="#encryptionsettings" title="EncryptionSettings">EncryptionSettings</a>: <i>
      - <a href="encryptionsettings.md">EncryptionSettings</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="diskencryptionkey.md">DiskEncryptionKey</a></i>
    <a href="#keyencryptionkey" title="KeyEncryptionKey">KeyEncryptionKey</a>: <i>
      - <a href="keyencryptionkey.md">KeyEncryptionKey</a></i>
</pre>

## Properties

#### CreateOption

The method to use when creating the managed disk. Changing this forces a new resource to be created. Possible values include:
* `Import` - Import a VHD file in to the managed disk (VHD specified with `source_uri`).
* `Empty` - Create an empty managed disk.
* `Copy` - Copy an existing managed disk or snapshot (specified with `source_resource_id`).
* `FromImage` - Copy a Platform Image (specified with `image_reference_id`)
* `Restore` - Set by Azure Backup or Site Recovery on a restored disk (specified with `source_resource_id`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionSetId

The ID of a Disk Encryption Set which should be used to encrypt this Managed Disk. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskIopsReadWrite

The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskMbpsReadWrite

The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

Specifies the size of the managed disk to create in gigabytes. If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageReferenceId

ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Managed Disk. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

Specify a value when the source of an `Import` or `Copy` operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the Managed Disk should exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceResourceId

The ID of an existing Managed Disk to copy `create_option` is `Copy` or the recovery point to restore when `create_option` is `Restore`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUri

URI to a valid VHD file to be used when `create_option` is `Import`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountId

The ID of the Storage Account where the `source_uri` is located. Required when `create_option` is set to `Import`.  Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageAccountType

The type of storage to use for the managed disk. Possible values are `Standard_LRS`, `Premium_LRS`, `StandardSSD_LRS` or `UltraSSD_LRS`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

A collection containing the availability zone to allocate the Managed Disk in.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionSettings

_Required_: No

_Type_: List of <a href="encryptionsettings.md">EncryptionSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="diskencryptionkey.md">DiskEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyEncryptionKey

_Required_: No

_Type_: List of <a href="keyencryptionkey.md">KeyEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

