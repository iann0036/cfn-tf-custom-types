# TF::Google::ComputeInstanceTemplate DiskDefinition

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
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#resourcepolicies" title="ResourcePolicies">ResourcePolicies</a>" : <i>[ String, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#sourceimage" title="SourceImage">SourceImage</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>, ... ]</i>
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
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#resourcepolicies" title="ResourcePolicies">ResourcePolicies</a>: <i>
      - String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#sourceimage" title="SourceImage">SourceImage</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a></i>
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
`"local-ssd"`, `"pd-balanced"` or `"pd-standard"`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specifies the disk interface to use for attaching this disk,
which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI
and the request will fail if you attempt to attach a persistent disk in any other format
than SCSI. Local SSDs can use either NVME or SCSI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode in which to attach this disk, either READ_WRITE
or READ_ONLY. If you are attaching or creating a boot disk, this must
read-write mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The name (**not self_link**)
of the disk (such as those managed by `google_compute_disk`) to attach.
~> **Note:** Either `source` or `source_image` is **required** in a disk block unless the disk type is `local-ssd`. Check the API [docs](https://cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) for details.

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
~> **Note:** Either `source` or `source_image` is **required** in a disk block unless the disk type is `local-ssd`. Check the API [docs](https://cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) for details.

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

_Type_: List of <a href="diskencryptionkeydefinition.md">DiskEncryptionKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

