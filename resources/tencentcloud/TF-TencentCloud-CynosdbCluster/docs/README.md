# TF::TencentCloud::CynosdbCluster

Provide a resource to create a CynosDB cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CynosdbCluster",
    "Properties" : {
        "<a href="#autorenewflag" title="AutoRenewFlag">AutoRenewFlag</a>" : <i>Double</i>,
        "<a href="#availablezone" title="AvailableZone">AvailableZone</a>" : <i>String</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#clustername" title="ClusterName">ClusterName</a>" : <i>String</i>,
        "<a href="#dbtype" title="DbType">DbType</a>" : <i>String</i>,
        "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#instancecpucore" title="InstanceCpuCore">InstanceCpuCore</a>" : <i>Double</i>,
        "<a href="#instancemaintainduration" title="InstanceMaintainDuration">InstanceMaintainDuration</a>" : <i>Double</i>,
        "<a href="#instancemaintainstarttime" title="InstanceMaintainStartTime">InstanceMaintainStartTime</a>" : <i>Double</i>,
        "<a href="#instancemaintainweekdays" title="InstanceMaintainWeekdays">InstanceMaintainWeekdays</a>" : <i>[ String, ... ]</i>,
        "<a href="#instancememorysize" title="InstanceMemorySize">InstanceMemorySize</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#prepaidperiod" title="PrepaidPeriod">PrepaidPeriod</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#rogroupsg" title="RoGroupSg">RoGroupSg</a>" : <i>[ String, ... ]</i>,
        "<a href="#rwgroupsg" title="RwGroupSg">RwGroupSg</a>" : <i>[ String, ... ]</i>,
        "<a href="#storagelimit" title="StorageLimit">StorageLimit</a>" : <i>Double</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CynosdbCluster
Properties:
    <a href="#autorenewflag" title="AutoRenewFlag">AutoRenewFlag</a>: <i>Double</i>
    <a href="#availablezone" title="AvailableZone">AvailableZone</a>: <i>String</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#clustername" title="ClusterName">ClusterName</a>: <i>String</i>
    <a href="#dbtype" title="DbType">DbType</a>: <i>String</i>
    <a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#instancecpucore" title="InstanceCpuCore">InstanceCpuCore</a>: <i>Double</i>
    <a href="#instancemaintainduration" title="InstanceMaintainDuration">InstanceMaintainDuration</a>: <i>Double</i>
    <a href="#instancemaintainstarttime" title="InstanceMaintainStartTime">InstanceMaintainStartTime</a>: <i>Double</i>
    <a href="#instancemaintainweekdays" title="InstanceMaintainWeekdays">InstanceMaintainWeekdays</a>: <i>
      - String</i>
    <a href="#instancememorysize" title="InstanceMemorySize">InstanceMemorySize</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#prepaidperiod" title="PrepaidPeriod">PrepaidPeriod</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#rogroupsg" title="RoGroupSg">RoGroupSg</a>: <i>
      - String</i>
    <a href="#rwgroupsg" title="RwGroupSg">RwGroupSg</a>: <i>
      - String</i>
    <a href="#storagelimit" title="StorageLimit">StorageLimit</a>: <i>Double</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### AutoRenewFlag

Auto renew flag. Valid values are `0`(MANUAL_RENEW), `1`(AUTO_RENEW). Default value is `0`. Only works for PREPAID cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableZone

The available zone of the CynosDB Cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

The charge type of instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`. Default value is `POSTPAID_BY_HOUR`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterName

Name of CynosDB cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbType

Type of CynosDB, and available values include `MYSQL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbVersion

Version of CynosDB, which is related to `db_type`. For `MYSQL`, available value is `5.7`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

Indicate whether to delete cluster instance directly or not. Default is false. If set true, the cluster and its `All RELATED INSTANCES` will be deleted instead of staying recycle bin. Note: works for both `PREPAID` and `POSTPAID_BY_HOUR` cluster.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCpuCore

The number of CPU cores of read-write type instance in the CynosDB cluster. Note: modification of this field will take effect immediately, if want to upgrade on maintenance window, please upgrade from console.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMaintainDuration

Duration time for maintenance, unit in second. `3600` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMaintainStartTime

Offset time from 00:00, unit in second. For example, 03:00am should be `10800`. `10800` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMaintainWeekdays

Weekdays for maintenance. `["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]` by default.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMemorySize

Memory capacity of read-write type instance, unit in GB. Note: modification of this field will take effect immediately, if want to upgrade on maintenance window, please upgrade from console.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password of `root` account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port of CynosDB cluster.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrepaidPeriod

The tenancy (time unit is month) of the prepaid instance. Valid values are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `24`, `36`. NOTE: it only works when charge_type is set to `PREPAID`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project. `0` by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoGroupSg

IDs of security group for `ro_group`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RwGroupSg

IDs of security group for `rw_group`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageLimit

Storage limit of CynosDB cluster instance, unit in GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

ID of the subnet within this VPC.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The tags of the CynosDB cluster.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

ID of the VPC.

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

#### Charset

Returns the <code>Charset</code> value.

#### ClusterStatus

Returns the <code>ClusterStatus</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

#### InstanceName

Returns the <code>InstanceName</code> value.

#### InstanceStatus

Returns the <code>InstanceStatus</code> value.

#### InstanceStorageSize

Returns the <code>InstanceStorageSize</code> value.

#### RoGroupAddr

Returns the <code>RoGroupAddr</code> value.

#### RoGroupId

Returns the <code>RoGroupId</code> value.

#### RoGroupInstances

Returns the <code>RoGroupInstances</code> value.

#### RwGroupAddr

Returns the <code>RwGroupAddr</code> value.

#### RwGroupId

Returns the <code>RwGroupId</code> value.

#### RwGroupInstances

Returns the <code>RwGroupInstances</code> value.

#### StorageUsed

Returns the <code>StorageUsed</code> value.

