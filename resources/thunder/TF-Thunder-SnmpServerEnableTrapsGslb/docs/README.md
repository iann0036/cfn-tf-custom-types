# TF::Thunder::SnmpServerEnableTrapsGslb

`thunder_snmp_server_enable_traps_gslb` Provides details about thunder snmp server enable traps gslb

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsGslb",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#group" title="Group">Group</a>" : <i>Double</i>,
        "<a href="#serviceip" title="ServiceIp">ServiceIp</a>" : <i>Double</i>,
        "<a href="#site" title="Site">Site</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsGslb
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#group" title="Group">Group</a>: <i>Double</i>
    <a href="#serviceip" title="ServiceIp">ServiceIp</a>: <i>Double</i>
    <a href="#site" title="Site">Site</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>Double</i>
</pre>

## Properties

#### All

Enable all GSLB traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Enable GSLB group related traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceIp

Enable GSLB service-ip related traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Site

Enable GSLB site related traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

Enable GSLB zone related traps.

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

