# TF::Alicloud::Instance

Provides a ECS instance resource.

-> **NOTE:** You can launch an ECS instance for a VPC network via specifying parameter `vswitch_id`. One instance can only belong to one VSwitch.

-> **NOTE:** If a VSwitchId is specified for creating an instance, SecurityGroupId and VSwitchId must belong to one VPC, VSwitchId Cannot be modified after creation.

-> **NOTE:** Several instance types have outdated in some regions and availability zones, such as `ecs.t1.*`, `ecs.s2.*`, `ecs.n1.*` and so on. If you want to keep them, you should set `is_outdated` to true. For more about the upgraded instance type, refer to `alicloud_instance_types` datasource.

-> **NOTE:** At present, 'PrePaid' instance cannot be deleted and must wait it to be outdated and release it automatically.

-> **NOTE:** The resource supports modifying instance charge type from 'PrePaid' to 'PostPaid' from version 1.9.6.
 However, at present, this modification has some limitation about CPU core count in one month, so strongly recommand that `Don't mod...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::Instance",
    "Properties" : {
        "<a href="#allocatepublicip" title="AllocatePublicIp">AllocatePublicIp</a>" : <i>Boolean</i>,
        "<a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>" : <i>String</i>,
        "<a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>" : <i>Double</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>Boolean</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#includedatadisks" title="IncludeDataDisks">IncludeDataDisks</a>" : <i>Boolean</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#internetmaxbandwidthin" title="InternetMaxBandwidthIn">InternetMaxBandwidthIn</a>" : <i>Double</i>,
        "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
        "<a href="#iooptimized" title="IoOptimized">IoOptimized</a>" : <i>String</i>,
        "<a href="#isoutdated" title="IsOutdated">IsOutdated</a>" : <i>Boolean</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#periodunit" title="PeriodUnit">PeriodUnit</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#securityenhancementstrategy" title="SecurityEnhancementStrategy">SecurityEnhancementStrategy</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#spotpricelimit" title="SpotPriceLimit">SpotPriceLimit</a>" : <i>Double</i>,
        "<a href="#spotstrategy" title="SpotStrategy">SpotStrategy</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#systemdiskautosnapshotpolicyid" title="SystemDiskAutoSnapshotPolicyId">SystemDiskAutoSnapshotPolicyId</a>" : <i>String</i>,
        "<a href="#systemdiskcategory" title="SystemDiskCategory">SystemDiskCategory</a>" : <i>String</i>,
        "<a href="#systemdiskdescription" title="SystemDiskDescription">SystemDiskDescription</a>" : <i>String</i>,
        "<a href="#systemdiskname" title="SystemDiskName">SystemDiskName</a>" : <i>String</i>,
        "<a href="#systemdiskperformancelevel" title="SystemDiskPerformanceLevel">SystemDiskPerformanceLevel</a>" : <i>String</i>,
        "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#volumetags" title="VolumeTags">VolumeTags</a>" : <i>[ <a href="volumetagsdefinition.md">VolumeTagsDefinition</a>, ... ]</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#datadisks" title="DataDisks">DataDisks</a>" : <i>[ <a href="datadisksdefinition.md">DataDisksDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::Instance
Properties:
    <a href="#allocatepublicip" title="AllocatePublicIp">AllocatePublicIp</a>: <i>Boolean</i>
    <a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>: <i>String</i>
    <a href="#autorenewperiod" title="AutoRenewPeriod">AutoRenewPeriod</a>: <i>Double</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>Boolean</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#hostname" title="HostName">HostName</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#includedatadisks" title="IncludeDataDisks">IncludeDataDisks</a>: <i>Boolean</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#internetmaxbandwidthin" title="InternetMaxBandwidthIn">InternetMaxBandwidthIn</a>: <i>Double</i>
    <a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
    <a href="#iooptimized" title="IoOptimized">IoOptimized</a>: <i>String</i>
    <a href="#isoutdated" title="IsOutdated">IsOutdated</a>: <i>Boolean</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a></i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#periodunit" title="PeriodUnit">PeriodUnit</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#renewalstatus" title="RenewalStatus">RenewalStatus</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#securityenhancementstrategy" title="SecurityEnhancementStrategy">SecurityEnhancementStrategy</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#spotpricelimit" title="SpotPriceLimit">SpotPriceLimit</a>: <i>Double</i>
    <a href="#spotstrategy" title="SpotStrategy">SpotStrategy</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#systemdiskautosnapshotpolicyid" title="SystemDiskAutoSnapshotPolicyId">SystemDiskAutoSnapshotPolicyId</a>: <i>String</i>
    <a href="#systemdiskcategory" title="SystemDiskCategory">SystemDiskCategory</a>: <i>String</i>
    <a href="#systemdiskdescription" title="SystemDiskDescription">SystemDiskDescription</a>: <i>String</i>
    <a href="#systemdiskname" title="SystemDiskName">SystemDiskName</a>: <i>String</i>
    <a href="#systemdiskperformancelevel" title="SystemDiskPerformanceLevel">SystemDiskPerformanceLevel</a>: <i>String</i>
    <a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#volumetags" title="VolumeTags">VolumeTags</a>: <i>
      - <a href="volumetagsdefinition.md">VolumeTagsDefinition</a></i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#datadisks" title="DataDisks">DataDisks</a>: <i>
      - <a href="datadisksdefinition.md">DataDisksDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllocatePublicIp

It has been deprecated from version "1.7.0". Setting "internet_max_bandwidth_out" larger than 0 can allocate a public ip address for an instance.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoReleaseTime

The automatic release time of the `PostPaid` instance.
The time follows the ISO 8601 standard and is in UTC time. Format: yyyy-MM-ddTHH:mm:ssZ. It must be at least half an hour later than the current time and less than 3 years since the current time.
Set it to null can cancel automatic release attribute and the ECS instance will not be released automatically.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenewPeriod

Auto renewal period of an instance, in the unit of month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid value:
- [1, 2, 3, 6, 12] when `period_unit` in "Month"
- [1, 2, 3] when `period_unit` in "Week".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

The Zone to start the instance in. It is ignored and will be computed when set `vswitch_id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

