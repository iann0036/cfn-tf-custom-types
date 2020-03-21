# Terraform::TencentCloud::AsLifecycleHook

Provides a resource for an AS (Auto scaling) lifecycle hook.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::AsLifecycleHook",
    "Properties" : {
        "<a href="#defaultresult" title="DefaultResult">DefaultResult</a>" : <i>String</i>,
        "<a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>" : <i>Double</i>,
        "<a href="#lifecyclehookname" title="LifecycleHookName">LifecycleHookName</a>" : <i>String</i>,
        "<a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>" : <i>String</i>,
        "<a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>" : <i>String</i>,
        "<a href="#notificationqueuename" title="NotificationQueueName">NotificationQueueName</a>" : <i>String</i>,
        "<a href="#notificationtargettype" title="NotificationTargetType">NotificationTargetType</a>" : <i>String</i>,
        "<a href="#notificationtopicname" title="NotificationTopicName">NotificationTopicName</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::AsLifecycleHook
Properties:
    <a href="#defaultresult" title="DefaultResult">DefaultResult</a>: <i>String</i>
    <a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>: <i>Double</i>
    <a href="#lifecyclehookname" title="LifecycleHookName">LifecycleHookName</a>: <i>String</i>
    <a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>: <i>String</i>
    <a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>: <i>String</i>
    <a href="#notificationqueuename" title="NotificationQueueName">NotificationQueueName</a>: <i>String</i>
    <a href="#notificationtargettype" title="NotificationTargetType">NotificationTargetType</a>: <i>String</i>
    <a href="#notificationtopicname" title="NotificationTopicName">NotificationTopicName</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
</pre>

## Properties

#### DefaultResult

Defines the action the AS group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The valid values are CONTINUE and ABANDON. The default value is CONTINUE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeartbeatTimeout

Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. The range is 30 to 3600, and default value is 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleHookName

The name of the lifecycle hook.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleTransition

The instance state to which you want to attach the lifecycle hook. The valid values are INSTANCE_LAUNCHING and INSTANCE_TERMINATING.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationMetadata

Contains additional information that you want to include any time AS sends a message to the notification target.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationQueueName

For CMQ_QUEUE type, a name of queue must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTargetType

Target type, which can be CMQ_QUEUE or CMQ_TOPIC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTopicName

For CMQ_TOPIC type, a name of topic must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

ID of a scaling group.

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

