# Terraform::OpenTelekomCloud::AsPolicyV1

Manages a V1 AS Policy resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::AsPolicyV1",
    "Properties" : {
        "<a href="#alarmid" title="AlarmId">AlarmId</a>" : <i>String</i>,
        "<a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#scalingpolicyname" title="ScalingPolicyName">ScalingPolicyName</a>" : <i>String</i>,
        "<a href="#scalingpolicytype" title="ScalingPolicyType">ScalingPolicyType</a>" : <i>String</i>,
        "<a href="#scalingpolicyaction" title="ScalingPolicyAction">ScalingPolicyAction</a>" : <i>[ <a href="scalingpolicyaction.md">ScalingPolicyAction</a>, ... ]</i>,
        "<a href="#scheduledpolicy" title="ScheduledPolicy">ScheduledPolicy</a>" : <i>[ <a href="scheduledpolicy.md">ScheduledPolicy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::AsPolicyV1
Properties:
    <a href="#alarmid" title="AlarmId">AlarmId</a>: <i>String</i>
    <a href="#cooldowntime" title="CoolDownTime">CoolDownTime</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#scalingpolicyname" title="ScalingPolicyName">ScalingPolicyName</a>: <i>String</i>
    <a href="#scalingpolicytype" title="ScalingPolicyType">ScalingPolicyType</a>: <i>String</i>
    <a href="#scalingpolicyaction" title="ScalingPolicyAction">ScalingPolicyAction</a>: <i>
      - <a href="scalingpolicyaction.md">ScalingPolicyAction</a></i>
    <a href="#scheduledpolicy" title="ScheduledPolicy">ScheduledPolicy</a>: <i>
      - <a href="scheduledpolicy.md">ScheduledPolicy</a></i>
</pre>

## Properties

#### AlarmId

The alarm rule ID. This argument is mandatory
when `scaling_policy_type` is set to `ALARM`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoolDownTime

The cooling duration (in seconds), and is 900 by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

The AS group ID. Changing this creates a new AS policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyName

The name of the AS policy. The name can contain letters,
digits, underscores(_), and hyphens(-),and cannot exceed 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyType

The AS policy type. The values can be `ALARM`, `SCHEDULED`,
and `RECURRENCE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingPolicyAction

_Required_: No

_Type_: List of <a href="scalingpolicyaction.md">ScalingPolicyAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledPolicy

_Required_: No

_Type_: List of <a href="scheduledpolicy.md">ScheduledPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

