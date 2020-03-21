# Terraform::AWS::AutoscalingGroup InitialLifecycleHook

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultresult" title="DefaultResult">DefaultResult</a>" : <i>String</i>,
    "<a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>" : <i>Double</i>,
    "<a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>" : <i>String</i>,
    "<a href="#notificationtargetarn" title="NotificationTargetArn">NotificationTargetArn</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#defaultresult" title="DefaultResult">DefaultResult</a>: <i>String</i>
<a href="#heartbeattimeout" title="HeartbeatTimeout">HeartbeatTimeout</a>: <i>Double</i>
<a href="#lifecycletransition" title="LifecycleTransition">LifecycleTransition</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#notificationmetadata" title="NotificationMetadata">NotificationMetadata</a>: <i>String</i>
<a href="#notificationtargetarn" title="NotificationTargetArn">NotificationTargetArn</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
</pre>

## Properties

#### DefaultResult

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeartbeatTimeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleTransition

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationMetadata

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTargetArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

