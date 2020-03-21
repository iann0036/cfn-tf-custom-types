# Terraform::Google::MonitoringAlertPolicy

CloudFormation equivalent of google_monitoring_alert_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::MonitoringAlertPolicy",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#combiner" title="Combiner">Combiner</a>" : <i>String</i>,
        "<a href="#creationrecord" title="CreationRecord">CreationRecord</a>" : <i>[ &lt;a href=&#34;creationrecord.md&#34;&gt;CreationRecord&lt;/a&gt;, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>" : <i>[ String, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#userlabels" title="UserLabels">UserLabels</a>" : <i>[ &lt;a href=&#34;userlabels.md&#34;&gt;UserLabels&lt;/a&gt;, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;, ... ]</i>,
        "<a href="#documentation" title="Documentation">Documentation</a>" : <i>[ &lt;a href=&#34;documentation.md&#34;&gt;Documentation&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>" : <i>[ &lt;a href=&#34;conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;, ... ]</i>,
        "<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>" : <i>[ &lt;a href=&#34;conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;, ... ]</i>,
        "<a href="#aggregations" title="Aggregations">Aggregations</a>" : <i>[ &lt;a href=&#34;aggregations.md&#34;&gt;Aggregations&lt;/a&gt;, ... ]</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;, ... ]</i>,
        "<a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>" : <i>[ &lt;a href=&#34;denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::MonitoringAlertPolicy
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#combiner" title="Combiner">Combiner</a>: <i>String</i>
    <a href="#creationrecord" title="CreationRecord">CreationRecord</a>: <i>
      - &lt;a href=&#34;creationrecord.md&#34;&gt;CreationRecord&lt;/a&gt;</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>: <i>
      - String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#userlabels" title="UserLabels">UserLabels</a>: <i>
      - &lt;a href=&#34;userlabels.md&#34;&gt;UserLabels&lt;/a&gt;</i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;</i>
    <a href="#documentation" title="Documentation">Documentation</a>: <i>
      - &lt;a href=&#34;documentation.md&#34;&gt;Documentation&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>: <i>
      - &lt;a href=&#34;conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;</i>
    <a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>: <i>
      - &lt;a href=&#34;conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;</i>
    <a href="#aggregations" title="Aggregations">Aggregations</a>: <i>
      - &lt;a href=&#34;aggregations.md&#34;&gt;Aggregations&lt;/a&gt;</i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;</i>
    <a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>: <i>
      - &lt;a href=&#34;denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Combiner

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationRecord

_Required_: No

_Type_: List of &lt;a href=&#34;creationrecord.md&#34;&gt;CreationRecord&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationChannels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserLabels

_Required_: No

_Type_: List of &lt;a href=&#34;userlabels.md&#34;&gt;UserLabels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of &lt;a href=&#34;conditions.md&#34;&gt;Conditions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Documentation

_Required_: No

_Type_: List of &lt;a href=&#34;documentation.md&#34;&gt;Documentation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionAbsent

_Required_: No

_Type_: List of &lt;a href=&#34;conditionabsent.md&#34;&gt;ConditionAbsent&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionThreshold

_Required_: No

_Type_: List of &lt;a href=&#34;conditionthreshold.md&#34;&gt;ConditionThreshold&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregations

_Required_: No

_Type_: List of &lt;a href=&#34;aggregations.md&#34;&gt;Aggregations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of &lt;a href=&#34;trigger.md&#34;&gt;Trigger&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenominatorAggregations

_Required_: No

_Type_: List of &lt;a href=&#34;denominatoraggregations.md&#34;&gt;DenominatorAggregations&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationRecord

Returns the &lt;code&gt;CreationRecord&lt;/code&gt; value.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

