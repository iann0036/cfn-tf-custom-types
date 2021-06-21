# TF::Thunder::SnmpServerSlbDataCacheTimeout

`thunder_snmp_server_slb_data_cache_timeout` Provides details about thunder snmp server slb data cache timeout

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerSlbDataCacheTimeout",
    "Properties" : {
        "<a href="#slblimit" title="Slblimit">Slblimit</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerSlbDataCacheTimeout
Properties:
    <a href="#slblimit" title="Slblimit">Slblimit</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### Slblimit

Cache time-out in seconds, default as 60 seconds.

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
