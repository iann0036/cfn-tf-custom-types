# Terraform::Datadog::Monitor

Provides a Datadog monitor resource. This can be used to create and manage Datadog monitors.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Monitor",
    "Properties" : {
        "<a href="#enablelogssample" title="EnableLogsSample">EnableLogsSample</a>" : <i>Boolean</i>,
        "<a href="#escalationmessage" title="EscalationMessage">EscalationMessage</a>" : <i>String</i>,
        "<a href="#evaluationdelay" title="EvaluationDelay">EvaluationDelay</a>" : <i>Double</i>,
        "<a href="#includetags" title="IncludeTags">IncludeTags</a>" : <i>Boolean</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#newhostdelay" title="NewHostDelay">NewHostDelay</a>" : <i>Double</i>,
        "<a href="#nodatatimeframe" title="NoDataTimeframe">NoDataTimeframe</a>" : <i>Double</i>,
        "<a href="#notifyaudit" title="NotifyAudit">NotifyAudit</a>" : <i>Boolean</i>,
        "<a href="#notifynodata" title="NotifyNoData">NotifyNoData</a>" : <i>Boolean</i>,
        "<a href="#query" title="Query">Query</a>" : <i>String</i>,
        "<a href="#renotifyinterval" title="RenotifyInterval">RenotifyInterval</a>" : <i>Double</i>,
        "<a href="#requirefullwindow" title="RequireFullWindow">RequireFullWindow</a>" : <i>Boolean</i>,
        "<a href="#silenced" title="Silenced">Silenced</a>" : <i>[ <a href="silenced.md">Silenced</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#thresholdwindows" title="ThresholdWindows">ThresholdWindows</a>" : <i>[ <a href="thresholdwindows.md">ThresholdWindows</a>, ... ]</i>,
        "<a href="#thresholds" title="Thresholds">Thresholds</a>" : <i>[ <a href="thresholds.md">Thresholds</a>, ... ]</i>,
        "<a href="#timeouth" title="TimeoutH">TimeoutH</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Monitor
Properties:
    <a href="#enablelogssample" title="EnableLogsSample">EnableLogsSample</a>: <i>Boolean</i>
    <a href="#escalationmessage" title="EscalationMessage">EscalationMessage</a>: <i>String</i>
    <a href="#evaluationdelay" title="EvaluationDelay">EvaluationDelay</a>: <i>Double</i>
    <a href="#includetags" title="IncludeTags">IncludeTags</a>: <i>Boolean</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#newhostdelay" title="NewHostDelay">NewHostDelay</a>: <i>Double</i>
    <a href="#nodatatimeframe" title="NoDataTimeframe">NoDataTimeframe</a>: <i>Double</i>
    <a href="#notifyaudit" title="NotifyAudit">NotifyAudit</a>: <i>Boolean</i>
    <a href="#notifynodata" title="NotifyNoData">NotifyNoData</a>: <i>Boolean</i>
    <a href="#query" title="Query">Query</a>: <i>String</i>
    <a href="#renotifyinterval" title="RenotifyInterval">RenotifyInterval</a>: <i>Double</i>
    <a href="#requirefullwindow" title="RequireFullWindow">RequireFullWindow</a>: <i>Boolean</i>
    <a href="#silenced" title="Silenced">Silenced</a>: <i>
      - <a href="silenced.md">Silenced</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#thresholdwindows" title="ThresholdWindows">ThresholdWindows</a>: <i>
      - <a href="thresholdwindows.md">ThresholdWindows</a></i>
    <a href="#thresholds" title="Thresholds">Thresholds</a>: <i>
      - <a href="thresholds.md">Thresholds</a></i>
    <a href="#timeouth" title="TimeoutH">TimeoutH</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### EnableLogsSample

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EscalationMessage

A message to include with a re-notification. Supports the '@username'
notification allowed elsewhere.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationDelay

_Required_: No

_Type_: Double

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

A message to include with notifications for this monitor.
Email notifications can be sent to specific users by using the same '@username' notation as events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Datadog monitor.

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

#### Query

The monitor query to notify on. Note this is not the same query you see in the UI and
the syntax is different depending on the monitor `type`, please see the [API Reference](https://docs.datadoghq.com/api/?lang=python#create-a-monitor) for details. **Warning:** `terraform plan` won't perform any validation of the query contents.

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

#### Silenced

_Required_: No

_Type_: List of <a href="silenced.md">Silenced</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdWindows

_Required_: No

_Type_: List of <a href="thresholdwindows.md">ThresholdWindows</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thresholds

* Metric alerts:
A dictionary of thresholds by threshold type. Currently we have four threshold types for metric alerts: critical, critical recovery, warning, and warning recovery. Critical is defined in the query, but can also be specified in this option. Warning and recovery thresholds can only be specified using the thresholds option.
Example usage:
```
thresholds = {
critical          = 90
critical_recovery = 85
warning           = 80
warning_recovery  = 75
}
```
**Warning:** the `critical` threshold value must match the one contained in the `query` argument. The `threshold` from the previous example is valid along with a query like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} > 90` but
along with something like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} > 95` would make the Datadog API return a HTTP error 400, complaining "The value provided for parameter 'query' is invalid".
* Service checks:
A dictionary of thresholds by status. Because service checks can have multiple thresholds, we don't define them directly in the query.
Default values:
```
thresholds = {
ok       = 1
critical = 1
warning  = 1
unknown  = 1
}
```.

_Required_: No

_Type_: List of <a href="thresholds.md">Thresholds</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutH

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API [documentation](https://docs.datadoghq.com/api/?lang=python#create-a-monitor) page. The available options are below. **Note**: The monitor type cannot be changed after a monitor is created.
* `metric alert`
* `service check`
* `event alert`
* `query alert`
* `composite`
* `log alert`.

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

