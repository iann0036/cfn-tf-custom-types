# TF::NewRelic::NrqlAlertCondition

Use this resource to create and manage NRQL alert conditions in New Relic.

-> **IMPORTANT!** Version 2.0.0 of the New Relic Terraform Provider introduces some [additional requirements](/docs/providers/newrelic/index.html) for configuring the provider.
<br><br>
Before upgrading to version 2.0.0 or later, it is recommended to upgrade to the most recent 1.x version of the provider and ensure that your environment successfully runs `terraform plan` without unexpected changes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::NrqlAlertCondition",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>" : <i>Double</i>,
        "<a href="#baselinedirection" title="BaselineDirection">BaselineDirection</a>" : <i>String</i>,
        "<a href="#closeviolationsonexpiration" title="CloseViolationsOnExpiration">CloseViolationsOnExpiration</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#expectedgroups" title="ExpectedGroups">ExpectedGroups</a>" : <i>Double</i>,
        "<a href="#expirationduration" title="ExpirationDuration">ExpirationDuration</a>" : <i>Double</i>,
        "<a href="#filloption" title="FillOption">FillOption</a>" : <i>String</i>,
        "<a href="#fillvalue" title="FillValue">FillValue</a>" : <i>Double</i>,
        "<a href="#ignoreoverlap" title="IgnoreOverlap">IgnoreOverlap</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#openviolationonexpiration" title="OpenViolationOnExpiration">OpenViolationOnExpiration</a>" : <i>Boolean</i>,
        "<a href="#openviolationongroupoverlap" title="OpenViolationOnGroupOverlap">OpenViolationOnGroupOverlap</a>" : <i>Boolean</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#valuefunction" title="ValueFunction">ValueFunction</a>" : <i>String</i>,
        "<a href="#violationtimelimit" title="ViolationTimeLimit">ViolationTimeLimit</a>" : <i>String</i>,
        "<a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>" : <i>Double</i>,
        "<a href="#critical" title="Critical">Critical</a>" : <i>[ <a href="criticaldefinition.md">CriticalDefinition</a>, ... ]</i>,
        "<a href="#nrql" title="Nrql">Nrql</a>" : <i>[ <a href="nrqldefinition.md">NrqlDefinition</a>, ... ]</i>,
        "<a href="#term" title="Term">Term</a>" : <i>[ <a href="termdefinition.md">TermDefinition</a>, ... ]</i>,
        "<a href="#warning" title="Warning">Warning</a>" : <i>[ <a href="warningdefinition.md">WarningDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::NrqlAlertCondition
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>: <i>Double</i>
    <a href="#baselinedirection" title="BaselineDirection">BaselineDirection</a>: <i>String</i>
    <a href="#closeviolationsonexpiration" title="CloseViolationsOnExpiration">CloseViolationsOnExpiration</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#expectedgroups" title="ExpectedGroups">ExpectedGroups</a>: <i>Double</i>
    <a href="#expirationduration" title="ExpirationDuration">ExpirationDuration</a>: <i>Double</i>
    <a href="#filloption" title="FillOption">FillOption</a>: <i>String</i>
    <a href="#fillvalue" title="FillValue">FillValue</a>: <i>Double</i>
    <a href="#ignoreoverlap" title="IgnoreOverlap">IgnoreOverlap</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#openviolationonexpiration" title="OpenViolationOnExpiration">OpenViolationOnExpiration</a>: <i>Boolean</i>
    <a href="#openviolationongroupoverlap" title="OpenViolationOnGroupOverlap">OpenViolationOnGroupOverlap</a>: <i>Boolean</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#valuefunction" title="ValueFunction">ValueFunction</a>: <i>String</i>
    <a href="#violationtimelimit" title="ViolationTimeLimit">ViolationTimeLimit</a>: <i>String</i>
    <a href="#violationtimelimitseconds" title="ViolationTimeLimitSeconds">ViolationTimeLimitSeconds</a>: <i>Double</i>
    <a href="#critical" title="Critical">Critical</a>: <i>
      - <a href="criticaldefinition.md">CriticalDefinition</a></i>
    <a href="#nrql" title="Nrql">Nrql</a>: <i>
      - <a href="nrqldefinition.md">NrqlDefinition</a></i>
    <a href="#term" title="Term">Term</a>: <i>
      - <a href="termdefinition.md">TermDefinition</a></i>
    <a href="#warning" title="Warning">Warning</a>: <i>
      - <a href="warningdefinition.md">WarningDefinition</a></i>
</pre>

## Properties

#### AccountId

The New Relic account ID of the account you wish to create the condition. Defaults to the account ID set in your environment variable `NEW_RELIC_ACCOUNT_ID`.
- `baseline_direction` - (Optional) The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
- `description` - (Optional) The description of the NRQL alert condition.
- `policy_id` - (Required) The ID of the policy where this condition should be used.
- `name` - (Required) The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregationWindow

The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
- `expiration_duration` - (Optional) The amount of time (in seconds) to wait before considering the signal expired.
- `open_violation_on_expiration` - (Optional) Whether to create a new violation to capture that the signal expired.
- `close_violations_on_expiration` - (Optional) Whether to close all open violations when the signal expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaselineDirection

