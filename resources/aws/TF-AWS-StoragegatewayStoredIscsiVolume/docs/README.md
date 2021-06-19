# TF::AWS::StoragegatewayStoredIscsiVolume

Manages an AWS Storage Gateway stored iSCSI volume.

~> **NOTE:** The gateway must have a working storage added (e.g. via the [`aws_storagegateway_working_storage`](/docs/providers/aws/r/storagegateway_working_storage.html) resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as `WORKING STORAGE NOT CONFIGURED`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::StoragegatewayStoredIscsiVolume",
    "Properties" : {
        "<a href="#diskid" title="DiskId">DiskId</a>" : <i>String</i>,
        "<a href="#gatewayarn" title="GatewayArn">GatewayArn</a>" : <i>String</i>,
        "<a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>" : <i>Boolean</i>,
        "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>,
        "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#preserveexistingdata" title="PreserveExistingData">PreserveExistingData</a>" : <i>Boolean</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#targetname" title="TargetName">TargetName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::StoragegatewayStoredIscsiVolume
Properties:
    <a href="#diskid" title="DiskId">DiskId</a>: <i>String</i>
    <a href="#gatewayarn" title="GatewayArn">GatewayArn</a>: <i>String</i>
    <a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>: <i>Boolean</i>
    <a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
    <a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
    <a href="#preserveexistingdata" title="PreserveExistingData">PreserveExistingData</a>: <i>Boolean</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#targetname" title="TargetName">TargetName</a>: <i>String</i>
</pre>

## Properties

#### DiskId

The unique identifier for the gateway local disk that is configured as a stored volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayArn

The Amazon Resource Name (ARN) of the gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncrypted

`true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Optional.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

The Amazon Resource Name (ARN) of the AWS KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceId

The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveExistingData

Specify this field as `true` if you want to preserve the data on the local disk. Otherwise, specifying this field as false creates an empty volume.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

The snapshot ID of the snapshot to restore as the new stored volume. e.g. `snap-1122aabb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetName

The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ChapEnabled

Returns the <code>ChapEnabled</code> value.

#### Id

Returns the <code>Id</code> value.

#### LunNumber

Returns the <code>LunNumber</code> value.

#### NetworkInterfacePort

Returns the <code>NetworkInterfacePort</code> value.

#### TargetArn

Returns the <code>TargetArn</code> value.

#### VolumeAttachmentStatus

Returns the <code>VolumeAttachmentStatus</code> value.

#### VolumeId

Returns the <code>VolumeId</code> value.

#### VolumeSizeInBytes

Returns the <code>VolumeSizeInBytes</code> value.

#### VolumeStatus

Returns the <code>VolumeStatus</code> value.

#### VolumeType

Returns the <code>VolumeType</code> value.

