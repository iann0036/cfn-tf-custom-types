# Terraform::Google::MonitoringAlertPolicy

CloudFormation equivalent of google_monitoring_alert_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::MonitoringAlertPolicy",
    "Properties" : {
        "<a href="#combiner" title="Combiner">Combiner</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>" : <i>[ String, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#userlabels" title="UserLabels">UserLabels</a>" : <i>[ <a href="userlabels.md">UserLabels</a>, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditions.md">Conditions</a>, ... ]</i>,
        "<a href="#documentation" title="Documentation">Documentation</a>" : <i>[ <a href="documentation.md">Documentation</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>" : <i>[ <a href="conditionabsent.md">ConditionAbsent</a>, ... ]</i>,
        "<a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>" : <i>[ <a href="conditionthreshold.md">ConditionThreshold</a>, ... ]</i>,
        "<a href="#aggregations" title="Aggregations">Aggregations</a>" : <i>[ <a href="aggregations.md">Aggregations</a>, ... ]</i>,
        "<a href="#trigger" title="Trigger">Trigger</a>" : <i>[ <a href="trigger.md">Trigger</a>, ... ]</i>,
        "<a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>" : <i>[ <a href="denominatoraggregations.md">DenominatorAggregations</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::MonitoringAlertPolicy
Properties:
    <a href="#combiner" title="Combiner">Combiner</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#notificationchannels" title="NotificationChannels">NotificationChannels</a>: <i>
      - String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#userlabels" title="UserLabels">UserLabels</a>: <i>
      - <a href="userlabels.md">UserLabels</a></i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditions.md">Conditions</a></i>
    <a href="#documentation" title="Documentation">Documentation</a>: <i>
      - <a href="documentation.md">Documentation</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#conditionabsent" title="ConditionAbsent">ConditionAbsent</a>: <i>
      - <a href="conditionabsent.md">ConditionAbsent</a></i>
    <a href="#conditionthreshold" title="ConditionThreshold">ConditionThreshold</a>: <i>
      - <a href="conditionthreshold.md">ConditionThreshold</a></i>
    <a href="#aggregations" title="Aggregations">Aggregations</a>: <i>
      - <a href="aggregations.md">Aggregations</a></i>
    <a href="#trigger" title="Trigger">Trigger</a>: <i>
      - <a href="trigger.md">Trigger</a></i>
    <a href="#denominatoraggregations" title="DenominatorAggregations">DenominatorAggregations</a>: <i>
      - <a href="denominatoraggregations.md">DenominatorAggregations</a></i>
</pre>

## Properties

#### Combiner

_Required_: Yes

_Type_: String

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

_Type_: List of <a href="userlabels.md">UserLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditions.md">Conditions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Documentation

_Required_: No

_Type_: List of <a href="documentation.md">Documentation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionAbsent

_Required_: No

_Type_: List of <a href="conditionabsent.md">ConditionAbsent</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionThreshold

_Required_: No

_Type_: List of <a href="conditionthreshold.md">ConditionThreshold</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregations

_Required_: No

_Type_: List of <a href="aggregations.md">Aggregations</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trigger

_Required_: No

_Type_: List of <a href="trigger.md">Trigger</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenominatorAggregations

_Required_: No

_Type_: List of <a href="denominatoraggregations.md">DenominatorAggregations</a>

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

Returns the <code>CreationRecord</code> value.

#### Name

Returns the <code>Name</code> value.