Performance mode of the t5 burstable instance. Valid values: 'Standard', 'Unlimited'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

Whether enable the deletion protection or not. Default value: `false`.
- true: Enable deletion protection.
- false: Disable deletion protection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the data disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DryRun

Specifies whether to send a dry-run request. Default to false.
- true: Only a dry-run request is sent and no instance is created. The system checks whether the required parameters are set, and validates the request format, service permissions, and available ECS instances. If the validation fails, the corresponding error code is returned. If the validation succeeds, the `DryRunOperation` error code is returned.
- false: A request is sent. If the validation succeeds, the instance is created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

If it is true, the "PrePaid" instance will be change to "PostPaid" and then deleted forcibly.
However, because of changing instance charge type has CPU core count quota limitation, so strongly recommand that "Don't modify instance charge type frequentlly in one month".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

Host name of the ECS, which is a string of at least two characters. “hostname” cannot start or end with “.” or “-“. In addition, two or more consecutive “.” or “-“ symbols are not allowed. On Windows, the host name can contain a maximum of 15 characters, which can be a combination of uppercase/lowercase letters, numerals, and “-“. The host name cannot contain dots (“.”) or contain only numeric characters. When it is changed, the instance will reboot to make the change take effect.
On other OSs such as Linux, the host name can contain a maximum of 64 characters, which can be segments separated by dots (“.”), where each segment can contain uppercase/lowercase letters, numerals, or “_“. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The Image to use for the instance. ECS instance's image can be replaced via changing `image_id`. When it is changed, the instance will reboot to make the change take effect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeDataDisks

Whether to change instance disks charge type when changing instance charge type.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

