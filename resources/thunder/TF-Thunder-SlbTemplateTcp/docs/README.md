# TF::Thunder::SlbTemplateTcp

`thunder_slb_template_tcp` Provides details about thunder slb template tcp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateTcp",
    "Properties" : {
        "<a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>" : <i>Double</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>" : <i>Double</i>,
        "<a href="#lanfastack" title="LanFastAck">LanFastAck</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resetfollowfin" title="ResetFollowFin">ResetFollowFin</a>" : <i>Double</i>,
        "<a href="#resetfwd" title="ResetFwd">ResetFwd</a>" : <i>Double</i>,
        "<a href="#resetrev" title="ResetRev">ResetRev</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateTcp
Properties:
    <a href="#delsessiononserverdown" title="DelSessionOnServerDown">DelSessionOnServerDown</a>: <i>Double</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#insertclientip" title="InsertClientIp">InsertClientIp</a>: <i>Double</i>
    <a href="#lanfastack" title="LanFastAck">LanFastAck</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resetfollowfin" title="ResetFollowFin">ResetFollowFin</a>: <i>Double</i>
    <a href="#resetfwd" title="ResetFwd">ResetFwd</a>: <i>Double</i>
    <a href="#resetrev" title="ResetRev">ResetRev</a>: <i>Double</i>
</pre>

## Properties

#### DelSessionOnServerDown

Delete session if the server/port goes down (either disabled/hm down).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

Idle Timeout value (Interval of 60 seconds), default 120 seconds (idle timeout in second, default 120).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertClientIp

Insert client ip into TCP option.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LanFastAck

Enable fast TCP ack on LAN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Fast TCP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetFollowFin

send reset to client or server upon receiving first fin.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetFwd

send reset to server if error happens.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetRev

send reset to client if error happens.

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

