# TF::Alicloud::LogAlert

Log alert is a unit of log service, which is used to monitor and alert the user's logstore status information. 
Log Service enables you to configure alerts based on the charts in a dashboard to monitor the service status in real time.

-> **NOTE:** Available in 1.78.0

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::LogAlert",
    "Properties" : {
        "<a href="#alertdescription" title="AlertDescription">AlertDescription</a>" : <i>String</i>,
        "<a href="#alertdisplayname" title="AlertDisplayname">AlertDisplayname</a>" : <i>String</i>,
        "<a href="#alertname" title="AlertName">AlertName</a>" : <i>String</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>String</i>,
        "<a href="#dashboard" title="Dashboard">Dashboard</a>" : <i>String</i>,
        "<a href="#muteuntil" title="MuteUntil">MuteUntil</a>" : <i>Double</i>,
        "<a href="#notifythreshold" title="NotifyThreshold">NotifyThreshold</a>" : <i>Double</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#scheduleinterval" title="ScheduleInterval">ScheduleInterval</a>" : <i>String</i>,
        "<a href="#scheduletype" title="ScheduleType">ScheduleType</a>" : <i>String</i>,
        "<a href="#throttling" title="Throttling">Throttling</a>" : <i>String</i>,
        "<a href="#notificationlist" title="NotificationList">NotificationList</a>" : <i>[ <a href="notificationlistdefinition.md">NotificationListDefinition</a>, ... ]</i>,
        "<a href="#querylist" title="QueryList">QueryList</a>" : <i>[ <a href="querylistdefinition.md">QueryListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::LogAlert
Properties:
    <a href="#alertdescription" title="AlertDescription">AlertDescription</a>: <i>String</i>
    <a href="#alertdisplayname" title="AlertDisplayname">AlertDisplayname</a>: <i>String</i>
    <a href="#alertname" title="AlertName">AlertName</a>: <i>String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>String</i>
    <a href="#dashboard" title="Dashboard">Dashboard</a>: <i>String</i>
    <a href="#muteuntil" title="MuteUntil">MuteUntil</a>: <i>Double</i>
    <a href="#notifythreshold" title="NotifyThreshold">NotifyThreshold</a>: <i>Double</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#scheduleinterval" title="ScheduleInterval">ScheduleInterval</a>: <i>String</i>
    <a href="#scheduletype" title="ScheduleType">ScheduleType</a>: <i>String</i>
    <a href="#throttling" title="Throttling">Throttling</a>: <i>String</i>
    <a href="#notificationlist" title="NotificationList">NotificationList</a>: <i>
      - <a href="notificationlistdefinition.md">NotificationListDefinition</a></i>
    <a href="#querylist" title="QueryList">QueryList</a>: <i>
      - <a href="querylistdefinition.md">QueryListDefinition</a></i>
</pre>

## Properties

#### AlertDescription

Alert description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertDisplayname

Alert displayname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertName

Name of logstore for configuring alarm service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

Conditional expression, such as: count> 100.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dashboard

The name of the dashboard associated with the alarm. The name of the instrument cluster associated with the alarm. If there is no such instrument cluster, terraform will help you create an empty instrument cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MuteUntil

Timestamp, notifications before closing again.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyThreshold

Notification threshold, which is not notified until the number of triggers is reached. The default is 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

The project name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleInterval

Execution interval. 60 seconds minimum, such as 60s, 1h.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleType

Default FixedRate. No need to configure this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Throttling

Notification interval, default is no interval. Support number + unit type, for example 60s, 1h.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationList

_Required_: No

_Type_: List of <a href="notificationlistdefinition.md">NotificationListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryList

_Required_: No

_Type_: List of <a href="querylistdefinition.md">QueryListDefinition</a>

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

