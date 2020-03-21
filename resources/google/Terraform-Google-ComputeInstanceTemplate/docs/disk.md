# Terraform::Google::ComputeInstanceTemplate Disk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
    "<a href="#boot" title="Boot">Boot</a>" : <i>Boolean</i>,
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#diskname" title="DiskName">DiskName</a>" : <i>String</i>,
    "<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="disk-labels.md">Labels</a>, ... ]</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#sourceimage" title="SourceImage">SourceImage</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="disk-diskencryptionkey.md">DiskEncryptionKey</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
<a href="#boot" title="Boot">Boot</a>: <i>Boolean</i>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#diskname" title="DiskName">DiskName</a>: <i>String</i>
<a href="#disksizegb" title="DiskSizeGb">DiskSizeGb</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="disk-labels.md">Labels</a></i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#sourceimage" title="SourceImage">SourceImage</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="disk-diskencryptionkey.md">DiskEncryptionKey</a></i>
</pre>

## Properties

#### AutoDelete

Whether or not the disk should be auto-deleted.
This defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Boot

Indicates that this is a boot disk.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

A unique device name that is reflected into the
/dev/  tree of a Linux operating system running within the instance. If not
specified, the server chooses a default device name to apply to this disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskName

Name of the disk. When not provided, this defaults
to the name of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSizeGb

The size of the image in gigabytes. If not
specified, it will inherit the size of its base image. For SCRATCH disks,
the size must be exactly 375GB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

The GCE disk type. Can be either `"pd-ssd"`,
`"local-ssd"`, or `"pd-standard"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specifies the disk interface to use for attaching
this disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="disk-labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The name (**not self_link**)
of the disk (such as those managed by `google_compute_disk`) to attach.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImage

The image from which to
initialize this disk. This can be one of: the image's `self_link`,
`projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of GCE disk, can be either `"SCRATCH"` or
`"PERSISTENT"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of <a href="disk-diskencryptionkey.md">DiskEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

