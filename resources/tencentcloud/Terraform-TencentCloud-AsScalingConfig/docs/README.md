# Terraform::TencentCloud::AsScalingConfig

Provides a resource to create a configuration for an AS (Auto scaling) instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::AsScalingConfig",
    "Properties" : {
        "<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>" : <i>String</i>,
        "<a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>" : <i>Boolean</i>,
        "<a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>" : <i>Boolean</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetags" title="InstanceTags">InstanceTags</a>" : <i>[ <a href="instancetags.md">InstanceTags</a>, ... ]</i>,
        "<a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>" : <i>Double</i>,
        "<a href="#keepimagelogin" title="KeepImageLogin">KeepImageLogin</a>" : <i>Boolean</i>,
        "<a href="#keyids" title="KeyIds">KeyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>" : <i>Boolean</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>" : <i>Double</i>,
        "<a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadisk.md">DataDisk</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::AsScalingConfig
Properties:
    <a href="#configurationname" title="ConfigurationName">ConfigurationName</a>: <i>String</i>
    <a href="#enhancedmonitorservice" title="EnhancedMonitorService">EnhancedMonitorService</a>: <i>Boolean</i>
    <a href="#enhancedsecurityservice" title="EnhancedSecurityService">EnhancedSecurityService</a>: <i>Boolean</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetags" title="InstanceTags">InstanceTags</a>: <i>
      - <a href="instancetags.md">InstanceTags</a></i>
    <a href="#instancetypes" title="InstanceTypes">InstanceTypes</a>: <i>
      - String</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#internetmaxbandwidthout" title="InternetMaxBandwidthOut">InternetMaxBandwidthOut</a>: <i>Double</i>
    <a href="#keepimagelogin" title="KeepImageLogin">KeepImageLogin</a>: <i>Boolean</i>
    <a href="#keyids" title="KeyIds">KeyIds</a>: <i>
      - String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#publicipassigned" title="PublicIpAssigned">PublicIpAssigned</a>: <i>Boolean</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#systemdisksize" title="SystemDiskSize">SystemDiskSize</a>: <i>Double</i>
    <a href="#systemdisktype" title="SystemDiskType">SystemDiskType</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadisk.md">DataDisk</a></i>
</pre>

## Properties

#### ConfigurationName

Name of a launch configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedMonitorService

To specify whether to enable cloud monitor service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedSecurityService

To specify whether to enable cloud security service. Default is TRUE.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

An available image ID for a cvm instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTags

A list of tags used to associate different resources.

_Required_: No

_Type_: List of <a href="instancetags.md">InstanceTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypes

Specified types of CVM instances.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Charge types for network traffic. Available values include `BANDWIDTH_PREPAID`, `TRAFFIC_POSTPAID_BY_HOUR`, `TRAFFIC_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetMaxBandwidthOut

Max bandwidth of Internet access in Mbps. Default is 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepImageLogin

Specify whether to keep original settings of a CVM image. And it can't be used with password or key_ids together.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyIds

ID list of keys.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password to access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

Specifys to which project the configuration belongs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpAssigned

Specify whether to assign an Internet IP address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

Security groups to which a CVM instance belongs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskSize

Volume of system disk in GB. Default is 50.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDiskType

Type of a CVM disk, and available values include CLOUD_PREMIUM and CLOUD_SSD. Default is CLOUD_PREMIUM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

ase64-encoded User Data text, the length limit is 16KB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadisk.md">DataDisk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

