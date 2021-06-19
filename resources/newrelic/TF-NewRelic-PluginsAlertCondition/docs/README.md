# TF::NewRelic::PluginsAlertCondition

~> **DEPRECATED** Use at your own risk. Use the [`newrelic_nrql_alert_condition`](nrql_alert_condition.html) resource instead. This feature will stop being supported as of June 16, 2021. For more information, check out [https://discuss.newrelic.com/t/new-relic-plugin-eol-wednesday-june-16th-2021/127267](https://discuss.newrelic.com/t/new-relic-plugin-eol-wednesday-june-16th-2021/127267)

Use this resource to create and manage plugins alert conditions in New Relic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::PluginsAlertCondition",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#entities" title="Entities">Entities</a>" : <i>[ Double, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
        "<a href="#metricdescription" title="MetricDescription">MetricDescription</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pluginguid" title="PluginGuid">PluginGuid</a>" : <i>String</i>,
        "<a href="#pluginid" title="PluginId">PluginId</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#valuefunction" title="ValueFunction">ValueFunction</a>" : <i>String</i>,
        "<a href="#term" title="Term">Term</a>" : <i>[ <a href="termdefinition.md">TermDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::PluginsAlertCondition
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#entities" title="Entities">Entities</a>: <i>
      - Double</i>
    <a href="#metric" title="Metric">Metric</a>: <i>String</i>
    <a href="#metricdescription" title="MetricDescription">MetricDescription</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pluginguid" title="PluginGuid">PluginGuid</a>: <i>String</i>
    <a href="#pluginid" title="PluginId">PluginId</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#valuefunction" title="ValueFunction">ValueFunction</a>: <i>String</i>
    <a href="#term" title="Term">Term</a>: <i>
      - <a href="termdefinition.md">TermDefinition</a></i>
</pre>

## Properties

#### Enabled

Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entities

The plugin component IDs to target.
* `plugin_id` - (Required) The ID of the installed plugin instance which produces the metric.
* `plugin_guid` - (Required) The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

The plugin metric to evaluate.
* `entities` - (Required) The plugin component IDs to target.
* `plugin_id` - (Required) The ID of the installed plugin instance which produces the metric.
* `plugin_guid` - (Required) The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDescription

The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the condition. Must be between 1 and 64 characters, inclusive.
* `metric` - (Required) The plugin metric to evaluate.
* `entities` - (Required) The plugin component IDs to target.
* `plugin_id` - (Required) The ID of the installed plugin instance which produces the metric.
* `plugin_guid` - (Required) The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginGuid

The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PluginId

The ID of the installed plugin instance which produces the metric.
* `plugin_guid` - (Required) The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition should be used.
* `name` - (Required) The title of the condition. Must be between 1 and 64 characters, inclusive.
* `metric` - (Required) The plugin metric to evaluate.
* `entities` - (Required) The plugin component IDs to target.
* `plugin_id` - (Required) The ID of the installed plugin instance which produces the metric.
* `plugin_guid` - (Required) The GUID of the plugin which produces the metric.
* `metric_description` - (Required) The metric description.
* `value_function` - (Required) The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueFunction

The value function to apply to the metric data.  One of `min`, `max`, `average`, `sample_size`, `total`, or `percent`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `enabled` - (Optional) Whether or not this condition is enabled.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Term

_Required_: No

_Type_: List of <a href="termdefinition.md">TermDefinition</a>

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