Valid values are `PrePaid`, `PostPaid`, The default is `PostPaid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The name of the ECS. This instance_name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen, and must not begin with http:// or https://. If not specified,
Terraform will autogenerate a default name is `ECS-Instance`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of instance to start. When it is changed, the instance will reboot to make the change take effect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Internet charge type of the instance, Valid values are `PayByBandwidth`, `PayByTraffic`. Default is `PayByTraffic`. At present, 'PrePaid' instance cannot change the value to "PayByBandwidth" from "PayByTraffic".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthIn

Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). Value range: [1, 200]. If this value is not specified, then automatically sets it to 200 Mbps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

Maximum outgoing bandwidth to the public network, measured in Mbps (Mega bit per second). Value range:  [0, 100]. Default to 0 Mbps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoOptimized

It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOutdated

Whether to use outdated instance type. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedPassword

An KMS encrypts password used to an instance. If the `password` is filled in, this field will be ignored. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionContext

An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating an instance with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: List of <a href="kmsencryptioncontextdefinition.md">KmsEncryptionContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password to an instance is a string of 8 to 30 characters. It must contain uppercase/lowercase letters and numerals, but cannot contain special symbols. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values:
- [1-9, 12, 24, 36, 48, 60] when `period_unit` in "Month"
- [1-3] when `period_unit` in "Week".

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodUnit

The duration unit that you will buy the resource. It is valid when `instance_charge_type` is 'PrePaid'. Valid value: ["Week", "Month"]. Default to "Month".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

Instance private IP address can be specified when you creating new instance. It is valid when `vswitch_id` is specified. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewalStatus

Whether to renew an ECS instance automatically or not. It is valid when `instance_charge_type` is `PrePaid`. Default to "Normal". Valid values:
- `AutoRenewal`: Enable auto renewal.
- `Normal`: Disable auto renewal.
- `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the instance belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

Instance RAM role name. The name is provided and maintained by RAM. You can use `alicloud_ram_role` to create a new one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityEnhancementStrategy

The security enhancement strategy.
- Active: Enable security enhancement strategy, it only works on system images.
- Deactive: Disable security enhancement strategy, it works on all images.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

A list of security group ids to associate with.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPriceLimit

The hourly price threshold of a instance, and it takes effect only when parameter 'spot_strategy' is 'SpotWithPriceLimit'. Three decimals is allowed at most.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotStrategy

The spot strategy of a Pay-As-You-Go instance, and it takes effect only when parameter `instance_charge_type` is 'PostPaid'. Value range:
- NoSpot: A regular Pay-As-You-Go instance.
- SpotWithPriceLimit: A price threshold for a spot instance
- SpotAsPriceGo: A price that is based on the highest Pay-As-You-Go instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The instance status. Valid values: ["Running", "Stopped"]. You can control the instance start and stop through this parameter. Default to `Running`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskAutoSnapshotPolicyId

The ID of the automatic snapshot policy applied to the system disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskCategory

Valid values are `ephemeral_ssd`, `cloud_efficiency`, `cloud_ssd`, `cloud_essd`, `cloud`. `cloud` only is used to some none I/O optimized instance. Default to `cloud_efficiency`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskPerformanceLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

Size of the system disk, measured in GiB. Value range: [20, 500]. The specified value must be equal to or greater than max{20, Imagesize}. Default value: max{40, ImageSize}.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance. From version 1.60.0, it can be update in-place. If updated, the instance will reboot to make the change take effect. Note: Not all of changes will take effect and it depends on [cloud-init module type](https://cloudinit.readthedocs.io/en/latest/topics/modules.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeTags

A mapping of tags to assign to the devices created by the instance at launch time.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.

_Required_: No

_Type_: List of <a href="volumetagsdefinition.md">VolumeTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The virtual switch ID to launch in VPC. This parameter must be set unless you can create classic network instances. When it is changed, the instance will reboot to make the change take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisks

_Required_: No

_Type_: List of <a href="datadisksdefinition.md">DataDisksDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### PublicIp

Returns the <code>PublicIp</code> value.

