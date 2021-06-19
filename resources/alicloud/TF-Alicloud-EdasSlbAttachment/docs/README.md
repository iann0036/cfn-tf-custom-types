# TF::Alicloud::EdasSlbAttachment

Binds SLB to an EDAS application.

-> **NOTE:** Available in 1.82.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EdasSlbAttachment",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#listenerport" title="ListenerPort">ListenerPort</a>" : <i>Double</i>,
        "<a href="#slbid" title="SlbId">SlbId</a>" : <i>String</i>,
        "<a href="#slbip" title="SlbIp">SlbIp</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vservergroupid" title="VserverGroupId">VserverGroupId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EdasSlbAttachment
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#listenerport" title="ListenerPort">ListenerPort</a>: <i>Double</i>
    <a href="#slbid" title="SlbId">SlbId</a>: <i>String</i>
    <a href="#slbip" title="SlbIp">SlbIp</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vservergroupid" title="VserverGroupId">VserverGroupId</a>: <i>String</i>
</pre>

## Properties

#### AppId

The ID of the applicaton to which you want to bind an SLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerPort

The listening port for the bound SLB instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbId

The ID of the SLB instance that is going to be bound.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbIp

The IP address that is allocated to the bound SLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the bound SLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VserverGroupId

The ID of the virtual server (VServer) group associated with the intranet SLB instance.

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

#### SlbStatus

Returns the <code>SlbStatus</code> value.

#### VswitchId

Returns the <code>VswitchId</code> value.

