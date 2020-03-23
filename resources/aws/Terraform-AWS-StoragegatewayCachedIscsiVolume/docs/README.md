# Terraform::AWS::StoragegatewayCachedIscsiVolume

Manages an AWS Storage Gateway cached iSCSI volume.

~> **NOTE:** The gateway must have cache added (e.g. via the [`aws_storagegateway_cache`](/docs/providers/aws/r/storagegateway_cache.html) resource) before creating volumes otherwise the Storage Gateway API will return an error.

~> **NOTE:** The gateway must have an upload buffer added (e.g. via the [`aws_storagegateway_upload_buffer`](/docs/providers/aws/r/storagegateway_upload_buffer.html) resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as `UPLOAD BUFFER NOT CONFIGURED`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::StoragegatewayCachedIscsiVolume",
    "Properties" : {
        "<a href="#gatewayarn" title="GatewayArn">GatewayArn</a>" : <i>String</i>,
        "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#sourcevolumearn" title="SourceVolumeArn">SourceVolumeArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#targetname" title="TargetName">TargetName</a>" : <i>String</i>,
        "<a href="#volumesizeinbytes" title="VolumeSizeInBytes">VolumeSizeInBytes</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::StoragegatewayCachedIscsiVolume
Properties:
    <a href="#gatewayarn" title="GatewayArn">GatewayArn</a>: <i>String</i>
    <a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#sourcevolumearn" title="SourceVolumeArn">SourceVolumeArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#targetname" title="TargetName">TargetName</a>: <i>String</i>
    <a href="#volumesizeinbytes" title="VolumeSizeInBytes">VolumeSizeInBytes</a>: <i>Double</i>
</pre>

## Properties

#### GatewayArn

The Amazon Resource Name (ARN) of the gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceId

The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVolumeArn

The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetName

The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeSizeInBytes

The size of the volume in bytes.

_Required_: Yes

_Type_: Double

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

#### VolumeArn

Returns the <code>VolumeArn</code> value.

#### VolumeId

Returns the <code>VolumeId</code> value.

