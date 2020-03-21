# Terraform::AWS::FsxWindowsFileSystem

CloudFormation equivalent of aws_fsx_windows_file_system

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticBackupRetentionDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyTagsToBackups

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DailyAutomaticBackupStartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipFinalBackup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputCapacity

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeeklyMaintenanceStartTime

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

#### NetworkInterfaceIds

Returns the <code>NetworkInterfaceIds</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

