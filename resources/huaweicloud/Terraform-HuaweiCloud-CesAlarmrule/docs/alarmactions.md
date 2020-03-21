# Terraform::HuaweiCloud::CesAlarmrule AlarmActions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#notificationlist" title="NotificationList">NotificationList</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#notificationlist" title="NotificationList">NotificationList</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### NotificationList

specifies the topic urn list of the target
notification objects. the maximum length is 5. the topic urn list can be
obtained from simple message notification (smn) and in the following format:
urn: smn:([a-z]|[a-z]|[0-9]|\-){1,32}:([a-z]|[a-z]|[0-9]){32}:([a-z]|[a-z]|[0-9]|\-|\_){1,256}.
if type is set to notification, the value of notification_list cannot be
empty. if type is set to autoscaling, the value of notification_list must
be [] and the value of namespace must be sys.as.
Note: to enable the as alarm rules take effect, you must bind scaling
policies. for details, see the auto scaling api reference.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

specifies the type of action triggered by an alarm. the
value can be notification or autoscaling.
notification: indicates that a notification will be sent to the user.
autoscaling: indicates that a scaling action will be triggered.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

