# Terraform::OpenTelekomCloud::VbsBackupShareV2

Provides an VBS Backup Share resource.
 
# Example Usage

 ```hcl
variable "backup_id" {}

variable "to_project_ids" {}
 
resource "opentelekomcloud_vbs_backup_share_v2" "backupshare" {
  backup_id = "${var.backup_id}"
  to_project_ids = "${var.to_project_ids}"
}
 ```

# Argument Reference

The following arguments are supported:

* `backup_id` - (Required) The ID of the backup to be shared. Changing the parameter will create new resource.

* `to_project_ids` - (Required) The IDs of projects with which the backup is shared. Changing the parameter will create new resource.

# Attributes Reference

In addition to all arguments above, the following attributes are exported:

* `container` - The container of the backup.

* `backup_status` - The status of the VBS backup.

* `description` - The status of the VBS backup.

* `availability_zone` - The AZ where the backup resides.

* `size` - The size of the vbs backup.

* `backup_name` - The backup name.

* `snapshot_id` - The ID of the snapshot associated with the backup.

* `volume_id` - The ID of the tenant to which the backup belongs.

* `share_ids` - The backup share IDs.

* `service_metadata` - The metadata of the vbs backup.

# Import

VBS Backup Share can be imported using the `backup id`, e.g.

```
 $ terraform import opentelekomcloud_vbs_backup_share_v2.backupshare 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::VbsBackupShareV2",
    "Properties" : {
        "<a href="#backupid" title="BackupId">BackupId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#toprojectids" title="ToProjectIds">ToProjectIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::VbsBackupShareV2
Properties:
    <a href="#backupid" title="BackupId">BackupId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#toprojectids" title="ToProjectIds">ToProjectIds</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BackupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToProjectIds

_Required_: Yes

_Type_: List of String

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

#### BackupName

Returns the <code>BackupName</code> value.

#### BackupStatus

Returns the <code>BackupStatus</code> value.

#### Container

Returns the <code>Container</code> value.

#### Description

Returns the <code>Description</code> value.

#### ServiceMetadata

Returns the <code>ServiceMetadata</code> value.

#### ShareIds

Returns the <code>ShareIds</code> value.

#### Size

Returns the <code>Size</code> value.

#### SnapshotId

Returns the <code>SnapshotId</code> value.

#### VolumeId

Returns the <code>VolumeId</code> value.

