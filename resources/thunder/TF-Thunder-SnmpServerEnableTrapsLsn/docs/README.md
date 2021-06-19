# TF::Thunder::SnmpServerEnableTrapsLsn

`thunder_snmp_server_enable_traps_lsn` Provides details about thunder snmp server enable traps lsn

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsLsn",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#fixednatportmappingfilechange" title="FixedNatPortMappingFileChange">FixedNatPortMappingFileChange</a>" : <i>Double</i>,
        "<a href="#maxipportthreshold" title="MaxIpportThreshold">MaxIpportThreshold</a>" : <i>Double</i>,
        "<a href="#maxportthreshold" title="MaxPortThreshold">MaxPortThreshold</a>" : <i>Double</i>,
        "<a href="#peripportusagethreshold" title="PerIpPortUsageThreshold">PerIpPortUsageThreshold</a>" : <i>Double</i>,
        "<a href="#totalportusagethreshold" title="TotalPortUsageThreshold">TotalPortUsageThreshold</a>" : <i>Double</i>,
        "<a href="#trafficexceeded" title="TrafficExceeded">TrafficExceeded</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsLsn
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#fixednatportmappingfilechange" title="FixedNatPortMappingFileChange">FixedNatPortMappingFileChange</a>: <i>Double</i>
    <a href="#maxipportthreshold" title="MaxIpportThreshold">MaxIpportThreshold</a>: <i>Double</i>
    <a href="#maxportthreshold" title="MaxPortThreshold">MaxPortThreshold</a>: <i>Double</i>
    <a href="#peripportusagethreshold" title="PerIpPortUsageThreshold">PerIpPortUsageThreshold</a>: <i>Double</i>
    <a href="#totalportusagethreshold" title="TotalPortUsageThreshold">TotalPortUsageThreshold</a>: <i>Double</i>
    <a href="#trafficexceeded" title="TrafficExceeded">TrafficExceeded</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### All

Enable all LSN group traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedNatPortMappingFileChange

Enable LSN trap when fixed nat port mapping file change.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIpportThreshold

Maximum threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPortThreshold

Maximum threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerIpPortUsageThreshold

Enable LSN trap when IP total port usage reaches the threshold (default 64512).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalPortUsageThreshold

Enable LSN trap when NAT total port usage reaches the threshold (default 655350000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficExceeded

Enable LSN trap when NAT pool reaches the threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

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

