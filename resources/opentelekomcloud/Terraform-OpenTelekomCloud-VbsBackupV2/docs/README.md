# Terraform::OpenTelekomCloud::VbsBackupV2

Provides an VBS Backup resource.
 
# Example Usage

 ```hcl
variable "backup_name" {}

variable "volume_id" {}
 
resource "opentelekomcloud_vbs_backup_v2" "mybackup" {
  volume_id = "${var.volume_id}"
  name = "${var.backup_name}"
}
 ```

# Argument Reference

The following arguments are supported:

* `name` - (Required) The name of the vbs backup. Changing the parameter will create new resource.

* `volume_id` - (Required) The id of the disk to be backed up. Changing the parameter will create new resource.

* `snapshot_id` - (Optional) The snapshot id of the disk to be backed up. Changing the parameter will create new resource.

* `description` - (Optional) The description of the vbs backup. Changing the parameter will create new resource.

**tags** **- (Optional)** List of tags to be configured for the backup resources. Changing the parameter will create new resource.

* `key` - (Required) Specifies the tag key.

* `value` - (Required) Specifies the tag value.

# Attributes Reference

In addition to all arguments above, the following attributes are exported:

* `id` - The id of the vbs backup.

* `container` - The container of the backup.

* `status` - The status of the VBS backup.

* `availability_zone` - The AZ where the backup resides.

* `size` - The size of the vbs backup.

* `service_metadata` - The metadata of the vbs backup.

# Import

VBS Backup can be imported using the `backup id`, e.g.

```
 $ terraform import opentelekomcloud_vbs_backup_v2.mybackup 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::VbsBackupV2",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#volumeid" title="VolumeId">VolumeId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::VbsBackupV2
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#volumeid" title="VolumeId">VolumeId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

#### AvailabilityZone

Returns the <code>AvailabilityZone</code> value.

#### Container

Returns the <code>Container</code> value.

#### Id

Returns the <code>Id</code> value.

#### ServiceMetadata

Returns the <code>ServiceMetadata</code> value.

#### Size

Returns the <code>Size</code> value.

#### Status

Returns the <code>Status</code> value.

