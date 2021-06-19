# TF::Thunder::SnmpServerDisableTraps

`thunder_snmp_server_disable_traps` Provides details about thunder snmp server disable traps

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerDisableTraps",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#gslb" title="Gslb">Gslb</a>" : <i>Double</i>,
        "<a href="#slb" title="Slb">Slb</a>" : <i>Double</i>,
        "<a href="#slbchange" title="SlbChange">SlbChange</a>" : <i>Double</i>,
        "<a href="#snmp" title="Snmp">Snmp</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrrpa" title="VrrpA">VrrpA</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerDisableTraps
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#gslb" title="Gslb">Gslb</a>: <i>Double</i>
    <a href="#slb" title="Slb">Slb</a>: <i>Double</i>
    <a href="#slbchange" title="SlbChange">SlbChange</a>: <i>Double</i>
    <a href="#snmp" title="Snmp">Snmp</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrrpa" title="VrrpA">VrrpA</a>: <i>Double</i>
</pre>

## Properties

#### All

Disable all traps on this partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gslb

Disable all gslb traps on this partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slb

Disable all slb traps on this partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbChange

Disable all slb-change traps on this partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snmp

Disable all snmp traps on this partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpA

Disable all vrrp-a on this partition.

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

