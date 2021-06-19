# TF::NewRelic::AlertCondition

Use this resource to create and manage alert conditions for APM, Browser, and Mobile in New Relic.

-> **NOTE:** The [newrelic_nrql_alert_condition](nrql_alert_condition.html) resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::AlertCondition",
    "Properties" : {
        "<a href="#conditionscope" title="ConditionScope">ConditionScope</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#entities" title="Entities">Entities</a>" : <i>[ Double, ... ]</i>,
        "<a href="#gcmetric" title="GcMetric">GcMetric</a>" : <i>String</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userdefinedmetric" title="UserDefinedMetric">UserDefinedMetric</a>" : <i>String</i>,
        "<a href="#userdefinedvaluefunction" title="UserDefinedValueFunction">UserDefinedValueFunction</a>" : <i>String</i>,
        "<a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>" : <i>Double</i>,
        "<a href="#term" title="Term">Term</a>" : <i>[ <a href="termdefinition.md">TermDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::AlertCondition
Properties:
    <a href="#conditionscope" title="ConditionScope">ConditionScope</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#entities" title="Entities">Entities</a>: <i>
      - Double</i>
    <a href="#gcmetric" title="GcMetric">GcMetric</a>: <i>String</i>
    <a href="#metric" title="Metric">Metric</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userdefinedmetric" title="UserDefinedMetric">UserDefinedMetric</a>: <i>String</i>
    <a href="#userdefinedvaluefunction" title="UserDefinedValueFunction">UserDefinedValueFunction</a>: <i>String</i>
    <a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>: <i>Double</i>
    <a href="#term" title="Term">Term</a>: <i>
      - <a href="termdefinition.md">TermDefinition</a></i>
</pre>

## Properties

#### ConditionScope

`application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entities

The instance IDs associated with this condition.
* `metric` - (Required) The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
* `condition_scope` - (Required for some types) `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcMetric

A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
* `condition_scope` - (Required for some types) `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the condition. Must be between 1 and 64 characters, inclusive.
* `type` - (Required) The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
* `entities` - (Required) The instance IDs associated with this condition.
* `metric` - (Required) The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
* `condition_scope` - (Required for some types) `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition should be used.
* `name` - (Required) The title of the condition. Must be between 1 and 64 characters, inclusive.
* `type` - (Required) The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
* `entities` - (Required) The instance IDs associated with this condition.
* `metric` - (Required) The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
* `condition_scope` - (Required for some types) `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
* `entities` - (Required) The instance IDs associated with this condition.
* `metric` - (Required) The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
* `apm_app_metric`
* `apdex`
* `error_percentage`
* `response_time_background`
* `response_time_web`
* `throughput_background`
* `throughput_web`
* `user_defined`
* `apm_jvm_metric`
* `cpu_utilization_time`
* `deadlocked_threads`
* `gc_cpu_time`
* `heap_memory_usage`
* `apm_kt_metric`
* `apdex`
* `error_count`
* `error_percentage`
* `response_time`
* `throughput`
* `browser_metric`
* `ajax_response_time`
* `ajax_throughput`
* `dom_processing`
* `end_user_apdex`
* `network`
* `page_rendering`
* `page_view_throughput`
* `page_views_with_js_errors`
* `request_queuing`
* `total_page_load`
* `user_defined`
* `web_application`
* `mobile_metric`
* `database`
* `images`
* `json`
* `mobile_crash_rate`
* `network_error_percentage`
* `network`
* `status_error_percentage`
* `user_defined`
* `view_loading`
* `condition_scope` - (Required for some types) `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
* `enabled` - (Optional) Whether the condition is enabled or not. Defaults to true.
* `gc_metric` - (Optional) A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
* `violation_close_timer` - (Optional) Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDefinedMetric

A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDefinedValueFunction

One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationCloseTimer

Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
* `runbook_url` - (Optional) Runbook URL to display in notifications.
* `term` - (Required) A list of terms for this condition. See [Terms](#terms) below for details.
* `user_defined_metric` - (Optional) A custom metric to be evaluated.
* `user_defined_value_function` - (Optional) One of: `average`, `min`, `max`, `total`, or `sample_size`.

_Required_: No

_Type_: Double

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

