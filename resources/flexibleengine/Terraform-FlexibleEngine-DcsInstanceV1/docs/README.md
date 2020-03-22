# Terraform::FlexibleEngine::DcsInstanceV1

Manages a DCS instance in the flexibleengine DCS Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::DcsInstanceV1",
    "Properties" : {
        "<a href="#accessuser" title="AccessUser">AccessUser</a>" : <i>String</i>,
        "<a href="#availablezones" title="AvailableZones">AvailableZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#backupat" title="BackupAt">BackupAt</a>" : <i>[ Double, ... ]</i>,
        "<a href="#backuptype" title="BackupType">BackupType</a>" : <i>String</i>,
        "<a href="#beginat" title="BeginAt">BeginAt</a>" : <i>String</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#maintainbegin" title="MaintainBegin">MaintainBegin</a>" : <i>String</i>,
        "<a href="#maintainend" title="MaintainEnd">MaintainEnd</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#periodtype" title="PeriodType">PeriodType</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>,
        "<a href="#savedays" title="SaveDays">SaveDays</a>" : <i>Double</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::DcsInstanceV1
Properties:
    <a href="#accessuser" title="AccessUser">AccessUser</a>: <i>String</i>
    <a href="#availablezones" title="AvailableZones">AvailableZones</a>: <i>
      - String</i>
    <a href="#backupat" title="BackupAt">BackupAt</a>: <i>
      - Double</i>
    <a href="#backuptype" title="BackupType">BackupType</a>: <i>String</i>
    <a href="#beginat" title="BeginAt">BeginAt</a>: <i>String</i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#maintainbegin" title="MaintainBegin">MaintainBegin</a>: <i>String</i>
    <a href="#maintainend" title="MaintainEnd">MaintainEnd</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#periodtype" title="PeriodType">PeriodType</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
    <a href="#savedays" title="SaveDays">SaveDays</a>: <i>Double</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AccessUser

Username used for accessing a DCS instance after password
authentication. A username starts with a letter, consists of 1 to 64 characters,
and supports only letters, digits, and hyphens (-).
Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableZones

IDs of the AZs where cache nodes reside. For details
on how to query AZs, see Querying AZ Information.
Changing this creates a new instance.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupAt

Day in a week on which backup starts. Range: 1–7. Where: 1
indicates Monday; 7 indicates Sunday. Changing this creates a new instance.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupType

Backup type. Options:
auto: automatic backup.
manual: manual backup.
Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeginAt

Time at which backup starts. "00:00-01:00" indicates that backup
starts at 00:00:00. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

Indicates the Cache capacity. Unit: GB.
For a DCS Redis or Memcached instance in single-node or master/standby mode, the cache
capacity can be 2 GB, 4 GB, 8 GB, 16 GB, 32 GB, or 64 GB.
For a DCS Redis instance in cluster mode, the cache capacity can be 64, 128, 256, 512,
or 1024 GB. Changing this creates a new instance.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Indicates the description of an instance. It is a character
string containing not more than 1024 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

Indicates a cache engine. Only Redis is supported.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

Indicates the version of a cache engine, which is 3.0.7.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainBegin

Indicates the time at which a maintenance time window starts.
Format: HH:mm:ss.
The start time and end time of a maintenance time window must indicate the time segment of
a supported maintenance time window. For details, see section Querying Maintenance Time Windows.
The start time must be set to 22:00, 02:00, 06:00, 10:00, 14:00, or 18:00.
Parameters maintain_begin and maintain_end must be set in pairs. If parameter maintain_begin
is left blank, parameter maintain_end is also blank. In this case, the system automatically
allocates the default start time 02:00.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainEnd

Indicates the time at which a maintenance time window ends.
Format: HH:mm:ss.
The start time and end time of a maintenance time window must indicate the time segment of
a supported maintenance time window. For details, see section Querying Maintenance Time Windows.
The end time is four hours later than the start time. For example, if the start time is 22:00,
the end time is 02:00.
Parameters maintain_begin and maintain_end must be set in pairs. If parameter maintain_end is left
blank, parameter maintain_begin is also blank. In this case, the system automatically allocates
the default end time 06:00.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Indicates the name of an instance. An instance name starts with a letter,
consists of 4 to 64 characters, and supports only letters, digits, and hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

Network ID. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of a DCS instance.
The password of a DCS Redis instance must meet the following complexity requirements:
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeriodType

Interval at which backup is performed. Currently, only weekly
backup is supported. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

Product ID used to differentiate DCS instance types.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SaveDays

Retention time. Unit: day. Range: 1–7.
Changing this creates a new instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

Tenant's security group ID. For details on how to
create security groups, see the Virtual Private Cloud API Reference.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Network ID. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Tenant's VPC ID. For details on how to create VPCs, see the
Virtual Private Cloud API Reference.
Changing this creates a new instance.

_Required_: Yes

_Type_: String

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

#### InternalVersion

Returns the <code>InternalVersion</code> value.

#### Ip

Returns the <code>Ip</code> value.

#### MaxMemory

Returns the <code>MaxMemory</code> value.

#### OrderId

Returns the <code>OrderId</code> value.

#### Port

Returns the <code>Port</code> value.

#### ResourceSpecCode

Returns the <code>ResourceSpecCode</code> value.

#### SecurityGroupName

Returns the <code>SecurityGroupName</code> value.

#### SubnetName

Returns the <code>SubnetName</code> value.

#### UsedMemory

Returns the <code>UsedMemory</code> value.

#### UserId

Returns the <code>UserId</code> value.

#### VpcName

Returns the <code>VpcName</code> value.

