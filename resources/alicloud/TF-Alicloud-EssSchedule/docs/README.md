# TF::Alicloud::EssSchedule

-> **NOTE:** This resource has been deprecated from [v1.45.0](https://releases.hashicorp.com/terraform-provider-alicloud/1.45.0/). New resource `alicloud_ess_scheduled_task` will replace.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::EssSchedule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>" : <i>Double</i>,
        "<a href="#launchtime" title="LaunchTime">LaunchTime</a>" : <i>String</i>,
        "<a href="#maxvalue" title="MaxValue">MaxValue</a>" : <i>Double</i>,
        "<a href="#minvalue" title="MinValue">MinValue</a>" : <i>Double</i>,
        "<a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>" : <i>String</i>,
        "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
        "<a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>" : <i>String</i>,
        "<a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>" : <i>String</i>,
        "<a href="#scheduledaction" title="ScheduledAction">ScheduledAction</a>" : <i>String</i>,
        "<a href="#scheduledtaskname" title="ScheduledTaskName">ScheduledTaskName</a>" : <i>String</i>,
        "<a href="#taskenabled" title="TaskEnabled">TaskEnabled</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::EssSchedule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#launchexpirationtime" title="LaunchExpirationTime">LaunchExpirationTime</a>: <i>Double</i>
    <a href="#launchtime" title="LaunchTime">LaunchTime</a>: <i>String</i>
    <a href="#maxvalue" title="MaxValue">MaxValue</a>: <i>Double</i>
    <a href="#minvalue" title="MinValue">MinValue</a>: <i>Double</i>
    <a href="#recurrenceendtime" title="RecurrenceEndTime">RecurrenceEndTime</a>: <i>String</i>
    <a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
    <a href="#recurrencevalue" title="RecurrenceValue">RecurrenceValue</a>: <i>String</i>
    <a href="#scalinggroupid" title="ScalingGroupId">ScalingGroupId</a>: <i>String</i>
    <a href="#scheduledaction" title="ScheduledAction">ScheduledAction</a>: <i>String</i>
    <a href="#scheduledtaskname" title="ScheduledTaskName">ScheduledTaskName</a>: <i>String</i>
    <a href="#taskenabled" title="TaskEnabled">TaskEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchExpirationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceEndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTaskName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskEnabled

_Required_: No

_Type_: Boolean

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

