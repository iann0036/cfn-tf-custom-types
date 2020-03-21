# Terraform::TencentCloud::AsNotification

Provides a resource for an AS (Auto scaling) notification.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::AsNotification",
    "Properties" : {
        "<a href="#notificationtypes" title="NotificationTypes">NotificationTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationusergroupids" title="NotificationUserGroupIds">NotificationUserGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::AsNotification
Properties:
    <a href="#notificationtypes" title="NotificationTypes">NotificationTypes</a>: <i>
      - String</i>
    <a href="#notificationusergroupids" title="NotificationUserGroupIds">NotificationUserGroupIds</a>: <i>
      - String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
</pre>

## Properties

#### NotificationTypes

A list of Notification Types that trigger notifications. Acceptable values are SCALE_OUT_FAILED, SCALE_IN_SUCCESSFUL, SCALE_IN_FAILED, REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL and REPLACE_UNHEALTHY_INSTANCE_FAILED.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationUserGroupIds

A group of user IDs to be notified.

_Required_: Yes

_Type_: List of String

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

