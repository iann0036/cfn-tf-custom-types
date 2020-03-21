# Terraform::Google::ComputeInstance BootDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autodelete" title="AutoDelete">AutoDelete</a>" : <i>Boolean</i>,
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>" : <i>String</i>,
    "<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#initializeparams" title="InitializeParams">InitializeParams</a>" : <i>[ <a href="bootdisk-initializeparams.md">InitializeParams</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autodelete" title="AutoDelete">AutoDelete</a>: <i>Boolean</i>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>: <i>String</i>
<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#initializeparams" title="InitializeParams">InitializeParams</a>: <i>
      - <a href="bootdisk-initializeparams.md">InitializeParams</a></i>
</pre>

## Properties

#### AutoDelete

Whether the disk will be auto-deleted when the instance
is deleted. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceName

Name with which attached disk will be accessible.
On the instance, this device will be `/dev/disk/by-id/google-{{device_name}}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKeyRaw

A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw`
may be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeySelfLink

The self_link of the encryption key that is
stored in Google Cloud KMS to encrypt this disk. Only one of `kms_key_self_link`
and `disk_encryption_key_raw` may be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The mode in which to attach this disk, either `READ_WRITE`
or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The name or self_link of the existing disk (such as those managed by
`google_compute_disk`) or disk image. To create an instance from a snapshot, first create a
`google_compute_disk` from a snapshot and reference it here.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitializeParams

_Required_: No

_Type_: List of <a href="bootdisk-initializeparams.md">InitializeParams</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