The baseline direction of a _baseline_ NRQL alert condition. Valid values are: `lower_only`, `upper_and_lower`, `upper_only` (case insensitive).
- `description` - (Optional) The description of the NRQL alert condition.
- `policy_id` - (Required) The ID of the policy where this condition should be used.
- `name` - (Required) The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloseViolationsOnExpiration

Whether to close all open violations when the signal expires.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the NRQL alert condition.
- `policy_id` - (Required) The ID of the policy where this condition should be used.
- `name` - (Required) The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedGroups

Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationDuration

The amount of time (in seconds) to wait before considering the signal expired.
- `open_violation_on_expiration` - (Optional) Whether to create a new violation to capture that the signal expired.
- `close_violations_on_expiration` - (Optional) Whether to close all open violations when the signal expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillOption

Which strategy to use when filling gaps in the signal. Possible values are `none`, `last_value` or `static`. If `static`, the `fill_value` field will be used for filling gaps in the signal.
- `fill_value` - (Optional, required when `fill_option` is `static`) This value will be used for filling gaps in the signal.
- `aggregation_window` - (Optional) The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
- `expiration_duration` - (Optional) The amount of time (in seconds) to wait before considering the signal expired.
- `open_violation_on_expiration` - (Optional) Whether to create a new violation to capture that the signal expired.
- `close_violations_on_expiration` - (Optional) Whether to close all open violations when the signal expires.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FillValue

This value will be used for filling gaps in the signal.
- `aggregation_window` - (Optional) The duration of the time window used to evaluate the NRQL query, in seconds. The value must be at least 30 seconds, and no more than 15 minutes (900 seconds). Default is 60 seconds.
- `expiration_duration` - (Optional) The amount of time (in seconds) to wait before considering the signal expired.
- `open_violation_on_expiration` - (Optional) Whether to create a new violation to capture that the signal expired.
- `close_violations_on_expiration` - (Optional) Whether to close all open violations when the signal expires.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOverlap

**DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenViolationOnExpiration

Whether to create a new violation to capture that the signal expired.
- `close_violations_on_expiration` - (Optional) Whether to close all open violations when the signal expires.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenViolationOnGroupOverlap

Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy where this condition should be used.
- `name` - (Required) The title of the condition.
- `type` - (Optional) The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the condition. Valid values are `static`, `baseline`, or `outlier`. Defaults to `static`.
- `runbook_url` - (Optional) Runbook URL to display in notifications.
- `enabled` - (Optional) Whether to enable the alert condition. Valid values are `true` and `false`. Defaults to `true`.
- `nrql` - (Required) A NRQL query. See [NRQL](#nrql) below for details.
- `term` - (Optional) **DEPRECATED** Use `critical`, and `warning` instead.  A list of terms for this condition. See [Terms](#terms) below for details.
- `critical` - (Required) A list containing the `critical` threshold values. See [Terms](#terms) below for details.
- `warning` - (Optional) A list containing the `warning` threshold values. See [Terms](#terms) below for details.
- `value_function` - (Required if `type` is `static`, optional when `type` is `baseline` or `outlier` ) Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueFunction

Possible values are `single_value`, `sum` (case insensitive).
- `expected_groups` - (Optional) Number of expected groups when using `outlier` detection.
- `open_violation_on_group_overlap` - (Optional) Whether or not to trigger a violation when groups overlap. Set to `true` if you want to trigger a violation when groups overlap. This argument is only applicable in `outlier` conditions.
- `ignore_overlap` - (Optional) **DEPRECATED:** Use `open_violation_on_group_overlap` instead, but use the inverse value of your boolean - e.g. if `ignore_overlap = false`, use `open_violation_on_group_overlap = true`. This argument sets whether to trigger a violation when groups overlap. If set to `true` overlapping groups will not trigger a violation. This argument is only applicable in `outlier` conditions.
- `violation_time_limit` - (Optional) **DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTimeLimit

**DEPRECATED:** Use `violation_time_limit_seconds` instead. Sets a time limit, in hours, that will automatically force-close a long-lasting violation after the time limit you select. Possible values are `ONE_HOUR`, `TWO_HOURS`, `FOUR_HOURS`, `EIGHT_HOURS`, `TWELVE_HOURS`, `TWENTY_FOUR_HOURS`, `THIRTY_DAYS` (case insensitive).<br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTimeLimitSeconds

Sets a time limit, in seconds, that will automatically force-close a long-lasting violation after the time limit you select. The value must be between 300 seconds (5 minutes) to 2592000 seconds (30 days) (inclusive). <br>
<small>\***Note**: One of `violation_time_limit` _or_ `violation_time_limit_seconds` must be set, but not both.</small>.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Critical

_Required_: No

_Type_: List of <a href="criticaldefinition.md">CriticalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

_Required_: No

_Type_: List of <a href="nrqldefinition.md">NrqlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Term

_Required_: No

_Type_: List of <a href="termdefinition.md">TermDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

