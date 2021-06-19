# TF::AWS::AutoscalingLifecycleHook

Provides an AutoScaling Lifecycle Hook resource.

~> **NOTE:** Terraform has two types of ways you can add lifecycle hooks - via
the `initial_lifecycle_hook` attribute from the
[`aws_autoscaling_group`](/docs/providers/aws/r/autoscaling_group.html)
resource, or via this one. Hooks added via this resource will not be added
until the autoscaling group has been created, and depending on your
[capacity](/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity)
settings, after the initial instances have been launched, creating unintended
behavior. If you need hooks to run on all instances, add them with
`initial_lifecycle_hook` in
[`aws_autoscaling_group`](/docs/providers/aws/r/autoscaling_group.html),
but take care to not duplicate those hooks with this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AutoscalingLifecycleHook",
    "Properties" : {
        "<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>" : <i>String</i>,
        "<a href="#defaultresult" title="DefaultResult">DefaultResult</a>" : <i>String</i>,
        "<a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>" : <i>Double</i>,
        "<a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>" : <i>String</i>,
        "<a href="#notificationtargetarn" title="NotificationTargetArn">NotificationTargetArn</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AutoscalingLifecycleHook
Properties:
    <a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>: <i>String</i>
    <a href="#defaultresult" title="DefaultResult">DefaultResult</a>: <i>String</i>
    <a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>: <i>Double</i>
    <a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>: <i>String</i>
    <a href="#notificationtargetarn" title="NotificationTargetArn">NotificationTargetArn</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
</pre>

## Properties

#### AutoscalingGroupName

The name of the Auto Scaling group to which you want to assign the lifecycle hook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultResult

Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeartbeatTimeout

Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleTransition

The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the lifecycle hook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationMetadata

Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTargetArn

The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

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

