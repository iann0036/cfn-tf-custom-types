# Terraform::Datadog::Monitor

CloudFormation equivalent of datadog_monitor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Datadog::Monitor",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
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
        "<a href="#silenced" title="Silenced">Silenced</a>" : <i>[ &lt;a href=&#34;silenced.md&#34;&gt;Silenced&lt;/a&gt;, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#thresholdwindows" title="ThresholdWindows">ThresholdWindows</a>" : <i>[ &lt;a href=&#34;thresholdwindows.md&#34;&gt;ThresholdWindows&lt;/a&gt;, ... ]</i>,
        "<a href="#thresholds" title="Thresholds">Thresholds</a>" : <i>[ &lt;a href=&#34;thresholds.md&#34;&gt;Thresholds&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouth" title="TimeoutH">TimeoutH</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Datadog::Monitor
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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
      - &lt;a href=&#34;silenced.md&#34;&gt;Silenced&lt;/a&gt;</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#thresholdwindows" title="ThresholdWindows">ThresholdWindows</a>: <i>
      - &lt;a href=&#34;thresholdwindows.md&#34;&gt;ThresholdWindows&lt;/a&gt;</i>
    <a href="#thresholds" title="Thresholds">Thresholds</a>: <i>
      - &lt;a href=&#34;thresholds.md&#34;&gt;Thresholds&lt;/a&gt;</i>
    <a href="#timeouth" title="TimeoutH">TimeoutH</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Silenced

_Required_: No

_Type_: List of &lt;a href=&#34;silenced.md&#34;&gt;Silenced&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdWindows

_Required_: No

_Type_: List of &lt;a href=&#34;thresholdwindows.md&#34;&gt;ThresholdWindows&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thresholds

_Required_: No

_Type_: List of &lt;a href=&#34;thresholds.md&#34;&gt;Thresholds&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutH

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

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

