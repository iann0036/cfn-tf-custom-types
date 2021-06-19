# TF::NewRelic::InfraAlertCondition

Use this resource to create and manage Infrastructure alert conditions in New Relic.

-> **NOTE:** The [newrelic_nrql_alert_condition](nrql_alert_condition.html) resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::InfraAlertCondition",
    "Properties" : {
        "<a href="#comparison" title="Comparison">Comparison</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#event" title="Event">Event</a>" : <i>String</i>,
        "<a href="#integrationprovider" title="IntegrationProvider">IntegrationProvider</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#processwhere" title="ProcessWhere">ProcessWhere</a>" : <i>String</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#select" title="Select">Select</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>" : <i>Double</i>,
        "<a href="#where" title="Where">Where</a>" : <i>String</i>,
        "<a href="#critical" title="Critical">Critical</a>" : <i>[ <a href="criticaldefinition.md">CriticalDefinition</a>, ... ]</i>,
        "<a href="#warning" title="Warning">Warning</a>" : <i>[ <a href="warningdefinition.md">WarningDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::InfraAlertCondition
Properties:
    <a href="#comparison" title="Comparison">Comparison</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#event" title="Event">Event</a>: <i>String</i>
    <a href="#integrationprovider" title="IntegrationProvider">IntegrationProvider</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#processwhere" title="ProcessWhere">ProcessWhere</a>: <i>String</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#select" title="Select">Select</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>: <i>Double</i>
    <a href="#where" title="Where">Where</a>: <i>String</i>
    <a href="#critical" title="Critical">Critical</a>: <i>
      - <a href="criticaldefinition.md">CriticalDefinition</a></i>
    <a href="#warning" title="Warning">Warning</a>: <i>
      - <a href="warningdefinition.md">WarningDefinition</a></i>
</pre>

## Properties

#### Comparison

The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

The metric event; for example, `SystemSample` or `StorageSample`.  Supported by the `infra_metric` condition type.
* `select` - (Required) The attribute name to identify the metric being targeted; for example, `cpuPercent`, `diskFreePercent`, or `memoryResidentSizeBytes`.  The underlying API will automatically populate this value for Infrastructure integrations (for example `diskFreePercent`), so make sure to explicitly include this value to avoid diff issues.  Supported by the `infra_metric` condition type.
* `comparison` - (Required) The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationProvider

For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Infrastructure alert condition's name.
* `type` - (Required) The type of Infrastructure alert condition.  Valid values are  `infra_process_running`, `infra_metric`, and `infra_host_not_reporting`.
* `event` - (Required) The metric event; for example, `SystemSample` or `StorageSample`.  Supported by the `infra_metric` condition type.
* `select` - (Required) The attribute name to identify the metric being targeted; for example, `cpuPercent`, `diskFreePercent`, or `memoryResidentSizeBytes`.  The underlying API will automatically populate this value for Infrastructure integrations (for example `diskFreePercent`), so make sure to explicitly include this value to avoid diff issues.  Supported by the `infra_metric` condition type.
* `comparison` - (Required) The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the alert policy where this condition should be used.
* `name` - (Required) The Infrastructure alert condition's name.
* `type` - (Required) The type of Infrastructure alert condition.  Valid values are  `infra_process_running`, `infra_metric`, and `infra_host_not_reporting`.
* `event` - (Required) The metric event; for example, `SystemSample` or `StorageSample`.  Supported by the `infra_metric` condition type.
* `select` - (Required) The attribute name to identify the metric being targeted; for example, `cpuPercent`, `diskFreePercent`, or `memoryResidentSizeBytes`.  The underlying API will automatically populate this value for Infrastructure integrations (for example `diskFreePercent`), so make sure to explicitly include this value to avoid diff issues.  Supported by the `infra_metric` condition type.
* `comparison` - (Required) The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessWhere

Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Select

The attribute name to identify the metric being targeted; for example, `cpuPercent`, `diskFreePercent`, or `memoryResidentSizeBytes`.  The underlying API will automatically populate this value for Infrastructure integrations (for example `diskFreePercent`), so make sure to explicitly include this value to avoid diff issues.  Supported by the `infra_metric` condition type.
* `comparison` - (Required) The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of Infrastructure alert condition.  Valid values are  `infra_process_running`, `infra_metric`, and `infra_host_not_reporting`.
* `event` - (Required) The metric event; for example, `SystemSample` or `StorageSample`.  Supported by the `infra_metric` condition type.
* `select` - (Required) The attribute name to identify the metric being targeted; for example, `cpuPercent`, `diskFreePercent`, or `memoryResidentSizeBytes`.  The underlying API will automatically populate this value for Infrastructure integrations (for example `diskFreePercent`), so make sure to explicitly include this value to avoid diff issues.  Supported by the `infra_metric` condition type.
* `comparison` - (Required) The operator used to evaluate the threshold value.  Valid values are `above`, `below`, and `equal`.  Supported by the `infra_metric` and `infra_process_running` condition types.
* `critical` - (Required) Identifies the threshold parameters for opening a critical alert violation. See [Thresholds](#thresholds) below for details.
* `warning` - (Optional) Identifies the threshold parameters for opening a warning alert violation. See [Thresholds](#thresholds) below for details.
* `enabled` - (Optional) Whether the condition is turned on or off.  Valid values are `true` and `false`.  Defaults to `true`.
* `where` - (Optional) If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationCloseTimer

Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Where

If applicable, this identifies any Infrastructure host filters used; for example: `hostname LIKE '%cassandra%'`.
* `process_where` - (Optional) Any filters applied to processes; for example: `commandName = 'java'`.  Required by the `infra_process_running` condition type.
* `integration_provider` - (Optional) For alerts on integrations, use this instead of `event`.  Supported by the `infra_metric` condition type.
* `description` - (Optional) The description of the Infrastructure alert condition.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `violation_close_timer` - (Optional) Determines how much time will pass before a violation is automatically closed. Setting the time limit to 0 prevents a violation from being force-closed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Critical

_Required_: No

_Type_: List of <a href="criticaldefinition.md">CriticalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

_Required_: No

_Type_: List of <a href="warningdefinition.md">WarningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

