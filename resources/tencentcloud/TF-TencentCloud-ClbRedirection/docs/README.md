# TF::TencentCloud::ClbRedirection

Provides a resource to create a CLB redirection.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbRedirection",
    "Properties" : {
        "<a href="#clbid" title="ClbId">ClbId</a>" : <i>String</i>,
        "<a href="#deleteallautorewrite" title="DeleteAllAutoRewrite">DeleteAllAutoRewrite</a>" : <i>Boolean</i>,
        "<a href="#isautorewrite" title="IsAutoRewrite">IsAutoRewrite</a>" : <i>Boolean</i>,
        "<a href="#sourcelistenerid" title="SourceListenerId">SourceListenerId</a>" : <i>String</i>,
        "<a href="#sourceruleid" title="SourceRuleId">SourceRuleId</a>" : <i>String</i>,
        "<a href="#targetlistenerid" title="TargetListenerId">TargetListenerId</a>" : <i>String</i>,
        "<a href="#targetruleid" title="TargetRuleId">TargetRuleId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbRedirection
Properties:
    <a href="#clbid" title="ClbId">ClbId</a>: <i>String</i>
    <a href="#deleteallautorewrite" title="DeleteAllAutoRewrite">DeleteAllAutoRewrite</a>: <i>Boolean</i>
    <a href="#isautorewrite" title="IsAutoRewrite">IsAutoRewrite</a>: <i>Boolean</i>
    <a href="#sourcelistenerid" title="SourceListenerId">SourceListenerId</a>: <i>String</i>
    <a href="#sourceruleid" title="SourceRuleId">SourceRuleId</a>: <i>String</i>
    <a href="#targetlistenerid" title="TargetListenerId">TargetListenerId</a>: <i>String</i>
    <a href="#targetruleid" title="TargetRuleId">TargetRuleId</a>: <i>String</i>
</pre>

## Properties

#### ClbId

ID of CLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAllAutoRewrite

Indicates whether delete all auto redirection. Default is `false`. It will take effect only when this redirection is auto-rewrite and this auto-rewrite auto redirected more than one rules. All the auto-rewrite relations will be deleted when this parameter set true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoRewrite

Indicates whether automatic forwarding is enable, default is `false`. If enabled, the source listener and location should be empty, the target listener must be https protocol and port is 443.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceListenerId

ID of source listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRuleId

Rule ID of source listener.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetListenerId

ID of source listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRuleId

Rule ID of target listener.

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

