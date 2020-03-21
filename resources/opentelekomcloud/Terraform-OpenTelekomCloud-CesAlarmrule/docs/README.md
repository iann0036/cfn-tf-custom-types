# Terraform::OpenTelekomCloud::CesAlarmrule

Manages a V2 topic resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::CesAlarmrule",
    "Properties" : {
        "<a href="#alarmactionenabled" title="AlarmActionEnabled">AlarmActionEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>" : <i>String</i>,
        "<a href="#alarmenabled" title="AlarmEnabled">AlarmEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmname" title="AlarmName">AlarmName</a>" : <i>String</i>,
        "<a href="#alarmstate" title="AlarmState">AlarmState</a>" : <i>String</i>,
        "<a href="#updatetime" title="UpdateTime">UpdateTime</a>" : <i>Double</i>,
        "<a href="#alarmactions" title="AlarmActions">AlarmActions</a>" : <i>[ <a href="alarmactions.md">AlarmActions</a>, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="condition.md">Condition</a>, ... ]</i>,
        "<a href="#insufficientdataactions" title="InsufficientdataActions">InsufficientdataActions</a>" : <i>[ <a href="insufficientdataactions.md">InsufficientdataActions</a>, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metric.md">Metric</a>, ... ]</i>,
        "<a href="#okactions" title="OkActions">OkActions</a>" : <i>[ <a href="okactions.md">OkActions</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::CesAlarmrule
Properties:
    <a href="#alarmactionenabled" title="AlarmActionEnabled">AlarmActionEnabled</a>: <i>Boolean</i>
    <a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>: <i>String</i>
    <a href="#alarmenabled" title="AlarmEnabled">AlarmEnabled</a>: <i>Boolean</i>
    <a href="#alarmname" title="AlarmName">AlarmName</a>: <i>String</i>
    <a href="#alarmstate" title="AlarmState">AlarmState</a>: <i>String</i>
    <a href="#updatetime" title="UpdateTime">UpdateTime</a>: <i>Double</i>
    <a href="#alarmactions" title="AlarmActions">AlarmActions</a>: <i>
      - <a href="alarmactions.md">AlarmActions</a></i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="condition.md">Condition</a></i>
    <a href="#insufficientdataactions" title="InsufficientdataActions">InsufficientdataActions</a>: <i>
      - <a href="insufficientdataactions.md">InsufficientdataActions</a></i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metric.md">Metric</a></i>
    <a href="#okactions" title="OkActions">OkActions</a>: <i>
      - <a href="okactions.md">OkActions</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
</pre>

## Properties

#### AlarmActionEnabled

Specifies whether to enable the action
to be triggered by an alarm. The default value is true.
Note: If alarm_action_enabled is set to true, at least one of the following
parameters alarm_actions, insufficientdata_actions, and ok_actions cannot
be empty. If alarm_actions, insufficientdata_actions, and ok_actions coexist,
their corresponding notification_list must be of the same value.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmDescription

The value can be a string of 0 to 256 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmEnabled

Specifies whether to enable the alarm. The default
value is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmName

Specifies the name of an alarm rule. The value can
be a string of 1 to 128 characters that can consist of numbers, lowercase letters,
uppercase letters, underscores (_), or hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmActions

_Required_: No

_Type_: List of <a href="alarmactions.md">AlarmActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="condition.md">Condition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientdataActions

_Required_: No

_Type_: List of <a href="insufficientdataactions.md">InsufficientdataActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metric.md">Metric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OkActions

_Required_: No

_Type_: List of <a href="okactions.md">OkActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

