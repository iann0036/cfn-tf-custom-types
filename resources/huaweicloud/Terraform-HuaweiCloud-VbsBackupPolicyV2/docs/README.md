# Terraform::HuaweiCloud::VbsBackupPolicyV2

Provides an VBS Backup Policy resource.

# Example Usage

 ```hcl
resource "huaweicloud_vbs_backup_policy_v2" "vbs" {
  name                = "policy_002"
  start_time          = "12:00"
  status              = "ON"
  retain_first_backup = "N"
  rentention_num      = 2
  frequency           = 1
  tags = [
    {
      key   = "k1"
      value = "v1"
  }]
}
 ```

# Argument Reference

The following arguments are supported:

* `name` (Required) - Specifies the policy name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), and hyphens (-). It cannot start with default.

* `start_time` (Required) - Specifies the start time of the backup job.The value is in the HH:mm format.                                                         

* `status` (Required) - Specifies the backup policy status. The value can ON or OFF.

* `retain_first_backup` (Required) - Specifies whether to retain the first backup in the current month. Possible values are Y or N. 

* `rentention_num` (Required) - Specifies number of retained backups. Minimum value is 2.

* `frequency` (Required) - Specifies the backup interval. The value is in the range of 1 to 14 days.

**tags** **- (Optional)** Represents the list of tags to be configured for the backup policy.

* `key` - (Required) Specifies the tag key. A tag key consists of up to 36 characters, chosen from letters, digits, hyphens (-), and underscores (_).

* `value` - (Required) Specifies the tag value. A tag value consists of 0 to 43 characters, chosen from letters, digits, hyphens (-), and underscores (_).


# Attributes Reference

All of the argument attributes are also exported as
result attributes:

* `id` - Specifies a backup policy ID.
 
* `policy_resource_count` - Specifies the number of volumes associated with the backup policy.

# Import

Backup Policy can be imported using the `id`, e.g.

```
$ terraform import huaweicloud_vbs_backup_policy_v2.vbs 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::VbsBackupPolicyV2",
    "Properties" : {
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#rententionnum" title="RententionNum">RententionNum</a>" : <i>Double</i>,
        "<a href="#retainfirstbackup" title="RetainFirstBackup">RetainFirstBackup</a>" : <i>String</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::VbsBackupPolicyV2
Properties:
    <a href="#frequency" title="Frequency">Frequency</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#rententionnum" title="RententionNum">RententionNum</a>: <i>Double</i>
    <a href="#retainfirstbackup" title="RetainFirstBackup">RetainFirstBackup</a>: <i>String</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Frequency

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RententionNum

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainFirstBackup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

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

#### PolicyResourceCount

Returns the <code>PolicyResourceCount</code> value.

