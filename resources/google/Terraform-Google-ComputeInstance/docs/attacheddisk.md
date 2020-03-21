# Terraform::Google::ComputeInstance AttachedDisk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#devicename" title="DeviceName">DeviceName</a>" : <i>String</i>,
    "<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>" : <i>String</i>,
    "<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>" : <i>String</i>,
    "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#devicename" title="DeviceName">DeviceName</a>: <i>String</i>
<a href="#diskencryptionkeyraw" title="DiskEncryptionKeyRaw">DiskEncryptionKeyRaw</a>: <i>String</i>
<a href="#kmskeyselflink" title="KmsKeySelfLink">KmsKeySelfLink</a>: <i>String</i>
<a href="#mode" title="Mode">Mode</a>: <i>String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### DeviceName

Name with which the attached disk will be accessible
under `/dev/disk/by-id/google-*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKeyRaw

A 256-bit [customer-supplied encryption key]
(https://cloud.google.com/compute/docs/disks/customer-supplied-encryption),
encoded in [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
to encrypt this disk. Only one of `kms_key_self_link` and `disk_encryption_key_raw` may be set.

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

Either "READ_ONLY" or "READ_WRITE", defaults to "READ_WRITE"
If you have a persistent disk with data that you want to share
between multiple instances, detach it from any read-write instances and
attach it to one or more instances in read-only mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The name or self_link of the disk to attach to this instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

