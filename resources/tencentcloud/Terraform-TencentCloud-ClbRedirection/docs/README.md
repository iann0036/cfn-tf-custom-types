# Terraform::TencentCloud::ClbRedirection

CloudFormation equivalent of tencentcloud_clb_redirection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::ClbRedirection",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#clbid" title="ClbId">ClbId</a>" : <i>String</i>,
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
Type: Terraform::TencentCloud::ClbRedirection
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#clbid" title="ClbId">ClbId</a>: <i>String</i>
    <a href="#isautorewrite" title="IsAutoRewrite">IsAutoRewrite</a>: <i>Boolean</i>
    <a href="#sourcelistenerid" title="SourceListenerId">SourceListenerId</a>: <i>String</i>
    <a href="#sourceruleid" title="SourceRuleId">SourceRuleId</a>: <i>String</i>
    <a href="#targetlistenerid" title="TargetListenerId">TargetListenerId</a>: <i>String</i>
    <a href="#targetruleid" title="TargetRuleId">TargetRuleId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClbId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsAutoRewrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceListenerId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceRuleId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetListenerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRuleId

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

