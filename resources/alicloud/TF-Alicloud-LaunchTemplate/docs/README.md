# TF::Alicloud::LaunchTemplate

Provides an ECS Launch Template resource.

For information about Launch Template and how to use it, see [Launch Template](https://www.alibabacloud.com/help/doc-detail/73916.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::LaunchTemplate",
    "Properties" : {
        "<a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>" : <i>String</i>,
        "<a href="#deploymentsetid" title="DeploymentSetId">DeploymentSetId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablevmosconfig" title="EnableVmOsConfig">EnableVmOsConfig</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="HostName">HostName</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#imageowneralias" title="ImageOwnerAlias">ImageOwnerAlias</a>" : <i>String</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#internetmaxbandwidthin" title="InternetMaxBandwidthIn">InternetMaxBandwidthIn</a>" : <i>Double</i>,
        "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
        "<a href="#iooptimized" title="IoOptimized">IoOptimized</a>" : <i>String</i>,
        "<a href="#keypairname" title="KeyPairName">KeyPairName</a>" : <i>String</i>,
        "<a href="#launchtemplatename" title="LaunchTemplateName">LaunchTemplateName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#passwordinherit" title="PasswordInherit">PasswordInherit</a>" : <i>Boolean</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
        "<a href="#ramrolename" title="RamRoleName">RamRoleName</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#securityenhancementstrategy" title="SecurityEnhancementStrategy">SecurityEnhancementStrategy</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#spotduration" title="SpotDuration">SpotDuration</a>" : <i>String</i>,
        "<a href="#spotpricelimit" title="SpotPriceLimit">SpotPriceLimit</a>" : <i>Double</i>,
        "<a href="#spotstrategy" title="SpotStrategy">SpotStrategy</a>" : <i>String</i>,
        "<a href="#systemdiskcategory" title="SystemDiskCategory">SystemDiskCategory</a>" : <i>String</i>,
        "<a href="#systemdiskdescription" title="SystemDiskDescription">SystemDiskDescription</a>" : <i>String</i>,
        "<a href="#systemdiskname" title="SystemDiskName">SystemDiskName</a>" : <i>String</i>,
        "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#templateresourcegroupid" title="TemplateResourceGroupId">TemplateResourceGroupId</a>" : <i>String</i>,
        "<a href="#templatetags" title="TemplateTags">TemplateTags</a>" : <i>[ <a href="templatetagsdefinition.md">TemplateTagsDefinition</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#userdata" title="Userdata">Userdata</a>" : <i>String</i>,
        "<a href="#versiondescription" title="VersionDescription">VersionDescription</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#datadisks" title="DataDisks">DataDisks</a>" : <i>[ <a href="datadisksdefinition.md">DataDisksDefinition</a>, ... ]</i>,
        "<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>" : <i>[ <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>, ... ]</i>,
        "<a href="#systemdisk" title="SystemDisk">SystemDisk</a>" : <i>[ <a href="systemdiskdefinition.md">SystemDiskDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::LaunchTemplate
Properties:
    <a href="#autoreleasetime" title="AutoReleaseTime">AutoReleaseTime</a>: <i>String</i>
    <a href="#deploymentsetid" title="DeploymentSetId">DeploymentSetId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablevmosconfig" title="EnableVmOsConfig">EnableVmOsConfig</a>: <i>Boolean</i>
    <a href="#hostname" title="HostName">HostName</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#imageowneralias" title="ImageOwnerAlias">ImageOwnerAlias</a>: <i>String</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#internetmaxbandwidthin" title="InternetMaxBandwidthIn">InternetMaxBandwidthIn</a>: <i>Double</i>
    <a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
    <a href="#iooptimized" title="IoOptimized">IoOptimized</a>: <i>String</i>
    <a href="#keypairname" title="KeyPairName">KeyPairName</a>: <i>String</i>
    <a href="#launchtemplatename" title="LaunchTemplateName">LaunchTemplateName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#passwordinherit" title="PasswordInherit">PasswordInherit</a>: <i>Boolean</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
    <a href="#ramrolename" title="RamRoleName">RamRoleName</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#securityenhancementstrategy" title="SecurityEnhancementStrategy">SecurityEnhancementStrategy</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#spotduration" title="SpotDuration">SpotDuration</a>: <i>String</i>
    <a href="#spotpricelimit" title="SpotPriceLimit">SpotPriceLimit</a>: <i>Double</i>
    <a href="#spotstrategy" title="SpotStrategy">SpotStrategy</a>: <i>String</i>
    <a href="#systemdiskcategory" title="SystemDiskCategory">SystemDiskCategory</a>: <i>String</i>
    <a href="#systemdiskdescription" title="SystemDiskDescription">SystemDiskDescription</a>: <i>String</i>
    <a href="#systemdiskname" title="SystemDiskName">SystemDiskName</a>: <i>String</i>
    <a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#templateresourcegroupid" title="TemplateResourceGroupId">TemplateResourceGroupId</a>: <i>String</i>
    <a href="#templatetags" title="TemplateTags">TemplateTags</a>: <i>
      - <a href="templatetagsdefinition.md">TemplateTagsDefinition</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#userdata" title="Userdata">Userdata</a>: <i>String</i>
    <a href="#versiondescription" title="VersionDescription">VersionDescription</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#datadisks" title="DataDisks">DataDisks</a>: <i>
      - <a href="datadisksdefinition.md">DataDisksDefinition</a></i>
    <a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>: <i>
      - <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a></i>
    <a href="#systemdisk" title="SystemDisk">SystemDisk</a>: <i>
      - <a href="systemdiskdefinition.md">SystemDiskDefinition</a></i>
</pre>

## Properties

#### AutoReleaseTime

Instance auto release time. The time is presented using the ISO8601 standard and in UTC time. The format is  YYYY-MM-DDTHH:MM:SSZ.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentSetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the data disk.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVmOsConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostName

Instance host name.It cannot start or end with a period (.) or a hyphen (-) and it cannot have two or more consecutive periods (.) or hyphens (-).For Windows: The host name can be [2, 15] characters in length. It can contain A-Z, a-z, numbers, periods (.), and hyphens (-). It cannot only contain numbers. For other operating systems: The host name can be [2, 64] characters in length. It can be segments separated by periods (.). It can contain A-Z, a-z, numbers, and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

Image ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageOwnerAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

Billing methods. Optional values:
- PrePaid: Monthly, or annual subscription. Make sure that your registered credit card is invalid or you have insufficient balance in your PayPal account. Otherwise, InvalidPayMethod error may occur.
- PostPaid: Pay-As-You-Go.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The name of the instance. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

Instance type. For more information, call resource_alicloud_instances to obtain the latest instance type list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Internet bandwidth billing method. Optional values: `PayByTraffic` | `PayByBandwidth`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthIn

The maximum inbound bandwidth from the Internet network, measured in Mbit/s. Value range: [1, 200].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

Maximum outbound bandwidth from the Internet, its unit of measurement is Mbit/s. Value range: [0, 100].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoOptimized

Whether it is an I/O-optimized instance or not. Optional values:
- none
- optimized.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPairName

The name of the key pair.
- Ignore this parameter for Windows instances. It is null by default. Even if you enter this parameter, only the  Password content is used.
- The password logon method for Linux instances is set to forbidden upon initialization.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the data disk.
* `size` - (Required) The size of the data disk.
- cloud：[5, 2000]
- cloud_efficiency：[20, 32768]
- cloud_ssd：[20, 32768]
- cloud_essd：[20, 32768]
- ephemeral_ssd: [5, 800]
* `category` - (Optional) The category of the disk:
- cloud: Basic cloud disk.
- cloud_efficiency: Ultra cloud disk.
- cloud_ssd: SSD cloud Disks.
- ephemeral_ssd: local SSD Disks
- cloud_essd: ESSD cloud Disks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Network type of the instance. Value options: `classic` | `vpc`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordInherit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamRoleName

The RAM role name of the instance. You can use the RAM API ListRoles to query instance RAM role names.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityEnhancementStrategy

Whether or not to activate the security enhancement feature and install network security software free of charge. Optional values: Active | Deactive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The security group ID must be one in the same VPC.
* `vswitch_id` - (Optional) The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPriceLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotStrategy

The spot strategy for a Pay-As-You-Go instance. This parameter is valid and required only when InstanceChargeType is set to PostPaid. Value range:
- NoSpot: Normal Pay-As-You-Go instance.
- SpotWithPriceLimit: Sets the maximum price for a spot instance.
- SpotAsPriceGo: The system automatically calculates the price. The maximum value is the Pay-As-You-Go price.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskCategory

The category of the system disk. System disk type. Optional values:
- cloud: Basic cloud disk.
- cloud_efficiency: Ultra cloud disk.
- cloud_ssd: SSD cloud Disks.
- ephemeral_ssd: local SSD Disks
- cloud_essd: ESSD cloud Disks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskDescription

System disk description. It cannot begin with http:// or https://.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskName

System disk name. The name is a string of 2 to 128 characters. It must begin with an English or a Chinese character. It can contain A-Z, a-z, Chinese characters, numbers, periods (.), colons (:), underscores (_), and hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

Size of the system disk, measured in GB. Value range: [20, 500].

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

#### TemplateResourceGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTags

_Required_: No

_Type_: List of <a href="templatetagsdefinition.md">TemplateTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userdata

User data of the instance, which is Base64-encoded. Size of the raw data cannot exceed 16 KB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The VSwitch ID for ENI. The instance must be in the same zone of the same VPC network as the ENI, but they may belong to different VSwitches.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The zone ID of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisks

_Required_: No

_Type_: List of <a href="datadisksdefinition.md">DataDisksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaces

_Required_: No

_Type_: List of <a href="networkinterfacesdefinition.md">NetworkInterfacesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDisk

_Required_: No

_Type_: List of <a href="systemdiskdefinition.md">SystemDiskDefinition</a>

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

