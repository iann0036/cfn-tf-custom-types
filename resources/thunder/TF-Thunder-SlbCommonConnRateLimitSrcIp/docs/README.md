# TF::Thunder::SlbCommonConnRateLimitSrcIp

`thunder_slb_common_conn_rate_limit_src_ip` Provides details about thunder slb common conn rate limit src ip

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbCommonConnRateLimitSrcIp",
    "Properties" : {
        "<a href="#exceedaction" title="ExceedAction">ExceedAction</a>" : <i>Double</i>,
        "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
        "<a href="#limitperiod" title="LimitPeriod">LimitPeriod</a>" : <i>String</i>,
        "<a href="#lockout" title="LockOut">LockOut</a>" : <i>Double</i>,
        "<a href="#log" title="Log">Log</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbCommonConnRateLimitSrcIp
Properties:
    <a href="#exceedaction" title="ExceedAction">ExceedAction</a>: <i>Double</i>
    <a href="#limit" title="Limit">Limit</a>: <i>Double</i>
    <a href="#limitperiod" title="LimitPeriod">LimitPeriod</a>: <i>String</i>
    <a href="#lockout" title="LockOut">LockOut</a>: <i>Double</i>
    <a href="#log" title="Log">Log</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### ExceedAction

Set action if threshold exceeded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

Set max connections per period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitPeriod

‘100’: 100 ms; ‘1000’: 1000 ms;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockOut

Set lockout period in seconds if threshold exceeded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Send log if threshold exceeded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

‘tcp’: Set TCP connection rate limit; ‘udp’: Set UDP packet rate limit;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

Set threshold shared amongst all virtual ports.

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

