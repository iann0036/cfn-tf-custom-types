# Terraform::Alicloud::MongodbShardingInstance

Provides a MongoDB sharding instance resource supports replica set instances only. the MongoDB provides stable, reliable, and automatic scalable database services. 
It offers a full range of database solutions, such as disaster recovery, backup, recovery, monitoring, and alarms.
You can see detail product introduction [here](https://www.alibabacloud.com/help/doc-detail/26558.htm)

-> **NOTE:**  Available in 1.40.0+

-> **NOTE:**  The following regions don't support create Classic network MongoDB sharding instance.
[`cn-zhangjiakou`,`cn-huhehaote`,`ap-southeast-2`,`ap-southeast-3`,`ap-southeast-5`,`ap-south-1`,`me-east-1`,`ap-northeast-1`,`eu-west-1`] 

-> **NOTE:**  Create MongoDB Sharding instance or change instance type and storage would cost 10~20 minutes. Please make full preparation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::MongodbShardingInstance",
    "Properties" : {
        "<a href="#accountpassword" title="AccountPassword">AccountPassword</a>" : <i>String</i>,
        "<a href="#backupperiod" title="BackupPeriod">BackupPeriod</a>" : <i>[ String, ... ]</i>,
        "<a href="#backuptime" title="BackupTime">BackupTime</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>[ <a href="kmsencryptioncontext.md">KmsEncryptionContext</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#securityiplist" title="SecurityIpList">SecurityIpList</a>" : <i>[ String, ... ]</i>,
        "<a href="#storageengine" title="StorageEngine">StorageEngine</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#mongolist" title="MongoList">MongoList</a>" : <i>[ <a href="mongolist.md">MongoList</a>, ... ]</i>,
        "<a href="#shardlist" title="ShardList">ShardList</a>" : <i>[ <a href="shardlist.md">ShardList</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::MongodbShardingInstance
Properties:
    <a href="#accountpassword" title="AccountPassword">AccountPassword</a>: <i>String</i>
    <a href="#backupperiod" title="BackupPeriod">BackupPeriod</a>: <i>
      - String</i>
    <a href="#backuptime" title="BackupTime">BackupTime</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#kmsencryptedpassword" title="KmsEncryptedPassword">KmsEncryptedPassword</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>
      - <a href="kmsencryptioncontext.md">KmsEncryptionContext</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#securityiplist" title="SecurityIpList">SecurityIpList</a>: <i>
      - String</i>
    <a href="#storageengine" title="StorageEngine">StorageEngine</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#mongolist" title="MongoList">MongoList</a>: <i>
      - <a href="mongolist.md">MongoList</a></i>
    <a href="#shardlist" title="ShardList">ShardList</a>: <i>
      - <a href="shardlist.md">ShardList</a></i>
</pre>

## Properties

#### AccountPassword

Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupPeriod

MongoDB Instance backup period. It is required when `backup_time` was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupTime

MongoDB instance backup time. It is required when `backup_period` was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like "23:00Z-24:00Z".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/zh/doc-detail/61884.htm) `EngineVersion`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedPassword

An KMS encrypts password used to a instance. If the `account_password` is filled in, this field will be ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionContext

An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating instance with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.

_Required_: No

_Type_: List of <a href="kmsencryptioncontext.md">KmsEncryptionContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of DB instance. It a string of 2 to 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. System default to 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityIpList

List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]). System default to `["127.0.0.1"]`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageEngine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The virtual switch ID to launch DB instances in one VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The Zone to launch the DB instance. MongoDB sharding instance does not support multiple-zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in one of them.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MongoList

_Required_: No

_Type_: List of <a href="mongolist.md">MongoList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShardList

_Required_: No

_Type_: List of <a href="shardlist.md">ShardList</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### RetentionPeriod

Returns the <code>RetentionPeriod</code> value.

