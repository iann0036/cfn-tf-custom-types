# TF::Alicloud::HbaseInstance

Provides a HBase instance resource supports replica set instances only. the HBase provides stable, reliable, and automatic scalable database services. 
It offers a full range of database solutions, such as disaster recovery, backup, recovery, monitoring, and alarms.
You can see detail product introduction [here](https://help.aliyun.com/product/49055.html)

-> **NOTE:**  Available in 1.67.0+

-> **NOTE:**  The following regions don't support create Classic network HBase instance.
[`cn-hangzhou`,`cn-shanghai`,`cn-qingdao`,`cn-beijing`,`cn-shenzhen`,`ap-southeast-1a`,.....]
the official website mark  more regions. or you can call [DescribeRegions](https://help.aliyun.com/document_detail/144489.html)

-> **NOTE:**  Create HBase instance or change instance type and storage would cost 15 minutes. Please make full preparation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::HbaseInstance",
    "Properties" : {
        "<a href="#account" title="Account">Account</a>" : <i>String</i>,
        "<a href="#autorenew" title="AutoRenew">AutoRenew</a>" : <i>Boolean</i>,
        "<a href="#coldstoragesize" title="ColdStorageSize">ColdStorageSize</a>" : <i>Double</i>,
        "<a href="#coredisksize" title="CoreDiskSize">CoreDiskSize</a>" : <i>Double</i>,
        "<a href="#coredisktype" title="CoreDiskType">CoreDiskType</a>" : <i>String</i>,
        "<a href="#coreinstancequantity" title="CoreInstanceQuantity">CoreInstanceQuantity</a>" : <i>Double</i>,
        "<a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>" : <i>String</i>,
        "<a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
        "<a href="#engine" title="Engine">Engine</a>" : <i>String</i>,
        "<a href="#engineversion" title="EngineVersion">EngineVersion</a>" : <i>String</i>,
        "<a href="#immediatedeleteflag" title="ImmediateDeleteFlag">ImmediateDeleteFlag</a>" : <i>Boolean</i>,
        "<a href="#ipwhite" title="IpWhite">IpWhite</a>" : <i>String</i>,
        "<a href="#maintainendtime" title="MaintainEndTime">MaintainEndTime</a>" : <i>String</i>,
        "<a href="#maintainstarttime" title="MaintainStartTime">MaintainStartTime</a>" : <i>String</i>,
        "<a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#paytype" title="PayType">PayType</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::HbaseInstance
Properties:
    <a href="#account" title="Account">Account</a>: <i>String</i>
    <a href="#autorenew" title="AutoRenew">AutoRenew</a>: <i>Boolean</i>
    <a href="#coldstoragesize" title="ColdStorageSize">ColdStorageSize</a>: <i>Double</i>
    <a href="#coredisksize" title="CoreDiskSize">CoreDiskSize</a>: <i>Double</i>
    <a href="#coredisktype" title="CoreDiskType">CoreDiskType</a>: <i>String</i>
    <a href="#coreinstancequantity" title="CoreInstanceQuantity">CoreInstanceQuantity</a>: <i>Double</i>
    <a href="#coreinstancetype" title="CoreInstanceType">CoreInstanceType</a>: <i>String</i>
    <a href="#deletionprotection" title="DeletionProtection">DeletionProtection</a>: <i>Boolean</i>
    <a href="#duration" title="Duration">Duration</a>: <i>Double</i>
    <a href="#engine" title="Engine">Engine</a>: <i>String</i>
    <a href="#engineversion" title="EngineVersion">EngineVersion</a>: <i>String</i>
    <a href="#immediatedeleteflag" title="ImmediateDeleteFlag">ImmediateDeleteFlag</a>: <i>Boolean</i>
    <a href="#ipwhite" title="IpWhite">IpWhite</a>: <i>String</i>
    <a href="#maintainendtime" title="MaintainEndTime">MaintainEndTime</a>: <i>String</i>
    <a href="#maintainstarttime" title="MaintainStartTime">MaintainStartTime</a>: <i>String</i>
    <a href="#masterinstancetype" title="MasterInstanceType">MasterInstanceType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#paytype" title="PayType">PayType</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Account

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRenew

`true`, `false`, System default to `false`, valid when pay_type = PrePaid.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColdStorageSize

0 or 0+. 0 means is_cold_storage = false. 0+ means is_cold_storage = true.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreDiskSize

User-defined HBase instance one core node's storage space.Unit: GB. Value range:
- Custom storage space; value range: [400, 8000]
- 40-GB increments.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreDiskType

Valid values are `cloud_ssd`, `cloud_efficiency`, `local_hdd_pro`, `local_ssd_pro`. local_disk size is fixed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceQuantity

default=2. if core_instance_quantity > 1,this is cluster's instance.  if core_instance_quantity = 1,this is a single instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreInstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtection

the switch of delete protection. true: delete protect, false: no delete protect. you must set false when you want to delete cluster.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 60, valid when pay_type = PrePaid. unit: month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Engine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineVersion

hbase major version. hbase:1.1/2.0, hbaseue:2.0, bds:1.0, unsupport other engine temporarily. Value options can refer to the latest docs [CreateInstance](https://help.aliyun.com/document_detail/144607.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImmediateDeleteFlag

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpWhite

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainEndTime

The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaintainStartTime

The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterInstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

HBase instance name. Length must be 2-128 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PayType

Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

if vswitch_id is not empty, that mean net_type = vpc and has a same region. if vswitch_id is empty, net_type_classic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The Zone to launch the HBase instance. if vswitch_id is not empty, this zone_id can be "" or consistent.

_Required_: No

_Type_: String

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

#### MasterInstanceQuantity

Returns the <code>MasterInstanceQuantity</code> value.

#### SlbConnAddrs

Returns the <code>SlbConnAddrs</code> value.

#### UiProxyConnAddrs

Returns the <code>UiProxyConnAddrs</code> value.

#### ZkConnAddrs

Returns the <code>ZkConnAddrs</code> value.

