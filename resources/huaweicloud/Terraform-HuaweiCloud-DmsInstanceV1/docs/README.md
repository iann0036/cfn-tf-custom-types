# Terraform::HuaweiCloud::DmsInstanceV1

Manages a DMS instance in the huaweicloud DMS Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::DmsInstanceV1",
    "Properties" : {
        "<a href="#accessuser" title="AccessUser">AccessUser</a>" : <i>String</i>,
        "<a href="#availablezones" title="AvailableZones">AvailableZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#maintainbegin" title="MaintainBegin">MaintainBegin</a>" : <i>String</i>,
        "<a href="#maintainend" title="MaintainEnd">MaintainEnd</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partitionnum" title="PartitionNum">PartitionNum</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#specification" title="Specification">Specification</a>" : <i>String</i>,
        "<a href="#storagespace" title="StorageSpace">StorageSpace</a>" : <i>Double</i>,
        "<a href="#storagespeccode" title="StorageSpecCode">StorageSpecCode</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::DmsInstanceV1
Properties:
    <a href="#accessuser" title="AccessUser">AccessUser</a>: <i>String</i>
    <a href="#availablezones" title="AvailableZones">AvailableZones</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#maintainbegin" title="MaintainBegin">MaintainBegin</a>: <i>String</i>
    <a href="#maintainend" title="MaintainEnd">MaintainEnd</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partitionnum" title="PartitionNum">PartitionNum</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#specification" title="Specification">Specification</a>: <i>String</i>
    <a href="#storagespace" title="StorageSpace">StorageSpace</a>: <i>Double</i>
    <a href="#storagespeccode" title="StorageSpecCode">StorageSpecCode</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AccessUser

Indicates a username. If the engine is rabbitmq, this
parameter is mandatory. If the engine is kafka, this parameter is optional.
A username consists of 4 to 64 characters and supports only letters, digits, and
hyphens (-).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableZones

Indicates the ID of an AZ. The parameter value can not be
left blank or an empty array. For details, see section Querying AZ Information.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Indicates the description of an instance. It is a character
string containing not more than 1024 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

Indicates a message engine. Options: rabbitmq and kafka.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

Indicates the version of a message engine.

_Required_: No

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

#### PartitionNum

This parameter is mandatory when a Kafka instance is created.
Indicates the maximum number of topics in a Kafka instance.
When specification is 300 MB: 900
When specification is 600 MB: 1800
When specification is 1200 MB: 1800.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

If the engine is rabbitmq, this parameter is mandatory.
If the engine is kafka, this parameter is mandatory when ssl_enable is true and is
invalid when ssl_enable is false. Indicates the password of an instance. An instance
password must meet the following complexity requirements: Must be 8 to 32 characters long.
Must contain at least 2 of the following character types: lowercase letters, uppercase
letters, digits, and special characters (`~!@#$%^&*()-_=+\|[{}]:'",<.>/?).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

Indicates a product ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

Indicates the ID of a security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specification

This parameter is mandatory if the engine is kafka.
Indicates the baseline bandwidth of a Kafka instance, that is, the maximum amount
of data transferred per unit time. Unit: byte/s. Options: 300 MB, 600 MB, 1200 MB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSpace

Indicates the message storage space.
Value range:
Single-node RabbitMQ instance: 100–90000 GB
Cluster RabbitMQ instance: 100 GB x Number of nodes to 90000 GB, 200 GB x Number of
nodes to 90000 GB, 300 GB x Number of nodes to 90000 GB
Kafka instance with specification being 300 MB: 1200–90000 GB
Kafka instance with specification being 600 MB: 2400–90000 GB
Kafka instance with specification being 1200 MB: 4800–90000 GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSpecCode

Indicates the storage I/O specification. For details on how to
select a disk type, see Disk Types and Disk Performance. Options for a RabbitMQ instance:
dms.physical.storage.normal
dms.physical.storage.high
dms.physical.storage.ultra
Options for a Kafka instance:
When specification is 300 MB: dms.physical.storage.high or dms.physical.storage.ultra
When specification is 600 MB: dms.physical.storage.ultra
When specification is 1200 MB: dms.physical.storage.ultra.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Indicates the ID of a subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Indicates the ID of a VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ConnectAddress

Returns the <code>ConnectAddress</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrderId

Returns the <code>OrderId</code> value.

#### Port

Returns the <code>Port</code> value.

#### ResourceSpecCode

Returns the <code>ResourceSpecCode</code> value.

#### SecurityGroupName

Returns the <code>SecurityGroupName</code> value.

#### Status

Returns the <code>Status</code> value.

#### SubnetName

Returns the <code>SubnetName</code> value.

#### Type

Returns the <code>Type</code> value.

#### UsedStorageSpace

Returns the <code>UsedStorageSpace</code> value.

#### UserId

Returns the <code>UserId</code> value.

#### VpcName

Returns the <code>VpcName</code> value.

