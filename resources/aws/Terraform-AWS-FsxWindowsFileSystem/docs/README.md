# Terraform::AWS::FsxWindowsFileSystem

Manages a FSx Windows File System. See the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) for more information.

~> **NOTE:** Either the `active_directory_id` argument or `self_managed_active_directory` configuration block must be specified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::FsxWindowsFileSystem",
    "Properties" : {
        "<a href="#activedirectoryid" title="ActiveDirectoryId">ActiveDirectoryId</a>" : <i>String</i>,
        "<a href="#automaticbackupretentiondays" title="AutomaticBackupRetentionDays">AutomaticBackupRetentionDays</a>" : <i>Double</i>,
        "<a href="#copytagstobackups" title="CopyTagsToBackups">CopyTagsToBackups</a>" : <i>Boolean</i>,
        "<a href="#dailyautomaticbackupstarttime" title="DailyAutomaticBackupStartTime">DailyAutomaticBackupStartTime</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#skipfinalbackup" title="SkipFinalBackup">SkipFinalBackup</a>" : <i>Boolean</i>,
        "<a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>" : <i>Double</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#throughputcapacity" title="ThroughputCapacity">ThroughputCapacity</a>" : <i>Double</i>,
        "<a href="#weeklymaintenancestarttime" title="WeeklyMaintenanceStartTime">WeeklyMaintenanceStartTime</a>" : <i>String</i>,
        "<a href="#selfmanagedactivedirectory" title="SelfManagedActiveDirectory">SelfManagedActiveDirectory</a>" : <i>[ <a href="selfmanagedactivedirectory.md">SelfManagedActiveDirectory</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::FsxWindowsFileSystem
Properties:
    <a href="#activedirectoryid" title="ActiveDirectoryId">ActiveDirectoryId</a>: <i>String</i>
    <a href="#automaticbackupretentiondays" title="AutomaticBackupRetentionDays">AutomaticBackupRetentionDays</a>: <i>Double</i>
    <a href="#copytagstobackups" title="CopyTagsToBackups">CopyTagsToBackups</a>: <i>Boolean</i>
    <a href="#dailyautomaticbackupstarttime" title="DailyAutomaticBackupStartTime">DailyAutomaticBackupStartTime</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#skipfinalbackup" title="SkipFinalBackup">SkipFinalBackup</a>: <i>Boolean</i>
    <a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>: <i>Double</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#throughputcapacity" title="ThroughputCapacity">ThroughputCapacity</a>: <i>Double</i>
    <a href="#weeklymaintenancestarttime" title="WeeklyMaintenanceStartTime">WeeklyMaintenanceStartTime</a>: <i>String</i>
    <a href="#selfmanagedactivedirectory" title="SelfManagedActiveDirectory">SelfManagedActiveDirectory</a>: <i>
      - <a href="selfmanagedactivedirectory.md">SelfManagedActiveDirectory</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ActiveDirectoryId

The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticBackupRetentionDays

The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyTagsToBackups

A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyAutomaticBackupStartTime

The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipFinalBackup

When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCapacity

Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the file system.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputCapacity

Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyMaintenanceStartTime

The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfManagedActiveDirectory

_Required_: No

_Type_: List of <a href="selfmanagedactivedirectory.md">SelfManagedActiveDirectory</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetworkInterfaceIds

Returns the <code>NetworkInterfaceIds</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

