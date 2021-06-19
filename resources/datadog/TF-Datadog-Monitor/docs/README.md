# TF::Datadog::Monitor

CloudFormation equivalent of datadog_monitor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::Monitor",
    "Properties" : {
        "<a href="#enablelogssample" title="EnableLogsSample">EnableLogsSample</a>" : <i>Boolean</i>,
        "<a href="#escalationmessage" title="EscalationMessage">EscalationMessage</a>" : <i>String</i>,
        "<a href="#evaluationdelay" title="EvaluationDelay">EvaluationDelay</a>" : <i>Double</i>,
        "<a href="#forcedelete" title="ForceDelete">ForceDelete</a>" : <i>Boolean</i>,
        "<a href="#groupbysimplemonitor" title="GroupbySimpleMonitor">GroupbySimpleMonitor</a>" : <i>Boolean</i>,
        "<a href="#includetags" title="IncludeTags">IncludeTags</a>" : <i>Boolean</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#newhostdelay" title="NewHostDelay">NewHostDelay</a>" : <i>Double</i>,
        "<a href="#nodatatimeframe" title="NoDataTimeframe">NoDataTimeframe</a>" : <i>Double</i>,
        "<a href="#notifyaudit" title="NotifyAudit">NotifyAudit</a>" : <i>Boolean</i>,
        "<a href="#notifynodata" title="NotifyNoData">NotifyNoData</a>" : <i>Boolean</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#renotifyinterval" title="RenotifyInterval">RenotifyInterval</a>" : <i>Double</i>,
        "<a href="#requirefullwindow" title="RequireFullWindow">RequireFullWindow</a>" : <i>Boolean</i>,
        "<a href="#restrictedroles" title="RestrictedRoles">RestrictedRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouth" title="TimeoutH">TimeoutH</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#validate" title="Validate">Validate</a>" : <i>Boolean</i>,
        "<a href="#monitorthresholdwindows" title="MonitorThresholdWindows">MonitorThresholdWindows</a>" : <i>[ <a href="monitorthresholdwindowsdefinition.md">MonitorThresholdWindowsDefinition</a>, ... ]</i>,
        "<a href="#monitorthresholds" title="MonitorThresholds">MonitorThresholds</a>" : <i>[ <a href="monitorthresholdsdefinition.md">MonitorThresholdsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::Monitor
Properties:
    <a href="#enablelogssample" title="EnableLogsSample">EnableLogsSample</a>: <i>Boolean</i>
    <a href="#escalationmessage" title="EscalationMessage">EscalationMessage</a>: <i>String</i>
    <a href="#evaluationdelay" title="EvaluationDelay">EvaluationDelay</a>: <i>Double</i>
    <a href="#forcedelete" title="ForceDelete">ForceDelete</a>: <i>Boolean</i>
    <a href="#groupbysimplemonitor" title="GroupbySimpleMonitor">GroupbySimpleMonitor</a>: <i>Boolean</i>
    <a href="#includetags" title="IncludeTags">IncludeTags</a>: <i>Boolean</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#newhostdelay" title="NewHostDelay">NewHostDelay</a>: <i>Double</i>
    <a href="#nodatatimeframe" title="NoDataTimeframe">NoDataTimeframe</a>: <i>Double</i>
    <a href="#notifyaudit" title="NotifyAudit">NotifyAudit</a>: <i>Boolean</i>
    <a href="#notifynodata" title="NotifyNoData">NotifyNoData</a>: <i>Boolean</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#renotifyinterval" title="RenotifyInterval">RenotifyInterval</a>: <i>Double</i>
    <a href="#requirefullwindow" title="RequireFullWindow">RequireFullWindow</a>: <i>Boolean</i>
    <a href="#restrictedroles" title="RestrictedRoles">RestrictedRoles</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#timeouth" title="TimeoutH">TimeoutH</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#validate" title="Validate">Validate</a>: <i>Boolean</i>
    <a href="#monitorthresholdwindows" title="MonitorThresholdWindows">MonitorThresholdWindows</a>: <i>
      - <a href="monitorthresholdwindowsdefinition.md">MonitorThresholdWindowsDefinition</a></i>
    <a href="#monitorthresholds" title="MonitorThresholds">MonitorThresholds</a>: <i>
      - <a href="monitorthresholdsdefinition.md">MonitorThresholdsDefinition</a></i>
</pre>

## Properties

#### EnableLogsSample

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupbySimpleMonitor

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewHostDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoDataTimeframe

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyAudit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyNoData

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenotifyInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireFullWindow

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutH

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Validate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorThresholdWindows

_Required_: No

_Type_: List of <a href="monitorthresholdwindowsdefinition.md">MonitorThresholdWindowsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorThresholds

_Required_: No

_Type_: List of <a href="monitorthresholdsdefinition.md">MonitorThresholdsDefinition</a>

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

