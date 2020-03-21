# Terraform::UCloud::Instance

Provides an UHost Instance resource.

~> **Note** If you try to update some properties which requires stopping the instance, you must set `allow_stopping_for_update` to `true` in your config to allows Terraform to stop the instance to update its properties like `instance_type`, `root_password`, `boot_disk_size`, `data_disk_size`. In addition, once the instance complete creation, it takes around 10 minutes for boot disk initialization for the running instance, and the updates will only be made to some specific attributes (`root_password`, `boot_disk_size`) if required once the instance initialization completed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::Instance",
    "Properties" : {
        "<a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>" : <i>Boolean</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#bootdisksize" title="BootDiskSize">BootDiskSize</a>" : <i>Double</i>,
        "<a href="#bootdisktype" title="BootDiskType">BootDiskType</a>" : <i>String</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>" : <i>Double</i>,
        "<a href="#datadisktype" title="DataDiskType">DataDiskType</a>" : <i>String</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#isolationgroup" title="IsolationGroup">IsolationGroup</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#rootpassword" title="RootPassword">RootPassword</a>" : <i>String</i>,
        "<a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::Instance
Properties:
    <a href="#allowstoppingforupdate" title="AllowStoppingForUpdate">AllowStoppingForUpdate</a>: <i>Boolean</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#bootdisksize" title="BootDiskSize">BootDiskSize</a>: <i>Double</i>
    <a href="#bootdisktype" title="BootDiskType">BootDiskType</a>: <i>String</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#datadisksize" title="DataDiskSize">DataDiskSize</a>: <i>Double</i>
    <a href="#datadisktype" title="DataDiskType">DataDiskType</a>: <i>String</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#isolationgroup" title="IsolationGroup">IsolationGroup</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#rootpassword" title="RootPassword">RootPassword</a>: <i>String</i>
    <a href="#securitygroup" title="SecurityGroup">SecurityGroup</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AllowStoppingForUpdate

If you try to update some properties which requires stopping the instance, you must set `allow_stopping_for_update` to `true` in your config to allows Terraform to stop the instance to update its properties like `instance_type`, `root_password`, `boot_disk_size`, `data_disk_size`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

Availability zone where instance is located. such as: `cn-bj2-02`. You may refer to [list of availability zone](https://docs.ucloud.cn/api/summary/regionlist).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiskSize

The size of the boot disk, measured in GB (GigaByte). Range: 20-100. The value set of disk size must be larger or equal to `20`(default: `20`) for Linux and `40` (default: `40`) for Windows. The responsive time is a bit longer if the value set is larger than default for local boot disk, and further settings may be required on host instance if the value set is larger than default for cloud boot disk. The disk volume adjustment must be a multiple of 10 GB. In addition, any reduction of boot disk size is not supported.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootDiskType

The type of boot disk. Possible values are: `local_normal` and `local_ssd` for local boot disk, `cloud_ssd` for cloud SSD boot disk. (Default: `local_normal`). The `local_ssd` and `cloud_ssd` are not fully support by all regions as boot disk type, please proceed to UCloud console for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

The charge type of instance, possible values are: `year`, `month` and `dynamic` as pay by hour (specific permission required). (Default: `month`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskSize

The size of local data disk, measured in GB (GigaByte), range: 0-8000 (Default: `20`), 0-8000 for cloud disk, 0-2000 for local sata disk and 100-1000 for local ssd disk (all the GPU type instances are included). The volume adjustment must be a multiple of 10 GB. In addition, any reduction of data disk size is not supported.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDiskType

The type of local data disk. Possible values are: `local_normal` and `local_ssd` for local data disk. (Default: `local_normal`). The `local_ssd` is not fully support by all regions as data disk type, please proceed to UCloud console for more details. In addition, the `data_disk_type` must be same as `boot_disk_type` if specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

The duration that you will buy the instance (Default: `1`). The value is `0` when pay by month and the instance will be valid till the last day of that month. It is not required when `dynamic` (pay by hour).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

The ID for the image to use for the instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The type of instance, please visit the [instance type table](https://www.terraform.io/docs/providers/ucloud/appendix/instance_type.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsolationGroup

The ID of the associated isolation group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of instance, which contains 1-63 characters and only support Chinese, English, numbers, '-', '_', '.'. If not specified, terraform will auto-generate a name beginning with `tf-instance`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

The private IP address assigned to the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

The remarks of instance. (Default: `""`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootPassword

The password for the instance, which contains 8-30 characters, and at least 2 items of capital letters, lower case letters, numbers and special characters. The special characters include <code>`()~!@#$%^&*-+=_|{}\[]:;'<>,.?/</code>. If not specified, terraform will auto-generate a password.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroup

The ID of the associated security group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of subnet. If defined `vpc_id`, the `subnet_id` is Required. If not defined `vpc_id` and `subnet_id`, the instance will use the default subnet in the current region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

A tag assigned to instance, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The ID of VPC linked to the instance. If not defined `vpc_id`, the instance will use the default VPC in the current region.

_Required_: No

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

#### AutoRenew

Returns the <code>AutoRenew</code> value.

#### Cpu

Returns the <code>Cpu</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### DiskSet

Returns the <code>DiskSet</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### IpSet

Returns the <code>IpSet</code> value.

#### Memory

Returns the <code>Memory</code> value.

#### Status

Returns the <code>Status</code> value.

