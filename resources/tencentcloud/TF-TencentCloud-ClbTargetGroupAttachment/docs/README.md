# TF::TencentCloud::ClbTargetGroupAttachment

Provides a resource to create a CLB target group attachment is bound to the load balancing listener or forwarding rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbTargetGroupAttachment",
    "Properties" : {
        "<a href="#clbid" title="ClbId">ClbId</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#ruleid" title="RuleId">RuleId</a>" : <i>String</i>,
        "<a href="#targetgroupid" title="TargetGroupId">TargetGroupId</a>" : <i>String</i>,
        "<a href="#targrtgroupid" title="TargrtGroupId">TargrtGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbTargetGroupAttachment
Properties:
    <a href="#clbid" title="ClbId">ClbId</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#ruleid" title="RuleId">RuleId</a>: <i>String</i>
    <a href="#targetgroupid" title="TargetGroupId">TargetGroupId</a>: <i>String</i>
    <a href="#targrtgroupid" title="TargrtGroupId">TargrtGroupId</a>: <i>String</i>
</pre>

## Properties

#### ClbId

ID of the CLB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

ID of the CLB listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleId

ID of the CLB listener rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupId

ID of the CLB target group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargrtGroupId

It has been deprecated from version 1.47.1. Use `target_group_id` instead. ID of the CLB target group.

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

