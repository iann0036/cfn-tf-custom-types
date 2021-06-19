# TF::AWS::FsxWindowsFileSystem

Manages a FSx Windows File System. See the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) for more information.

~> **NOTE:** Either the `active_directory_id` argument or `self_managed_active_directory` configuration block must be specified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::FsxWindowsFileSystem",
    "Properties" : {
        "<a href="#activedirectoryid" title="ActiveDirectoryId">ActiveDirectoryId</a>" : <i>String</i>,
        "<a href="#automaticbackupretentiondays" title="AutomaticBackupRetentionDays">AutomaticBackupRetentionDays</a>" : <i>Double</i>,
        "<a href="#copytagstobackups" title="CopyTagsToBackups">CopyTagsToBackups</a>" : <i>Boolean</i>,
        "<a href="#dailyautomaticbackupstarttime" title="DailyAutomaticBackupStartTime">DailyAutomaticBackupStartTime</a>" : <i>String</i>,
        "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#preferredsubnetid" title="PreferredSubnetId">PreferredSubnetId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#skipfinalbackup" title="SkipFinalBackup">SkipFinalBackup</a>" : <i>Boolean</i>,
        "<a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>" : <i>Double</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#throughputcapacity" title="ThroughputCapacity">ThroughputCapacity</a>" : <i>Double</i>,
        "<a href="#weeklymaintenancestarttime" title="WeeklyMaintenanceStartTime">WeeklyMaintenanceStartTime</a>" : <i>String</i>,
        "<a href="#selfmanagedactivedirectory" title="SelfManagedActiveDirectory">SelfManagedActiveDirectory</a>" : <i>[ <a href="selfmanagedactivedirectorydefinition.md">SelfManagedActiveDirectoryDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::FsxWindowsFileSystem
Properties:
    <a href="#activedirectoryid" title="ActiveDirectoryId">ActiveDirectoryId</a>: <i>String</i>
    <a href="#automaticbackupretentiondays" title="AutomaticBackupRetentionDays">AutomaticBackupRetentionDays</a>: <i>Double</i>
    <a href="#copytagstobackups" title="CopyTagsToBackups">CopyTagsToBackups</a>: <i>Boolean</i>
    <a href="#dailyautomaticbackupstarttime" title="DailyAutomaticBackupStartTime">DailyAutomaticBackupStartTime</a>: <i>String</i>
    <a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#preferredsubnetid" title="PreferredSubnetId">PreferredSubnetId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#skipfinalbackup" title="SkipFinalBackup">SkipFinalBackup</a>: <i>Boolean</i>
    <a href="#storagecapacity" title="StorageCapacity">StorageCapacity</a>: <i>Double</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#throughputcapacity" title="ThroughputCapacity">ThroughputCapacity</a>: <i>Double</i>
    <a href="#weeklymaintenancestarttime" title="WeeklyMaintenanceStartTime">WeeklyMaintenanceStartTime</a>: <i>String</i>
    <a href="#selfmanagedactivedirectory" title="SelfManagedActiveDirectory">SelfManagedActiveDirectory</a>: <i>
      - <a href="selfmanagedactivedirectorydefinition.md">SelfManagedActiveDirectoryDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ActiveDirectoryId

The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticBackupRetentionDays

The number of days to retain automatic backups. Minimum of `0` and maximum of `90`. Defaults to `7`. Set to `0` to disable.

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

#### DeploymentType

Specifies the file system deployment type, valid values are `MULTI_AZ_1`, `SINGLE_AZ_1` and `SINGLE_AZ_2`. Default value is `SINGLE_AZ_1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredSubnetId

Specifies the subnet in which you want the preferred file server to be located. Required for when deployment type is `MULTI_AZ_1`.

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

Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536. If the storage type is set to `HDD` the minimum value is 2000.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

Specifies the storage type, Valid values are `SSD` and `HDD`. `HDD` is supported on `SINGLE_AZ_2` and `MULTI_AZ_1` Windows file system deployment types. Default value is `SSD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A list of IDs for the subnets that the file system will be accessible from. To specify more than a single subnet set `deployment_type` to `MULTI_AZ_1`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the file system. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

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

_Type_: List of <a href="selfmanagedactivedirectorydefinition.md">SelfManagedActiveDirectoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### PreferredFileServerIp

Returns the <code>PreferredFileServerIp</code> value.

#### RemoteAdministrationEndpoint

Returns the <code>RemoteAdministrationEndpoint</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

