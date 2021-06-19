# TF::TencentCloud::CynosdbReadonlyInstance

Provide a resource to create a CynosDB readonly instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CynosdbReadonlyInstance",
    "Properties" : {
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#instancecpucore" title="InstanceCpuCore">InstanceCpuCore</a>" : <i>Double</i>,
        "<a href="#instancemaintainduration" title="InstanceMaintainDuration">InstanceMaintainDuration</a>" : <i>Double</i>,
        "<a href="#instancemaintainstarttime" title="InstanceMaintainStartTime">InstanceMaintainStartTime</a>" : <i>Double</i>,
        "<a href="#instancemaintainweekdays" title="InstanceMaintainWeekdays">InstanceMaintainWeekdays</a>" : <i>[ String, ... ]</i>,
        "<a href="#instancememorysize" title="InstanceMemorySize">InstanceMemorySize</a>" : <i>Double</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CynosdbReadonlyInstance
Properties:
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#instancecpucore" title="InstanceCpuCore">InstanceCpuCore</a>: <i>Double</i>
    <a href="#instancemaintainduration" title="InstanceMaintainDuration">InstanceMaintainDuration</a>: <i>Double</i>
    <a href="#instancemaintainstarttime" title="InstanceMaintainStartTime">InstanceMaintainStartTime</a>: <i>Double</i>
    <a href="#instancemaintainweekdays" title="InstanceMaintainWeekdays">InstanceMaintainWeekdays</a>: <i>
      - String</i>
    <a href="#instancememorysize" title="InstanceMemorySize">InstanceMemorySize</a>: <i>Double</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
</pre>

## Properties

#### ClusterId

Cluster ID which the readonly instance belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

Indicate whether to delete readonly instance directly or not. Default is false. If set true, instance will be deleted instead of staying recycle bin. Note: works for both `PREPAID` and `POSTPAID_BY_HOUR` cluster.

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

#### InstanceName

Name of instance.

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

#### InstanceStatus

Returns the <code>InstanceStatus</code> value.

#### InstanceStorageSize

Returns the <code>InstanceStorageSize</code> value.

