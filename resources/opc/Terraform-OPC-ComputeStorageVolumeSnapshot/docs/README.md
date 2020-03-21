# Terraform::OPC::ComputeStorageVolumeSnapshot

The ``opc_compute_storage_volume_snapshot`` resource creates and manages a storage volume snapshot in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::ComputeStorageVolumeSnapshot",
    "Properties" : {
        "<a href="#collocated" title="Collocated">Collocated</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentvolumebootable" title="ParentVolumeBootable">ParentVolumeBootable</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#volumename" title="VolumeName">VolumeName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::ComputeStorageVolumeSnapshot
Properties:
    <a href="#collocated" title="Collocated">Collocated</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentvolumebootable" title="ParentVolumeBootable">ParentVolumeBootable</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#volumename" title="VolumeName">VolumeName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Collocated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentVolumeBootable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Comma-separated strings that tag the storage volume.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Account

Returns the <code>Account</code> value.

#### MachineImageName

Returns the <code>MachineImageName</code> value.

#### Platform

Returns the <code>Platform</code> value.

#### Property

Returns the <code>Property</code> value.

#### Size

Returns the <code>Size</code> value.

#### SnapshotId

Returns the <code>SnapshotId</code> value.

#### SnapshotTimestamp

Returns the <code>SnapshotTimestamp</code> value.

#### StartTimestamp

Returns the <code>StartTimestamp</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusDetail

Returns the <code>StatusDetail</code> value.

#### StatusTimestamp

Returns the <code>StatusTimestamp</code> value.

#### Uri

Returns the <code>Uri</code> value.

