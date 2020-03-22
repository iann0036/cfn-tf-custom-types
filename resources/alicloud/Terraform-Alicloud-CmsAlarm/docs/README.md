# Terraform::Alicloud::CmsAlarm

This resource provides a alarm rule resource and it can be used to monitor several cloud services according different metrics.
Details for [alarm rule](https://www.alibabacloud.com/help/doc-detail/28608.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CmsAlarm",
    "Properties" : {
        "<a href="#contactgroups" title="ContactGroups">ContactGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>,
        "<a href="#effectiveinterval" title="EffectiveInterval">EffectiveInterval</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifytype" title="NotifyType">NotifyType</a>" : <i>Double</i>,
        "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#silencetime" title="SilenceTime">SilenceTime</a>" : <i>Double</i>,
        "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>,
        "<a href="#statistics" title="Statistics">Statistics</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>String</i>,
        "<a href="#triggeredcount" title="TriggeredCount">TriggeredCount</a>" : <i>Double</i>,
        "<a href="#webhook" title="Webhook">Webhook</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CmsAlarm
Properties:
    <a href="#contactgroups" title="ContactGroups">ContactGroups</a>: <i>
      - String</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
    <a href="#effectiveinterval" title="EffectiveInterval">EffectiveInterval</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
    <a href="#metric" title="Metric">Metric</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifytype" title="NotifyType">NotifyType</a>: <i>Double</i>
    <a href="#operator" title="Operator">Operator</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#silencetime" title="SilenceTime">SilenceTime</a>: <i>Double</i>
    <a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
    <a href="#statistics" title="Statistics">Statistics</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>String</i>
    <a href="#triggeredcount" title="TriggeredCount">TriggeredCount</a>: <i>Double</i>
    <a href="#webhook" title="Webhook">Webhook</a>: <i>String</i>
</pre>

## Properties

#### ContactGroups

List contact groups of the alarm rule, which must have been created on the console.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

Map of the resources associated with the alarm rule, such as "instanceId", "device" and "port". Each key's value is a string and it uses comma to split multiple items. For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

_Required_: Yes

_Type_: List of <a href="dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EffectiveInterval

The interval of effecting alarm rule. It foramt as "hh:mm-hh:mm", like "0:00-4:00". Default to "00:00-23:59".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether to enable alarm rule. Default to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

It has been deprecated from provider version 1.50.0 and 'effective_interval' instead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

Name of the monitoring metrics corresponding to a project, such as "CPUUtilization" and "networkin_rate". For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The alarm rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyType

Notification type. Valid value [0, 1]. The value 0 indicates TradeManager+email, and the value 1 indicates that TradeManager+email+SMS.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

Alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Index query cycle, which must be consistent with that defined for metrics. Default to 300, in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

Monitor project name, such as "acs_ecs_dashboard" and "acs_rds_dashboard". For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SilenceTime

Notification silence period in the alarm state, in seconds. Valid value range: [300, 86400]. Default to 86400.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

It has been deprecated from provider version 1.50.0 and 'effective_interval' instead.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statistics

Statistical method. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

Alarm threshold value, which must be a numeric value currently.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggeredCount

Number of consecutive times it has been detected that the values exceed the threshold. Default to 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhook

The webhook that should be called when the alarm is triggered. Currently, only http protocol is supported. Default is empty string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

