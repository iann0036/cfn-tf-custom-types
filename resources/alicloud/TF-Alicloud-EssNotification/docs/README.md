# TF::Alicloud::EssNotification

Provides a ESS notification resource. More about Ess notification, see [Autoscaling Notification](https://www.alibabacloud.com/help/doc-detail/71114.htm).

-> **NOTE:** Available in 1.55.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EssNotification",
    "Properties" : {
        "<a href="#notificationarn" title="NotificationArn">NotificationArn</a>" : <i>String</i>,
        "<a href="#notificationtypes" title="NotificationTypes">NotificationTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EssNotification
Properties:
    <a href="#notificationarn" title="NotificationArn">NotificationArn</a>: <i>String</i>
    <a href="#notificationtypes" title="NotificationTypes">NotificationTypes</a>: <i>
      - String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
</pre>

## Properties

#### NotificationArn

The Alibaba Cloud Resource Name (ARN) of the notification object, The value must be in `acs:ess:{region}:{account-id}:{resource-relative-id}` format.
* region: the region ID of the scaling group. For more information, see `Regions and zones`
* account-id: the ID of your account.
* resource-relative-id: the notification method. Valid values : `cloudmonitor`, MNS queue: `queue/{queuename}`, Replace the queuename with the specific MNS queue name, MNS topic: `topic/{topicname}`, Replace the topicname with the specific MNS topic name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationTypes

The notification types of Auto Scaling events and resource changes. Supported notification types: 'AUTOSCALING:SCALE_OUT_SUCCESS', 'AUTOSCALING:SCALE_IN_SUCCESS', 'AUTOSCALING:SCALE_OUT_ERROR', 'AUTOSCALING:SCALE_IN_ERROR', 'AUTOSCALING:SCALE_REJECT', 'AUTOSCALING:SCALE_OUT_START', 'AUTOSCALING:SCALE_IN_START', 'AUTOSCALING:SCHEDULE_TASK_EXPIRING'.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

The ID of the Auto Scaling group.

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

