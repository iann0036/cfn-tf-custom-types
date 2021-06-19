# TF::Thunder::SnmpServerEnableTrapsSlbChange

`thunder_snmp_server_enable_traps_slb_change` Provides details about thunder snmp server enable traps slb change

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsSlbChange",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#connectionresourceevent" title="ConnectionResourceEvent">ConnectionResourceEvent</a>" : <i>Double</i>,
        "<a href="#resourceusagewarning" title="ResourceUsageWarning">ResourceUsageWarning</a>" : <i>Double</i>,
        "<a href="#server" title="Server">Server</a>" : <i>Double</i>,
        "<a href="#serverport" title="ServerPort">ServerPort</a>" : <i>Double</i>,
        "<a href="#sslcertchange" title="SslCertChange">SslCertChange</a>" : <i>Double</i>,
        "<a href="#sslcertexpire" title="SslCertExpire">SslCertExpire</a>" : <i>Double</i>,
        "<a href="#systemthreshold" title="SystemThreshold">SystemThreshold</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vip" title="Vip">Vip</a>" : <i>Double</i>,
        "<a href="#vipport" title="VipPort">VipPort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsSlbChange
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#connectionresourceevent" title="ConnectionResourceEvent">ConnectionResourceEvent</a>: <i>Double</i>
    <a href="#resourceusagewarning" title="ResourceUsageWarning">ResourceUsageWarning</a>: <i>Double</i>
    <a href="#server" title="Server">Server</a>: <i>Double</i>
    <a href="#serverport" title="ServerPort">ServerPort</a>: <i>Double</i>
    <a href="#sslcertchange" title="SslCertChange">SslCertChange</a>: <i>Double</i>
    <a href="#sslcertexpire" title="SslCertExpire">SslCertExpire</a>: <i>Double</i>
    <a href="#systemthreshold" title="SystemThreshold">SystemThreshold</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vip" title="Vip">Vip</a>: <i>Double</i>
    <a href="#vipport" title="VipPort">VipPort</a>: <i>Double</i>
</pre>

## Properties

#### All

Enable all system group traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionResourceEvent

Enable system connection resource event trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceUsageWarning

Enable partition resource usage warning trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Enable slb server create/delete trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerPort

Enable slb server port create/delete trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertChange

Enable SSL certificate change trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertExpire

Enable SSL certificate expiring trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemThreshold

Enable slb system threshold trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vip

Enable slb vip create/delete trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPort

Enable slb vip-port create/delete trap.

_Required_: No

_Type_: Double

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

