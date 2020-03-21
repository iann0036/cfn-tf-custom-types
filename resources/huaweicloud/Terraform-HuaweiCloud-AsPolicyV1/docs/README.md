# Terraform::HuaweiCloud::AsPolicyV1

CloudFormation equivalent of huaweicloud_as_policy_v1

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::AsPolicyV1",
    "Properties" : {
        "<a href="#alarmid" title="AlarmId">AlarmId</a>" : <i>String</i>,
        "<a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#scalingpolicyname" title="ScalingPolicyName">ScalingPolicyName</a>" : <i>String</i>,
        "<a href="#scalingpolicytype" title="ScalingPolicyType">ScalingPolicyType</a>" : <i>String</i>,
        "<a href="#scalingpolicyaction" title="ScalingPolicyAction">ScalingPolicyAction</a>" : <i>[ &lt;a href=&#34;scalingpolicyaction.md&#34;&gt;ScalingPolicyAction&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduledpolicy" title="ScheduledPolicy">ScheduledPolicy</a>" : <i>[ &lt;a href=&#34;scheduledpolicy.md&#34;&gt;ScheduledPolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::AsPolicyV1
Properties:
    <a href="#alarmid" title="AlarmId">AlarmId</a>: <i>String</i>
    <a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#scalingpolicyname" title="ScalingPolicyName">ScalingPolicyName</a>: <i>String</i>
    <a href="#scalingpolicytype" title="ScalingPolicyType">ScalingPolicyType</a>: <i>String</i>
    <a href="#scalingpolicyaction" title="ScalingPolicyAction">ScalingPolicyAction</a>: <i>
      - &lt;a href=&#34;scalingpolicyaction.md&#34;&gt;ScalingPolicyAction&lt;/a&gt;</i>
    <a href="#scheduledpolicy" title="ScheduledPolicy">ScheduledPolicy</a>: <i>
      - &lt;a href=&#34;scheduledpolicy.md&#34;&gt;ScheduledPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### AlarmId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyAction

_Required_: No

_Type_: List of &lt;a href=&#34;scalingpolicyaction.md&#34;&gt;ScalingPolicyAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;scheduledpolicy.md&#34;&gt;ScheduledPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

